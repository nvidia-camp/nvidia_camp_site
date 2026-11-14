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
- 홈: 맨 위 제목·최근 수업·지금 과목 표지 → 100일 일정 → 참고 문서 모음 → 과목별 챕터(Day 목록).
  참고 문서 모음은 공통 묶음(COMMON_GROUPS)별 설치 가이드 칸 + '과목 참고 문서' 칸(치트시트·과목 설치 가이드).
- 홈·과목 목록은 Pretendard(OFL, assets/fonts → public/fonts)를 쓴다. 각 요약 페이지 글꼴은 건드리지 않는다.
- 각 폴더의 index.html과 요약 PDF를 public/에 복사한다.
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
    "local-ai": ("로컬 AI 코딩", "ollama.png", "내 PC의 GPU로 AI 모델 돌리기 · Ollama + OpenCode 설치", "AI 코딩", False),
    "ai-coding": ("AI 코딩 도구", "code.svg", "OpenCode · Claude Code · Codex · agy 사용법", "AI 코딩", False),
    "cli": ("CLI 도구", "terminal.svg", "AI 에이전트가 쓰는 터미널 도구", "AI 코딩", False),
}
# 과정 전체에서 쓰는 가이드의 묶음과 순서. 홈 '공통 가이드' 섹션에 묶음마다 한 줄씩 나온다.
COMMON_GROUPS = ["개발 환경", "AI 코딩"]
# 페이지와 함께 내려받게 둘 파일: 사이트 경로 → [파일 이름]. 페이지에서는 data-site를 붙여 링크한다.
FILES = {
    "setup/local-ai": ["SETUP_FOR_AI.md"],
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
        days.append({
            "n": row["day"], "date": row["date"], "ymd": folder, "key": key, "short": short,
            "subject": row["subject"], "link": row["link"],
            "src": src if src and (src / "index.html").exists() else None,
        })
    return days


def page_h1(src):
    text = (src / "index.html").read_text(encoding="utf-8")
    m = re.search(r"<h1[^>]*>(.*?)</h1>", text, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1)).strip()) if m else src.name


def pdf_of(src):
    pdfs = sorted(p.name for p in src.glob("*.pdf"))
    return pdfs[0] if pdfs else None


def md(date):
    return f"{int(date[5:7])}/{int(date[8:10])}"


# ── 내용 페이지 위쪽 메뉴 ────────────────────────────────────────────────
NAV_CSS = f"""<style>
.cn-nav{{box-sizing:border-box;display:flex;flex-wrap:wrap;align-items:center;gap:.25rem 1rem;
  padding:.5rem 1rem;background:#142849;color:#fff;font:500 .875rem/1.5 {FONT}}}
.cn-nav a{{color:#fff;text-decoration:none;padding:.125rem .375rem;border-radius:.375rem}}
.cn-nav a:hover,.cn-nav a:focus-visible{{background:rgba(255,255,255,.16);outline:none}}
.cn-nav .cn-here{{opacity:.7}}
.cn-nav .cn-right{{margin-left:auto;display:flex;gap:.25rem .75rem;flex-wrap:wrap}}
@media print{{.cn-nav{{display:none}}}}
</style>"""


def nav_html(depth, crumbs, here=None, pdf=None, prev=None, next_=None, lecture=None):
    """crumbs: [(이름, 루트 기준 경로)], here: 현재 위치 글자, prev/next_: (이름, 경로)"""
    up = "../" * depth
    left = [f'<a href="{up or "./"}">← {SITE_NAME}</a>']
    left += [f'<a href="{up}{path}">{html.escape(name)}</a>' for name, path in crumbs]
    if here:
        left.append(f'<span class="cn-here">{html.escape(here)}</span>')
    right = []
    if lecture:
        right.append(f'<a href="{html.escape(lecture)}" target="_blank" rel="noopener">강의 자료 ↗</a>')
    if pdf:
        right.append(f'<a href="{html.escape(pdf)}">PDF</a>')
    if prev:
        right.append(f'<a href="{up}{prev[1]}">‹ {html.escape(prev[0])}</a>')
    if next_:
        right.append(f'<a href="{up}{next_[1]}">{html.escape(next_[0])} ›</a>')
    side = f'<span class="cn-right">{"".join(right)}</span>' if right else ""
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


