"""목록 페이지: 홈, 과목 페이지, 요약 전 강의 목차 페이지."""
import html

from .config import COMMON_GROUPS, DAY_SUBPAGES, HERE, ICON_ARROW, ICON_VIEW, PAGES, PRACTICE, RELEASE, SITE_NAME, SUBJECTS, TODAY, refs_of, setup_items, web
from .tree import day_top, read_tree
from .data import PLANNED_TITLES, day_title, has_page, image_data, md, page_h1
from .nav import ANALYTICS, DOWNLOAD_MARK, THEME_BTN, THEME_HEAD, THEME_MARK, nav_html


# ── 목록 페이지 (홈, 과목) ───────────────────────────────────────────────
# 이 저장소에서 그린 아이콘: 두 테마 모두에서 보이는 색이라 다크 모드 흰 받침을 깔지 않는다
OWN_ICONS = {"code.svg", "terminal.svg", "path.svg"}
# 어두운 배경에서 안 보이는 로고 → 공식 다크 버전 (출처는 assets/logos/README.md)
DARK_LOGOS = {"ollama.png": "ollama-dark.png"}


PAGE_CSS = "\n" + web("list.css")



def day_range(ds):
    """과목의 Day 범위. 같은 날 두 번째 회차 표시(-2)는 뺀다: Day9–11"""
    return f'Day{ds[0]["n"].split("-")[0]}–{ds[-1]["n"].split("-")[0]}'
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
    """Day 한 줄 오른쪽의 작은 버튼: 강의 자료(사이트의 강의 HTML) · Slack 로고 · 하위 페이지"""
    href = f'{up}{d["key"]}/{d["ymd"]}/'
    out = []
    if d["lecture"]:
        out.append(f'<a class="mini view" href="{href}lecture/">{ICON_VIEW}강의 자료</a>')
    if d["link"]:
        out.append(slack_link(d["link"], "mini slack").replace('title="Slack"', 'data-tip="Slack 강의 자료 게시물 (새 탭)"'))
    for sub, label in DAY_SUBPAGES.get(f'{d["key"]}/{d["ymd"]}', []):
        out.append(f'<a class="mini" href="{href}{sub}/">{ICON_ARROW}{html.escape(label)}</a>')
    if d["colab"]:
        out.append(colab_link(d["colab"], "mini colab").replace('title="Colab 실습 폴더 (Google Drive)"', 'data-tip="Colab 실습 폴더 · Google Drive (새 탭)"'))
    return "".join(out)


def slack_link(url, cls, text=""):
    """Slack 게시물 링크: Slack 로고 (+ 글자). 화살표 대신 로고로 도착지를 보인다."""
    img = f'<img src="{image_data(HERE / "assets" / "logos" / "slack.svg")}" alt="" width="16" height="16">'
    label = f'<span>{html.escape(text)}</span>' if text else ""
    return (f'<a class="{cls}" href="{html.escape(url)}" target="_blank" rel="noopener" '
            f'title="Slack" aria-label="Slack (새 탭)">{img}{label}</a>')


def colab_link(url, cls, text=""):
    """Colab 실습 폴더(Google Drive) 링크: 공식 Colab 로고 (+ 글자)"""
    img = f'<img src="{image_data(HERE / "assets" / "logos" / "colab.png")}" alt="" width="27" height="16">'
    label = f'<span>{html.escape(text)}</span>' if text else ""
    return (f'<a class="{cls}" href="{html.escape(url)}" target="_blank" rel="noopener" '
            f'title="Colab 실습 폴더 (Google Drive)" aria-label="Colab 실습 폴더 (Google Drive, 새 탭)">{img}{label}</a>')


def logo_span(logo):
    """참고 칩 로고. 다크 모드에서도 받침 없이 투명. 검은 로고는 공식 다크 버전(DARK_LOGOS)으로 바꿔 보인다."""
    own = " own" if logo in OWN_ICONS else ""
    img = lambda name, cls="": (f'<img{cls} src="{image_data(HERE / "assets" / "logos" / name)}" alt="" width="32" height="22">')
    dark = DARK_LOGOS.get(logo)
    imgs = img(logo, ' class="lg-l"') + img(dark, ' class="lg-d"') if dark else img(logo)
    return f'<span class="ref-logo{own}">{imgs}</span>'


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
    today = TODAY
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
            groups[-1][1].append(f'<a class="cell {state}" href="{d["key"]}/{d["ymd"]}/" data-tip="{tip}" aria-label="{tip}"></a>')
        elif d["lecture"]:
            tip = html.escape(f'Day{d["n"]} · {md(d["date"])} · 강의 자료')
            groups[-1][1].append(f'<a class="cell {state}" href="{d["key"]}/{d["ymd"]}/lecture/" data-tip="{tip}" aria-label="{tip}"></a>')
        elif d["link"]:
            tip = html.escape(f'Day{d["n"]} · {md(d["date"])} · 강의 자료')
            groups[-1][1].append(f'<a class="cell {state}" href="{html.escape(d["link"])}" target="_blank" rel="noopener" '
                                 f'data-tip="{tip}" aria-label="{tip}"></a>')
        else:
            groups[-1][1].append(f'<span class="cell {state}" title="{tip}"></span>')
    return "".join(f'<div class="tl"><span class="tl-name">{name}</span><span class="tl-cells">{"".join(c)}</span></div>'
                   for name, c in groups)


def tree_day_page(d):
    """요약이 아직 없는 날: 머리 + 자료 줄 + 강의 목차(강사님 자료 기준) + 요약 준비 중 표시"""
    book, _ = read_tree(d["tree"])
    title = PLANNED_TITLES.get(f'{d["key"]}/{d["ymd"]}') or book or f'Day{d["n"]}'
    sub = f'<p class="sub">교재 · {html.escape(book)}</p>' if book and book != title else ""
    body = f"""<header class="day-head"><p class="eyebrow">Day{d["n"]} · {md(d["date"])} · {html.escape(d["short"])}</p>
<h1>{html.escape(title)}</h1>{sub}</header>
<div class="lt-top">{day_top(d)}</div>
<p class="sum-empty">요약 준비 중입니다.</p>"""
    nav = nav_html(2, [(d["short"], f'{d["key"]}/')], here=f'Day{d["n"]}', lecture=d["link"], colab=d["colab"],
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
                       f'<img src="{image_data(HERE / "assets" / "logos" / logo)}" alt="" width="20" height="20">{name}</a>'
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
