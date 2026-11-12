from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy import select, text
from sqlalchemy.orm import Session, joinedload

from app.db import get_db, transaction
from app.models import Category, Knowledge
from app.schemas import KnowledgeRead, KnowledgeWrite

app = FastAPI(title="Knowledge API · PostgreSQL")


def to_read(item):
    # DB 쪽 category_id 대신 분류명을 넣어 API 응답 모양으로 바꾼다
    return KnowledgeRead(id=item.id, title=item.title, content=item.content, category=item.category.name)


def load_one(db, knowledge_id):
    stmt = select(Knowledge).options(joinedload(Knowledge.category)).where(Knowledge.id == knowledge_id)
    item = db.scalar(stmt)
    if item is None:
        raise HTTPException(status_code=404, detail="Knowledge not found")
    return item


def get_or_create_category(db, name):
    category = db.scalar(select(Category).where(Category.name == name))
    if category is None:
        category = Category(name=name)
        db.add(category)
        # INSERT를 보내 id만 받아 둔다. 아직 확정 아님
        db.flush()
    return category


@app.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "reachable"}


@app.get("/api/knowledge", response_model=list[KnowledgeRead])
def list_knowledge(category: str | None = None, db: Session = Depends(get_db)):
    stmt = select(Knowledge).options(joinedload(Knowledge.category)).order_by(Knowledge.id)
    if category is not None:
        stmt = stmt.join(Knowledge.category).where(Category.name == category)
    return [to_read(item) for item in db.scalars(stmt).unique()]


@app.get("/api/knowledge/{knowledge_id}", response_model=KnowledgeRead)
def read_knowledge(knowledge_id: int, db: Session = Depends(get_db)):
    return to_read(load_one(db, knowledge_id))


@app.post("/api/knowledge", response_model=KnowledgeRead, status_code=201)
def create_knowledge(payload: KnowledgeWrite, db: Session = Depends(get_db)):
    with transaction(db):
        category = get_or_create_category(db, payload.category)
        item = Knowledge(title=payload.title, content=payload.content, category=category)
        db.add(item)
        # DB가 id를 발급한다
        db.flush()
        result = to_read(item)
    return result


@app.put("/api/knowledge/{knowledge_id}", response_model=KnowledgeRead)
def update_knowledge(knowledge_id: int, payload: KnowledgeWrite, db: Session = Depends(get_db)):
    item = load_one(db, knowledge_id)
    with transaction(db):
        category = get_or_create_category(db, payload.category)
        # 객체의 값을 바꾸면 Session이 UPDATE를 만든다
        item.title = payload.title
        item.content = payload.content
        item.category = category
        db.flush()
        result = to_read(item)
    return result


@app.delete("/api/knowledge/{knowledge_id}", status_code=204)
def delete_knowledge(knowledge_id: int, db: Session = Depends(get_db)):
    item = load_one(db, knowledge_id)
    with transaction(db):
        db.delete(item)
    return Response(status_code=204)
