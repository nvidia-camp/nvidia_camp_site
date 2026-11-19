# /// script
# requires-python = ">=3.12"   # sitebuild/tree.py가 f-string 안에 역슬래시를 쓴다 (3.12부터)
# dependencies = []
# ///
"""pages/의 요약을 모아 배포용 사이트(public/)를 만든다.

사용: uv run build_site.py   (site 폴더에서. make build와 같다)

코드 위치 (import는 위에서 아래 한 방향):
    site.toml             설정: 과목·치트시트·가이드·공개 여부·Colab 링크 (매일 고치는 값은 여기)
    web/                  페이지에 끼우는 CSS·JS·아이콘 (nav·list·tree·theme .css, theme·analytics .js, icons/)
    sitebuild/config.py   경로·site.toml·web/ 읽기, --release·--as-of
    sitebuild/tree.py     강의 트리(tree.md)와 '강의 목차 한눈에 보기' 블록
    sitebuild/data.py     lectures.json·pages/에서 Day 목록과 제목
    sitebuild/fonts.py    글꼴 통일 (Pretendard)
    sitebuild/nav.py      위쪽 메뉴·라이트/다크 전환·방문 통계
    sitebuild/content.py  요약·가이드·강의 HTML을 public/으로 복사
    sitebuild/listing.py  홈·과목 페이지·요약 전 강의 목차 페이지
    build_site.py         main(): 위 모듈로 public/을 만든다

- 원본은 pages/ 아래에 둔다. 폴더 이름만 맞추면 자동으로 사이트에 들어간다.
    pages/<과목>/<YYYYMMDD>/   매일 요약     → /<과목>/<YYYYMMDD>/  (같은 날 두 번째 회차는 <YYYYMMDD>-2)
    pages/<과목>/all/          과목 4일 종합 → /<과목>/  (없으면 날짜 카드 목록)
    pages/cheatsheet/<이름>/   치트시트      → /cheatsheet/<이름>/ (site.toml [cheatsheets])
    pages/setup/<이름>/        설치 가이드   → /setup/<이름>/      (site.toml [setup])
    pages/setup/<이름>/<하위>/ 가이드 안 페이지 → /setup/<이름>/<하위>/ (site.toml [setup_pages])
    pages/<과목>/<YYYYMMDD>/tree.md  강의 트리(교재 구성) → 요약이 아직 없으면 그날 페이지가 '강의 목차 한눈에 보기'가 된다.
        원본은 작업 폴더의 Day<N>_강의트리.md(또는 Day<N>_강의구조_핵심설명.md)를 복사한 것. 첫 ```text 블록만 읽는다.
- Colab 실습 폴더(Google Drive)는 site.toml [colab]에 주소를 등록하면 홈 Day 줄·그날 페이지에 Colab 로고로 나온다.
- 홈: 맨 위 제목·최근 수업·지금 과목 표지 → 100일 일정 → 참고 문서 모음 → 과목별 챕터(Day 목록).
  참고 문서 모음은 공통 묶음(site.toml common_groups)별 설치 가이드 칸 + '과목 참고 문서' 칸(치트시트·과목 설치 가이드).
- 본문 글꼴은 Pretendard만: copy_page가 unify_fonts()로 모든 페이지의 비-코드 글꼴 선언 앞에 붙이고, 못 고치면 빌드 끝에 ⚠ 경고만 한다(코드 monospace는 예외, inherit는 그대로). 강의 원본 lecture는 Pretendard를 96%로 줄인 PretendardLecture를 쓴다.
- 홈·과목 목록은 Pretendard(OFL, assets/fonts → public/fonts)를 쓴다. 요약 페이지도 같은 Pretendard를 쓴다(--font-body 앞에 두고 /fonts 링크, 2026-11-17).
- 각 폴더의 index.html을 public/에 복사하고, 사이트 메뉴·통계를 뺀 원본을 download.html로 함께 둔다(메뉴의 "HTML 받기"). PDF는 만들지 않는다(2026-11-14 폐지).
- 강사님 강의 HTML(sync_lecture_html.py가 pages/<과목>/<날짜>/lecture/에 옮김)은 원본 그대로 /<과목>/<날짜>/lecture/download.html에 두고, 화면(view.html)은 글꼴만 바꾼다. view.html을
  메뉴 아래 전체 화면으로 띄운다. 홈 Day 줄·Day 페이지 메뉴의 '강의 자료'로 열고, Slack 게시물은 로고만 둔다
  (사이트에 강의 HTML이 없는 날은 Slack 링크가 '강의 자료').
- 복사본에만 위쪽 메뉴를 넣고, 사이트에 없는 파일을 가리키는 상대 링크는 글자만 남긴다.
- Day 번호·날짜·과목·강의 자료 링크는 lectures.json(sync_lectures.py가 학습 자료 시트에서 만듦)에서 읽는다.
- public/은 매번 지우고 새로 만든다. 직접 고치지 않는다. 강의 교재 PDF는 넣지 않는다.
- 공개 전(site.toml [setup]의 public = false) 페이지는 main 빌드에는 들어가고 `--release`로 만들면 빠진다.
  화면에 따로 표시하지 않는다(공개 구분은 main/deploy 브랜치로 한다).
- 사이트의 '오늘'은 18:20부터 다음 수업일이다. `--release`는 그날까지의 수업 자료만 넣는다
  (전날 18:20 공개, auto_release.sh). 특정 날짜 기준으로 만들려면 `--as-of YYYY-MM-DD`.
"""
import shutil
from sitebuild.config import CHEATSHEETS, DAY_PAGES, DAY_SUBPAGES, HERE, LECTURES, PAGES, PUBLIC, RELEASE, SETUP, SETUP_PAGES, SUBJECTS, TODAY, setup_items
from sitebuild.tree import day_top
from sitebuild.data import read_days
from sitebuild.fonts import FONT_WARNINGS, write_lecture_font_css
from sitebuild.nav import add_totop, nav_html
from sitebuild.content import copy_lecture, copy_page
from sitebuild.listing import home_page, subject_page, tree_day_page

