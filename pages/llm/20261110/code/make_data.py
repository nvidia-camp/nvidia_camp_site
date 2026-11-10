# make_data.py — 시작 데이터 파일 만들기 (서버를 켜기 전에 한 번만 실행)
import json
from pathlib import Path

# ── [준비] 시작 지식 3건 ──
start = {
    "next_id": 4,
    "entries": [
        {"id": 1, "title": "가상환경",
         "content": "프로젝트별 패키지를 분리한다.", "category": "setup"},
        {"id": 2, "title": "서버 실행",
         "content": "uvicorn으로 개발 서버를 켠다.", "category": "api"},
        {"id": 3, "title": "입력 오류",
         "content": "422이면 입력값을 확인한다.", "category": "api"},
    ],
}

data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(exist_ok=True)
path = data_dir / "knowledge.json"

# 이미 파일이 있으면 기존 지식을 덮어쓰지 않는다
if path.exists():
    print("이미 있음:", path)
else:
    text = json.dumps(start, ensure_ascii=False, indent=2)
    path.write_text(text, encoding="utf-8")
    print("만듦:", path)
