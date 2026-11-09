# /// script
# requires-python = ">=3.11"
# dependencies = ["opencv-python-headless<5", "numpy"]
# ///
"""Day13 개념 지도용 합성 사진과 단계별 처리 결과를 만든다.

출력: <out>/*.png 와 <out>/facts.json (지도에 적을 실제 값)
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(13)
H, W = 240, 320


def save(name, img):
    cv2.imwrite(str(OUT / f"{name}.png"), img)


def make_scene(shift=0, dust=True):
    img = np.zeros((H, W, 3), np.float32)
    img[:] = (95, 75, 55)                                   # 어두운 바탕 (BGR)
    x1, y1, x2, y2 = 60 + shift, 50, 250 + shift, 190
    cv2.rectangle(img, (x1, y1), (x2, y2), (40, 140, 230), -1)  # 주황 제품
    cv2.ellipse(img, (190 + shift, 105), (11, 6), 25, 0, 360, (35, 45, 60), -1)  # 흠집
    if dust:                                                # 바탕의 작은 흰 먼지 (5×5)
        for (x, y) in [(22, 30), (35, 210), (285, 40), (300, 160), (270, 215), (120, 222), (20, 120), (295, 100)]:
            img[y:y + 5, x:x + 5] = (250, 250, 250)
        for (x, y) in [(90, 80), (120, 160), (150, 70), (220, 165), (100, 130)]:  # 제품 위 작은 핀홀 (4×4)
            img[y:y + 4, x + shift:x + shift + 4] = (35, 45, 60)
    img += rng.normal(0, 14, img.shape)                     # 고른 잡음
    return np.clip(img, 0, 255).astype(np.uint8)


scene = make_scene()
save("orig", scene)

gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
save("gray", gray)
small = cv2.resize(gray, (160, 120), interpolation=cv2.INTER_AREA)
save("small", small)
blur = cv2.GaussianBlur(small, (5, 5), 0)
save("blur", blur)
ret, binary = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY)
save("binary", binary)
k3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, k3)
save("opened", opened)
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, k3)
save("closed", closed)
morph = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, k3)      # Opening → Closing
save("morph", morph)
edge = cv2.Canny(blur, 70, 150)
save("canny", edge)
edge_noblur = cv2.Canny(small, 70, 150)
save("canny_noblur", edge_noblur)

# 결과: 물체 안의 검은 구멍 = 흠집 후보 (외곽 윤곽 + 안쪽 구멍)
cnts, hier = cv2.findContours(morph, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
result = cv2.resize(scene, (160, 120), interpolation=cv2.INTER_AREA)
holes = []
for i, c in enumerate(cnts):
    if hier[0][i][3] == -1:                                 # 바깥 윤곽 = 제품
        cv2.drawContours(result, [c], -1, (90, 200, 90), 1)
    elif cv2.contourArea(c) >= 20:                           # 안쪽 구멍 = 흠집 후보
        x, y, w, h = cv2.boundingRect(c)
        holes.append([int(x), int(y), int(w), int(h)])
        cv2.rectangle(result, (x - 3, y - 3), (x + w + 2, y + h + 2), (40, 40, 230), 1)
save("result", result)

# 비교용
blur_med = cv2.medianBlur(small, 5)
save("blur_median", blur_med)
for t in (60, 128, 200):
    save(f"thr_{t}", cv2.threshold(blur, t, 255, cv2.THRESH_BINARY)[1])
crop = gray[95:115, 178:202]                                # 흠집 주변 24×20
save("up_nearest", cv2.resize(crop, None, fx=6, fy=6, interpolation=cv2.INTER_NEAREST))
save("up_linear", cv2.resize(crop, None, fx=6, fy=6, interpolation=cv2.INTER_LINEAR))
save("down_skip", small_skip := gray[::2, ::2].copy())
# 먼지 주변 확대 (작은 사진 기준 좌표, 먼지 (300,160) → (150,80))
def zoom(img, x, y, r=10, f=6):
    c = img[max(0, y - r):y + r, max(0, x - r):x + r]
    return cv2.resize(c, None, fx=f, fy=f, interpolation=cv2.INTER_NEAREST)
save("z_small", zoom(small, 150, 80))
save("z_gauss", zoom(blur, 150, 80))
save("z_median", zoom(blur_med, 150, 80))
save("z_bin", zoom(binary, 150, 80))
save("z_open", zoom(opened, 150, 80))
save("zh_bin", zoom(binary, 60, 80))                        # 핀홀 (120,160) → 작은 사진 (60,80)
save("zh_close", zoom(closed, 60, 80))
save("zh_open", zoom(opened, 60, 80))
# Canny: 원본 크기에서 Blur 없이 / 있게 (흠집·제품 가장자리 주변)
cz = (slice(30, 120), slice(150, 270))
save("cz_noblur", cv2.Canny(gray, 70, 150)[cz])
save("cz_blur", cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 70, 150)[cz])

# 입력 확대: 제품 가장자리 8×6 칸
px_y, px_x = 52, 64
zoom_in = scene[px_y - 3:px_y + 3, px_x - 4:px_x + 4]
save("pix_zoom", cv2.resize(zoom_in, None, fx=14, fy=14, interpolation=cv2.INTER_NEAREST))
bgr = scene[px_y, px_x].tolist()

# 영상: 제품이 오른쪽으로 움직이는 Frame 4장
for i, s in enumerate((-40, -20, 0, 20)):
    f = make_scene(shift=s, dust=False)
    save(f"v_in{i}", cv2.resize(f, (96, 72), interpolation=cv2.INTER_AREA))
    fs = cv2.GaussianBlur(cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), (160, 120), interpolation=cv2.INTER_AREA), (5, 5), 0)
    fb = cv2.threshold(fs, 128, 255, cv2.THRESH_BINARY)[1]
    fm = cv2.morphologyEx(cv2.morphologyEx(fb, cv2.MORPH_OPEN, k3), cv2.MORPH_CLOSE, k3)  # 한 장 처리와 같은 상자
    save(f"v_out{i}", cv2.resize(cv2.cvtColor(fm, cv2.COLOR_GRAY2BGR), (96, 72), interpolation=cv2.INTER_AREA))

# 증강
sm = cv2.resize(scene, (160, 120), interpolation=cv2.INTER_AREA)
save("aug_orig", sm)
save("aug_flip", cv2.flip(sm, 1))
M = cv2.getRotationMatrix2D((80, 60), 10, 1.0)
save("aug_rot", cv2.warpAffine(sm, M, (160, 120)))
save("aug_bright", np.clip(sm.astype(np.float32) + 30, 0, 255).astype(np.uint8))
tile = np.full((60, 60, 3), 255, np.uint8)
cv2.putText(tile, "b", (14, 46), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (40, 43, 28), 4, cv2.LINE_AA)
save("aug_b", tile)
save("aug_d", cv2.flip(tile, 1))

facts = {
    "scene_shape": list(scene.shape), "dtype": str(scene.dtype),
    "pixel_xy": [px_x, px_y], "pixel_bgr": bgr,
    "pixel_gray": int(gray[px_y, px_x]),
    "gray_shape": list(gray.shape), "small_shape": list(small.shape),
    "ret": float(ret), "holes": holes,
    "white_binary": int(cv2.countNonZero(binary)), "white_opened": int(cv2.countNonZero(opened)),
    "edge_px_blur": int(cv2.countNonZero(edge)), "edge_px_noblur": int(cv2.countNonZero(edge_noblur)),
    "n_components_binary": int(cv2.connectedComponents(binary)[0] - 1),
    "n_components_opened": int(cv2.connectedComponents(opened)[0] - 1),
    "holes_binary": int(cv2.connectedComponents(255 - binary)[0] - 2),
    "holes_morph": int(cv2.connectedComponents(255 - morph)[0] - 2),
    "edge_full_noblur": int(cv2.countNonZero(cv2.Canny(gray, 70, 150))),
    "cv": cv2.__version__,
    "edge_full_blur": int(cv2.countNonZero(cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 70, 150))),
}
(OUT / "facts.json").write_text(json.dumps(facts, ensure_ascii=False, indent=1))
print(json.dumps(facts, ensure_ascii=False))