# auto_release.sh가 이 파일을 import해서 LECTURES·SETUP·read_days를 쓴다 (이름을 바꾸지 말 것)
__all__ = ["LECTURES", "SETUP", "read_days", "main"]

# ── 만들기 ──────────────────────────────────────────────────────────────
def main():
    days = read_days()
    today = TODAY
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()
    shutil.copytree(HERE / "assets" / "fonts", PUBLIC / "fonts")   # 홈·과목 목록의 Pretendard(OFL)
    write_lecture_font_css()

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
        tabs = DAY_PAGES.get(f'{d["key"]}/{d["ymd"]}')
        if not tabs:
            nav = nav_html(2, [(d["short"], f'{d["key"]}/')], here=f'Day{d["n"]}',
                           prev=prev, next_=nxt, lecture=d["link"], colab=d["colab"], view="lecture/" if d["lecture"] else None)
            copy_page(d["src"], f'{d["key"]}/{d["ymd"]}', nav, top=day_top(d) if d["tree"] else "", totop=True)
        else:
            paths = [f'{d["key"]}/{d["ymd"]}/' + (f"{sub}/" if sub else "") for sub, _ in tabs]
            for j, (sub, label) in enumerate(tabs):
                t_prev = (tabs[j - 1][1], paths[j - 1]) if j else prev
                t_next = (tabs[j + 1][1], paths[j + 1]) if j + 1 < len(tabs) else nxt
                view = ("../lecture/" if sub else "lecture/") if d["lecture"] else None
                # 탭을 오가도 위쪽 메뉴 모양이 같도록 모든 탭이 '과목 › DayNN › 탭 이름'을 쓴다
                nav = nav_html(3 if sub else 2, [(d["short"], f'{d["key"]}/'), (f'Day{d["n"]}', paths[0])],
                               here=label, prev=t_prev, next_=t_next, lecture=d["link"], colab=d["colab"], view=view)
                copy_page(d["src"] / sub if sub else d["src"], paths[j].rstrip("/"), nav,
                          top=day_top(d) if not sub and d["tree"] else "", totop=True)
        for sub, label in DAY_SUBPAGES.get(f'{d["key"]}/{d["ymd"]}', []):
            copy_page(d["src"] / sub, f'{d["key"]}/{d["ymd"]}/{sub}',
                      nav_html(3, [(d["short"], f'{d["key"]}/'), (f'Day{d["n"]}', f'{d["key"]}/{d["ymd"]}/')], here=label), totop=True)

    print("강의 목차 (요약 전)")
    for d in days:
        if d["tree"] and not d["src"]:
            out = PUBLIC / d["key"] / d["ymd"]
            out.mkdir(parents=True, exist_ok=True)
            page = tree_day_page(d)
            (out / "index.html").write_text(add_totop(page, "prefers-color-scheme" in page), encoding="utf-8")
            print(f'  /{d["key"]}/{d["ymd"]}/ ← {d["tree"].relative_to(HERE)} (강의 목차 한눈에 보기)')

    print("강의 자료 (사이트 안 강의 HTML)")
    for d in days:
        if not d["lecture"]:
            continue
        crumbs = [(d["short"], f'{d["key"]}/')]
        if d["src"] or d["tree"]:
            crumbs.append((f'Day{d["n"]}', f'{d["key"]}/{d["ymd"]}/'))
        here = "강의 자료" if d["src"] or d["tree"] else f'Day{d["n"]} 강의 자료'
        copy_lecture(d["lecture"], f'{d["key"]}/{d["ymd"]}/lecture', nav_html(3, crumbs, here=here, lecture=d["link"], on_lecture=True, colab=d["colab"]))

    print("과목")
    for key, ds in subjects:
        src = PAGES / key / "all"
        if (src / "index.html").exists():
            copy_page(src, key, nav_html(1, [], here=f'{ds[0]["short"]} 4일 종합'), totop=True)
        else:
            (PUBLIC / key).mkdir(parents=True, exist_ok=True)
            (PUBLIC / key / "index.html").write_text(subject_page(key, ds), encoding="utf-8")
            print(f"  /{key}/ ← 날짜 카드 목록")

    print("치트시트")
    for k, (name, *_) in CHEATSHEETS.items():
        src = PAGES / "cheatsheet" / k
        copy_page(src, f"cheatsheet/{k}", nav_html(2, [], here=name), totop=True)

    print("설치 가이드" + (" (--release: 공개 전 페이지 제외)" if RELEASE else ""))
    for k, name, *_ in setup_items():
        subs = SETUP_PAGES.get(k)
        if not subs:
            copy_page(PAGES / "setup" / k, f"setup/{k}", nav_html(2, [], here=name), totop=True)
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
                      paths[i].rstrip("/"), nav, totop=True)

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

