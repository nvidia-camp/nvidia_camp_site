"""Day15 oneday 요약의 실측 숫자와 그림 데이터를 만든다 → facts.json

응용 실습 데이터로 YOLO를 직접 학습하고(약 3분, CPU), 구성안의 실측 항목을 모두 다시 잰다.
원본 실습 폴더는 읽기만 하고, 학습 결과는 작업 폴더에 저장한다.

실행:
  uv run --project ~/envs/dl --with ultralytics --with opencv-python-headless --with lap \
      python -I make_figures.py <02_intermediate 폴더> <작업 폴더> <출력 폴더>
"""
import base64
import json
import sys
import time
from pathlib import Path

import cv2
import numpy as np
import pandas as pd
import torch
import yaml
from torchvision.ops import box_iou
from ultralytics import YOLO
from ultralytics.utils.nms import non_max_suppression

APP, WORK, OUT = (Path(a).resolve() for a in sys.argv[1:4])
DATA = APP / "data"
NAMES = ["square", "circle", "triangle"]
WORK.mkdir(parents=True, exist_ok=True)
facts = {"names": NAMES}


def b64png(img_bgr):
    ok, buf = cv2.imencode(".png", img_bgr)
    assert ok
    return "data:image/png;base64," + base64.b64encode(buf.tobytes()).decode()


def read_gt(label_path, W, H):
    boxes, classes = [], []
    for line in label_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            c, cx, cy, w, h = map(float, line.split())
            boxes.append([(cx - w / 2) * W, (cy - h / 2) * H, (cx + w / 2) * W, (cy + h / 2) * H])
            classes.append(int(c))
    return boxes, classes


def match(pred_xyxy, pred_cls, pred_conf, gt_boxes, gt_cls, thr=0.5):
    """점수 높은 예측부터, 같은 클래스의 아직 안 쓴 정답과 IoU ≥ thr이면 1:1 연결."""
    used, flags = set(), [False] * len(pred_conf)
    if gt_boxes and len(pred_conf):
        ov = box_iou(torch.tensor(pred_xyxy, dtype=torch.float32), torch.tensor(gt_boxes, dtype=torch.float32))
        for i in sorted(range(len(pred_conf)), key=lambda i: -pred_conf[i]):
            cand = [j for j in range(len(gt_boxes)) if gt_cls[j] == pred_cls[i] and j not in used]
            for j in sorted(cand, key=lambda j: -float(ov[i, j])):
                if ov[i, j] >= thr:
                    used.add(j)
                    flags[i] = True
                break
    return flags, len(used)


def score(results, thr=0.5):
    tp = fp = fn = 0
    for r in results:
        H, W = r.orig_shape
        g, gc = read_gt(DATA / "labels/val" / (Path(r.path).stem + ".txt"), W, H)
        b = r.boxes.cpu()
        flags, m = match(b.xyxy.tolist(), [int(c) for c in b.cls.tolist()], b.conf.tolist(), g, gc, thr)
        tp += m
        fp += len(b) - m
        fn += len(g) - m
    return dict(boxes=tp + fp, tp=tp, fp=fp, fn=fn,
                P=round(tp / (tp + fp), 3) if tp + fp else 0.0, R=round(tp / (tp + fn), 3))


# ── 학습: 핵심 코드와 같은 설정(구조 yaml, 60 epoch, imgsz 160) ──
cfg = WORK / "dataset.yaml"
cfg.write_text(yaml.safe_dump({"path": str(DATA), "train": "images/train", "val": "images/val",
                               "names": dict(enumerate(NAMES))}, sort_keys=False), encoding="utf-8")
common = dict(data=str(cfg), imgsz=160, batch=4, seed=42, deterministic=True, device="cpu", workers=0,
              pretrained=False, amp=False, plots=False, project=str(WORK), exist_ok=True, verbose=False)
torch.set_num_threads(4)
t0 = time.time()
model = YOLO("yolo26n.yaml")
model.train(epochs=60, name="main", **common)
facts["train_seconds"] = round(time.time() - t0)
e1 = YOLO("yolo26n.yaml")
e1.train(epochs=1, name="e1", **common)
m1 = e1.val(verbose=False, plots=False)
facts["epoch1"] = {"map50": round(float(m1.box.map50), 4), "map": round(float(m1.box.map), 4)}
torch.set_num_threads(1)

run = WORK / "main"
best_w, last_w = run / "weights/best.pt", run / "weights/last.pt"
hist = pd.read_csv(run / "results.csv")
facts["curve"] = {"epoch": hist["epoch"].astype(int).tolist(),
                  "map50": hist["metrics/mAP50(B)"].round(4).tolist(),
                  "map": hist["metrics/mAP50-95(B)"].round(4).tolist()}
# best.pt는 fitness가 가장 높은 epoch. 이 버전의 fitness = mAP50-95 (가중치 [P, R, mAP50, mAP50-95] = [0, 0, 0, 1])
facts["best_epoch"] = int(hist.loc[hist["metrics/mAP50-95(B)"].idxmax(), "epoch"])
facts["last_epoch"] = int(hist["epoch"].max())

