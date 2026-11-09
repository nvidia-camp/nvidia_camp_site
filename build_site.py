# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""pages/의 요약을 모아 배포용 사이트(public/)를 만든다.

사용: uv run build_site.py   (site 폴더에서)

- 원본은 pages/ 아래에 둔다. 폴더 이름만 맞추면 자동으로 사이트에 들어간다.
    pages/<과목>/<YYYYMMDD>/   매일 요약     → /<과목>/<YYYYMMDD>/  (같은 날 두 번째 회차는 <YYYYMMDD>-2)
    pages/<과목>/all/          과목 4일 종합 → /<과목>/  (없으면 날짜 카드 목록)
    pages/cheatsheet/<이름>/   치트시트      → /cheatsheet/<이름>/ (CHEATSHEETS에 보이는 이름 등록)
- 각 폴더의 index.html과 요약 PDF를 public/에 복사한다.
- 복사본에만 위쪽 메뉴를 넣고, 사이트에 없는 파일을 가리키는 상대 링크는 글자만 남긴다.
- Day 번호·날짜·과목·강의 자료 링크는 lectures.json(sync_lectures.py가 학습 자료 시트에서 만듦)에서 읽는다.
- public/은 매번 지우고 새로 만든다. 직접 고치지 않는다. 강의 교재 PDF는 넣지 않는다.
"""
import datetime
import json
import html
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGES = HERE / "pages"
PUBLIC = HERE / "public"
LECTURES = HERE / "lectures.json"
SITE_NAME = "AI 코어 엔지니어 학습 노트"

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
# 문제 풀이 사이트 (홈 위쪽 링크)
PRACTICE = [
    ("SWEA", "https://swexpertacademy.com/main/talk/solvingClub/clubView.do?solveclubId=AaFX6-bK02vHBISG"),
    ("프로그래머스", "https://school.programmers.co.kr/learn/challenges?order=recent&page=1&languages=python3"),
]
# 치트시트: pages/cheatsheet/<이름> → 보이는 이름
CHEATSHEETS = {"sklearn": "scikit-learn", "pytorch": "PyTorch", "opencv": "OpenCV"}

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
    left = [f'<a href="{up or "./"}">← 학습 노트</a>']
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


LOCAL_LINK = re.compile(r'<a\s[^>]*href="(?!https?:|#|mailto:|data:)[^"]*"[^>]*>(.*?)</a>', re.S)


def copy_page(src, dest, nav):
    text = (src / "index.html").read_text(encoding="utf-8")
    text, n_links = LOCAL_LINK.subn(r"<span>\1</span>", text)
    text, n_body = re.subn(r"(<body[^>]*>)", lambda m: m.group(1) + nav, text, count=1)
    assert n_body == 1, f"<body> 없음: {src}"
    out = PUBLIC / dest
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(text, encoding="utf-8")
    pdf = pdf_of(src)
    if pdf:
        shutil.copy2(src / pdf, out / pdf)
    note = f" (사이트에 없는 링크 {n_links}개를 글자로)" if n_links else ""
    print(f"  /{dest}/ ← {src.relative_to(HERE)}{note}")


# ── 목록 페이지 (홈, 과목) ───────────────────────────────────────────────
PAGE_CSS = f"""
:root{{--bg:#F9FBFE;--surface:#FFFFFF;--soft:#F0F6FD;--border:#D8E4F2;--primary:#142849;
  --heading:#1C2B40;--text:#222F44;--muted:#52667E;--cell-past:#C9D7EA;--cell-future:#E2EAF5;
  --on-primary:#FFFFFF;--focus:#4B74A6}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0E1626;--surface:#152038;--soft:#1A2844;--border:#2A3B5C;
  --primary:#A9C3EC;--heading:#E7EEF9;--text:#D4DDEB;--muted:#9DADC4;--cell-past:#33476B;
  --cell-future:#1C2943;--on-primary:#0E1626;--focus:#A9C3EC;color-scheme:dark}}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--text);font:400 16px/1.6 {FONT};word-break:keep-all;overflow-wrap:break-word}}
main{{max-width:1120px;margin:0 auto;padding:40px 16px 72px;display:grid;gap:56px}}
h1,h2,h3{{color:var(--heading);margin:0;line-height:1.35;text-wrap:balance}}
h1{{font-size:clamp(26px,4vw,34px);letter-spacing:-.02em}}
h2{{font-size:20px}}
h3{{font-size:16px;line-height:1.45;font-weight:600}}
a{{color:inherit;text-decoration:none}}
a:focus-visible{{outline:2px solid var(--focus);outline-offset:3px;border-radius:6px}}
p{{margin:0}}
.top{{display:grid;gap:20px}}
.row{{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px 24px}}
.links{{display:flex;flex-wrap:wrap;gap:8px}}
.links a{{display:inline-flex;align-items:center;min-height:40px;padding:0 14px;border:1px solid var(--border);
  border-radius:999px;background:var(--surface);font-size:14px;font-weight:600;color:var(--heading)}}
.links a:hover{{border-color:var(--primary)}}
.quiet-list{{display:grid;gap:12px}}
.quiet h2{{font-size:17px;color:var(--muted);font-weight:600}}
.soon{{font-size:12px;border:1px dashed var(--border);border-radius:999px;padding:0 8px}}
.count{{color:var(--muted);font-size:15px;font-variant-numeric:tabular-nums}}
.count b{{color:var(--heading)}}
.timeline{{display:flex;flex-wrap:wrap;gap:14px 24px;padding:20px;background:var(--surface);
  border:1px solid var(--border);border-radius:16px}}
.tl{{display:grid;gap:6px;min-width:0}}
.tl-name{{font-size:13px;font-weight:600;color:var(--heading)}}
.tl-cells{{display:flex;flex-wrap:wrap;gap:3px}}
.cell{{width:14px;height:14px;border-radius:3px;display:inline-block;background:var(--cell-future)}}
.cell.past{{background:var(--cell-past)}}
.cell.has{{background:var(--primary)}}
a.cell:hover{{transform:scale(1.25)}}
.cell.today{{box-shadow:0 0 0 2px var(--surface),0 0 0 4px var(--primary)}}
.subject{{display:grid;gap:16px}}
.subject-head{{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px}}
.subject-head a:hover h2{{text-decoration:underline}}
.subject-head span{{color:var(--muted);font-size:14px;font-variant-numeric:tabular-nums}}
.grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px 16px}}
.card{{display:grid;gap:6px;align-content:start;min-width:0;padding:16px;background:var(--surface);
  border:1px solid var(--border);border-radius:14px}}
