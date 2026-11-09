# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""template.html + facts.json → index.html

- 그림(SVG 안의 실제 실행 이미지와 Box)과 답 코드를 facts.json에서 채운다.
- 날짜 글자색이 흰 글자와 4.5:1 이상 대비인지 검사한다.

사용: uv run build.py   (all 폴더에서, make_figures.py 다음)
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
facts = json.loads((HERE / "facts.json").read_text())
html = (HERE / "template.html").read_text()


def num(x, digits=2):
    """숫자 표기를 한 곳에서 통일한다. 1.0을 "1"로, 0.40을 "0.4"로 줄이지 않는다."""
    return f"{x:.{digits}f}" if digits > 1 else f"{x:.1f}"


def half_up(x):
    return int(x + 0.5)


# ── 날짜 색 대비 검사 ─────────────────────────────────────────────────────
def luminance(hex_color):
    rgb = []
    for i in (1, 3, 5):
        c = int(hex_color[i:i + 2], 16) / 255
        rgb.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]


for name, color in re.findall(r"--(ink1[3-6]): (#[0-9A-Fa-f]{6})", html):
    ratio = 1.05 / (luminance(color) + 0.05)
    assert ratio >= 4.5, f"{name} {color} 대비 {ratio:.2f}"
    print(f"{name} {color} 흰 글자 대비 {ratio:.2f}:1")

# ── Day13: 합성 제품 사진 + 칸 하나 ───────────────────────────────────────
d13 = facts["d13"]
px, py = d13["pixel_xy"]
b, g, r = d13["pixel_bgr"]
assert (px, py) == (64, 52) and [b, g, r] == [52, 136, 214]
fig13 = f"""<svg viewBox="0 0 320 240" role="img" aria-label="합성 제품 사진과 확대한 픽셀 1개">
  <image href="{d13['image']}" x="0" y="0" width="320" height="240"/>
  <rect x="{px - 5}" y="{py - 5}" width="10" height="10" fill="none" stroke="#fff" stroke-width="2"/>
  <line x1="{px + 5}" y1="{py - 3}" x2="262" y2="34" stroke="#fff" stroke-width="1.5"/>
  <rect x="262" y="8" width="50" height="50" rx="4" fill="rgb({r},{g},{b})" stroke="#fff" stroke-width="2.5"/>
  <text x="287" y="72" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">픽셀 1개</text>
</svg>"""
px13 = f"[{b}, {g}, {r}]"

# ── Day14: 분류 샘플 한 장 ────────────────────────────────────────────────
d14 = facts["d14"]
assert d14["label"] in d14["classes"]
fig14 = f"""<svg viewBox="0 0 160 120" role="img" aria-label="triangle 샘플 이미지">
  <image href="{d14['image']}" x="26" y="12" width="96" height="96" style="image-rendering:pixelated"/>
  <rect x="26" y="12" width="96" height="96" fill="none" stroke="#D8E4F2"/>
</svg>"""

# ── Day15: 탐지 장면 + conf 0.5 이상 Box ──────────────────────────────────
d15 = facts["d15"]
assert len(d15["boxes"]) == 3
rects = []
lines15 = []
for box in d15["boxes"]:
    x1, y1, x2, y2 = box["xyxy"]
    label = f"{box['name']} {num(box['conf'])}"
    rects.append(
        f'<rect x="{x1}" y="{y1}" width="{x2 - x1:.1f}" height="{y2 - y1:.1f}" fill="none" stroke="#5B4A8E" stroke-width="1.4"/>'
        f'<rect x="{x1 - 0.7}" y="{y1 - 9}" width="{len(label) * 4.1 + 4:.1f}" height="8.5" fill="#5B4A8E"/>'
        f'<text x="{x1 + 1.3}" y="{y1 - 2.4}" font-size="6.6" font-weight="700" fill="#fff">{label}</text>'
    )
    xyxy = ",".join(str(half_up(v)) for v in box["xyxy"])
    lines15.append(f'<span class="s">{box["name"]:<8}</span> <span class="n">{num(box["conf"])}</span> [{xyxy}]')
fig15 = f"""<svg viewBox="0 -4 {d15['W']} {d15['H'] + 4}" role="img" aria-label="도형 장면의 탐지 결과 Box 3개">
  <image href="{d15['image']}" x="0" y="0" width="{d15['W']}" height="{d15['H']}"/>
  {''.join(rects)}
</svg>"""
ans15 = "\n".join(lines15)

# ── Day16: 정면 보정한 청구서 + 합계 줄 단어 Box ──────────────────────────
d16 = facts["d16"]
words = {w["text"]: w for w in d16["words"]}
total = words["33000"]
rects16 = []
for w in d16["words"]:
    left, top, width, height = w["box"]
    rects16.append(f'<rect x="{left - 4}" y="{top - 4}" width="{width + 8}" height="{height + 8}" rx="3" fill="none" stroke="#245C9C" stroke-width="4"/>')
left, top, width, height = total["box"]
rects16.append(f'<rect x="{left + width + 10}" y="{top - 3}" width="98" height="27" rx="4" fill="#245C9C"/>'
               f'<text x="{left + width + 59}" y="{top + 16}" text-anchor="middle" font-size="17" font-weight="700" fill="#fff">conf {num(total["conf"], 1)}</text>')
fig16 = f"""<svg viewBox="10 140 400 300" role="img" aria-label="정면 보정한 청구서와 합계 줄의 단어 Box">
  <image href="{d16['image']}" x="0" y="0" width="{d16['W']}" height="{d16['H']}"/>
  {''.join(rects16)}
</svg>"""
box16 = ", ".join(str(v) for v in total["box"])
ans16 = (f'{{<span class="k">"raw"</span>: <span class="s">"{total["text"]}"</span>, '
         f'<span class="k">"value"</span>: <span class="n">{int(total["text"])}</span>,\n'
         f' <span class="k">"conf"</span>: <span class="n">{num(total["conf"], 1)}</span>,\n'
         f' <span class="k">"box"</span>: [{box16}]}}')

fill = {
    "FIG13": fig13, "PX13": px13, "FIG14": fig14, "FIG15": fig15, "ANS15": ans15,
    "FIG16": fig16, "ANS16": ans16,
}
for key, value in fill.items():
    assert "{{" + key + "}}" in html, key
    html = html.replace("{{" + key + "}}", value)
assert "{{" not in html, re.findall(r"\{\{\w+\}\}", html)

(HERE / "index.html").write_text(html)
print("index.html", len(html) // 1024, "KB")
