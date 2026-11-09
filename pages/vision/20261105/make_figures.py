"""Day14 oneday 요약 그림 데이터 생성.

강사용 실습 데이터(01_basic/data, 02_intermediate/data)로 실제 학습을 돌려
그림에 쓸 숫자(facts.json)와 이미지(PNG)를 만듭니다.

실행:
  uv run --project ~/envs/dl python make_figures.py <mentor(강사용) 폴더> <출력 폴더>
"""
import base64
import io
import json
import sys
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, recall_score
from torch import nn
from torchvision import transforms as tr
from torchvision.datasets import ImageFolder

torch.set_num_threads(1)
SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
BASIC = SRC / "01_basic" / "data"
APPLIED = SRC / "02_intermediate" / "data"
T = tr.Compose([tr.Resize((32, 32)), tr.ToTensor()])


def load(data_dir):
    sets = [ImageFolder(data_dir / s, transform=T) for s in ("train", "valid")]
    return sets, [(torch.stack([d[i][0] for i in range(len(d))]), torch.tensor(d.targets)) for d in sets]


def build(data_dir, pretrained=True):
    m = nn.Sequential(
        nn.Conv2d(3, 8, 3, padding=1, bias=False), nn.BatchNorm2d(8), nn.ReLU(), nn.MaxPool2d(2),
        nn.Conv2d(8, 16, 3, padding=1, bias=False), nn.BatchNorm2d(16), nn.ReLU(),
        nn.AdaptiveAvgPool2d((4, 4)), nn.Flatten(), nn.Linear(256, 3))
    if pretrained:
        with np.load(data_dir / "source_backbone.npz", allow_pickle=False) as s:
            st = m.state_dict()
            st.update({k: torch.from_numpy(s[k].copy()) for k in s.files})
        m.load_state_dict(st)
    return m


def train(data_dir, data, strategy="head", lr=0.003, epochs=8, wd=1e-4, balance=None, seed=14):
    (X, y), (Xv, yv) = data
    torch.manual_seed(seed)
    m = build(data_dir)
    for p in m.parameters():
        p.requires_grad = False
    for p in m[9].parameters():
        p.requires_grad = True
    if strategy == "partial":
        for p in m[4].parameters():
            p.requires_grad = True
    if strategy == "full":
        for p in m.parameters():
            p.requires_grad = True
    m.eval()
    opt = torch.optim.AdamW([p for p in m.parameters() if p.requires_grad], lr=lr, weight_decay=wd)
    weight = None
    if balance == "weight":
        c = torch.bincount(y, minlength=3).float()
        weight = (1 / c) / (1 / c).mean()
    crit = nn.CrossEntropyLoss(weight=weight)
    best, hist, best_state, best_ep = 1e9, [], None, 0
    for e in range(1, epochs + 1):
        opt.zero_grad()
        crit(m(X), y).backward()
        opt.step()
        with torch.no_grad():
            vl = nn.functional.cross_entropy(m(Xv), yv).item()
        hist.append(round(vl, 4))
        if vl < best:
            best, best_ep = vl, e
            best_state = {k: v.clone() for k, v in m.state_dict().items()}
    m.load_state_dict(best_state)
    with torch.no_grad():
        pred = m(Xv).argmax(1)
    return m, pred, dict(
        acc=round(accuracy_score(yv, pred), 3),
        f1=round(f1_score(yv, pred, labels=[0, 1, 2], average="macro", zero_division=0), 3),
        recall=[round(r, 3) for r in recall_score(yv, pred, labels=[0, 1, 2], average=None, zero_division=0)],
        cm=confusion_matrix(yv, pred, labels=[0, 1, 2]).tolist(),
        hist=hist, best_ep=best_ep,
        trainable=sum(p.numel() for p in m.parameters() if p.requires_grad),
        weight=None if weight is None else [round(w, 2) for w in weight.tolist()])


def png_b64(arr, size):
    img = Image.fromarray(arr).resize((size, size), Image.NEAREST)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def colormap(v):
    """0~1 → 노랑에서 진한 주황으로 (강의 팔레트의 노랑·주황 계열)."""
    stops = np.array([[251, 230, 160], [240, 170, 80], [214, 110, 40], [150, 50, 20]], float)
    pos = np.array([0, 0.35, 0.7, 1.0])
    out = np.zeros(v.shape + (3,))
    for c in range(3):
        out[..., c] = np.interp(v, pos, stops[:, c])
    return out


