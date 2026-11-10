# storage.py — 파일 읽기·저장 (실습에서 제공하는 코드)
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "knowledge.json"


def read_data():
    """knowledge.json 전체를 dict로 읽는다."""
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def write_data(data):
    """dict 전체를 knowledge.json에 저장한다."""
    text = json.dumps(data, ensure_ascii=False, indent=2)
    DATA_FILE.write_text(text, encoding="utf-8")