.card:hover{{border-color:var(--primary)}}
.card:hover h3{{text-decoration:underline}}
.meta{{display:flex;gap:8px;font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}}
.meta b{{color:var(--heading)}}
.pdf,.links-row a{{font-size:13px;color:var(--primary);text-decoration:underline;text-underline-offset:3px}}
.pdf{{justify-self:start}}
.links-row{{display:flex;flex-wrap:wrap;gap:4px 14px}}
.feature{{display:grid;gap:6px;padding:20px;background:var(--soft);border:1px solid var(--border);border-radius:16px}}
.feature:hover{{border-color:var(--primary)}}
.feature:hover h3{{text-decoration:underline}}
.feature h3{{font-size:22px;font-weight:700}}
.label{{font-size:13px;font-weight:600;color:var(--muted)}}
.btn{{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:12px;
  background:var(--primary);color:var(--on-primary);font-weight:600;font-size:15px}}
.sheets{{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:900px){{.grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:640px){{.sheets{{grid-template-columns:1fr 1fr}}}}
@media (prefers-reduced-motion:reduce){{a.cell:hover{{transform:none}}}}
"""


def list_page(title, body, nav=""):
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{PAGE_CSS}</style>
</head>
<body>{nav}
<main>
{body}
</main>
</body>
</html>
"""


def day_card(d, up):
    href = f'{up}{d["key"]}/{d["ymd"]}/'
    pdf = pdf_of(d["src"])
    links = []
    if pdf:
        links.append(f'<a href="{href}{html.escape(pdf)}">PDF</a>')
    if d["link"]:
        links.append(f'<a href="{html.escape(d["link"])}" target="_blank" rel="noopener">강의 자료 ↗</a>')
    row = f'<p class="links-row">{"".join(links)}</p>' if links else ""
    return (f'<div class="card"><a href="{href}">'
            f'<p class="meta"><b>Day{d["n"]}</b><span>{md(d["date"])}</span></p>'
            f'<h3>{html.escape(page_h1(d["src"]))}</h3></a>{row}</div>')


def feature_card(key, up):
    src = PAGES / key / "all"
    href = f"{up}{key}/"
    pdf = pdf_of(src)
    pdf_link = f'<a class="pdf" href="{href}{html.escape(pdf)}">PDF</a>' if pdf else ""
    return (f'<div class="feature"><a href="{href}"><p class="label">4일 종합</p>'
            f'<h3>{html.escape(page_h1(src))}</h3></a>{pdf_link}</div>')


def subject_block(key, ds, up, link_head=True):
    made = [d for d in ds if d["src"]]
    has_all = (PAGES / key / "all" / "index.html").exists()
    if not made and not has_all:
        return (f'<section class="subject quiet"><div class="subject-head"><h2>{html.escape(ds[0]["subject"])}</h2>'
                f'<span>Day{ds[0]["n"]}–{ds[-1]["n"]}</span><span class="soon">준비 중</span></div></section>')
    head = f'<h2>{html.escape(ds[0]["subject"])}</h2>'
    if link_head:
        head = f'<a href="{up}{key}/">{head}</a>'
    parts = [f'<div class="subject-head">{head}<span>Day{ds[0]["n"]}–{ds[-1]["n"]}</span></div>']
    if has_all:
        parts.append(feature_card(key, up))
    if made:
        parts.append(f'<div class="grid">{"".join(day_card(d, up) for d in made)}</div>')
    return f'<section class="subject">{"".join(parts)}</section>'


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


def home_page(days, subjects, today):
    dates = sorted({d["date"] for d in days})
    done = sum(x <= today for x in dates)
    made = sum(bool(d["src"]) for d in days)
    ordered = list(reversed(subjects))
    full = [subject_block(k, ds, "") for k, ds in ordered if "quiet" not in subject_block(k, ds, "")]
    quiet = [subject_block(k, ds, "") for k, ds in ordered if "quiet" in subject_block(k, ds, "")]
    blocks = "".join(full) + (f'<div class="quiet-list">{"".join(quiet)}</div>' if quiet else "")
    sheets = "".join(
        f'<div class="card"><a href="cheatsheet/{k}/"><h3>{name}</h3></a></div>' for k, name in CHEATSHEETS.items())
    practice = "".join(f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{name} ↗</a>'
                       for name, url in PRACTICE)
    body = f"""<header class="top">
<h1>{SITE_NAME}</h1>
<div class="row"><p class="count">수업 <b>{done}</b> / {len(dates)}일 · 요약 <b>{made}</b>일</p>
<nav class="links" aria-label="문제 풀이">{practice}</nav></div>
<div class="timeline" aria-label="과정 전체 일정">{timeline(days, today)}</div>
</header>
{blocks}
<section class="subject" id="cheatsheet"><div class="subject-head"><h2>치트시트</h2></div>
<div class="grid sheets">{sheets}</div></section>"""
    return list_page(SITE_NAME, body)


def subject_page(key, ds):
    nav = nav_html(1, [], here=ds[0]["short"])
    return list_page(f'{ds[0]["short"]} · {SITE_NAME}', subject_block(key, ds, "../", link_head=False), nav)


# ── 만들기 ──────────────────────────────────────────────────────────────
def main():
    days = read_days()
    today = datetime.date.today().isoformat()
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()

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
    for k, name in CHEATSHEETS.items():
        src = PAGES / "cheatsheet" / k
        copy_page(src, f"cheatsheet/{k}", nav_html(2, [], here=name, pdf=pdf_of(src)))

    (PUBLIC / "index.html").write_text(home_page(days, started, today), encoding="utf-8")
    print(f"홈 · 기준일 {today}")


if __name__ == "__main__":
    main()