def gradcam(m, x, target):
    image = x[None].clone().requires_grad_(True)
    feats = m[:7](image)
    score = m[7:](feats)
    grad = torch.autograd.grad(score[0, target], feats)[0]
    w = grad.mean((2, 3), keepdim=True)
    raw = (w * feats).sum(1)
    neg_share = float((raw < 0).float().mean())
    cam = raw.relu()
    cam = nn.functional.interpolate(cam[None], (32, 32), mode="bilinear", align_corners=False)[0, 0]
    cam = (cam / cam.max().clamp_min(1e-8)).detach().numpy()
    return cam, round(float(score[0, target]), 3), score.softmax(1)[0].tolist(), neg_share


facts = {}

# ── 1. 데이터: 클래스별 개수와 샘플 사진 ──
(tr_a, va_a), data_a = load(APPLIED)
(tr_b, va_b), data_b = load(BASIC)
classes = tr_a.classes
facts["classes"] = classes
facts["counts"] = {
    "applied_train": torch.bincount(data_a[0][1], minlength=3).tolist(),
    "applied_valid": torch.bincount(data_a[1][1], minlength=3).tolist(),
    "basic_train": torch.bincount(data_b[0][1], minlength=3).tolist(),
    "basic_valid": torch.bincount(data_b[1][1], minlength=3).tolist(),
}
samples = {}
for ci, name in enumerate(classes):
    idx = [i for i, t in enumerate(tr_a.targets) if t == ci][:3]
    samples[name] = [png_b64(np.uint8(data_a[0][0][i].permute(1, 2, 0).numpy() * 255), 96) for i in idx]
facts["samples"] = samples

# ── 2. 학습 범위: 전략별 학습 파라미터 수 ──
facts["trainable"] = {s: train(BASIC, data_b, strategy=s, lr=0.01, wd=0)[2]["trainable"]
                      for s in ("head", "partial", "full")}

# ── 3. 학습 속도와 양: valid loss 곡선 (응용 데이터, Head-only, 16 epoch) ──
facts["curves"] = {}
for lr in (0.001, 0.003, 0.01, 0.1):
    _, _, r = train(APPLIED, data_a, lr=lr, epochs=16)
    facts["curves"][str(lr)] = {"hist": r["hist"], "best_ep": r["best_ep"], "f1": r["f1"]}

# ── 4. 불균형: class weight 전후 (응용 데이터, 기본 설정) ──
m_base, pred_base, r_base = train(APPLIED, data_a)
m_w, pred_w, r_w = train(APPLIED, data_a, balance="weight")
facts["imbalance"] = {"none": r_base, "weight": r_w}

# ── 5. 평가: 전부 circle로 예측한 손 예제 (circle 4, square 2, triangle 1) ──
y_true = [0, 0, 0, 0, 1, 1, 2]
y_pred = [0] * 7
facts["all_circle"] = {
    "y_true": y_true,
    "acc": round(accuracy_score(y_true, y_pred), 3),
    "macro": round(f1_score(y_true, y_pred, labels=[0, 1, 2], average="macro", zero_division=0), 3),
    "weighted": round(f1_score(y_true, y_pred, labels=[0, 1, 2], average="weighted", zero_division=0), 3),
    "per_class": [round(v, 3) for v in f1_score(y_true, y_pred, labels=[0, 1, 2], average=None, zero_division=0)],
}

# ── 6. 설명: 같은 이미지, target만 바꾼 Grad-CAM (class weight 모델) ──
Xv, yv = data_a[1]
with torch.no_grad():
    probs = m_w(Xv).softmax(1)
# 정답을 맞힌 square 중 확신이 가장 높은 이미지
cands = [i for i in range(len(yv)) if yv[i] == 1 and probs[i].argmax() == 1]
i = max(cands, key=lambda k: float(probs[k, 1]))
orig = np.uint8(Xv[i].permute(1, 2, 0).numpy() * 255)
cams = []
for target in (1, 0):
    cam, score, sm, neg = gradcam(m_w, Xv[i], target)
    a = (0.8 * cam)[..., None]
    overlay = np.uint8((1 - a) * orig + a * colormap(cam))
    cams.append({"target": classes[target], "score": score, "prob": round(sm[target], 3),
                 "neg_share": round(neg, 3), "png": png_b64(overlay, 160)})
facts["gradcam"] = {"label": classes[int(yv[i])], "orig": png_b64(orig, 160), "cams": cams}

(OUT / "facts.json").write_text(json.dumps(facts, ensure_ascii=False, indent=1), encoding="utf-8")

# 사람이 읽을 요약
short = {k: v for k, v in facts.items() if k not in ("samples", "gradcam")}
short["gradcam"] = {"label": facts["gradcam"]["label"],
                    "cams": [{k: c[k] for k in ("target", "score", "prob", "neg_share")} for c in cams]}
for name in ("none", "weight"):
    short["imbalance"][name] = {k: facts["imbalance"][name][k] for k in ("acc", "f1", "recall", "cm", "best_ep", "weight")}
print(json.dumps(short, ensure_ascii=False, indent=1))
