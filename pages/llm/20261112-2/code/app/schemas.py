from pydantic import BaseModel, Field


# API로 받는 세 필드 (오전과 같다)
class KnowledgeWrite(BaseModel):
    title: str = Field(min_length=1, max_length=80)
    content: str = Field(min_length=1, max_length=2000)
    category: str = Field(min_length=1, max_length=30)


# API로 돌려주는 네 필드 = 세 필드 + DB가 발급한 id
class KnowledgeRead(KnowledgeWrite):
    id: int
