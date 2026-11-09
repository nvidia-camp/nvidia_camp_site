# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright", "pillow"]
# ///
"""각 페이지의 첫 화면을 미리보기 이미지(thumb.jpg)로 저장한다.

사용: uv run make_thumbs.py          (site 폴더에서, 바뀐 페이지만)
      uv run make_thumbs.py --all    (전부 다시)

- pages/*/*/index.html을 1280×800 화면으로 열어 첫 화면을 560×350 JPEG로 줄인다.
- index.html이 thumb.jpg보다 새로울 때만 다시 만든다.
- 시스템 Chrome을 쓴다. 경로는 환경 변수 CHROME으로 바꿀 수 있다.
"""
import io
import os
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
redo_all = "--all" in sys.argv

targets = []
for page in sorted((HERE / "pages").glob("*/*/index.html")):
    thumb = page.parent / "thumb.jpg"
    if redo_all or not thumb.exists() or thumb.stat().st_mtime < page.stat().st_mtime:
        targets.append((page, thumb))

if not targets:
    print("바뀐 페이지 없음")
    sys.exit()

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME)
    tab = browser.new_page(viewport={"width": 1280, "height": 800})
    for page, thumb in targets:
        tab.goto(page.as_uri())
        tab.wait_for_timeout(300)
        shot = Image.open(io.BytesIO(tab.screenshot())).convert("RGB")
        small = shot.resize((560, 350), Image.LANCZOS)
        small.save(thumb, "JPEG", quality=72, optimize=True)
        print(f"{thumb.relative_to(HERE)}  {thumb.stat().st_size // 1024} KB")