model = YOLO(best_w)
mb = model.val(verbose=False, plots=False)
ml = YOLO(last_w).val(verbose=False, plots=False)
facts["val"] = {"best": {"map50": round(float(mb.box.map50), 4), "map": round(float(mb.box.map), 4)},
                "last": {"map50": round(float(ml.box.map50), 4), "map": round(float(ml.box.map), 4)},
                "map_by_iou": [round(float(v), 4) for v in mb.box.all_ap.mean(0)]}

# ── 6교시: conf와 NMS IoU ──
val_dir = str(DATA / "images/val")
facts["conf_sweep"] = [dict(conf=c, **score(model.predict(val_dir, conf=c, verbose=False)))
                       for c in [round(x, 2) for x in np.arange(0.05, 0.96, 0.05)]]
facts["nms_sweep"] = [dict(iou=u, **score(model.predict(val_dir, conf=0.25, iou=u, verbose=False)))
                      for u in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]]
facts["eval95"] = score(model.predict(val_dir, conf=0.25, verbose=False), thr=0.95)

# ── 1구역 깔때기: 공식 추론 경로의 후보 → conf → NMS → 채점 ──
img_path = DATA / "images/val/standard_val_000.png"
img = cv2.imread(str(img_path))
model.predict(str(img_path), verbose=False)
P = model.predictor
x = P.preprocess([img])
raw = P.inference(x)
raw = raw[0] if isinstance(raw, (list, tuple)) else raw
Hin, Win = x.shape[2:]
assert (Hin, Win) == img.shape[:2], "입력과 원본 크기가 같아야 좌표를 그대로 쓸 수 있다"
anchors = []
for s in (8, 16, 32):
    for gy in range(Hin // s):
        for gx in range(Win // s):
            anchors.append(((gx + 0.5) * s, (gy + 0.5) * s, s))
assert len(anchors) == raw.shape[-1]
p = raw[0].T
xywh, cls_scores = p[:, :4], p[:, 4:]
conf, cls = cls_scores.max(1)
xyxy = torch.cat([xywh[:, :2] - xywh[:, 2:] / 2, xywh[:, :2] + xywh[:, 2:] / 2], 1)
keep_conf = (conf > 0.25).nonzero().flatten().tolist()
nms = non_max_suppression(raw, 0.25, 0.7, max_det=300, nc=0)[0]
final = model.predict(str(img_path), conf=0.25, verbose=False)[0].boxes
assert len(nms) == len(final)
g, gc = read_gt(DATA / "labels/val/standard_val_000.txt", Win, Hin)
flags, _ = match(final.xyxy.tolist(), [int(c) for c in final.cls.tolist()], final.conf.tolist(), g, gc)
facts["funnel"] = {
    "image": b64png(img), "W": Win, "H": Hin,
    "grids": [[Win // s, Hin // s] for s in (8, 16, 32)],
    "anchors": [[a[0], a[1], a[2], round(float(conf[i]), 3)] for i, a in enumerate(anchors)],
    "n_candidates": len(anchors),
    "after_conf": [[*map(lambda v: round(v, 1), xyxy[i].tolist()), round(float(conf[i]), 2), int(cls[i])] for i in keep_conf],
    "after_nms": [[*map(lambda v: round(v, 1), b), round(c, 2), int(k), bool(f)]
                  for b, c, k, f in zip(final.xyxy.tolist(), final.conf.tolist(), final.cls.tolist(), flags)],
    "gt": [[*b, c] for b, c in zip(g, gc)],
}

# ── 1교시: W·H 순서 실수 (정답 박스 3개) ──
gt = pd.read_csv(DATA / "boxes_gt.csv")
scene = cv2.imread(str(DATA / "scene.png"))
Hs, Ws = scene.shape[:2]
boxes = torch.tensor(gt[["x1", "y1", "x2", "y2"]].to_numpy(), dtype=torch.float32)
from torchvision.ops import box_convert  # noqa: E402  (핵심 코드와 같은 함수)
cxcywh = box_convert(boxes, in_fmt="xyxy", out_fmt="cxcywh")
right = cxcywh / torch.tensor([Ws, Hs, Ws, Hs])
wrong = cxcywh / torch.tensor([Hs, Ws, Hs, Ws])
back = box_convert(wrong * torch.tensor([Ws, Hs, Ws, Hs]), in_fmt="cxcywh", out_fmt="xyxy")
facts["wh_swap"] = {
    "image": b64png(scene), "W": Ws, "H": Hs,
    "gt": [[*b, int(c)] for b, c in zip(boxes.tolist(), gt.class_id)],
    "back": [[round(v, 1) for v in b] for b in back.tolist()],
    "iou": [round(float(box_iou(boxes[[i]], back[[i]])[0, 0]), 2) for i in range(len(boxes))],
    "label_right": [round(v, 6) for v in right[0].tolist()],
}

# ── 2교시: 손 예제 매칭 (예측 4 · 정답 3) ──
fx = pd.read_csv(DATA / "boxes_fixture.csv")
pb = torch.tensor(fx[["x1", "y1", "x2", "y2"]].to_numpy(), dtype=torch.float32)
iou_tab = box_iou(pb, boxes)
flags, m = match(pb.tolist(), fx.class_id.tolist(), fx.confidence.tolist(), boxes.tolist(), gt.class_id.tolist())
flags95, m95 = match(pb.tolist(), fx.class_id.tolist(), fx.confidence.tolist(), boxes.tolist(), gt.class_id.tolist(), 0.95)
facts["fixture"] = {
    "pred": [[*b, float(c), int(k), round(float(iou_tab[i].max()), 3), bool(f)]
             for i, (b, c, k, f) in enumerate(zip(pb.tolist(), fx.confidence, fx.class_id, flags))],
    "tp": m, "fp": len(fx) - m, "fn": len(gt) - m, "tp95": m95,
}

# ── 3교시: 분할 단위, Negative image ──
man = pd.read_csv(DATA / "manifest.csv")
dev = man[man.split != "test"].reset_index(drop=True)
groups = sorted(dev.group_id.unique())
cut = int(len(groups) * 0.75)
dev["group_split"] = dev.group_id.map({g_: ("train" if i < cut else "val") for i, g_ in enumerate(groups)})
dev["image_split"] = ["train" if i % 2 == 0 else "val" for i in range(len(dev))]
facts["split"] = {
    "groups": [[g_, dev[dev.group_id == g_].group_split.tolist(), dev[dev.group_id == g_].image_split.tolist()] for g_ in groups],
    "cross_group": int((dev.groupby("group_id").group_split.nunique() > 1).sum()),
    "cross_image": int((dev.groupby("group_id").image_split.nunique() > 1).sum()),
}
neg = man[(man.objects == 0) & (man.split == "val")].iloc[0]
facts["negative"] = {"image": b64png(cv2.imread(str(DATA / neg.image))), "name": neg.image_id,
                     "label_bytes": (DATA / neg.label).stat().st_size,
                     "counts": man[man.objects == 0].groupby("split").size().to_dict()}

# ── 7교시: 추적 (핵심 코드 그대로, tracker 기본 conf) ──
video = str(DATA / "demo.avi")
track_gt = pd.read_csv(DATA / "track_ground_truth.csv")


def track_ids(m, **kw):
    rows = []
    for f, r in enumerate(m.track(video, tracker="bytetrack.yaml", stream=True, verbose=False, **kw)):
        if r.boxes and r.boxes.is_track:
            ids = r.boxes.id.int().cpu().tolist()
            g_ = track_gt[track_gt.frame == f]
            ov = box_iou(r.boxes.xyxy.cpu(), torch.tensor(g_[["x1", "y1", "x2", "y2"]].to_numpy(), dtype=torch.float32))
            for i, tid in enumerate(ids):
                j = int(ov[i].argmax())
                obj = int(g_.iloc[j].gt_id) if float(ov[i, j]) >= 0.5 else 0
                rows.append([f, tid, obj])
    return rows


tm = YOLO(best_w)
first = track_ids(tm)
second = track_ids(tm, persist=True)
fresh = track_ids(YOLO(best_w))
facts["track"] = {
    "frames": int(track_gt.frame.max()) + 1, "objects": int(track_gt.gt_id.nunique()),
    "obj_class": {int(k): NAMES[int(v)] for k, v in track_gt.groupby("gt_id").class_id.first().items()},
    "rows": first,
    "ids_first": sorted({r[1] for r in first}), "ids_second_persist": sorted({r[1] for r in second}),
    "ids_fresh": sorted({r[1] for r in fresh}),
}

facts["env"] = {"ultralytics": __import__("ultralytics").__version__, "torch": torch.__version__, "opencv": cv2.__version__}
(OUT / "facts.json").write_text(json.dumps(facts, ensure_ascii=False), encoding="utf-8")
summary = {k: facts[k] for k in ("train_seconds", "epoch1", "best_epoch", "last_epoch", "val", "eval95")}
summary["conf"] = [r for r in facts["conf_sweep"] if r["conf"] in (0.25, 0.5, 0.9)]
summary["nms"] = [r for r in facts["nms_sweep"] if r["iou"] in (0.5, 0.7, 0.95)]
summary["funnel"] = [facts["funnel"]["n_candidates"], len(facts["funnel"]["after_conf"]), len(facts["funnel"]["after_nms"]),
                     [b[-1] for b in facts["funnel"]["after_nms"]]]
summary["wh_iou"] = facts["wh_swap"]["iou"]
summary["fixture"] = {k: facts["fixture"][k] for k in ("tp", "fp", "fn", "tp95")}
summary["split"] = [facts["split"]["cross_group"], facts["split"]["cross_image"]]
summary["track"] = {k: facts["track"][k] for k in ("ids_first", "ids_second_persist", "ids_fresh")}
print(json.dumps(summary, ensure_ascii=False, indent=1))