def copy_page(src, dest, nav):
    text = (src / "index.html").read_text(encoding="utf-8")
    text, n_links = strip_local_links(text)
    text, n_body = re.subn(r"(<body[^>]*>)", lambda m: m.group(1) + nav + ANALYTICS, text, count=1)
    assert n_body == 1, f"<body> 없음: {src}"
    out = PUBLIC / dest
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(text, encoding="utf-8")
    pdf = pdf_of(src)
    if pdf:
        shutil.copy2(src / pdf, out / pdf)
    for name in FILES.get(dest, []):
        shutil.copy2(src / name, out / name)
    note = f" (사이트에 없는 링크 {n_links}개를 글자로)" if n_links else ""
    print(f"  /{dest}/ ← {src.relative_to(HERE)}{note}")


# ── 목록 페이지 (홈, 과목) ───────────────────────────────────────────────
# 이 저장소에서 그린 아이콘: 두 테마 모두에서 보이는 색이라 다크 모드 흰 받침을 깔지 않는다
OWN_ICONS = {"code.svg", "terminal.svg"}


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
.shelf{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin:40px 0 8px;border:1px solid var(--line);border-radius:20px;background:var(--surface)}
.shelf .col{display:grid;gap:4px;align-content:start;padding:22px 24px;border-left:1px solid var(--line);margin-left:-1px}
.shelf h2{font-size:12px;font-weight:700;letter-spacing:.06em;color:var(--muted);margin-bottom:8px}
.shelf a{display:flex;align-items:center;gap:10px;padding:7px 8px;margin:0 -8px;border-radius:10px;font-size:15px;font-weight:600;color:var(--heading);transition:background .15s}
.shelf a:hover{background:var(--soft)}
.ref-logo{display:flex;align-items:center;justify-content:center;flex:none;border-radius:6px}
.ref-logo img{display:block;width:auto;height:22px;max-width:36px;object-fit:contain}
@media (prefers-color-scheme:dark){.ref-logo:not(.own){background:#FFFFFF;padding:3px 5px}}
.soon{white-space:nowrap;font-size:12px;font-weight:600;color:var(--muted);border:1px solid var(--line-2);border-radius:999px;padding:2px 10px;justify-self:start}

/* 과목 = 챕터 */
.chapter{display:grid;grid-template-columns:220px minmax(0,1fr);gap:40px;padding:44px 0;border-top:1px solid var(--line-2)}
.chapter.empty{grid-template-columns:1fr;padding:22px 0}
.ch-side{display:grid;gap:4px;align-content:start}
.ch-no{font-family:var(--mono);font-size:13px;font-weight:600;color:var(--accent)}
.ch-side h2{font-size:28px;letter-spacing:-.03em;line-height:1.15;margin:2px 0 6px}
.ch-side h2 a:hover{text-decoration:underline;text-underline-offset:4px}
.ch-meta{font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.chapter.empty .ch-side{grid-auto-flow:column;justify-content:start;align-items:baseline;gap:14px}
.chapter.empty h2{font-size:22px;margin:0}
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
.rows li.all .row{background:linear-gradient(90deg,var(--soft),transparent 70%)}
.rows li.all .no{color:var(--accent)}

@media (max-width:880px){.hero{grid-template-columns:1fr;gap:28px;margin-top:32px}.shelf{grid-template-columns:1fr}.shelf .col{border-left:0;margin-left:0;border-top:1px solid var(--line)}
  .shelf .col:first-child{border-top:0}.chapter{grid-template-columns:1fr;gap:16px;padding:32px 0}.rows li{grid-template-columns:1fr}
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
{ANALYTICS}
</head>
<body>{nav}
<main>
{body}
</main>
</body>
</html>
"""


def day_links(d, up):
    """Day 한 줄 오른쪽의 작은 버튼: PDF · 강의 자료 · 하위 페이지"""
    href = f'{up}{d["key"]}/{d["ymd"]}/'
    out = []
    pdf = pdf_of(d["src"])
    if pdf:
        out.append(f'<a class="mini" href="{href}{html.escape(pdf)}">{ICON_DOC}PDF</a>')
    if d["link"]:
        out.append(f'<a class="mini" href="{html.escape(d["link"])}" target="_blank" rel="noopener">{ICON_EXT}강의 자료</a>')
    for sub, label in DAY_SUBPAGES.get(f'{d["key"]}/{d["ymd"]}', []):
        out.append(f'<a class="mini" href="{href}{sub}/">{ICON_ARROW}{html.escape(label)}</a>')
    return "".join(out)


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
    """과목 한 블록: 왼쪽 챕터 번호·이름·범위, 오른쪽 Day 목록"""
    made = [d for d in ds if d["src"]]
    has_all = (PAGES / key / "all" / "index.html").exists()
    today = datetime.date.today().isoformat()
    name = html.escape(ds[0]["short"])
    if link_head and (made or has_all):
        name = f'<a href="{up}{key}/">{name}</a>'
    rng = f'Day{ds[0]["n"]}–{ds[-1]["n"]}'
    if not made and not has_all:
        return (f'<section class="chapter empty"><div class="ch-side"><span class="ch-no">{CHAPTER[key]:02d}</span>'
                f'<h2 title="{html.escape(ds[0]["subject"])}">{name}</h2><span class="ch-meta">{rng}</span><span class="soon">준비 중</span></div></section>')
    side = (f'<div class="ch-side"><span class="ch-no">{CHAPTER[key]:02d}</span><h2 title="{html.escape(ds[0]["subject"])}">{name}</h2>'
            f'<span class="ch-meta">{rng}</span><span class="ch-meta">요약 {len(made)} / {len(ds)}일</span></div>')
    rows = []
    if has_all:
        src = PAGES / key / "all"
        pdf = pdf_of(src)
        btn = f'<a class="mini" href="{up}{key}/{html.escape(pdf)}">{ICON_DOC}PDF</a>' if pdf else ""
        rows.append(f'<li class="all"><a class="row" href="{up}{key}/"><span class="no">종합</span>'
                    f'<span class="t">{html.escape(page_h1(src))}</span><span class="d">{len(ds)}일</span></a><span class="lk">{btn}</span></li>')
    for d in reversed(made):
        rows.append(f'<li><a class="row" href="{up}{d["key"]}/{d["ymd"]}/"><span class="no">Day{d["n"]}</span>'
                    f'<span class="t">{html.escape(page_h1(d["src"]))}</span><span class="d">{md(d["date"])}</span></a>'
                    f'<span class="lk">{day_links(d, up)}</span></li>')
    return f'<section class="chapter" id="{key}">{side}<ol class="rows">{"".join(rows)}</ol></section>'


def cover_card(days, subjects, today):
    """지금 과목 표지: 오늘이 속한(없으면 마지막으로 시작한) 과목"""
    key, ds = subjects[-1]
    n_done = len([d for d in ds if d["date"] <= today])
    made = [d for d in ds if d["src"]]
    if made:
        go_href, go_text = f'{made[-1]["key"]}/{made[-1]["ymd"]}/', f'Day{made[-1]["n"]} · {page_h1(made[-1]["src"])}'
    else:
        go_href, go_text = f'#{key}', f'{ds[0]["short"]} 보기'
    return (f'<a class="cover" href="{go_href}"><span class="wm" aria-hidden="true">{CHAPTER[key]:02d}</span>'
            f'<span class="eyebrow">CHAPTER {CHAPTER[key]:02d} · 지금 과목</span>'
            f'<b>{html.escape(ds[0]["short"])}</b><span class="c-n">{html.escape(ds[0]["subject"])}</span>'
            f'<span class="prog"><span class="bar"><i style="width:{round(100 * n_done / len(ds))}%"></i></span>'
            f'<span class="c-k">{n_done} / {len(ds)}일</span></span>'
            f'<span class="c-go"><span>{html.escape(go_text)}</span>{ICON_ARROW}</span></a>')


def timeline(days, today):
    groups, current = [], None
    for d in days:
        if d["subject"] != current:
            groups.append((d["short"], []))
            current = d["subject"]
        state = "has" if d["src"] else ("past" if d["date"] <= today else "")
        if d["date"] == today:
            state += " today"
        tip = html.escape(f'Day{d["n"]} · {md(d["date"])} · {d["subject"]}')
        if d["src"]:
            groups[-1][1].append(f'<a class="cell {state}" href="{d["key"]}/{d["ymd"]}/" title="{tip}" aria-label="{tip}"></a>')
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


def home_page(days, subjects, today):
    dates = sorted({d["date"] for d in days})
    done = sum(x <= today for x in dates)
    made = [d for d in days if d["src"]]
    latest = made[-1] if made else None
    recent = "".join(
        f'<li class="{"on" if d is latest else ""}"><a href="{d["key"]}/{d["ymd"]}/"><span class="no">Day{d["n"]}</span>'
        f'<span class="t">{html.escape(page_h1(d["src"]))}</span><span class="d">{md(d["date"])}</span>'
        f'<span class="go">{ICON_ARROW}</span></a></li>'
        for d in reversed(made[-4:]))
    practice = "".join(f'<a href="{html.escape(url)}" target="_blank" rel="noopener">'
                       f'<img src="{image_data(HERE / "assets" / "logos" / logo)}" alt="" width="20" height="20">{name} ↗</a>'
                       for name, logo, url in PRACTICE)
    sesac = image_data(HERE / "assets" / "branding" / "sesac.png")
    nvidia = image_data(HERE / "assets" / "branding" / "nvidia.svg")
    chapters = "".join(chapter_block(k, ds, "") for k, ds in reversed(subjects))
    body = f"""<header class="top">
<div class="brand"><span class="brand-logos"><img src="{sesac}" alt="새싹(SeSAC)" height="32"><span class="brand-sep" aria-hidden="true"></span><img src="{nvidia}" alt="NVIDIA" height="32"></span>
<p>청년취업사관학교 · AI 코어 엔지니어 2기</p></div>
<nav class="links" aria-label="문제 풀이">{practice}</nav>
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
        if any(d["src"] for d in ds) or (PAGES / key / "all" / "index.html").exists():
            subjects.append((key, ds))

    print("매일 요약")
    made = [d for d in days if d["src"]]
    for i, d in enumerate(made):
        prev = (f'Day{made[i-1]["n"]}', f'{made[i-1]["key"]}/{made[i-1]["ymd"]}/') if i > 0 else None
        nxt = (f'Day{made[i+1]["n"]}', f'{made[i+1]["key"]}/{made[i+1]["ymd"]}/') if i + 1 < len(made) else None
        nav = nav_html(2, [(d["short"], f'{d["key"]}/')], here=f'Day{d["n"]}',
                       pdf=pdf_of(d["src"]), prev=prev, next_=nxt, lecture=d["link"])
        copy_page(d["src"], f'{d["key"]}/{d["ymd"]}', nav)
        for sub, label in DAY_SUBPAGES.get(f'{d["key"]}/{d["ymd"]}', []):
            copy_page(d["src"] / sub, f'{d["key"]}/{d["ymd"]}/{sub}',
                      nav_html(3, [(d["short"], f'{d["key"]}/'), (f'Day{d["n"]}', f'{d["key"]}/{d["ymd"]}/')], here=label))

    print("과목")
    for key, ds in subjects:
        src = PAGES / key / "all"
        if (src / "index.html").exists():
            copy_page(src, key, nav_html(1, [], here=f'{ds[0]["short"]} 4일 종합', pdf=pdf_of(src)))
        else:
            (PUBLIC / key).mkdir(parents=True, exist_ok=True)
            (PUBLIC / key / "index.html").write_text(subject_page(key, ds), encoding="utf-8")
            print(f"  /{key}/ ← 날짜 카드 목록")

    print("치트시트")
    for k, (name, *_) in CHEATSHEETS.items():
        src = PAGES / "cheatsheet" / k
        copy_page(src, f"cheatsheet/{k}", nav_html(2, [], here=name, pdf=pdf_of(src)))

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


if __name__ == "__main__":
    main()
