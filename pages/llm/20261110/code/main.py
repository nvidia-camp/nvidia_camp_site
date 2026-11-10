# main.py — 지식 관리 API
# 실행: python -m uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from storage import read_data, write_data

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/knowledge")
def list_knowledge():
    return read_data()["entries"]


def find_entry(data, knowledge_id):
    for entry in data["entries"]:
        if entry["id"] == knowledge_id:
            return entry
    raise HTTPException(status_code=404, detail="Knowledge not found")


@app.get("/api/knowledge/{knowledge_id}")
def get_knowledge(knowledge_id: int):
    return find_entry(read_data(), knowledge_id)


class Knowledge(BaseModel):
    title: str = Field(min_length=1, max_length=80)
    content: str = Field(min_length=1, max_length=2000)
    category: str = Field(min_length=1, max_length=30)


@app.post("/api/knowledge", status_code=201)
def create_knowledge(knowledge: Knowledge):
    data = read_data()
    entry = {"id": data["next_id"], **knowledge.model_dump()}
    data["entries"].append(entry)
    data["next_id"] += 1
    write_data(data)
    return entry


@app.put("/api/knowledge/{knowledge_id}")
def update_knowledge(knowledge_id: int, knowledge: Knowledge):
    data = read_data()
    entry = find_entry(data, knowledge_id)
    entry.update(knowledge.model_dump())
    write_data(data)
    return entry


@app.delete("/api/knowledge/{knowledge_id}", status_code=204)
def delete_knowledge(knowledge_id: int):
    data = read_data()
    data["entries"].remove(find_entry(data, knowledge_id))
    write_data(data)
