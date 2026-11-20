"""Day25 3번 탭 'Basic 완주 안내' 만들기.

원본: nvidia_camp/05_LLM_RAG/20261120/안내서.html (강사님 자료, 읽기만 한다)
결과: 이 폴더의 index.html

본문 글자는 한 글자도 바꾸지 않는다. 바꾸는 것은 아래뿐이다.
  1. 원본 목차 <nav>에 class="toc"를 붙이고 CSS의 nav 규칙을 nav.toc로 좁힌다
     (사이트 위쪽 메뉴 nav.cn-nav에 원본 규칙이 걸리지 않게)
  2. 머리말 아래에 Day25 탭 줄(1 사전 준비 · 2 요구사항 명세서 · 3 Basic 완주 안내)을 넣는다
  3. 다크 모드 CSS와 접힌 코드(<details>)를 눈에 띄게 하는 CSS를 덧붙인다
  4. 작성자 개인 ChatGPT 라이브러리 링크 3개는 <a>만 벗겨 글자로 남긴다 (학생은 열 수 없는 주소)

실행: python3 make_page.py
"""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[4] / "05_LLM_RAG" / "20261120" / "안내서.html"
OUT = HERE / "index.html"


def replace_once(text: str, old: str, new: str) -> str:
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"'{old[:60]}' 이(가) {n}번 나옴 (1번이어야 함). 원본이 바뀌었는지 확인하세요.")
    return text.replace(old, new)


TABS_CSS = """
:root{--tab-bg:#ffffff;--tab-border:#cbd7e3;--tab-fg:#162237;--tab-n-bg:#e7eef6;--tab-n-fg:#172d49;
  --tab-act-bg:#172d49;--tab-act-fg:#ffffff;--tab-lec-bg:#eef6ff;--tab-lec-border:#b8d0e9;--tab-lec-fg:#124d8a}
.tabs-wrap{max-width:1220px;margin:18px auto 0;padding:0 20px}
.tabs{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.tabs a{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:6px 15px 6px 8px;border:1px solid var(--tab-border);border-radius:999px;background:var(--tab-bg);color:var(--tab-fg);text-decoration:none;font-size:15px;font-weight:650;line-height:1.5}
.tabs a:hover{border-color:#205a9c;color:var(--tab-fg)}
.tabs .n{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:999px;background:var(--tab-n-bg);color:var(--tab-n-fg);font-size:13px;font-weight:700}
.tabs a[aria-current='page']{background:var(--tab-act-bg);border-color:var(--tab-act-bg);color:var(--tab-act-fg)}
.tabs a[aria-current='page'] .n{background:var(--tab-act-fg);color:var(--tab-act-bg)}
.tabs a.lec{margin-left:auto;padding:6px 14px;background:var(--tab-lec-bg);border-color:var(--tab-lec-border);color:var(--tab-lec-fg)}
@media(max-width:720px){.tabs-wrap{padding:0 16px}.tabs a.lec{margin-left:0}}
@media print{.tabs-wrap{display:none}}
"""

# 접힌 전체 코드: 눌러서 펼치는 칸이라는 것이 보이게 (글자는 원본 그대로)
FOLD_CSS = """
.file-card details{border-color:#b8cbe2;border-left:4px solid #214e84;background:#f5f8fc}
.file-card details>summary{list-style:none;display:flex;align-items:center;gap:10px}
.file-card details>summary::-webkit-details-marker{display:none}
.file-card details>summary::before{content:"";flex:none;width:9px;height:9px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(-45deg);transition:transform .15s;margin:0 3px}
.file-card details[open]>summary::before{transform:rotate(45deg)}
.file-card details[open]{background:#fbfcfe}
"""

