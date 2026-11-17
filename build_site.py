# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""pages/의 요약을 모아 배포용 사이트(public/)를 만든다.

사용: uv run build_site.py   (site 폴더에서)

- 원본은 pages/ 아래에 둔다. 폴더 이름만 맞추면 자동으로 사이트에 들어간다.
    pages/<과목>/<YYYYMMDD>/   매일 요약     → /<과목>/<YYYYMMDD>/  (같은 날 두 번째 회차는 <YYYYMMDD>-2)
    pages/<과목>/all/          과목 4일 종합 → /<과목>/  (없으면 날짜 카드 목록)
    pages/cheatsheet/<이름>/   치트시트      → /cheatsheet/<이름>/ (CHEATSHEETS에 이름·과목 등록)
    pages/setup/<이름>/        설치 가이드   → /setup/<이름>/      (SETUP에 이름·과목·공개 여부 등록)
    pages/setup/<이름>/<하위>/ 가이드 안 페이지 → /setup/<이름>/<하위>/ (SETUP_PAGES에 순서·이름 등록)
    pages/<과목>/<YYYYMMDD>/tree.md  강의 트리(교재 구성) → 요약이 아직 없으면 그날 페이지가 '강의 목차 한눈에 보기'가 된다.
        원본은 작업 폴더의 Day<N>_강의트리.md(또는 Day<N>_강의구조_핵심설명.md)를 복사한 것. 첫 ```text 블록만 읽는다.
- Colab 실습 폴더(Google Drive)는 COLAB에 주소를 등록하면 홈 Day 줄·그날 페이지에 Colab 로고로 나온다.
- 홈: 맨 위 제목·최근 수업·지금 과목 표지 → 100일 일정 → 참고 문서 모음 → 과목별 챕터(Day 목록).
  참고 문서 모음은 공통 묶음(COMMON_GROUPS)별 설치 가이드 칸 + '과목 참고 문서' 칸(치트시트·과목 설치 가이드).
- 본문 글꼴은 Pretendard만: copy_page가 unify_fonts()로 모든 페이지의 비-코드 글꼴 선언 앞에 붙이고, 못 고치면 빌드 끝에 ⚠ 경고만 한다(코드 monospace·강의 원본 lecture는 예외).
- 홈·과목 목록은 Pretendard(OFL, assets/fonts → public/fonts)를 쓴다. 요약 페이지도 같은 Pretendard를 쓴다(--font-body 앞에 두고 /fonts 링크, 2026-11-17).
- 각 폴더의 index.html을 public/에 복사하고, 사이트 메뉴·통계를 뺀 원본을 download.html로 함께 둔다(메뉴의 "HTML 받기"). PDF는 만들지 않는다(2026-11-14 폐지).
- 강사님 강의 HTML(sync_lecture_html.py가 pages/<과목>/<날짜>/lecture/에 옮김)은 원본 그대로 /<과목>/<날짜>/lecture/에
  메뉴 아래 전체 화면으로 띄운다. 홈 Day 줄·Day 페이지 메뉴의 '바로 보기'로 열고, '강의 자료 ↗'는 지금처럼 Slack 링크.
- 복사본에만 위쪽 메뉴를 넣고, 사이트에 없는 파일을 가리키는 상대 링크는 글자만 남긴다.
- Day 번호·날짜·과목·강의 자료 링크는 lectures.json(sync_lectures.py가 학습 자료 시트에서 만듦)에서 읽는다.
- public/은 매번 지우고 새로 만든다. 직접 고치지 않는다. 강의 교재 PDF는 넣지 않는다.
- 공개 전(SETUP의 공개=False) 페이지는 main 빌드에는 들어가고 `--release`로 만들면 빠진다.
  화면에 따로 표시하지 않는다(공개 구분은 main/deploy 브랜치로 한다).
"""
import base64
import datetime
import json
import html
import posixpath
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGES = HERE / "pages"
PUBLIC = HERE / "public"
LECTURES = HERE / "lectures.json"
SITE_NAME = "학습 아카이브"

# 시트의 교과목 → (사이트 경로, 짧은 이름). 경로가 None이면 일정 띠에만 보인다.
SUBJECTS = {
    "AI 교육과정 오리엔테이션": (None, "OT"),
    "AI 개발을 위한 Python 데이터 처리 기초": ("python", "Python"),
    "머신러닝 모델링 및 성능평가": ("ml", "ML"),
    "딥러닝 핵심 아키텍처 및 학습": ("dl", "DL"),
    "직업기초능력평가": (None, "평가"),
    "Vision·멀티모달 AI 응용": ("vision", "Vision"),
    "생성형 AI·LLM 및 RAG 엔지니어링": ("llm", "LLM·RAG"),
    "LLM·RAG 실전 프로젝트": ("llm-project", "LLM·RAG 프로젝트"),
    "NCA-GenL 자격 대비": (None, "NCA-GenL"),
    "AI Agent 엔지니어링 및 서비스 개발": ("agent", "Agent"),
    "AI Agent End-to-End 종합 프로젝트": ("agent-project", "Agent 프로젝트"),
    "최종발표회 및 수료식": (None, "수료"),
}
# 문제 풀이 사이트 (홈 위쪽 링크): (이름, assets/logos의 공식 아이콘, 주소)
PRACTICE = [
    ("SWEA", "swea.png", "https://swexpertacademy.com/main/talk/solvingClub/clubView.do?solveclubId=AaFX6-bK02vHBISG"),
    ("Programmers", "programmers.png", "https://school.programmers.co.kr/learn/challenges?order=recent&page=1&languages=python3"),
]
# 치트시트: 경로 → (보이는 이름, 공식 로고 파일, 용도, 과목). 과목 블록 아래 '참고' 줄에 나온다.
CHEATSHEETS = {
    "sklearn": ("scikit-learn 치트시트", "sklearn.svg", "머신러닝 · 모델 평가", "ml"),
    "pytorch": ("PyTorch 치트시트", "pytorch.svg", "텐서 · 신경망 학습", "dl"),
    "opencv": ("OpenCV 치트시트", "opencv.png", "이미지 · 영상 처리", "vision"),
}

# 설치 가이드: 경로 → (보이는 이름, 공식 로고 파일, 용도, 과목 또는 공통 묶음, 공개 여부). 공개 전에는 False로 둔다.
SETUP = {
    "postgresql": ("PostgreSQL 가이드", "postgresql.svg", "Windows 셋업 · pgAdmin 사용법 · psql", "llm", True),
    "path": ("경로 설정 (PATH)", "path.svg", "명령을 찾을 수 없을 때 · PATH에 폴더 추가", "개발 환경", True),
    "python-venv": ("Python 가상환경", "python.png", "gpuenv · backendenv · 명령 두 줄로 만들고 설치 · 터미널과 VS Code 연결", "개발 환경", True),
    "vscode-extensions": ("VS Code Extension", "vscode.png", "수업 안내 3개 · Python 기본 3개 · 추천 2개", "개발 환경", True),
    "docker": ("Docker", "docker.png", "WSL 2 · Docker Desktop 설치와 기본 명령", "개발 환경", False),
    "local-ai": ("로컬 AI 코딩", "ollama.png", "내 PC의 GPU로 AI 모델 돌리기 · Ollama + OpenCode 설치", "AI 코딩", True),
    "ai-coding": ("AI 코딩 도구", "code.svg", "OpenCode · Claude Code · Codex · agy 사용법", "AI 코딩", True),
    "cli": ("CLI 도구", "terminal.svg", "AI 에이전트의 문서 조회 · 결과 검증 · 서비스 연결", "AI 코딩", True),
}
# 과정 전체에서 쓰는 가이드의 묶음과 순서. 홈 '공통 가이드' 섹션에 묶음마다 한 줄씩 나온다.
COMMON_GROUPS = ["개발 환경", "AI 코딩"]
# 페이지와 함께 내려받게 둘 파일: 사이트 경로 → [파일 이름]. 페이지에서는 data-site를 붙여 링크한다.
FILES = {
    "setup/local-ai": ["SETUP_FOR_AI.md"],
    "setup/python-venv": ["requirements-gpu.txt", "requirements-backend.txt", "requirements-all.txt"],
}
# 여러 페이지로 된 가이드: 경로 → [(하위 폴더, 페이지 이름)]. 첫 줄("")이 가이드 첫 페이지다.
SETUP_PAGES = {
    "postgresql": [("", "셋업"), ("pgadmin", "pgAdmin 사용법"), ("psql", "psql")],
    "ai-coding": [("", "공통"), ("opencode", "OpenCode"), ("claude-code", "Claude Code"), ("codex", "Codex"), ("agy", "agy")],
}
# Day 페이지 아래에 두는 하위 페이지: "과목/날짜" → [(하위 폴더, 이름)]. 홈 카드와 상단 경로에 붙는다.
DAY_SUBPAGES = {
    "llm/20261112": [("practice", "오전 실습 가이드")],
}
# Colab 실습 폴더: "과목/날짜" → Google Drive 폴더 주소 (공유: 링크가 있는 모든 사용자 · 뷰어). Day 줄·그날 페이지에 Colab 로고로 나온다.
COLAB = {
    "llm/20261113": "https://drive.google.com/drive/folders/14TnoVzqT0i4RWOdbONdwqW5a4Ce_vhEn",
    "llm/20261116": "https://drive.google.com/drive/folders/19rB2g83VexXoU47XW-Br_QkKtCgBKo0f",
    "llm/20261117": "https://drive.google.com/drive/folders/1jS8l2wm3YetcbodRCHgFhREVKyqgcvbN",
}
RELEASE = "--release" in sys.argv   # deploy용: 공개 전 페이지를 뺀다


def setup_items():
    return [(k, name, logo, desc, subj) for k, (name, logo, desc, subj, pub) in SETUP.items() if pub or not RELEASE]


def refs_of(subject):
    """과목에 딸린 참고 문서: [(루트 기준 경로, 이름, 로고 파일, 용도)]"""
    items = [(f"cheatsheet/{k}/", name, logo, desc)
             for k, (name, logo, desc, subj) in CHEATSHEETS.items() if subj == subject]
    items += [(f"setup/{k}/", name, logo, desc) for k, name, logo, desc, subj in setup_items() if subj == subject]
    return items


FONT = '-apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo","Malgun Gothic",sans-serif'


# ── 자료 읽기 ────────────────────────────────────────────────────────────
def read_days():
    days = []
    for row in json.loads(LECTURES.read_text(encoding="utf-8")):
        key, short = SUBJECTS.get(row["subject"], (None, row["subject"]))
        ymd = row["date"].replace("-", "")
        part = row["day"].split("-")[1] if "-" in row["day"] else "1"
        folder = ymd if part == "1" else f"{ymd}-{part}"      # 같은 날 두 번째 회차: 20261102-2
        src = PAGES / key / folder if key else None
        if RELEASE and row["date"] > datetime.date.today().isoformat():
            src = None   # deploy용: 내일 이후 수업 자료(강의 HTML·목차)는 그날 배포할 때까지 뺀다 (main에는 미리 둘 수 있다)
        days.append({
            "n": row["day"], "date": row["date"], "ymd": folder, "key": key, "short": short,
            "subject": row["subject"], "link": row["link"],
            "src": src if src and (src / "index.html").exists() else None,
            # 사이트에 올린 강의 HTML (sync_lecture_html.py) → '바로 보기'
            "lecture": src / "lecture" if src and (src / "lecture" / "index.html").exists() else None,
            # 강의 트리(교재 구성) → '강의 목차 한눈에 보기'
            "tree": src / "tree.md" if src and (src / "tree.md").exists() else None,
            "colab": COLAB.get(f"{key}/{folder}"),
        })
    return days


def page_h1(src):
    text = (src / "index.html").read_text(encoding="utf-8")
    m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1)).strip()) if m else src.name


def md(date):
    return f"{int(date[5:7])}/{int(date[8:10])}"


# ── 글꼴 통일: 본문은 Pretendard만, 코드(monospace)는 예외 ─────────────────
PRETENDARD_LINK = '<link rel="stylesheet" href="/fonts/pretendard/pretendardvariable-dynamic-subset.css">'
PRETENDARD_STACK = '"Pretendard Variable", Pretendard, '
FONT_DECL = re.compile(r"(font-family|--font[\w-]*|--sans)(\s*:\s*)((?:\"[^\"\n]*\"|'[^'\n]*'|[^;}\"'<\n])+)")
MONO_HINT = re.compile(r"monospace|consolas|menlo|sf mono|sfmono|courier|var\(", re.I)
FONT_WARNINGS = []


def unify_fonts(text, label):
    """페이지 안의 글꼴 선언 중 코드용이 아닌 것은 Pretendard를 맨 앞에 붙이고, 링크가 없으면 넣는다.
    덮어쓸 수 없는 경우(font: 줄임 표기 등)는 경고만 남긴다(빌드는 계속)."""
    def fix(m):
        value = m.group(3)
        if "pretendard" in value.lower() or MONO_HINT.search(value):
            return m.group(0)
        return m.group(1) + m.group(2) + PRETENDARD_STACK + value.lstrip()
    text = FONT_DECL.sub(fix, text)
    if "pretendardvariable" not in text:
        text, n = re.subn(r"</head>", lambda m: PRETENDARD_LINK + "\n</head>", text, count=1)
        if not n:
            FONT_WARNINGS.append(f"{label}: <head>가 없어 Pretendard 링크를 못 넣음")
    for m in re.finditer(r"(?<![\w-])font\s*:\s*[^;}\"<]*?(?:\d)(?:px|rem|em|pt)?[^;}\"<]*\s+([^;}\"<]+)", text):
        fam = m.group(1)
        if "pretendard" not in fam.lower() and not MONO_HINT.search(fam) and re.search(r"[A-Za-z\"']", fam):
            FONT_WARNINGS.append(f"{label}: font 줄임 표기에 Pretendard 아닌 글꼴 → {fam.strip()[:60]}")
    return text


# ── 내용 페이지 위쪽 메뉴 ────────────────────────────────────────────────
NAV_CSS = f"""<style>
.cn-nav{{position:sticky;top:0;z-index:100;box-sizing:border-box;display:flex;flex-wrap:wrap;align-items:center;gap:.25rem 1rem;
  padding:.5rem 1rem;background:#142849;color:#fff;font:500 .875rem/1.5 {FONT}}}
.cn-nav a{{color:#fff;text-decoration:none;padding:.125rem .375rem;border-radius:.375rem}}
.cn-nav a:hover,.cn-nav a:focus-visible{{background:rgba(255,255,255,.16);outline:none}}
.cn-nav .cn-here{{opacity:.7}}
.cn-nav .cn-right{{margin-left:auto;display:flex;gap:.25rem .75rem;flex-wrap:wrap}}
.cn-nav .cn-slack{{display:inline-flex;align-items:center;gap:.4rem}}
.cn-nav .cn-slack img{{display:block;width:1rem;height:1rem;background:#fff;border-radius:.25rem;padding:.1rem;box-sizing:content-box}}
.cn-nav .cn-dl{{background:rgba(255,255,255,.14);padding:.125rem .6rem}}
html{{scroll-padding-top:3rem}}
@media (max-width:600px){{.cn-nav{{flex-wrap:nowrap;overflow-x:auto;white-space:nowrap;gap:.25rem .5rem;padding:.4rem .75rem}}.cn-nav .cn-right{{flex-wrap:nowrap}}html{{scroll-padding-top:2.5rem}}}}
@media print{{.cn-nav{{display:none}}}}
</style>"""


DOWNLOAD_MARK = "<!--download-->"  # copy_page가 'HTML 받기' 링크로 바꾼다
THEME_MARK = "<!--theme-->"        # 다크 모드가 있는 페이지면 테마 버튼으로, 없으면 빈 글자로 바꾼다


# ── 라이트/다크 전환 ─────────────────────────────────────────────────────
# 페이지마다 다크 CSS는 @media (prefers-color-scheme:dark) 안에 있다. 버튼을 누르면 그 media 조건을
# 항상 참/항상 거짓으로 바꿔 끼워 OS 설정과 관계없이 고른 쪽을 보여 준다. 고른 값은 localStorage에 둔다.
# OS 설정과 같은 쪽을 고르면 저장값을 지워 다시 OS 설정을 따른다.
THEME_HEAD = """<script>(function(){
var K='site-theme',d=document,root=d.documentElement,mq=matchMedia('(prefers-color-scheme: dark)'),
RX=/\\(\\s*prefers-color-scheme\\s*:\\s*dark\\s*\\)/i,seen=[],rules=[],mem='';
function get(){try{var v=localStorage.getItem(K);return v==='dark'||v==='light'?v:''}catch(e){return mem}}
function put(v){mem=v;try{v?localStorage.setItem(K,v):localStorage.removeItem(K)}catch(e){}}
function scan(list){for(var i=0;i<list.length;i++){var r=list[i];
  if(r.media&&RX.test(r.media.mediaText))rules.push([r,r.media.mediaText]);if(r.cssRules)scan(r.cssRules)}}
function apply(){
  var ss=d.styleSheets;for(var i=0;i<ss.length;i++){var s=ss[i];if(seen.indexOf(s)<0){seen.push(s);try{scan(s.cssRules)}catch(e){}}}
  var f=get(),m=f||(mq.matches?'dark':'light');
  for(var j=0;j<rules.length;j++){var p=rules[j];
    p[0].media.mediaText=f?p[1].replace(RX,f==='dark'?'(min-width:0px)':'(max-width:0px) and (min-width:1px)'):p[1]}
  root.setAttribute('data-theme',m);root.style.colorScheme=f;
  var b=d.querySelectorAll('.theme-toggle'),t=m==='dark'?'밝은 화면으로 보기':'어두운 화면으로 보기';
  for(var k=0;k<b.length;k++){b[k].setAttribute('aria-label',t);b[k].title=t}}
d.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.theme-toggle');if(!b)return;
  var m=root.getAttribute('data-theme')==='dark'?'light':'dark';put(m===(mq.matches?'dark':'light')?'':m);apply()});
mq.addEventListener?mq.addEventListener('change',apply):mq.addListener(apply);
apply();d.addEventListener('DOMContentLoaded',apply);
})();</script>
<style>
.theme-toggle{display:inline-flex;align-items:center;justify-content:center;cursor:pointer;font:inherit;line-height:1}
.theme-toggle svg{display:block;width:1.05rem;height:1.05rem}
.theme-toggle .i-sun,:root[data-theme=dark] .theme-toggle .i-moon{display:none}
:root[data-theme=dark] .theme-toggle .i-sun{display:block}
.cn-nav .theme-toggle{margin:0;padding:.2rem .375rem;border:0;border-radius:.375rem;background:none;color:#fff}
.cn-nav .theme-toggle:hover,.cn-nav .theme-toggle:focus-visible{background:rgba(255,255,255,.16);outline:none}
@media print{.theme-toggle{display:none!important}}
</style>"""
THEME_BTN = ('<button class="theme-toggle" type="button" aria-label="화면 밝기 바꾸기">'
             '<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
             'stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
             '<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
             'stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4'
             'M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>')


def add_theme(text, nav, dark):
    """다크 모드가 있는 페이지에만 테마 스크립트(</head> 앞)와 버튼(메뉴 오른쪽 끝)을 넣는다."""
    if not dark:
        return text, nav.replace(THEME_MARK, "")
    nav = nav.replace(THEME_MARK, THEME_BTN)
    text, n = re.subn(r"</head>", lambda m: THEME_HEAD + "\n</head>", text, count=1, flags=re.I)
    return text, (nav if n else THEME_HEAD + nav)


def nav_html(depth, crumbs, here=None, prev=None, next_=None, lecture=None, view=None):
    """crumbs: [(이름, 루트 기준 경로)], here: 현재 위치 글자, prev/next_: (이름, 경로)"""
    up = "../" * depth
    left = [f'<a href="{up or "./"}">← {SITE_NAME}</a>']
    left += [f'<a href="{up}{path}">{html.escape(name)}</a>' for name, path in crumbs]
    if here:
        left.append(f'<span class="cn-here">{html.escape(here)}</span>')
    right = [DOWNLOAD_MARK]
    if view:
        right.append(f'<a href="{html.escape(view)}">바로 보기</a>')
    if lecture:
        right.append(f'<a class="cn-slack" href="{html.escape(lecture)}" target="_blank" rel="noopener" title="강의 자료 (Slack)" aria-label="강의 자료 (Slack, 새 탭)">'
                     f'<img src="{image_data(HERE / "assets" / "logos" / "slack.svg")}" alt="" width="16" height="16">강의 자료</a>')
    if prev:
        right.append(f'<a href="{up}{prev[1]}">‹ {html.escape(prev[0])}</a>')
    if next_:
        right.append(f'<a href="{up}{next_[1]}">{html.escape(next_[0])} ›</a>')
    right.append(THEME_MARK)
    side = f'<span class="cn-right">{"".join(right)}</span>'
    return f'{NAV_CSS}<nav class="cn-nav" aria-label="사이트 메뉴">{"".join(left)}{side}</nav>'


# Vercel Web Analytics: 모든 페이지에 넣는다 (Vercel 프로젝트에서 Analytics를 켜 둬야 동작)
ANALYTICS = """<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};</script>
<script defer src="/_vercel/insights/script.js"></script>"""

# 사이트 안 다른 페이지로 가는 링크는 data-site를 붙여 두면 살린다
LOCAL_LINK = re.compile(r'<a\s(?![^>]*data-site)[^>]*href="(?!https?:|#|mailto:|data:)[^"]*"[^>]*>(.*?)</a>', re.S)


SCRIPT_BLOCK = re.compile(r"(<script\b.*?</script>)", re.S | re.I)


def strip_local_links(text):
    """<script> 밖의 상대 링크만 글자로 바꾼다. 스크립트 안의 HTML 문자열은 그대로 둔다."""
    parts = SCRIPT_BLOCK.split(text)
    count = 0
    for i in range(0, len(parts), 2):
        parts[i], n = LOCAL_LINK.subn(r"<span>\1</span>", parts[i])
        count += n
    return "".join(parts), count


HIDDEN_LINK = re.compile(r'<a\b[^>]*\bhref="([^"#]*)(#[^"]*)?"[^>]*>(.*?)</a>', re.S)


def strip_hidden_links(text, dest):
    """--release에서만: 공개 전 설치 가이드로 가는 링크를 글자로 바꾼다 (라이브에서 404가 나지 않게)."""
    if not RELEASE:
        return text, 0
    hidden = {f"setup/{k}" for k, v in SETUP.items() if not v[4]}

    def repl(m):
        href = m.group(1)
        if not href or "://" in href or href.startswith(("mailto:", "/")):
            return m.group(0)
        target = posixpath.normpath(posixpath.join(dest, href)).strip("/")
        if any(target == h or target.startswith(h + "/") for h in hidden):
            return f"<span>{m.group(3)}</span>"
        return m.group(0)

    parts = SCRIPT_BLOCK.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = HIDDEN_LINK.sub(repl, parts[i])
    new = "".join(parts)
    return new, len(HIDDEN_LINK.findall(text)) - len(HIDDEN_LINK.findall(new))


def download_name(text):
    """받는 파일 이름: 페이지 <title>에서 · ( ) 공백을 _로. 예: Day10_최적화와_규제.html"""
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    name = html.unescape(m.group(1)) if m else "page"
    name = re.sub(r"[\\/:*?\"<>|·()\[\]–—|-]+", " ", name)
    name = re.sub(r"\s+", "_", name.strip())[:60].strip("_")
    return f"{name}.html"


def copy_lecture(src, dest, nav):
    """강사님 강의 HTML: 원본은 손대지 않고 download.html로 두고, 사이트 메뉴 아래 화면 전체에 띄운다.
    (강의 HTML은 자체 고정 머리·아래 막대가 있어 메뉴를 끼워 넣으면 겹친다)"""
    original = (src / "index.html").read_text(encoding="utf-8")
    m = re.search(r"<title>(.*?)</title>", original, re.S)
    title = m.group(1).strip() if m else "강의 자료"
    link = (f'<a class="cn-dl" href="download.html" download="{html.escape(download_name(original))}" '
            f'title="강의 자료를 HTML 파일 하나로 받기 (인터넷 없이 열림)">HTML 받기 ↓</a>')
    page = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>html,body{{margin:0;height:100%}}body{{display:flex;flex-direction:column;height:100dvh;background:#fff}}
.lecture-frame{{flex:1;width:100%;border:0;display:block}}</style>
{ANALYTICS}
</head>
<body>{nav.replace(DOWNLOAD_MARK, link).replace(THEME_MARK, "")}<iframe class="lecture-frame" src="download.html" title="{title}"></iframe></body>
</html>
"""
    out = PUBLIC / dest
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / "download.html").write_text(original, encoding="utf-8")   # 강의 원본 그대로 (화면 · 받기 공용)
    print(f"  /{dest}/ ← {src.relative_to(HERE)} (원본 그대로, 메뉴 아래 전체 화면)")


def copy_page(src, dest, nav, top=""):
    """top: 요약 제목 아래에 끼울 블록(자료 줄 + 강의 목차). 사이트 화면에만 넣고 download.html 원본에는 넣지 않는다."""
    original = (src / "index.html").read_text(encoding="utf-8")
    original, n_hidden = strip_hidden_links(original, dest)
    text, n_links = strip_local_links(original)
    if top:
        text = insert_after_title(text, top)
    link = (f'<a class="cn-dl" href="download.html" download="{html.escape(download_name(original))}" '
            f'title="이 페이지를 HTML 파일 하나로 받기 (인터넷 없이 열림)">HTML 받기 ↓</a>')
    nav = nav.replace(DOWNLOAD_MARK, link)
    if not dest.endswith("/lecture"):    # 강사님 원본 강의 페이지는 글꼴도 그대로 둔다
        text = unify_fonts(text, dest)
    text, nav = add_theme(text, nav, "prefers-color-scheme" in original)   # 끼운 목차 블록의 CSS가 아니라 원본 기준
    text, n_body = re.subn(r"(<body[^>]*>)", lambda m: m.group(1) + nav + ANALYTICS, text, count=1)
    assert n_body == 1, f"<body> 없음: {src}"
    out = PUBLIC / dest
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(text, encoding="utf-8")
    (out / "download.html").write_text(original, encoding="utf-8")   # 사이트 메뉴·통계 없는 원본
    for name in FILES.get(dest, []):
        shutil.copy2(src / name, out / name)
    note = f" (사이트에 없는 링크 {n_links}개를 글자로)" if n_links else ""
    note += f" (공개 전 가이드 링크 {n_hidden}개를 글자로)" if n_hidden else ""
    print(f"  /{dest}/ ← {src.relative_to(HERE)}{note}")


def insert_after_title(text, block):
    """요약 페이지의 제목 머리(<h1>을 감싼 <header>) 바로 뒤에 넣는다. 머리가 없으면 </h1> 뒤."""
    m = re.search(r"<h1\b", text)
    assert m, "<h1> 없음"
    end = text.find("</header>", m.end())
    nxt = min([i for i in (text.find("<section", m.end()), text.find("<h2", m.end())) if i != -1], default=len(text))
    if end != -1 and end < nxt:
        # 머리 안쪽 끝(제목과 같은 폭의 감싸개 안)에 넣는다: <header><div class="wrap">…</div></header>이면 그 </div> 앞
        inner = text[m.end():end].rstrip()
        before = text[text.rfind("<header", 0, m.start()):m.start()]
        wrapped = before.count("<div") - before.count("</div>") > 0      # 제목이 머리 안의 <div> 감싸개 속에 있다
        at = m.end() + len(inner) - len("</div>") if wrapped and inner.endswith("</div>") else end
    else:
        at = text.find("</h1>", m.end()) + len("</h1>")
    light = "" if "prefers-color-scheme" in text else " lt-light"   # 다크 모드가 없는 요약은 블록도 밝게 둔다
    return text[:at] + f'\n<div class="lt-top{light}">{block}</div>\n' + text[at:]


# ── 목록 페이지 (홈, 과목) ───────────────────────────────────────────────
# 이 저장소에서 그린 아이콘: 두 테마 모두에서 보이는 색이라 다크 모드 흰 받침을 깔지 않는다
OWN_ICONS = {"code.svg", "terminal.svg", "path.svg"}


PAGE_CSS = """
:root{--bg:#FBFCFE;--surface:#FFFFFF;--soft:#EFF4FB;--line:rgba(20,40,73,.10);--line-2:rgba(20,40,73,.18);
  --primary:#142849;--heading:#1C2B40;--text:#222F44;--muted:#52667E;--accent:#2F66DE;--accent-soft:rgba(47,102,222,.10);
  --cell:#E3EAF4;--cell-past:#C5D3E7;--focus:#2F66DE;
  --font:"Pretendard Variable",Pretendard,-apple-system,BlinkMacSystemFont,"Segoe UI","Apple SD Gothic Neo","Malgun Gothic",sans-serif;
  --mono:ui-monospace,"SFMono-Regular",Consolas,"Malgun Gothic",monospace}
@media (prefers-color-scheme:dark){:root{--bg:#0E1626;--surface:#152038;--soft:#1A2844;--line:rgba(169,195,236,.12);--line-2:rgba(169,195,236,.22);
  --primary:#A9C3EC;--heading:#E7EEF9;--text:#D4DDEB;--muted:#9DADC4;--accent:#7FA6FF;--accent-soft:rgba(127,166,255,.16);
  --cell:#1C2943;--cell-past:#33476B;--focus:#A9C3EC;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:400 16px/1.6 var(--font);word-break:keep-all;overflow-wrap:break-word;-webkit-font-smoothing:antialiased}
main{max-width:1160px;margin:0 auto;padding:36px 24px 80px}
h1,h2,h3,p,ol,ul{margin:0}
ol,ul{padding:0;list-style:none}
h1,h2,h3{color:var(--heading);text-wrap:balance}
a{color:inherit;text-decoration:none}
a:focus-visible{outline:2px solid var(--focus);outline-offset:3px;border-radius:8px}
svg{display:block}

/* 맨 위: 브랜드 줄 + 문제 풀이 */
.top{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.brand{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px}
.brand-logos{display:inline-flex;align-items:center;gap:12px;border-radius:8px}
.brand-logos img{display:block;width:auto;height:32px;object-fit:contain}
.brand-sep{width:1px;height:22px;background:#D8E4F2}
.brand p{color:var(--muted);font-size:14px;font-weight:600}
.links{display:flex;flex-wrap:wrap;gap:8px}
.links a{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 14px 0 10px;border:1px solid var(--line);border-radius:999px;
  background:var(--surface);font-size:13px;font-weight:600;color:var(--heading);transition:border-color .15s}
.links a:hover{border-color:var(--accent)}
.top-r{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.top .theme-toggle{width:36px;height:36px;padding:0;border:1px solid var(--line);border-radius:999px;background:var(--surface);color:var(--heading)}
.top .theme-toggle:hover{border-color:var(--accent)}
.top .theme-toggle:focus-visible{outline:2px solid var(--focus);outline-offset:3px}
.links img{display:block;width:20px;height:20px;border-radius:5px}
@media (prefers-color-scheme:dark){.brand-logos{background:#FFFFFF;padding:4px 10px}}

/* 첫 화면: 제목 · 최근 수업 · 지금 과목 표지 */
.hero{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:48px;align-items:end;margin:44px 0 40px}
.hero-l{display:grid;gap:22px}
.title{font-size:clamp(40px,6vw,60px);font-weight:800;letter-spacing:-.045em;line-height:1.02}
.count{font-size:15px;color:var(--muted);font-variant-numeric:tabular-nums}
.count b{color:var(--heading)}
.label{font-size:12px;font-weight:700;letter-spacing:.08em;color:var(--muted);margin-bottom:10px}
.recent{border-top:1px solid var(--line-2)}
.recent a{display:grid;grid-template-columns:72px minmax(0,1fr) auto 20px;gap:12px;align-items:center;padding:13px 4px;
  border-bottom:1px solid var(--line);font-size:15px;color:var(--heading);transition:background .15s,padding .15s}
.recent a:hover{background:var(--soft);padding-left:10px}
.recent .no,.recent .d{font-family:var(--mono);font-size:12px;color:var(--muted)}
.recent .go{opacity:0;transition:opacity .15s;color:var(--accent)}
.recent a:hover .go{opacity:1}
.recent .go svg{width:16px;height:16px}
.recent li.on .t{font-weight:700}
.recent li.on .no{color:var(--accent);font-weight:700}
.recent li.on .no::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--accent);margin-right:7px;vertical-align:2px;box-shadow:0 0 0 3px var(--accent-soft)}
.cover{position:relative;overflow:hidden;display:grid;gap:12px;align-content:end;min-height:340px;padding:30px;border-radius:20px;color:#FFFFFF;
  background:radial-gradient(120% 90% at 100% 0%,#2A4B82 0%,rgba(42,75,130,0) 55%),linear-gradient(165deg,#1A335E 0%,#142849 50%,#0D1B33 100%);
  box-shadow:0 1px 0 rgba(255,255,255,.06) inset,0 24px 48px -24px rgba(20,40,73,.55)}
.cover::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.16) 1px,transparent 1px);background-size:16px 16px;
  -webkit-mask:linear-gradient(200deg,#000 0%,transparent 55%);mask:linear-gradient(200deg,#000 0%,transparent 55%)}
.cover>*{position:relative}
.cover .wm{position:absolute;right:-6px;top:-34px;font-size:190px;font-weight:800;letter-spacing:-.06em;line-height:1;color:transparent;-webkit-text-stroke:1.5px rgba(255,255,255,.13)}
.cover .eyebrow{font-size:11px;font-weight:700;letter-spacing:.14em;opacity:.65}
.cover b{font-size:44px;letter-spacing:-.04em;line-height:1}
.cover .c-n{font-size:15px;opacity:.72}
.cover .prog{display:flex;align-items:center;gap:12px;margin-top:4px}
.cover .bar{flex:1;height:4px;border-radius:99px;background:rgba(255,255,255,.16)}
.cover .bar i{display:block;height:100%;border-radius:99px;background:#5B8BF0;box-shadow:0 0 12px #5B8BF0}
.cover .c-k{font-family:var(--mono);font-size:12px;opacity:.75}
.cover .c-go{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-top:10px;padding-top:16px;border-top:1px solid rgba(255,255,255,.14);font-weight:600;font-size:15px}
.cover .c-go svg{width:18px;height:18px;flex:none;transition:transform .15s}
.cover:hover .c-go svg{transform:translateX(4px)}
@media (prefers-color-scheme:dark){.cover{box-shadow:0 0 0 1px rgba(169,195,236,.16)}}

/* 100일 일정 */
.timeline{display:flex;flex-wrap:wrap;gap:12px 22px;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.tl{display:grid;gap:6px;min-width:0}
.tl-name{font-size:12px;font-weight:700;color:var(--heading)}
.tl-cells{display:flex;flex-wrap:wrap;gap:3px}
.cell{width:11px;height:11px;border-radius:2px;display:inline-block;background:var(--cell)}
.cell.past{background:var(--cell-past)}
.cell.has{background:var(--primary)}
a.cell:hover{transform:scale(1.3)}
.cell.today{background:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}

/* 참고 문서 모음 */
.shelf{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin:32px 0 12px;border:1px solid var(--line);border-radius:16px;background:var(--surface)}
.shelf .col{display:grid;gap:2px;align-content:start;padding:14px 18px}
.shelf .col+.col{border-left:1px solid var(--line)}
.shelf+.chapter{border-top:0}
.shelf h2{font-size:11px;font-weight:700;letter-spacing:.06em;color:var(--muted);margin-bottom:4px}
.shelf a{display:flex;align-items:center;gap:8px;padding:4px 8px;margin:0 -8px;border-radius:8px;font-size:14px;font-weight:600;color:var(--heading);transition:background .15s}
.shelf a:hover{background:var(--soft)}
.ref-logo{display:flex;align-items:center;justify-content:center;flex:none;border-radius:6px}
.ref-logo img{display:block;width:auto;height:18px;max-width:30px;object-fit:contain}
.ch-refs{display:grid;gap:2px;margin-top:12px}
.ch-refs a{display:flex;align-items:center;gap:8px;padding:4px 8px;margin:0 -8px;border-radius:8px;font-size:13px;font-weight:600;color:var(--heading);transition:background .15s}
.ch-refs a:hover{background:var(--soft)}
@media (prefers-color-scheme:dark){.ref-logo:not(.own){background:#FFFFFF;padding:3px 5px}}
.shelf .soon{margin:2px 0}
.soon{white-space:nowrap;font-size:12px;font-weight:600;color:var(--muted);border:1px solid var(--line-2);border-radius:999px;padding:2px 10px;justify-self:start}

/* 과목 = 챕터 */
.chapter{display:grid;grid-template-columns:220px minmax(0,1fr);gap:40px;padding:44px 0;border-top:1px solid var(--line-2)}
.row.off{cursor:default}.row.off:hover{background:none}.row.off .t{color:var(--text);font-weight:500}
.pend{display:inline-block;margin-left:8px;vertical-align:2px;white-space:nowrap;font-size:11px;font-weight:600;color:var(--muted);border:1px solid var(--line-2);border-radius:999px;padding:1px 8px;letter-spacing:0}
.rows li.all .row.off,.rows li.all .row.off:hover{background:linear-gradient(90deg,var(--soft),transparent 70%)}
.ch-side{display:grid;gap:4px;align-content:start}
.ch-no{font-family:var(--mono);font-size:13px;font-weight:600;color:var(--accent)}
.ch-side h2{font-size:28px;letter-spacing:-.03em;line-height:1.15;margin:2px 0 6px}
.ch-side h2 a:hover{text-decoration:underline;text-underline-offset:4px}
.ch-meta{font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.ch-side .soon{margin-top:6px}
.rows li{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:12px;border-bottom:1px solid var(--line)}
.rows li:first-child{border-top:1px solid var(--line)}
.row{display:grid;grid-template-columns:72px minmax(0,1fr) 52px;gap:14px;align-items:center;padding:16px 6px;border-radius:10px;transition:background .15s}
.row:hover{background:var(--soft)}
.row:hover .t{color:var(--accent)}
.row .no{font-family:var(--mono);font-size:12px;font-weight:600;color:var(--muted)}
.row .t{font-size:17px;font-weight:600;letter-spacing:-.01em;color:var(--heading);transition:color .15s}
.row .d{font-family:var(--mono);font-size:12px;color:var(--muted);text-align:right}
.lk{display:flex;flex-wrap:wrap;gap:6px;justify-content:flex-end;padding-right:4px}
.mini{display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 10px;border-radius:8px;border:1px solid var(--line-2);
  font-size:12px;font-weight:600;color:var(--heading);white-space:nowrap;transition:background .15s,border-color .15s}
.mini:hover{background:var(--soft);border-color:var(--accent)}
.mini svg{width:14px;height:14px}
.mini.view{background:var(--accent-soft);border-color:transparent;color:var(--accent)}
.mini.view:hover{border-color:var(--accent)}
.rows li.all .row{background:linear-gradient(90deg,var(--soft),transparent 70%)}
.rows li.all .no{color:var(--accent)}
.mini.slack{padding:0 8px}.mini.slack img{display:block;width:16px;height:16px}
.mini.colab{padding:0 8px}.mini.colab img{display:block;width:27px;height:16px}
@media (prefers-color-scheme:dark){.mini.colab{background:#FFFFFF;border-color:#FFFFFF}.mini.colab:hover{border-color:var(--accent)}}

/* 그날 페이지: 머리 · 자료 줄 · 강의 목차 한눈에 보기 */
.day-head{display:grid;gap:10px;margin:8px 0 22px}
.day-head .eyebrow{font-family:var(--mono);font-size:13px;font-weight:600;color:var(--accent)}
.day-head h1{font-size:clamp(28px,4.4vw,40px);font-weight:800;letter-spacing:-.035em;line-height:1.15}
.day-head .sub{font-size:15px;color:var(--muted)}
.sum-empty{margin-top:28px;padding:28px 20px;border:1px dashed var(--line-2);border-radius:14px;text-align:center;color:var(--muted);font-size:15px}

@media (max-width:880px){.hero{grid-template-columns:1fr;gap:28px;margin-top:32px}.shelf{grid-template-columns:1fr}.shelf .col+.col{border-top:1px solid var(--line)}
  .shelf .col+.col{border-left:0}.chapter{grid-template-columns:1fr;gap:16px;padding:32px 0}.rows li{grid-template-columns:1fr}
  .lk{justify-content:flex-start;padding:0 6px 14px}.row{grid-template-columns:60px minmax(0,1fr)}.row .d{display:none}}
@media (max-width:600px){main{padding:24px 16px 64px}.cover{min-height:280px;padding:24px}.cover b{font-size:36px}.cover .wm{font-size:150px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}a.cell:hover{transform:none}}
"""

ICON_DOC = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></svg>')
ICON_EXT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M7 17 17 7"/><path d="M8 7h9v9"/></svg>')
ICON_ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
              '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>')
def day_range(ds):
    """과목의 Day 범위. 같은 날 두 번째 회차 표시(-2)는 뺀다: Day9–11"""
    return f'Day{ds[0]["n"].split("-")[0]}–{ds[-1]["n"].split("-")[0]}'


# 요약 페이지가 아직 없는 Day의 제목(강의 목차 기준). 요약 페이지를 만들면 그 <h1>을 이 제목으로 쓰고 여기서 지운다.
PLANNED_TITLES = {
    "python/20261020": "Python 기초 문법",
    "python/20261021": "객체지향과 파일 처리",
    "python/20261022": "데이터 분석과 EDA",
    "ml/20261023": "데이터 전처리",
    "ml/20261026": "회귀와 분류 모델",
    "ml/20261027": "트리와 앙상블",
    "ml/20261028": "모델 평가와 군집",
    "dl/20261029": "신경망 학습 기초",
    "llm/20261116": "Prompt · Context Engineering",
}
ICON_VIEW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>')
# 과목 번호(챕터): SUBJECTS에서 경로가 있는 과목의 순서
CHAPTER = {key: i for i, key in enumerate([k for k, _ in SUBJECTS.values() if k], 1)}


def list_page(title, body, nav="", up=""):
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{up}fonts/pretendard/pretendardvariable-dynamic-subset.css">
<style>{PAGE_CSS}</style>
{THEME_HEAD}
{ANALYTICS}
</head>
<body>{nav.replace(THEME_MARK, THEME_BTN)}
<main>
{body}
</main>
</body>
</html>
"""


def day_links(d, up):
    """Day 한 줄 오른쪽의 작은 버튼: 바로 보기(사이트의 강의 HTML) · 강의 자료(Slack 원본) · 하위 페이지"""
    href = f'{up}{d["key"]}/{d["ymd"]}/'
    out = []
    if d["lecture"]:
        out.append(f'<a class="mini view" href="{href}lecture/">{ICON_VIEW}바로 보기</a>')
    if d["link"]:
        out.append(slack_link(d["link"], "mini slack"))
    for sub, label in DAY_SUBPAGES.get(f'{d["key"]}/{d["ymd"]}', []):
        out.append(f'<a class="mini" href="{href}{sub}/">{ICON_ARROW}{html.escape(label)}</a>')
    if d["colab"]:
        out.append(colab_link(d["colab"], "mini colab"))
    return "".join(out)


def slack_link(url, cls, text=""):
    """강의 자료(Slack 원본) 링크: Slack 로고 (+ 글자). 화살표 대신 로고로 도착지를 보인다."""
    img = f'<img src="{image_data(HERE / "assets" / "logos" / "slack.svg")}" alt="" width="16" height="16">'
    label = f'<span>{html.escape(text)}</span>' if text else ""
    return (f'<a class="{cls}" href="{html.escape(url)}" target="_blank" rel="noopener" '
            f'title="강의 자료 (Slack)" aria-label="강의 자료 (Slack, 새 탭)">{img}{label}</a>')


def colab_link(url, cls, text=""):
    """Colab 실습 폴더(Google Drive) 링크: 공식 Colab 로고 (+ 글자)"""
    img = f'<img src="{image_data(HERE / "assets" / "logos" / "colab.png")}" alt="" width="27" height="16">'
    label = f'<span>{html.escape(text)}</span>' if text else ""
    return (f'<a class="{cls}" href="{html.escape(url)}" target="_blank" rel="noopener" '
            f'title="Colab 실습 폴더 (Google Drive)" aria-label="Colab 실습 폴더 (Google Drive, 새 탭)">{img}{label}</a>')


def logo_span(logo):
    own = " own" if logo in OWN_ICONS else ""
    return (f'<span class="ref-logo{own}"><img src="{image_data(HERE / "assets" / "logos" / logo)}" alt="" '
            f'width="32" height="22"></span>')


def shelf_block(subjects, up):
    """참고 문서 모음: 공통 가이드 묶음 + 과목 참고 문서. 보일 것이 없는 칸은 main에서만 '준비 중'."""
    cols = []
    for group in COMMON_GROUPS:
        items = [(f"setup/{k}/", name, logo) for k, name, logo, desc, g in setup_items() if g == group]
        links = "".join(f'<a href="{up}{p}">{logo_span(lg)}<span>{html.escape(n)}</span></a>' for p, n, lg in items)
        if links or not RELEASE:
            cols.append(f'<div class="col"><h2>{html.escape(group)}</h2>{links or "<span class=soon>준비 중</span>"}</div>')
    refs = [r for key, _ in subjects for r in refs_of(key)]
    if refs:
        links = "".join(f'<a href="{up}{p}" title="{html.escape(desc)}">{logo_span(lg)}<span>{html.escape(n)}</span></a>'
                        for p, n, lg, desc in refs)
        cols.append(f'<div class="col"><h2>과목 참고 문서</h2>{links}</div>')
    return f'<section class="shelf" aria-label="참고 문서 모음">{"".join(cols)}</section>' if cols else ""


def chapter_block(key, ds, up, link_head=True):
    """과목 한 블록: 왼쪽 챕터 번호·이름·범위, 오른쪽 종합 + Day 목록(요약이 없으면 제목 + '요약 준비 중')"""
    made = [d for d in ds if d["src"]]
    has_all = (PAGES / key / "all" / "index.html").exists()
    has_page = made or has_all or any(d["tree"] for d in ds)   # 과목 페이지가 만들어지는 조건 (main과 같게)
    today = datetime.date.today().isoformat()
    name = html.escape(ds[0]["short"])
    if link_head and has_page:
        name = f'<a href="{up}{key}/">{name}</a>'
    rng = day_range(ds)
    refs = "".join(f'<a href="{up}{p}" title="{html.escape(desc)}">{logo_span(lg)}<span>{html.escape(n)}</span></a>'
                   for p, n, lg, desc in refs_of(key))
    refs = f'<div class="ch-refs" aria-label="참고 문서">{refs}</div>' if refs else ""
    status = (f'<span class="ch-meta">요약 {len(made)} / {len(ds)}일</span>' if has_page
              else '<span class="soon">준비 중</span>')
    side = (f'<div class="ch-side"><span class="ch-no">{CHAPTER[key]:02d}</span><h2 title="{html.escape(ds[0]["subject"])}">{name}</h2>'
            f'<span class="ch-meta">{rng}</span>{status}{refs}</div>')
    pend = '<span class="pend">요약 준비 중</span>'
    rows = []
    # 과목 종합: 있으면 링크, 없으면 제목 + 요약 준비 중
    if has_all:
        rows.append(f'<li class="all"><a class="row" href="{up}{key}/"><span class="no">종합</span>'
                    f'<span class="t">{html.escape(page_h1(PAGES / key / "all"))}</span><span class="d">{len(ds)}일</span></a><span class="lk"></span></li>')
    else:
        rows.append(f'<li class="all"><span class="row off"><span class="no">종합</span>'
                    f'<span class="t">{html.escape(ds[0]["short"])} {len(ds)}일 종합{pend}</span><span class="d">{len(ds)}일</span></span><span class="lk"></span></li>')
    for d in reversed(ds):
        if d["src"]:
            rows.append(f'<li><a class="row" href="{up}{d["key"]}/{d["ymd"]}/"><span class="no">Day{d["n"]}</span>'
                        f'<span class="t">{html.escape(page_h1(d["src"]))}</span><span class="d">{md(d["date"])}</span></a>'
                        f'<span class="lk">{day_links(d, up)}</span></li>')
        elif d["tree"]:   # 요약은 없지만 강의 트리가 있으면 그날 페이지(강의 목차)로 간다
            title = day_title(d)
            rows.append(f'<li><a class="row" href="{up}{d["key"]}/{d["ymd"]}/"><span class="no">Day{d["n"]}</span>'
                        f'<span class="t">{html.escape(title)}{pend}</span><span class="d">{md(d["date"])}</span></a>'
                        f'<span class="lk">{day_links(d, up)}</span></li>')
        elif d["date"] <= today or d["lecture"]:   # 요약이 아직 없으면 예정 제목 + '요약 준비 중' (강의 HTML이 있으면 미리 보임)
            title = day_title(d) if d["lecture"] else PLANNED_TITLES.get(f'{d["key"]}/{d["ymd"]}', "")
            rows.append(f'<li><span class="row off"><span class="no">Day{d["n"]}</span><span class="t">{html.escape(title)}{pend}</span>'
                        f'<span class="d">{md(d["date"])}</span></span><span class="lk">{day_links(d, up)}</span></li>')
    return f'<section class="chapter" id="{key}">{side}<ol class="rows">{"".join(rows)}</ol></section>'


def cover_card(days, subjects, today):
    """지금 과목 표지: 오늘이 속한(없으면 마지막으로 시작한) 과목"""
    key, ds = subjects[-1]
    n_done = len([d for d in ds if d["date"] <= today])
    shown = [d for d in ds if has_page(d) and d["date"] <= today]   # 요약이 없어도 강의 목차가 있으면 그날로 (내일 수업은 제외)
    if shown:
        go_href, go_text = f'{shown[-1]["key"]}/{shown[-1]["ymd"]}/', f'Day{shown[-1]["n"]} · {day_title(shown[-1])}'
    else:
        go_href, go_text = f'#{key}', f'{ds[0]["short"]} 보기'
    return (f'<a class="cover" href="{go_href}"><span class="wm" aria-hidden="true">{CHAPTER[key]:02d}</span>'
            f'<span class="eyebrow">CHAPTER {CHAPTER[key]:02d} · 지금 과목</span>'
            f'<b>{html.escape(ds[0]["short"])}</b><span class="c-n">{html.escape(ds[0]["subject"])}</span>'
            f'<span class="prog"><span class="bar"><i style="width:{round(100 * n_done / len(ds))}%"></i></span>'
            f'<span class="c-k">{n_done} / {len(ds)}일</span></span>'
            f'<span class="c-go"><span>{html.escape(go_text)}</span>{ICON_ARROW}</span></a>')


def timeline(days, today):
    last = max((d["date"] for d in days if d["date"] <= today), default=None)   # 오늘까지 가장 최근 수업일
    groups, current = [], None
    for d in days:
        if d["subject"] != current:
            groups.append((d["short"], []))
            current = d["subject"]
        state = "has" if has_page(d) else ("past" if d["date"] <= today else "")
        if d["date"] == last:
            state += " today"
        tip = html.escape(f'Day{d["n"]} · {md(d["date"])} · {d["subject"]}')
        if has_page(d):
            groups[-1][1].append(f'<a class="cell {state}" href="{d["key"]}/{d["ymd"]}/" title="{tip}" aria-label="{tip}"></a>')
        elif d["lecture"]:
            tip = html.escape(f'Day{d["n"]} · {md(d["date"])} · 강의 자료 바로 보기')
            groups[-1][1].append(f'<a class="cell {state}" href="{d["key"]}/{d["ymd"]}/lecture/" title="{tip}" aria-label="{tip}"></a>')
        elif d["link"]:
            tip = html.escape(f'Day{d["n"]} · {md(d["date"])} · 강의 자료')
            groups[-1][1].append(f'<a class="cell {state}" href="{html.escape(d["link"])}" target="_blank" rel="noopener" '
                                 f'title="{tip}" aria-label="{tip}"></a>')
        else:
            groups[-1][1].append(f'<span class="cell {state}" title="{tip}"></span>')
    return "".join(f'<div class="tl"><span class="tl-name">{name}</span><span class="tl-cells">{"".join(c)}</span></div>'
                   for name, c in groups)


def image_data(image):
    mime = "image/svg+xml" if image.suffix == ".svg" else "image/png"
    data = base64.b64encode(image.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


# ── 강의 트리 (교재 구성) ──────────────────────────────────────────────
TREE_LINE = re.compile(r"^([│ ]*)([├└]─ )?(.*)$")
PDF_PAGE = re.compile(r"\s*\((PDF p\.[^)]*)\)\s*$")
LAB = re.compile(r"^실습\s*\d|일일\s*프로젝트")


def read_tree(path):
    """tree.md의 첫 ```text 블록 → (교재 제목 또는 None, [묶음 {t, c}])"""
    m = re.search(r"```text\n(.*?)```", path.read_text(encoding="utf-8"), re.S)
    assert m, f"```text 블록 없음: {path}"
    roots, stack = [], []
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        prefix, conn, label = TREE_LINE.match(line).groups()
        depth = len(prefix) // 3 + 1 if conn else 0
        node = {"t": label.strip(), "c": []}
        while stack and stack[-1][0] >= depth:
            stack.pop()
        (stack[-1][1]["c"] if stack else roots).append(node)
        stack.append((depth, node))
    if len(roots) == 1 and roots[0]["c"]:      # 맨 위 한 줄이 교재 제목인 형식 (Day21)
        return roots[0]["t"], roots[0]["c"]
    return None, roots


def tree_leaves(n):
    return 1 if not n["c"] else sum(tree_leaves(c) for c in n["c"])


def tree_item(n):
    """카드 안 한 줄: 화면 제목(+ PDF 쪽). 가운데 묶음이 있으면 작은 소제목 아래로 넣는다."""
    t = n["t"]
    pg = PDF_PAGE.search(t)
    if pg:
        t = t[:pg.start()]
    if n["c"]:
        return f'<li class="lt-sg"><span>{html.escape(t)}</span><ul>{"".join(tree_item(c) for c in n["c"])}</ul></li>'
    page = f'<em>{html.escape(pg.group(1).replace("PDF ", ""))}</em>' if pg else ""
    return f'<li{" class=lt-lab" if LAB.search(t) else ""}><span>{wbr(t)}</span>{page}</li>'


def wbr(t):
    """가운뎃점(·)으로 이은 긴 영어 낱말이 좁은 카드에서 글자 중간에 끊기지 않게, · 뒤에서 줄을 바꿀 수 있게 한다."""
    return html.escape(t).replace("·", "·<wbr>")


def tree_flat(n):
    return [n] if not n["c"] else [x for c in n["c"] for x in tree_flat(c)]


# '강의 목차 한눈에 보기' 블록의 스타일. 요약 페이지에도 그대로 끼워 넣을 수 있게 .lt 안에서만 쓰고 색도 따로 둔다.
TREE_CSS = """<style>
.lt{--lt-bg:#FFFFFF;--lt-soft:#F0F6FD;--lt-line:#D8E4F2;--lt-head:#142849;--lt-text:#2B3A52;--lt-muted:#5B6E86;--lt-acc:#2F66DE;--lt-acc-soft:rgba(47,102,222,.10);
  margin:0 0 8px;color:var(--lt-text);font-size:16px;line-height:1.5;word-break:keep-all;overflow-wrap:break-word}
