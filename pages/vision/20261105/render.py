# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright"]
# ///
"""index.html → 배포용 PDF(1440px 폭 세로 한 장) + 화면 폭 검증 스크린샷.

실행: uv run render.py [스크린샷 폴더]
시스템 Chrome을 사용합니다.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
URL = (HERE / "index.html").as_uri()
SHOTS = Path(sys.argv[1]) if len(sys.argv) > 1 else None
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME)
    errors = []
    if SHOTS:
        SHOTS.mkdir(parents=True, exist_ok=True)
        for w in (375, 768, 1280, 1440):
            page = browser.new_page(viewport={"width": w, "height": 900})
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(URL)
            over = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            print(f"{w}px: 가로 넘침 {over}px, 높이 {page.evaluate('document.documentElement.scrollHeight')}px")
            page.screenshot(path=str(SHOTS / f"w{w}.png"), full_page=True)
            page.close()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(URL)
    page.evaluate("document.documentElement.classList.add('pdf')")
    page.emulate_media(media="screen")
    h = page.evaluate("Math.ceil(document.documentElement.scrollHeight)")
    page.pdf(path=str(HERE / "Day14_oneday요약.pdf"), width="1440px", height=f"{h + 2}px",
             print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    print("PDF 높이", h, "px", "· 스크립트 오류", errors or "없음")
    browser.close()