DARK_CSS = """
@media (prefers-color-scheme:dark){
:root{color-scheme:dark;--ink:#e5eaf2;--sub:#9ab6d4;--blue:#93c5fd;--teal:#7fd3c4;--border:#29384e;--paper:#102137;--wash:#0b1220;--soft:#132a44;--warn:#f3c98b;--warn-bg:#2b2112;
  --tab-bg:#102137;--tab-border:#35536d;--tab-fg:#e5eaf2;--tab-n-bg:#1c3554;--tab-n-fg:#93c5fd;
  --tab-act-bg:#93c5fd;--tab-act-fg:#0b1220;--tab-lec-bg:#132c45;--tab-lec-border:#3b6182;--tab-lec-fg:#b4d9f5}
a{color:#93c5fd}a:hover{color:#bfdbfe}
header{background:#0f2139;border-bottom:1px solid #2d4863}header .eyebrow{color:#95b9d5}header p{color:#bcd1e0}
.meta span{background:#1c3554;border-color:#3b6182}
nav.toc{background:#102137;border-bottom-color:#29384e;box-shadow:0 3px 12px #00000040}
section{box-shadow:none}
.legend span{background:#12302c;color:#bfe7de;border-color:#2c5a52}
blockquote{background:#10292a;color:#cdeee6}blockquote span{color:#8fd3c3}
.note{background:#112438;border-color:#2d4863}.note strong{color:#b4d9f5}
.attention{border-color:#6b5224}.attention strong{color:#f3c98b}
.gate{background:#10292a;color:#a8e3d6;border-top-color:#2c5a52}
th,td{border-right-color:#29384e;border-bottom-color:#29384e}th{background:#17304a;color:#e3f4ff}tbody tr:nth-child(even){background:#0f1e31}
code{background:#172940;color:#9fe4d1}
pre{background:#091321;color:#ccdfef;border-color:#2c4560}pre:before{color:#7fb3e0}
details{background:#0f1e31;border-color:#2d4863}summary{color:#b4d9f5}details[open] summary{border-bottom-color:#29384e}
.todo{border-top-color:#29384e}.todo .tag{color:#7fd3c4}.todo details{background:#0f1e31}
.file-card{background:#102137;border-color:#35536d}.file-meta,.small,.copy-status{color:#9ab6d4}.replace{color:#f3c98b}
.copy-button{background:#93c5fd;border-color:#93c5fd;color:#0b1220}.copy-button:hover{background:#bfdbfe}
.checkline{background:#10292a;border-color:#2c5a52}.checkline input{accent-color:#7fd3c4}.phase-status{color:#a8e3d6}
.request-card{border-top-color:#2d4863}.request-card .request-no{color:#7fd3c4}
.manual{background:#2b2112;border-color:#6b5224}
.empty-file{background:#0f1e31;border-color:#3b6182}
.file-card details{background:#0d1b2c;border-color:#3b6182;border-left-color:#93c5fd}.file-card details[open]{background:#0f1e31}
}
"""

TABS_HTML = (
    '<div class="tabs-wrap"><nav class="tabs" aria-label="Day25 문서 탭">'
    '<a data-site href="../"><span class="n">1</span>사전 준비</a>'
    '<a data-site href="../spec/"><span class="n">2</span>요구사항 명세서</a>'
    '<a data-site href="./" aria-current="page"><span class="n">3</span>Basic 완주 안내</a>'
    '<a class="lec" data-site href="../lecture/">오전 강의 자료 →</a>'
    '</nav></div>'
)


def main() -> None:
    s = SRC.read_text(encoding="utf-8")

    # 1. 원본 목차만 가리키도록 nav 규칙을 좁힌다 (사이트 위쪽 메뉴는 sticky top:0이라 그 아래에 붙인다)
    s = replace_once(s, "nav{position:sticky;top:0;z-index:10;background:#fff;",
                     "nav.toc{position:sticky;top:48px;z-index:10;background:#fff;")
    s = replace_once(s, "nav a{font-size:13px;", "nav.toc a{font-size:13px;")
    s = replace_once(s, "nav a:hover{", "nav.toc a:hover{")
    s = replace_once(s, "nav{position:static;justify-content:flex-start}", "nav.toc{position:static;justify-content:flex-start}")
    s = replace_once(s, "nav{display:none}", "nav.toc{display:none}")
    s = replace_once(s, "nav{justify-content:flex-start}", "nav.toc{justify-content:flex-start}")
    s = replace_once(s, '<nav aria-label="목차">', '<nav class="toc" aria-label="목차">')

    # 2. 탭 줄
    s = replace_once(s, "</header>", "</header>" + TABS_HTML)

    # 3. 덧붙이는 CSS
    s = replace_once(s, "</style></head>", TABS_CSS + FOLD_CSS + DARK_CSS + "</style></head>")

    # 4. 개인 ChatGPT 라이브러리 링크 → 글자만
    s, n = re.subn(r'<a href="https://chatgpt\.com/[^"]*">(.*?)</a>', r"\1", s, flags=re.S)
    if n != 3:
        raise SystemExit(f"ChatGPT 링크가 {n}개 (3개여야 함). 원본을 확인하세요.")

    OUT.write_text(s, encoding="utf-8")
    print(f"{OUT.relative_to(HERE.parents[3])} ← {SRC.name}")


if __name__ == "__main__":
    main()