@media (prefers-color-scheme:dark){.lt-top:not(.lt-light) .lt,.lt-top:not(.lt-light) .lt-res,body>main>.lt{--lt-bg:#152038;--lt-soft:#1A2844;--lt-line:rgba(169,195,236,.18);--lt-head:#E7EEF9;--lt-text:#D4DDEB;--lt-muted:#9DADC4;--lt-acc:#7FA6FF;--lt-acc-soft:rgba(127,166,255,.16)}}
.lt-top{display:grid;gap:12px}
.lt-res{--lt-bg:#FFFFFF;--lt-soft:#F0F6FD;--lt-line:#D8E4F2;--lt-head:#142849;--lt-acc:#2F66DE;--lt-acc-soft:rgba(47,102,222,.10);display:flex;flex-wrap:wrap;gap:8px}
.lt-res a{box-sizing:border-box;display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 14px;border:1px solid var(--lt-line);border-radius:10px;
  background:var(--lt-bg);font-size:14px;font-weight:600;line-height:1;color:var(--lt-head);text-decoration:none;transition:border-color .15s,background .15s}
.lt-res a:hover{border-color:var(--lt-acc);background:var(--lt-soft)}
.lt-res svg{display:block;width:16px;height:16px}.lt-res img{display:block;width:27px;height:16px}
.lt-res a.view{background:var(--lt-acc-soft);border-color:transparent;color:var(--lt-acc)}
.lt-res a.slack img{width:16px;height:16px}
.lt-res a.colab img{background:#FFFFFF;border-radius:4px;padding:2px 3px;box-sizing:content-box;margin-left:-3px}
.lt *{box-sizing:border-box}.lt ol,.lt ul{margin:0;padding:0;list-style:none}.lt h3,.lt p{margin:0}
.lt{display:block}.lt details.lt-box{padding:0;margin:0}.lt summary{font-weight:inherit;color:inherit}
.lt summary::before,.lt summary::after{content:none;display:none}.lt-top{margin-top:16px;text-align:left}
.lt-box{border:1px solid var(--lt-line);border-radius:16px;background:var(--lt-bg)}
.lt-box>summary{display:flex;align-items:center;gap:12px;padding:16px 20px;cursor:pointer;list-style:none;border-radius:16px}
.lt-box>summary::-webkit-details-marker{display:none}
.lt-box>summary:hover{background:var(--lt-soft)}
.lt-box>summary:focus-visible{outline:2px solid var(--lt-acc);outline-offset:2px}
.lt-t{flex:1;min-width:0;display:grid;gap:2px}
.lt-t b{font-size:18px;font-weight:800;color:var(--lt-head);letter-spacing:-.02em}
.lt-t small{font-size:13px;color:var(--lt-muted)}
.lt-btn{flex:none;display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:700;color:var(--lt-acc);background:var(--lt-acc-soft);border-radius:999px;padding:6px 12px}
.lt-btn::after{content:"";width:6px;height:6px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg) translateY(-2px);transition:transform .15s}
.lt-box[open] .lt-btn::after{transform:rotate(-135deg) translateX(-2px)}
.lt-box .lt-btn .c{display:none}.lt-box[open] .lt-btn .o{display:none}.lt-box[open] .lt-btn .c{display:inline}
.lt-body{display:grid;gap:12px;padding:4px 20px 20px}
.lt-intro{display:flex;gap:10px;align-items:baseline;font-size:13px;color:var(--lt-muted)}
.lt-intro b{flex:none;font-size:12px;color:var(--lt-head)}
.lt-board{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.lt-cd{display:flex;flex-direction:column;border:1px solid var(--lt-line);border-radius:14px;background:var(--lt-bg);overflow:hidden}
.lt-cd header{display:grid;grid-template-columns:1fr auto;align-items:center;gap:2px 8px;padding:12px 14px 10px;border-bottom:1px solid var(--lt-line);background:var(--lt-soft)}
.lt-n{font-family:ui-monospace,"SFMono-Regular",Consolas,monospace;font-size:12px;font-weight:700;color:var(--lt-acc)}
.lt-c{font-size:11px;color:var(--lt-muted);font-variant-numeric:tabular-nums}
.lt-cd h3{grid-column:1/-1;font-size:15px;font-weight:700;line-height:1.3;color:var(--lt-head)}
.lt-cd>ol{flex:1;display:grid;align-content:start;gap:1px;padding:10px 14px 12px}
.lt-cd li{display:grid;grid-template-columns:4px minmax(0,1fr) auto;column-gap:8px;font-size:13px;line-height:1.45;padding:2px 0}
.lt-cd li::before{content:"";width:4px;height:4px;border-radius:50%;background:var(--lt-line);margin-top:.6em}
.lt-cd li em{flex:none;font-style:normal;font-family:ui-monospace,"SFMono-Regular",Consolas,monospace;font-size:11px;color:var(--lt-muted)}
.lt-cd li.lt-sg{display:block;margin-top:4px}.lt-cd li.lt-sg::before{display:none}.lt-cd li.lt-sg>span{font-size:12px;font-weight:700;color:var(--lt-muted)}
.lt-cd li.lt-sg ul{padding:0 0 4px 10px}
.lt-cd li.lt-lab>span{font-weight:700;color:var(--lt-acc)}
.lt-lab-row{display:flex;gap:8px;align-items:baseline;padding:10px 14px;border-top:1px solid var(--lt-line);background:var(--lt-acc-soft);font-size:13px;font-weight:700;color:var(--lt-acc)}
.lt-lab-row span{flex:1;min-width:0}.lt-lab-row em{flex:none;font-style:normal;font-family:ui-monospace,"SFMono-Regular",Consolas,monospace;font-size:11px;font-weight:500;opacity:.8}
.lt-lab-row b{flex:none;font-size:11px;color:#fff;background:var(--lt-acc);border-radius:6px;padding:1px 6px}
.lt-note{font-size:12px;color:var(--lt-muted)}
@media (max-width:1000px){.lt-board{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:600px){.lt-board{grid-template-columns:1fr}.lt-body{padding:4px 12px 14px}.lt-box>summary{padding:14px}.lt-t b{font-size:16px}}
@media print{.lt-box>summary .lt-btn{display:none}}
</style>"""


def day_resources(d):
    """그날 자료 줄: 바로 보기 · 강의 자료 · Colab. 요약 페이지에도 끼우므로 스타일은 TREE_CSS(.lt-res)에 둔다."""
    res = []
    if d["lecture"]:
        res.append(f'<a class="view" href="lecture/">{ICON_VIEW}바로 보기</a>')
    if d["link"]:
        res.append(slack_link(d["link"], "slack", "강의 자료"))
    if d["colab"]:
        res.append(colab_link(d["colab"], "colab", "Colab 실습 ↗"))
    return f'<div class="lt-res" aria-label="보조 자료">{"".join(res)}</div>' if res else ""


def day_top(d):
    """요약 페이지 제목 아래 블록: 자료 줄 + 강의 목차 한눈에 보기"""
    return TREE_CSS + day_resources(d) + (tree_block(d["tree"], css=False) if d["tree"] else "")


def pull_labs(nodes):
    """실습 화면을 어느 깊이에 있든 뽑아낸다 → (실습들, 나머지). 실습만 있던 가운데 묶음은 지운다."""
    labs, keep = [], []
    for c in nodes:
        if c["c"]:
            sub_labs, sub_keep = pull_labs(c["c"])
            labs += sub_labs
            if sub_keep:
                keep.append({"t": c["t"], "c": sub_keep})
        elif LAB.search(c["t"]):
            labs.append(c)
        else:
            keep.append(c)
    return labs, keep


def lab_row(c):
    t = c["t"]
    pg = PDF_PAGE.search(t)
    if pg:
        t = t[:pg.start()]
    page = f'<em>{html.escape(pg.group(1).replace("PDF ", ""))}</em>' if pg else ""
    return f'<p class="lt-lab-row"><b>실습</b><span>{wbr(re.sub(r"^실습\s*", "", t))}</span>{page}</p>'


def tree_block(path, open_=False, css=True):
    """'강의 목차 한눈에 보기'(강사님 강의 자료 기준): 누르면 교시 카드 판이 펼쳐진다.
    교시마다 카드 하나에 원문 화면 제목을 모두 적고, 실습은 카드 맨 아래 띠로 둔다."""
    _, groups = read_tree(path)
    intro = [g for g in groups if g["t"].partition(" · ")[0] == "도입" and tree_leaves(g) <= 3]
    cards = []
    for g in groups:
        if g in intro:
            continue
        head, _, rest = g["t"].partition(" · ")
        labs, body = pull_labs(g["c"])
        name = (rest or head).strip().lower()
        body = [c for c in body if c["c"] or c["t"].strip().lower() != name]   # 교시 이름과 같은 화면(교시 표지)은 뺀다
        lab = "".join(lab_row(c) for c in labs)
        cards.append(f'<article class="lt-cd"><header><span class="lt-n">{html.escape(head) if rest else ""}</span>'
                     f'<span class="lt-c">화면 {tree_leaves(g)}</span><h3>{html.escape(rest or head)}</h3></header>'
                     f'<ol>{"".join(tree_item(c) for c in body)}</ol>{lab}</article>')
    strip = ""
    if intro:
        items = " · ".join(html.escape(n["t"]) for g in intro for n in tree_flat(g))
        strip = f'<p class="lt-intro"><b>도입</b><span>{items}</span></p>'
    total = sum(tree_leaves(g) for g in groups)
    return f"""{TREE_CSS if css else ""}<section class="lt" id="lecture-tree" aria-label="강의 목차">
<details class="lt-box"{" open" if open_ else ""}>
<summary><span class="lt-t"><b>강의 목차 한눈에 보기</b><small>강사님 강의 자료 기준 · {len(cards)}개 묶음 · 화면 {total}개</small></span>
<span class="lt-btn"><span class="o">펼치기</span><span class="c">접기</span></span></summary>
<div class="lt-body">{strip}<div class="lt-board">{"".join(cards)}</div>
<p class="lt-note">강의 자료의 화면 제목을 원문 그대로 옮겼습니다. 실습은 각 교시 카드 맨 아래에 모았습니다.</p></div>
</details></section>"""


def has_page(d):
    """그날 볼 페이지가 있는가: 요약 또는 강의 목차"""
    return bool(d["src"] or d["tree"])


def day_title(d):
    """그날 제목: 요약의 <h1>, 요약 전이면 예정 제목 → 교재 제목"""
    if d["src"]:
        return page_h1(d["src"])
    return (PLANNED_TITLES.get(f'{d["key"]}/{d["ymd"]}') or (read_tree(d["tree"])[0] if d["tree"] else "")
            or (lecture_title(d["lecture"]) if d["lecture"] else "") or f'Day{d["n"]}')


def lecture_title(lecture):
    """강의 HTML의 <title> (예: "Day22 · LLM API 클라이언트" → "LLM API 클라이언트")"""
    m = re.search(r"<title>(.*?)</title>", (lecture / "index.html").read_text(encoding="utf-8"), re.S)
    t = html.unescape(m.group(1)).strip() if m else ""
    return re.sub(r"^Day\s*\d+\s*[·:|-]\s*", "", t)


def tree_day_page(d):
    """요약이 아직 없는 날: 머리 + 자료 줄 + 강의 목차(강사님 자료 기준) + 요약 준비 중 표시"""
    book, _ = read_tree(d["tree"])
    title = PLANNED_TITLES.get(f'{d["key"]}/{d["ymd"]}') or book or f'Day{d["n"]}'
    sub = f'<p class="sub">교재 · {html.escape(book)}</p>' if book and book != title else ""
    body = f"""<header class="day-head"><p class="eyebrow">Day{d["n"]} · {md(d["date"])} · {html.escape(d["short"])}</p>
<h1>{html.escape(title)}</h1>{sub}</header>
<div class="lt-top">{day_top(d)}</div>
<p class="sum-empty">요약 준비 중입니다.</p>"""
    nav = nav_html(2, [(d["short"], f'{d["key"]}/')], here=f'Day{d["n"]}', lecture=d["link"],
                   view="lecture/" if d["lecture"] else None).replace(DOWNLOAD_MARK, "")
    return list_page(f'Day{d["n"]} {title} · {SITE_NAME}', body, nav, up="../../")


def home_page(days, subjects, today):
    dates = sorted({d["date"] for d in days})
    done = sum(x <= today for x in dates)
    made = [d for d in days if d["src"]]                 # '요약 N일' 숫자: 실제로 요약을 쓴 날
    shown = [d for d in days if has_page(d) and d["date"] <= today]   # 최근 수업: 오늘까지, 요약 또는 강의 목차가 있는 날
    latest = shown[-1] if shown else None
    pend = '<span class="pend">요약 준비 중</span>'
    recent = "".join(
        f'<li class="{"on" if d is latest else ""}"><a href="{d["key"]}/{d["ymd"]}/"><span class="no">Day{d["n"]}</span>'
        f'<span class="t">{html.escape(day_title(d))}{"" if d["src"] else pend}</span><span class="d">{md(d["date"])}</span>'
        f'<span class="go">{ICON_ARROW}</span></a></li>'
        for d in reversed(shown[-4:]))
    practice = "".join(f'<a href="{html.escape(url)}" target="_blank" rel="noopener">'
                       f'<img src="{image_data(HERE / "assets" / "logos" / logo)}" alt="" width="20" height="20">{name} ↗</a>'
                       for name, logo, url in PRACTICE)
    sesac = image_data(HERE / "assets" / "branding" / "sesac.png")
    nvidia = image_data(HERE / "assets" / "branding" / "nvidia.svg")
    chapters = "".join(chapter_block(k, ds, "") for k, ds in reversed(subjects))
    body = f"""<header class="top">
<div class="brand"><span class="brand-logos"><img src="{sesac}" alt="새싹(SeSAC)" height="32"><span class="brand-sep" aria-hidden="true"></span><img src="{nvidia}" alt="NVIDIA" height="32"></span>
<p>청년취업사관학교 · AI 코어 엔지니어 2기</p></div>
<div class="top-r"><nav class="links" aria-label="문제 풀이">{practice}</nav>{THEME_BTN}</div>
</header>
<section class="hero"><div class="hero-l"><h1 class="title">{SITE_NAME}</h1>
<p class="count">수업 <b>{done}</b> / {len(dates)}일 · 요약 <b>{len(made)}</b>일</p>
<div><p class="label">최근 수업</p><ol class="recent">{recent}</ol></div></div>
{cover_card(days, subjects, today)}</section>
<div class="timeline" aria-label="과정 전체 일정">{timeline(days, today)}</div>
{shelf_block(list(reversed(subjects)), "")}
{chapters}"""
    return list_page(SITE_NAME, body)


def subject_page(key, ds):
    nav = nav_html(1, [], here=ds[0]["short"])
    return list_page(f'{ds[0]["short"]} · {SITE_NAME}', chapter_block(key, ds, "../", link_head=False), nav, up="../")


# ── 만들기 ──────────────────────────────────────────────────────────────
def main():
    days = read_days()
    today = datetime.date.today().isoformat()
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()
    shutil.copytree(HERE / "assets" / "fonts", PUBLIC / "fonts")   # 홈·과목 목록의 Pretendard(OFL)

    # 과목별로 묶기: 수업이 시작된 과목은 홈에 모두 보이고, 과목 페이지는 요약이 있는 과목만 만든다
    started, subjects = [], []
    for name, (key, _) in SUBJECTS.items():
        ds = [d for d in days if d["subject"] == name]
        if not key or not ds:
            continue
        if ds[0]["date"] <= today:
            started.append((key, ds))
        if any(d["src"] or d["tree"] for d in ds) or (PAGES / key / "all" / "index.html").exists():
            subjects.append((key, ds))

    print("매일 요약")
    made = [d for d in days if d["src"]]
    for i, d in enumerate(made):
        prev = (f'Day{made[i-1]["n"]}', f'{made[i-1]["key"]}/{made[i-1]["ymd"]}/') if i > 0 else None
        nxt = (f'Day{made[i+1]["n"]}', f'{made[i+1]["key"]}/{made[i+1]["ymd"]}/') if i + 1 < len(made) else None
        nav = nav_html(2, [(d["short"], f'{d["key"]}/')], here=f'Day{d["n"]}',
                       prev=prev, next_=nxt, lecture=d["link"], view="lecture/" if d["lecture"] else None)
        copy_page(d["src"], f'{d["key"]}/{d["ymd"]}', nav, top=day_top(d) if d["tree"] or d["colab"] else "")
        for sub, label in DAY_SUBPAGES.get(f'{d["key"]}/{d["ymd"]}', []):
            copy_page(d["src"] / sub, f'{d["key"]}/{d["ymd"]}/{sub}',
                      nav_html(3, [(d["short"], f'{d["key"]}/'), (f'Day{d["n"]}', f'{d["key"]}/{d["ymd"]}/')], here=label))

    print("강의 목차 (요약 전)")
    for d in days:
        if d["tree"] and not d["src"]:
            out = PUBLIC / d["key"] / d["ymd"]
            out.mkdir(parents=True, exist_ok=True)
            (out / "index.html").write_text(tree_day_page(d), encoding="utf-8")
            print(f'  /{d["key"]}/{d["ymd"]}/ ← {d["tree"].relative_to(HERE)} (강의 목차 한눈에 보기)')

    print("강의 자료 바로 보기")
    for d in days:
        if not d["lecture"]:
            continue
        crumbs = [(d["short"], f'{d["key"]}/')]
        if d["src"] or d["tree"]:
            crumbs.append((f'Day{d["n"]}', f'{d["key"]}/{d["ymd"]}/'))
        here = "강의 자료" if d["src"] or d["tree"] else f'Day{d["n"]} 강의 자료'
        copy_lecture(d["lecture"], f'{d["key"]}/{d["ymd"]}/lecture', nav_html(3, crumbs, here=here, lecture=d["link"]))

    print("과목")
    for key, ds in subjects:
        src = PAGES / key / "all"
        if (src / "index.html").exists():
            copy_page(src, key, nav_html(1, [], here=f'{ds[0]["short"]} 4일 종합'))
        else:
            (PUBLIC / key).mkdir(parents=True, exist_ok=True)
            (PUBLIC / key / "index.html").write_text(subject_page(key, ds), encoding="utf-8")
            print(f"  /{key}/ ← 날짜 카드 목록")

    print("치트시트")
    for k, (name, *_) in CHEATSHEETS.items():
        src = PAGES / "cheatsheet" / k
        copy_page(src, f"cheatsheet/{k}", nav_html(2, [], here=name))

    print("설치 가이드" + (" (--release: 공개 전 페이지 제외)" if RELEASE else ""))
    for k, name, *_ in setup_items():
        subs = SETUP_PAGES.get(k)
        if not subs:
            copy_page(PAGES / "setup" / k, f"setup/{k}", nav_html(2, [], here=name))
            continue
        paths = [f"setup/{k}/" + (f"{sub}/" if sub else "") for sub, _ in subs]
        for i, (sub, label) in enumerate(subs):
            prev = (subs[i - 1][1], paths[i - 1]) if i else None
            next_ = (subs[i + 1][1], paths[i + 1]) if i + 1 < len(subs) else None
            if sub:
                nav = nav_html(3, [(name, paths[0])], here=label, prev=prev, next_=next_)
            else:
                nav = nav_html(2, [], here=f"{name} · {label}", next_=next_)
            copy_page(PAGES / "setup" / k / sub if sub else PAGES / "setup" / k,
                      paths[i].rstrip("/"), nav)

    (PUBLIC / "index.html").write_text(home_page(days, started, today), encoding="utf-8")
    print(f"홈 · 기준일 {today}")
    if FONT_WARNINGS:
        print(f"\n⚠ 글꼴 경고 {len(FONT_WARNINGS)}건 (빌드는 계속됨): 본문은 Pretendard만 씁니다")
        for w in FONT_WARNINGS:
            print("  -", w)
    else:
        print("글꼴 검사: 전 페이지 Pretendard 통과")


if __name__ == "__main__":
    main()
