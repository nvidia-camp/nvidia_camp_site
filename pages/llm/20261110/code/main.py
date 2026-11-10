# main.py — 지식 관리 API
# 실행: python -m uvicorn main:app --reload
import json
from pathlib import Path
from threading import Lock

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

# ── [1교시] 앱 만들기와 첫 경로 ──
app = FastAPI(title="Knowledge API")


@app.get("/health")
def health():
    return {"status": "ok"}


# ── [2교시] JSON 파일 읽기·저장 ──
DATA_FILE = Path(__file__).resolve().parent / "data" / "knowledge.json"
LOCK = Lock()


def read_data() -> dict:
    """knowledge.json 전체를 dict로 읽는다."""
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def write_data(data: dict) -> None:
    """임시 파일에 다 쓴 다음 원본과 바꾼다."""
    temp_file = DATA_FILE.with_suffix(".tmp")
    with temp_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    temp_file.replace(DATA_FILE)


def find_index(entries: list[dict], knowledge_id: int) -> int | None:
    """ID가 같은 지식의 목록 위치를 찾는다. 없으면 None."""
    for index, entry in enumerate(entries):
        if entry["id"] == knowledge_id:
            return index
    return None


# ── [2교시] 목록·상세 조회 ──
@app.get("/api/knowledge")
def list_knowledge(category: str | None = None):
    with LOCK:
        data = read_data()
    entries = data["entries"]
    if category is None:
        return entries
    return [entry for entry in entries if entry["category"] == category]


@app.get("/api/knowledge/{knowledge_id}")
def get_knowledge(knowledge_id: int):
    with LOCK:
        data = read_data()
    index = find_index(data["entries"], knowledge_id)
    if index is None:
        raise HTTPException(status_code=404, detail="Knowledge not found")
    return data["entries"][index]


# ── [3교시] 입력 모델과 생성 ──
class KnowledgeWrite(BaseModel):
    title: str = Field(min_length=1, max_length=80)
    content: str = Field(min_length=1, max_length=2000)
    category: str = Field(min_length=1, max_length=30)


class Knowledge(KnowledgeWrite):
    id: int


@app.post(
    "/api/knowledge",
    status_code=201,
    response_model=Knowledge,
)
def create_knowledge(payload: KnowledgeWrite):
    with LOCK:
        data = read_data()
        entry = payload.model_dump()
        entry["id"] = data["next_id"]
        data["entries"].append(entry)
        data["next_id"] += 1
        write_data(data)
    return entry


# ── [4교시] 수정 ──
@app.put("/api/knowledge/{knowledge_id}", response_model=Knowledge)
def update_knowledge(knowledge_id: int, payload: KnowledgeWrite):
    with LOCK:
        data = read_data()
        index = find_index(data["entries"], knowledge_id)
        if index is None:
            raise HTTPException(status_code=404, detail="Knowledge not found")
        updated = payload.model_dump()
        updated["id"] = knowledge_id
        data["entries"][index] = updated
        write_data(data)
    return updated


# ── [5교시] 삭제 ──
@app.delete("/api/knowledge/{knowledge_id}", status_code=204)
def delete_knowledge(knowledge_id: int):
    with LOCK:
        data = read_data()
        index = find_index(data["entries"], knowledge_id)
        if index is None:
            raise HTTPException(status_code=404, detail="Knowledge not found")
        del data["entries"][index]
        write_data(data)
    return Response(status_code=204)
