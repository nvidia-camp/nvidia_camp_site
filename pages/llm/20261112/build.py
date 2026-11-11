"""Day19-1 오전 실습 가이드: template.html에 사진과 그래프를 넣어 index.html을 만든다.

- {{IMG:이름}}  → img/이름.webp 를 data URI로
- {{SVG:이름}}  → diagrams/이름.svg 를 인라인으로 (mermaid 기본 id를 그래프마다 바꿔 스타일 충돌을 막는다)

그래프를 고칠 때: diagrams/*.mmd 수정 후
  npx -y @mermaid-js/mermaid-cli@11.4.2 -c diagrams/cfg.json -b transparent -i diagrams/api.mmd -o diagrams/api.svg
실행: uv run build.py
"""
import base64
import re
import struct
from pathlib import Path

HERE = Path(__file__).parent


def img(name):
    data = base64.b64encode((HERE / "img" / f"{name}.webp").read_bytes()).decode("ascii")
    return f"data:image/webp;base64,{data}"


def webp_size(path):
    """WebP(VP8/VP8L/VP8X) 헤더에서 가로·세로를 읽는다."""
    b = path.read_bytes()
    kind = b[12:16]
    if kind == b"VP8X":
        return 1 + int.from_bytes(b[24:27], "little"), 1 + int.from_bytes(b[27:30], "little")
    if kind == b"VP8L":
        bits = struct.unpack("<I", b[21:25])[0]
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    w, h = struct.unpack("<HH", b[26:30])
    return w & 0x3FFF, h & 0x3FFF


def img_tag(m):
    """<img src="{{IMG:이름}}" → data URI + 표시 크기. api_* 는 2배로 찍은 화면이라 절반 크기로 보인다."""
    name = m.group(1)
    w, h = webp_size(HERE / "img" / f"{name}.webp")
    scale = 2 if name.startswith("api_") else 1
    return f'<img src="{img(name)}" width="{w // scale}" height="{h // scale}"'


def svg(name):
    text = (HERE / "diagrams" / f"{name}.svg").read_text(encoding="utf-8")
    return text.replace("my-svg", f"g-{name}")


html = (HERE / "template.html").read_text(encoding="utf-8")
html = re.sub(r'<img src="\{\{IMG:(\w+)\}\}"', img_tag, html)
html = re.sub(r"\{\{SVG:(\w+)\}\}", lambda m: svg(m.group(1)), html)
left = re.findall(r"\{\{[^}]+\}\}", html)
assert not left, left
(HERE / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html) // 1024, "KB")
