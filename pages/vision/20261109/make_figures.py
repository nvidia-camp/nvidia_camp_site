"""Day16 oneday 요약 실측: 핵심 코드와 같은 데이터로 OCR·VLM을 실제로 돌려 facts.json을 만든다.

실행 (Tesseract 엔진 필요, VLM 모델은 처음 한 번 내려받음):
  uv run --project ~/envs/dl --with opencv-python-headless --with pytesseract \
      --with scikit-image --with jiwer python make_figures.py
"""
import base64
import json
import re
from pathlib import Path

import cv2
import jiwer
import numpy as np
import pytesseract
import skimage
import torch
import transformers
from skimage import data
from transformers import pipeline

HERE = Path(__file__).resolve().parent
WORK = HERE / "_work"                     # 실행 중 만든 이미지 (배포 대상 아님)
WORK.mkdir(exist_ok=True)
MODEL_ID = "HuggingFaceTB/SmolVLM-256M-Instruct"


def png(img, width=None):
    """이미지를 base64 PNG 데이터 URI로. width를 주면 비율 유지 축소."""
    if width and img.shape[1] > width:
        h = round(img.shape[0] * width / img.shape[1])
        img = cv2.resize(img, (width, h), interpolation=cv2.INTER_AREA)
    ok, buf = cv2.imencode(".png", img)
    assert ok
    return "data:image/png;base64," + base64.b64encode(buf.tobytes()).decode()


def clean(s):
    return " ".join(s.split())


def ocr(img, psm=6):
    return pytesseract.image_to_string(img, config=f"--psm {psm}")


FIELDS = {"issued_at": r"^DATE: (\d{4}-\d{2}-\d{2})$", "supplier": r"^SUPPLIER: (.+)$",
          "total_amount": r"^TOTAL: (\d+)$"}


def fields_of(text):
    """핵심 코드와 같은 방식(라벨 줄 정규식)으로 필드 3개를 꺼낸다."""
    out = {}
    for name, pat in FIELDS.items():
        m = re.search(pat, text, re.MULTILINE)
        out[name] = m.group(1).strip() if m else None
    return out


# ── 핵심 코드와 같은 데이터 ──
page = data.page()
PAGE_TEXT = """Region-based segmentation
Let us first determine markers of the coins and the
background. These markers are pixels that we can label
unambiguously as either object or background. Here,
the markers are found at the two extreme parts of the
histogram of grey values:
>>> markers = np.zeros_like(coins)"""
lines = ["INVOICE DOC03", "DATE: 2026-11-03", "SUPPLIER: ALPHA STUDIO", "PRINT 4 3000 12000",
         "FRAME 1 9000 9000", "PAPER 3 4000 12000", "TOTAL: 33000"]
