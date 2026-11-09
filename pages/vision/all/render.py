# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright"]
# ///
"""index.html → 배포용 PDF(1440px 폭 세로 한 장) + 화면 폭 검증.

사용:
  uv run render.py <index.html> <출력 PDF> [스크린샷 폴더]

- 375·768·1280·1440px에서 가로 넘침(px)과 스크립트 오류를 출력하고,
  스크린샷 폴더를 주면 전체 페이지 스크린샷을 저장합니다.
- PDF는 1440px 폭에서 <html>에 'pdf' 클래스를 붙인 뒤 문서 높이 그대로 한 쪽에 출력합니다.
- 시스템 Chrome을 사용합니다. 경로는 환경 변수 CHROME으로 바꿀 수 있습니다.
"""
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

if len(sys.argv) < 3:
    sys.exit(__doc__)
HTML = Path(sys.argv[1]).resolve()
PDF = Path(sys.argv[2]).resolve()
SHOTS = Path(sys.argv[3]).resolve() if len(sys.argv) > 3 else None
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME)
    errors = []
    for w in (375, 768, 1280, 1440):
        page = browser.new_page(viewport={"width": w, "height": 900})
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(HTML.as_uri())
        over = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        height = page.evaluate("document.documentElement.scrollHeight")
        print(f"{w}px: 가로 넘침 {over}px, 높이 {height}px")
        if SHOTS:
            SHOTS.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(SHOTS / f"w{w}.png"), full_page=True)
        page.close()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(HTML.as_uri())
    page.evaluate("document.documentElement.classList.add('pdf')")
    page.emulate_media(media="screen")
    h = page.evaluate("Math.ceil(document.documentElement.scrollHeight)")
    page.pdf(path=str(PDF), width="1440px", height=f"{h + 2}px", print_background=True,
             margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    print(f"PDF {PDF.name}: 높이 {h}px · 스크립트 오류 {errors or '없음'}")
    browser.close()
