"""사이트 설정·경로·web/ 자원. site.toml을 읽고, --release·--as-of 같은 실행 옵션을 정한다."""
import datetime
import json
import sys
import tomllib
from pathlib import Path



HERE = Path(__file__).resolve().parent.parent   # site/ 폴더
PAGES = HERE / "pages"
PUBLIC = HERE / "public"
LECTURES = HERE / "lectures.json"
SITE_NAME = "학습 아카이브"

# ── 설정·웹 자원 읽기 ─────────────────────────────────────────────────────
# 설정(과목·가이드·Colab 등)은 site.toml, 페이지에 끼워 넣는 CSS·JS·아이콘은 web/에 둔다.
WEB = HERE / "web"
CONFIG = tomllib.loads((HERE / "site.toml").read_text(encoding="utf-8"))


def web(name):
    """web/의 파일 내용 그대로"""
    return (WEB / name).read_text(encoding="utf-8")


def web_script(name):
    """web/의 JS 파일을 <script>로 감싼다 (파일 끝 줄바꿈은 뺀다)"""
    return "<script>" + web(name).rstrip("\n") + "</script>"


def icon(name):
    """web/icons/의 SVG 아이콘 (파일 끝 줄바꿈은 뺀다)"""
    return web(f"icons/{name}.svg").rstrip("\n")


ICON_DL = icon("download")      # HTML 받기
ICON_VIEW = icon("view")        # 강의 자료 보기
ICON_ARROW = icon("arrow")      # 카드·링크의 화살표

# 시트의 교과목 → (사이트 경로, 짧은 이름). 경로가 None이면 일정 띠에만 보인다.
SUBJECTS = {s["sheet_name"]: (s["path"] or None, s["short"]) for s in CONFIG["subjects"]}
# 문제 풀이 사이트 (홈 위쪽 링크): (이름, assets/logos의 공식 아이콘, 주소)
PRACTICE = [(p["name"], p["logo"], p["url"]) for p in CONFIG["practice"]]
# 치트시트: 경로 → (보이는 이름, 공식 로고 파일, 용도, 과목). 과목 블록 아래 '참고' 줄에 나온다.
CHEATSHEETS = {k: (v["name"], v["logo"], v["desc"], v["subject"]) for k, v in CONFIG["cheatsheets"].items()}

# 설치 가이드: 경로 → (보이는 이름, 공식 로고 파일, 용도, 과목 또는 공통 묶음, 공개 여부). 공개 전에는 False로 둔다.
SETUP = {k: (v["name"], v["logo"], v["desc"], v["group"], v["public"]) for k, v in CONFIG["setup"].items()}
# 과정 전체에서 쓰는 가이드의 묶음과 순서. 홈 '공통 가이드' 섹션에 묶음마다 한 줄씩 나온다.
COMMON_GROUPS = CONFIG["common_groups"]
# 페이지와 함께 내려받게 둘 파일: 사이트 경로 → [파일 이름]. 페이지에서는 data-site를 붙여 링크한다.
FILES = CONFIG["files"]
# 여러 페이지로 된 가이드: 경로 → [(하위 폴더, 페이지 이름)]. 첫 줄("")이 가이드 첫 페이지다.
SETUP_PAGES = {k: [tuple(x) for x in v] for k, v in CONFIG["setup_pages"].items()}
# Day 페이지 아래에 두는 하위 페이지: "과목/날짜" → [(하위 폴더, 이름)]. 홈 카드와 상단 경로에 붙는다.
DAY_SUBPAGES = {k: [tuple(x) for x in v] for k, v in CONFIG["day_subpages"].items()}
# Colab 실습 폴더: "과목/날짜" → Google Drive 폴더 주소 (공유: 링크가 있는 모든 사용자 · 뷰어). Day 줄·그날 페이지에 Colab 로고로 나온다.
COLAB = CONFIG["colab"]
RELEASE = "--release" in sys.argv   # deploy용: 공개 전 페이지를 뺀다
OPEN_AHEAD = datetime.time(18, 20)   # 이 시각부터 다음 수업일 자료를 공개한다 (auto_release.sh가 이 시각에 배포)


def site_today():
    """사이트의 '오늘': 18:20 전은 오늘, 18:20부터는 다음 수업일 (--as-of YYYY-MM-DD로 지정 가능)"""
    if "--as-of" in sys.argv:
        return datetime.date.fromisoformat(sys.argv[sys.argv.index("--as-of") + 1]).isoformat()
    now = datetime.datetime.now()
    today = now.date().isoformat()
    if now.time() < OPEN_AHEAD:
        return today
    later = sorted(r["date"] for r in json.loads(LECTURES.read_text(encoding="utf-8")) if r["date"] > today)
    return later[0] if later else today


TODAY = site_today()


def setup_items():
    return [(k, name, logo, desc, subj) for k, (name, logo, desc, subj, pub) in SETUP.items() if pub or not RELEASE]


def refs_of(subject):
    """과목에 딸린 참고 문서: [(루트 기준 경로, 이름, 로고 파일, 용도)]"""
    items = [(f"cheatsheet/{k}/", name, logo, desc)
             for k, (name, logo, desc, subj) in CHEATSHEETS.items() if subj == subject]
    items += [(f"setup/{k}/", name, logo, desc) for k, name, logo, desc, subj in setup_items() if subj == subject]
    return items
