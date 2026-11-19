"""자료 읽기: lectures.json과 pages/에서 Day 목록·제목을 만든다."""
import base64
import html
import json
import re

from .config import COLAB, LECTURES, PAGES, RELEASE, SUBJECTS, TODAY
from .tree import read_tree


# ── 자료 읽기 ────────────────────────────────────────────────────────────
def read_days():
    days = []
    for row in json.loads(LECTURES.read_text(encoding="utf-8")):
        key, short = SUBJECTS.get(row["subject"], (None, row["subject"]))
        ymd = row["date"].replace("-", "")
        part = row["day"].split("-")[1] if "-" in row["day"] else "1"
        folder = ymd if part == "1" else f"{ymd}-{part}"      # 같은 날 두 번째 회차: 20261102-2
        src = PAGES / key / folder if key else None
        if RELEASE and row["date"] > TODAY:
            src = None   # deploy용: 내일 이후 수업 자료(강의 HTML·목차)는 그날 배포할 때까지 뺀다 (main에는 미리 둘 수 있다)
        days.append({
            "n": row["day"], "date": row["date"], "ymd": folder, "key": key, "short": short,
            "subject": row["subject"], "link": row["link"],
            "src": src if src and (src / "index.html").exists() else None,
            # 사이트에 올린 강의 HTML (sync_lecture_html.py) → '강의 자료'
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


def image_data(image):
    mime = "image/svg+xml" if image.suffix == ".svg" else "image/png"
    data = base64.b64encode(image.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


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
