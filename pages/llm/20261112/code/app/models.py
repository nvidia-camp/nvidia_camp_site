from sqlalchemy import BigInteger, ForeignKey, Identity, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# public.categories 테이블 = Category 클래스
class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)


# public.knowledge 테이블 = Knowledge 클래스
class Knowledge(Base):
    __tablename__ = "knowledge"
    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    content: Mapped[str] = mapped_column(Text)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    # category_id로 이어진 Category 객체. item.category.name으로 분류명을 읽는다
    category: Mapped[Category] = relationship()