TRUTH = {"issued_at": "2026-11-03", "supplier": "ALPHA STUDIO", "total_amount": "33000"}
truth = " ".join(lines)
invoice = np.full((480, 700, 3), 255, np.uint8)
for i, line in enumerate(lines):
    cv2.putText(invoice, line, (40, 60 + 55 * i), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
corners = np.float32([[60, 40], [690, 10], [720, 470], [20, 450]])
dst = np.float32([[0, 0], [699, 0], [699, 479], [0, 479]])
photo = cv2.warpPerspective(invoice, cv2.getPerspectiveTransform(dst, corners), (760, 500))
M = cv2.getPerspectiveTransform(corners, dst)
warped = cv2.warpPerspective(photo, M, (700, 480))
cv2.imwrite(str(WORK / "invoice.png"), warped)

F = {}


def page_cer(img):
    return round(jiwer.cer(clean(PAGE_TEXT), clean(ocr(img))), 4)


def inv_eval(img, psm=6):
    t = ocr(img, psm)
    f = fields_of(t)
    return {"cer": round(jiwer.cer(truth, clean(t)), 4), "fields": sum(f[k] == TRUTH[k] for k in TRUTH),
            "values": f, "text": t.strip()}


# ── 1교시: 이진화 (스캔 페이지) ──
otsu_t, otsu = cv2.threshold(page, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
adaptive = cv2.adaptiveThreshold(page, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 11)
F["page"] = {"shape": list(page.shape), "gray_cer": page_cer(page), "otsu_t": float(otsu_t),
             "otsu_cer": page_cer(otsu), "adaptive_cer": page_cer(adaptive),
             "img_gray": png(page), "img_otsu": png(otsu), "img_adaptive": png(adaptive)}
F["block"] = [{"bs": bs, "cer": page_cer(cv2.adaptiveThreshold(page, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                              cv2.THRESH_BINARY, bs, 11))}
              for bs in (3, 15, 31, 101)]
F["C"] = [{"C": c, "cer": page_cer(cv2.adaptiveThreshold(page, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                         cv2.THRESH_BINARY, 31, c))}
          for c in (0, 11, 30, 60)]
try:
    cv2.adaptiveThreshold(page, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 30, 11)
    F["even_block"] = "ok"
except cv2.error:
    F["even_block"] = "error"

# ── 1교시: 원근 보정 (청구서 사진) ──
wrong = corners[[1, 2, 3, 0]]                       # 시작점을 오른쪽 위로 잡음
bad = cv2.warpPerspective(photo, cv2.getPerspectiveTransform(wrong, dst), (700, 480))
swap = cv2.warpPerspective(photo, cv2.getPerspectiveTransform(corners[[0, 1, 3, 2]], dst), (700, 480))
F["persp"] = {"photo": inv_eval(photo), "warped": inv_eval(warped), "wrong": inv_eval(bad),
              "swap_cer": inv_eval(swap)["cer"], "swap_visible": round(float((swap.sum(axis=2) > 30).mean()), 2),
              "img_photo": png(photo, 380), "img_warped": png(warped, 350), "img_wrong": png(bad, 350),
              "photo_size": [760, 500], "warped_shape": list(warped.shape)}

# ── 2교시: OCR 단어 표 ──
words = pytesseract.image_to_data(warped, config="--psm 6", output_type=pytesseract.Output.DATAFRAME)
words = words[words.conf >= 0]
F["words"] = [{"text": str(r.text), "conf": round(float(r.conf), 1),
               "box": [int(r.left), int(r.top), int(r.width), int(r.height)],
               "correct": str(r.text) in truth.split()} for r in words.itertuples()]
F["review"] = {th: int((words.conf < th).sum()) for th in (50, 90)}
F["psm"] = {p: inv_eval(warped, p) for p in (6, 7, 8)}
tot = words[words.text == "TOTAL:"].iloc[0]
same_line = words[(words.block_num == tot.block_num) & (words.par_num == tot.par_num)
                  & (words.line_num == tot.line_num)]
x1, y1 = int(same_line.left.min()) - 8, int(same_line.top.min()) - 8
x2 = int((same_line.left + same_line.width).max()) + 8
y2 = int((same_line.top + same_line.height).max()) + 8
crop = warped[max(y1, 0):y2, max(x1, 0):x2]
F["crop_psm"] = {p: ocr(crop, p).strip() for p in (7, 8)}

# 좌표 되돌리기: 보정본 Box의 왼쪽 위 점 → 사진 좌표
pt = np.float32([[[tot.left, tot.top]]])
back = cv2.perspectiveTransform(pt, np.linalg.inv(M)).reshape(-1)
pw = pytesseract.image_to_data(photo, config="--psm 6", output_type=pytesseract.Output.DATAFRAME)
pt_photo = pw[pw.text == "TOTAL:"].iloc[0]
F["box_back"] = {"warped": [int(tot.left), int(tot.top)], "back": [round(float(v), 1) for v in back],
                 "photo": [int(pt_photo.left), int(pt_photo.top)]}

# ── 3교시: 구조화 ──
text = ocr(warped)
F["text"] = text.strip()
F["cer"] = round(jiwer.cer(truth, clean(text)), 4)
raw = re.search(r"^TOTAL: (\d+)$", text, re.MULTILINE).group(1)
row = words[words.text == raw].iloc[0]
F["total"] = {"raw": raw, "conf": round(float(row.conf), 1),
              "box": [int(row.left), int(row.top), int(row.width), int(row.height)]}
F["first_number"] = re.search(r"(\d+)", text).group(1)
F["no_multiline"] = re.search(r"^TOTAL: (\d+)$", text) is None
amounts = re.findall(r"^[A-Z]+ \d+ \d+ (\d+)$", text, re.MULTILINE)
F["amounts"] = amounts
misread = text.replace("TOTAL: 33000", "TOTAL: 38000")
mis_total = int(re.search(r"^TOTAL: (\d+)$", misread, re.MULTILINE).group(1))
F["misread_reason"] = "total_mismatch" if sum(int(a) for a in amounts) != mis_total else None

# 저해상도: 줄였다가 그대로 / 2배 확대
F["lowres"] = []
for s in (0.5, 0.4):
    lo = cv2.resize(warped, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    up = cv2.resize(lo, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    a, b = inv_eval(lo), inv_eval(up)
    sup_line = next((ln for ln in a["text"].splitlines() if "SUPPLIER" in ln), "")
    F["lowres"].append({"scale": s, "size": [lo.shape[1], lo.shape[0]], "cer": a["cer"], "fields": a["fields"],
                        "missing": [k for k, v in a["values"].items() if v != TRUTH[k]],
                        "supplier_line": sup_line, "x2_cer": b["cer"], "x2_fields": b["fields"]})

# ── 4·5교시: 실제 VLM ──
pipe = pipeline("image-text-to-text", model=MODEL_ID)


def ask(question, max_new_tokens=128):
    messages = [{"role": "user", "content": [
        {"type": "image", "path": str(WORK / "invoice.png")},
        {"type": "text", "text": question}]}]
    out = pipe(text=messages, max_new_tokens=max_new_tokens, do_sample=False, return_full_text=False)
    return out[0]["generated_text"].strip()


QUESTIONS = [("합계", "What is the total amount?", raw),
             ("공급자", "What is the supplier name?", fields_of(text)["supplier"]),
             ("발행일", "What is the issue date?", fields_of(text)["issued_at"]),
             ("세금", "What is the tax amount?", None),
             ("할인액", "What is the discount amount?", None),
             ("전화번호", "What is the supplier phone number?", None)]
F["vlm"] = []
for label, q, ocr_value in QUESTIONS:
    a = ask(q)
    F["vlm"].append({"label": label, "question": q, "answer": a, "ocr": ocr_value,
                     "adopted": ocr_value is not None and a == ocr_value})
F["vlm_null"] = ask("What is the tax amount? If it is not written, answer null.")
F["vlm_tokens3"] = ask("What is the total amount?", max_new_tokens=3)
reply = ask("Return JSON with keys answer and evidence. What is the total?")
try:
    parsed = json.loads(reply)
except json.JSONDecodeError:
    parsed = None
F["vlm_json"] = {"reply": reply, "has_keys": isinstance(parsed, dict) and "evidence" in parsed}

F["env"] = {"tesseract": str(pytesseract.get_tesseract_version()), "opencv": cv2.__version__,
            "skimage": skimage.__version__, "transformers": transformers.__version__,
            "torch": torch.__version__, "jiwer": jiwer.__version__ if hasattr(jiwer, "__version__") else "",
            "model": MODEL_ID, "device": str(pipe.device)}

(HERE / "facts.json").write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("facts.json", len(json.dumps(F)) // 1024, "KB")
print({k: F["page"][k] for k in ("gray_cer", "otsu_t", "otsu_cer", "adaptive_cer")}, F["block"], F["C"])
print({k: (v["cer"], v["fields"]) for k, v in F["persp"].items() if isinstance(v, dict)})
print("psm", {p: (v["cer"], v["text"][:20]) for p, v in F["psm"].items()}, F["crop_psm"])
print("review", F["review"], [w for w in F["words"] if not w["correct"]], "cer", F["cer"], F["total"])
print("regex", F["first_number"], F["no_multiline"], F["misread_reason"], "box", F["box_back"])
print("lowres", [{k: v for k, v in r.items() if k != "supplier_line"} for r in F["lowres"]])
print("vlm", [(v["label"], v["answer"], v["adopted"]) for v in F["vlm"]], F["vlm_null"], F["vlm_tokens3"], F["vlm_json"])
