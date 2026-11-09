# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""4일 종합 페이지에 넣을 그림과 숫자를 각 날의 실제 실행 결과에서 모은다.

- Day13: 개념지도의 make_images.py를 다시 실행해 합성 제품 사진과 픽셀 값을 받는다.
- Day14·15·16: 각 날 oneday 요약의 facts.json(실제 실행 결과)에서 이미지와 숫자를 가져온다.

사용: uv run make_figures.py   (site/pages/vision/all 폴더에서)
출력: facts.json
"""
import base64
import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
VISION = HERE.parent          # site/pages/vision
D13 = VISION / "20261104"
D14 = VISION / "20261105/facts.json"
D15 = VISION / "20261106/facts.json"
D16 = VISION / "20261109/facts.json"


def png_uri(path):
    data = base64.b64encode(Path(path).read_bytes()).decode()
    return "data:image/png;base64," + data


# ── Day13: 합성 제품 사진 (개념지도와 같은 스크립트·seed) ─────────────────
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(["uv", "run", "-q", str(D13 / "make_images.py"), tmp], check=True,
                   capture_output=True)
    d13_facts = json.loads((Path(tmp) / "facts.json").read_text())
    d13_img = png_uri(Path(tmp) / "orig.png")

# ── Day14: 분류 샘플 한 장 (triangle) ────────────────────────────────────
d14 = json.loads(D14.read_text())
d14_img = d14["samples"]["triangle"][0]

# ── Day15: 탐지 장면 + NMS 뒤 결과 중 conf 0.5 이상 ─────────────────────
d15 = json.loads(D15.read_text())
funnel = d15["funnel"]
boxes15 = []
for x1, y1, x2, y2, conf, cls, is_tp in funnel["after_nms"]:
    if conf >= 0.5:
        boxes15.append({"xyxy": [x1, y1, x2, y2], "conf": conf, "name": d15["names"][cls]})

# ── Day16: 정면 보정한 청구서 + 합계 줄 단어 Box ─────────────────────────
d16 = json.loads(D16.read_text())
total_words = []
for word in d16["words"]:
    if word["text"] in ("TOTAL:", "33000"):
        total_words.append(word)

facts = {
    "d13": {
        "image": d13_img,
        "shape": [240, 320, 3],
        "pixel_xy": d13_facts["pixel_xy"],
        "pixel_bgr": d13_facts["pixel_bgr"],
    },
    "d14": {"image": d14_img, "label": "triangle", "classes": d14["classes"]},
    "d15": {
        "image": funnel["image"], "W": funnel["W"], "H": funnel["H"],
        "boxes": boxes15,
    },
    "d16": {
        "image": d16["persp"]["img_warped"],
        "W": d16["persp"]["warped_shape"][1], "H": d16["persp"]["warped_shape"][0],
        "words": total_words,
    },
}
(HERE / "facts.json").write_text(json.dumps(facts, ensure_ascii=False, indent=1))
print("Day13 pixel", facts["d13"]["pixel_xy"], facts["d13"]["pixel_bgr"])
print("Day15 boxes", [(b["name"], b["conf"]) for b in boxes15])
print("Day16 words", [(w["text"], w["conf"], w["box"]) for w in total_words])
