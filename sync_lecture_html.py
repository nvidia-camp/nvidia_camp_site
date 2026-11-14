# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""nvidia_camp의 강의 HTML(강사 배포본)을 사이트로 옮긴다. nvidia_camp는 읽기만 한다.

사용: uv run sync_lecture_html.py   (site 폴더에서)

- 찾는 곳: nvidia_camp/<과목 폴더>/<YYYYMMDD>/ 바로 아래 *.html
           nvidia_camp/<과목 폴더>/<YYYYMMDD>/Day*_0N/ 바로 아래 *.html (같은 날 N번째 회차)
- 옮기는 곳: pages/<과목>/<YYYYMMDD>/lecture/index.html  (두 번째 회차는 <YYYYMMDD>-2)
- 강사님 확인(2026-11-14): 강의 HTML은 웹사이트에 그대로 게시해도 된다.
- nvidia_camp에서는 이 HTML을 .gitignore로 제외하고, 게시본·버전 기록은 이 저장소가 맡는다.
- 한 폴더에 HTML이 여러 개면 옮기지 않고 알린다(어느 것이 강의 자료인지 사람이 정한다).
"""
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAMP = HERE.parent
PAGES = HERE / "pages"
# nvidia_camp 과목 폴더 → 사이트 경로
FOLDERS = {
    "01_python": "python", "02_ML": "ml", "03_DL": "dl", "04_vision": "vision",
    "05_LLM_RAG": "llm", "06_LLM_RAG_project": "llm-project",
    "07_agent": "agent", "08_agent_project": "agent-project",
}


def lecture_dirs():
    """(사이트 과목, 사이트 날짜 폴더, 강의 HTML이 있는 원본 폴더)"""
    for folder, key in FOLDERS.items():
        root = CAMP / folder
        if not root.is_dir():
            continue
        for day in sorted(p for p in root.iterdir() if p.is_dir() and re.fullmatch(r"2026\d{4}", p.name)):
            yield key, day.name, day
            for session in sorted(p for p in day.iterdir() if p.is_dir() and re.fullmatch(r"Day\d+_0(\d)", p.name)):
                n = int(session.name.rsplit("_0", 1)[1])
                yield key, day.name if n == 1 else f"{day.name}-{n}", session


copied, same, skipped = [], 0, []
for key, ymd, src_dir in lecture_dirs():
    htmls = sorted(src_dir.glob("*.html"))
    if not htmls:
        continue
    if len(htmls) > 1:
        skipped.append(f"{src_dir.relative_to(CAMP)}: HTML {len(htmls)}개 ({', '.join(h.name for h in htmls)})")
        continue
    dest = PAGES / key / ymd / "lecture" / "index.html"
    if dest.exists() and dest.read_bytes() == htmls[0].read_bytes():
        same += 1
        continue
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(htmls[0], dest)
    copied.append(f"{htmls[0].relative_to(CAMP)} → {dest.relative_to(HERE)}")

print(f"강의 HTML: 새로/바뀜 {len(copied)}개 · 그대로 {same}개")
for line in copied:
    print("  " + line)
for line in skipped:
    print("  건너뜀 · " + line)
