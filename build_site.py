# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""pages/의 요약 HTML을 모아 배포용 사이트(public/)를 만든다.

사용: uv run build_site.py   (site 폴더에서)

- 원본은 pages/ 아래에 둔다. 폴더 이름만 맞추면 자동으로 사이트에 들어간다.
    pages/<과목>/<YYYYMMDD>/index.html 매일 요약     → /<과목>/<YYYYMMDD>/
    pages/<과목>/all/index.html     과목 4일 종합    → /<과목>/  (없으면 날짜 목록 페이지)
    pages/overview/index.html       전체 과목 연결   → /overview/
    pages/cheatsheet/<이름>/index.html 치트시트      → /cheatsheet/<이름>/ (CHEATSHEETS에 이름·설명 등록)
- pages/의 원본은 고치지 않는다. 복사본에만 위쪽 메뉴를 넣고, 사이트에 없는 파일을 가리키는
  상대 링크(실습 코드 등)는 글자만 남긴다.
- public/은 매번 지우고 새로 만든다. 직접 고치지 않는다.
- 페이지 폴더에 요약 PDF가 있으면 public/에 함께 복사하고 위쪽 메뉴에 PDF 링크를 단다.
- 강의 교재 PDF는 넣지 않는다 (nvidia_camp에만 둔다).
"""
import html
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGES = HERE / "pages"
PUBLIC = HERE / "public"
SITE_NAME = "AI 코어 엔지니어 학습 노트"

# 과목: 사이트 경로, 이름, 기간, 날짜별 (DayNN, 날짜, 주제)
SUBJECTS = [
    {
        "key": "ml", "name": "머신러닝 모델링 및 성능평가", "short": "ML",
        "period": "2026.10.23 ~ 10.28",
        "days": [
            (5, "20261023", "문제 정의·전처리 Pipeline"),
            (6, "20261026", "선형 모델·KNN (회귀·분류)"),
            (7, "20261027", "트리·앙상블·교차검증"),
            (8, "20261028", "평가지표·최종 평가"),
        ],
    },
    {
        "key": "dl", "name": "딥러닝 핵심 아키텍처 및 학습", "short": "DL",
        "period": "2026.10.29 ~ 11.03",
        "days": [
            (9, "20261029", "Tensor·ANN 학습 루프"),
            (10, "20261030", "학습 안정화 (Optimizer·과적합 제어)"),
            (11, "20261102", "CNN 이미지 분류·전이학습"),
            (12, "20261103", "RNN·LSTM·Transformer"),
        ],
    },
    {
        "key": "vision", "name": "Vision·멀티모달 AI 응용", "short": "Vision",
        "period": "2026.11.04 ~ 11.09",
        "days": [
            (13, "20261104", "OpenCV 이미지 전처리"),
            (14, "20261105", "전이학습 기반 이미지 분류"),
            (15, "20261106", "객체 탐지·추적 (YOLO)"),
            (16, "20261109", "OCR·VLM 문서 AI"),
        ],
    },
]

# 매일 요약·과목 요약·전체 연결 요약은 pages/ 폴더를 보고 자동으로 찾는다.
def day_src(key, date):
    d = PAGES / key / date
    return d if (d / "index.html").exists() else None


def summary_src(key):
    d = PAGES / key / "all"
    return d if (d / "index.html").exists() else None


OVERVIEW = PAGES / "overview" if (PAGES / "overview" / "index.html").exists() else None

# 치트시트: pages/cheatsheet/<이름> → (보이는 이름, 설명)
CHEATSHEETS = {
    "sklearn": ("scikit-learn", "머신러닝 7단계 핵심 치트시트"),
    "pytorch": ("PyTorch", "전체 흐름과 파라미터"),
    "opencv": ("OpenCV", "이미지 한 장에서 영상 처리까지"),
}

# ── 위쪽 메뉴 ───────────────────────────────────────────────────────────
NAV_CSS = """<style>
.cn-nav{box-sizing:border-box;display:flex;flex-wrap:wrap;align-items:center;gap:.25rem .75rem;
  padding:.5rem 1rem;background:#142849;color:#fff;
  font:500 .875rem/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI","Malgun Gothic",sans-serif}
.cn-nav a{color:#fff;text-decoration:none;padding:.125rem .25rem;border-radius:.375rem}
.cn-nav a:hover,.cn-nav a:focus-visible{background:rgba(255,255,255,.16);outline:none}
.cn-nav .cn-home{font-weight:700}
.cn-nav .cn-sep{opacity:.5}
.cn-nav .cn-step{margin-left:auto;display:flex;gap:.5rem}
.cn-nav .cn-off{opacity:.4;padding:.125rem .25rem}
@media print{.cn-nav{display:none}}
</style>"""


def nav_html(depth, crumbs, prev=None, next_=None, pdf=None):
    """depth: 사이트 루트에서 몇 단계 아래인지. crumbs: [(이름, 루트 기준 경로)]"""
    up = "../" * depth
    parts = [f'<a class="cn-home" href="{up or "./"}">{SITE_NAME}</a>']
    for name, path in crumbs:
        parts.append('<span class="cn-sep">/</span>')
        parts.append(f'<a href="{up}{path}">{html.escape(name)}</a>')
    if pdf:
        parts.append('<span class="cn-sep">·</span>')
        parts.append(f'<a href="{html.escape(pdf)}">PDF</a>')
    step = []
    for label, item in (("‹ 이전 날", prev), ("다음 날 ›", next_)):
        if item:
            step.append(f'<a href="{up}{item[1]}">{label} · {html.escape(item[0])}</a>')
        else:
            step.append(f'<span class="cn-off">{label}</span>')
    if prev is not None or next_ is not None:
        parts.append(f'<span class="cn-step">{"".join(step)}</span>')
    return f'{NAV_CSS}<nav class="cn-nav" aria-label="사이트 메뉴">{"".join(parts)}</nav>'


LOCAL_LINK = re.compile(
    r'<a\s[^>]*href="(?!https?:|#|mailto:|data:)[^"]*"[^>]*>(.*?)</a>', re.S)


def pdf_of(src_dir):
    """페이지 폴더의 요약 PDF 이름 (없으면 None)"""
    pdfs = sorted(p.name for p in src_dir.glob("*.pdf"))
    return pdfs[0] if pdfs else None


def copy_page(src_dir, dest, nav):
    src = src_dir / "index.html"
    text = src.read_text(encoding="utf-8")
    text, n_links = LOCAL_LINK.subn(r"<span>\1</span>", text)
    text, n_body = re.subn(r"(<body[^>]*>)", lambda m: m.group(1) + nav, text, count=1)
    assert n_body == 1, f"<body> 없음: {src}"
    out = PUBLIC / dest / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    pdf = pdf_of(src_dir)
    if pdf:
        shutil.copy2(src_dir / pdf, out.parent / pdf)
    note = f" (사이트에 없는 링크 {n_links}개를 글자로 바꿈)" if n_links else ""
    print(f"  /{dest}/ ← {src_dir.relative_to(HERE)}{note}")


# ── 목록 페이지 (홈, 과목) ──────────────────────────────────────────────
PAGE_CSS = """
:root{--color-primary:#142849;--color-heading:#1C2B40;--color-text:#222F44;--color-muted:#52667E;
  --color-canvas:#F9FBFE;--color-surface:#FFFFFF;--color-soft:#F0F6FD;--color-border:#D8E4F2;
  --color-accent:#4B74A6;--radius-card:1rem;--radius-badge:9999px}
*{box-sizing:border-box}
body{margin:0;background:var(--color-canvas);color:var(--color-text);
  font:400 1rem/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI","Malgun Gothic",sans-serif;
  word-break:keep-all;overflow-wrap:break-word}
main{max-width:64rem;margin:0 auto;padding:2rem 1rem 4rem}
h1,h2,h3{color:var(--color-heading);margin:0;line-height:1.35}
h1{font-size:clamp(1.625rem,3vw,2.125rem);letter-spacing:-.02em}
h2{font-size:1.25rem;margin:2.5rem 0 1rem}
h3{font-size:1.0625rem}
.lede{color:var(--color-muted);margin:.5rem 0 0}
.grid{display:grid;gap:1rem;grid-template-columns:repeat(auto-fill,minmax(18rem,1fr))}
.card{background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-card);
  padding:1.25rem}
.card .meta{color:var(--color-muted);font-size:.875rem;margin:.25rem 0 .75rem}
a{color:var(--color-accent)}
.main-link{display:inline-block;font-weight:700;text-decoration:none;color:var(--color-primary);
  background:var(--color-soft);border-radius:var(--radius-badge);padding:.25rem .875rem;margin-bottom:.75rem}
.main-link:hover,.main-link:focus-visible{background:var(--color-border)}
ul.days{list-style:none;margin:0;padding:0;display:grid;gap:.375rem}
ul.days li{display:grid;grid-template-columns:3.5rem 1fr auto;gap:.5rem;align-items:baseline}
.day{font-weight:700;color:var(--color-heading);font-size:.875rem}
.todo{color:var(--color-muted)}
.badge{font-size:.75rem;border:1px solid var(--color-border);border-radius:var(--radius-badge);
  padding:0 .5rem;margin-left:.25rem;color:var(--color-muted);white-space:nowrap}
.empty{background:var(--color-soft);border:1px dashed var(--color-border)}
"""


def list_page(title, body, nav):
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


def day_items(subject, up):
    rows = []
    for num, date, topic in subject["days"]:
        label = f"Day{num}"
        shown = f"{date[4:6]}/{date[6:]}"
        if day_src(subject["key"], date):
            href = f'{up}{subject["key"]}/{date}/'
            rows.append(f'<li><span class="day">{label}</span>'
                        f'<a href="{href}">{html.escape(topic)}</a>'
                        f'<span class="badge">{shown}</span></li>')
        else:
            rows.append(f'<li class="todo"><span class="day">{label}</span>'
                        f'<span>{html.escape(topic)}</span><span class="badge">준비 중</span></li>')
    return '<ul class="days">' + "".join(rows) + "</ul>"


def subject_card(subject, up):
    key = subject["key"]
    if summary_src(key):
        top = f'<a class="main-link" href="{up}{key}/">4일 종합 요약 →</a>'
    else:
        top = f'<a class="main-link" href="{up}{key}/">날짜별 목록 →</a>'
    return (f'<section class="card"><h3>{html.escape(subject["name"])}</h3>'
            f'<p class="meta">{subject["period"]}</p>{top}{day_items(subject, up)}</section>')


def home_page():
    if OVERVIEW:
        overview = ('<section class="card"><h3>전체 과목 연결 요약</h3>'
                    '<p class="meta">과목 사이에 무엇이 이어지는지 한 장으로 봅니다.</p>'
                    '<a class="main-link" href="overview/">전체 연결 요약 →</a></section>')
    else:
        overview = ('<section class="card empty"><h3>전체 과목 연결 요약 <small class="badge">준비 중</small></h3>'
                    '<p class="meta">과목 사이에 무엇이 이어지는지 한 장으로 정리할 예정입니다.</p></section>')
    subjects = "".join(subject_card(s, "") for s in SUBJECTS)
    sheets = "".join(
        f'<section class="card"><h3>{html.escape(name)}</h3><p class="meta">{html.escape(desc)}</p>'
        f'<a class="main-link" href="cheatsheet/{key}/">치트시트 →</a></section>'
        for key, (name, desc) in CHEATSHEETS.items())
    body = f"""<header>
<h1>{SITE_NAME}</h1>
<p class="lede">과목별 4일 종합 요약과 매일 요약, 라이브러리 치트시트를 모았습니다.</p>
</header>
<h2>전체 과목</h2>
{overview}
<h2>과목별 요약</h2>
<div class="grid">{subjects}</div>
<h2 id="cheatsheet">라이브러리 치트시트</h2>
<div class="grid">{sheets}</div>"""
    return list_page(SITE_NAME, body, nav_html(0, []))


def subject_list_page(subject):
    body = f"""<header>
<h1>{html.escape(subject["name"])}</h1>
<p class="lede">{subject["period"]} · 4일 종합 요약은 준비 중입니다. 날짜별 요약을 먼저 볼 수 있습니다.</p>
</header>
<h2>날짜별 요약</h2>
<section class="card">{day_items(subject, "../")}</section>"""
    nav = nav_html(1, [(subject["short"], f'{subject["key"]}/')])
    return list_page(f'{subject["short"]} · {subject["name"]}', body, nav)


# ── 만들기 ──────────────────────────────────────────────────────────────
def main():
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()

    # 날짜 순서 (이전·다음 날 메뉴용)
    order = []
    for s in SUBJECTS:
        for num, date, _ in s["days"]:
            if day_src(s["key"], date):
                order.append((num, s, f'{s["key"]}/{date}/', day_src(s["key"], date)))

    print("매일 요약")
    for i, (num, s, path, src) in enumerate(order):
        prev = (f"Day{order[i-1][0]}", order[i-1][2]) if i > 0 else None
        nxt = (f"Day{order[i+1][0]}", order[i+1][2]) if i + 1 < len(order) else None
        nav = nav_html(2, [(s["short"], f'{s["key"]}/'), (f"Day{num}", path)], prev, nxt, pdf_of(src))
        copy_page(src, path.rstrip("/"), nav)

    print("과목별 요약")
    for s in SUBJECTS:
        key = s["key"]
        if summary_src(key):
            src = summary_src(key)
            copy_page(src, key, nav_html(1, [(s["short"], f"{key}/")], pdf=pdf_of(src)))
        else:
            out = PUBLIC / key / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(subject_list_page(s), encoding="utf-8")
            print(f"  /{key}/ ← 날짜 목록 (pages/{key}/all/index.html 없음)")

    print("전체 연결 요약")
    if OVERVIEW:
        copy_page(OVERVIEW, "overview", nav_html(1, [("전체 연결", "overview/")]))
    else:
        print("  없음 (홈에 준비 중으로 표시)")

    print("치트시트")
    for key, (name, _) in CHEATSHEETS.items():
        src = PAGES / "cheatsheet" / key
        nav = nav_html(2, [("치트시트", "#cheatsheet"), (name, f"cheatsheet/{key}/")], pdf=pdf_of(src))
        copy_page(src, f"cheatsheet/{key}", nav)

    (PUBLIC / "index.html").write_text(home_page(), encoding="utf-8")
    print("홈 ← 목록 페이지")


if __name__ == "__main__":
    main()
