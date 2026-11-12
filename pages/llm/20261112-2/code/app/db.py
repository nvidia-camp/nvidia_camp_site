from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

# Engine: 앱에 하나. DB 연결을 만들고 재사용한다
engine = create_engine(settings.database_url, pool_pre_ping=True)
# SessionLocal(): 부를 때마다 새 Session을 만든다
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db():
    # 요청이 들어오면 Session을 열고, 함수에 넘기고, 응답이 나가면 닫는다
    with SessionLocal() as db:
        yield db


@contextmanager
def transaction(db):
    try:
        yield
        # with 안이 모두 성공하면 한 번에 확정
        db.commit()
    except Exception:
        # 하나라도 실패하면 전부 취소하고 오류를 그대로 올린다
        db.rollback()
        raise
