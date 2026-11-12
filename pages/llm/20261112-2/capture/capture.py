# /// script
# requires-python = ">=3.11"
# dependencies = ["fastapi", "uvicorn", "sqlalchemy>=2.0", "psycopg[binary]", "pydantic-settings", "alembic", "playwright"]
# ///
"""페이지 코드(../code/app)를 실제 PostgreSQL에 연결해 페이지의 모든 결과를 capture.json에 기록한다.

사용: PGHOST=localhost PGPORT=55433 PGUSER=postgres uv run capture.py
- 사용자 서버(5432)에서는 실행하지 않는다. 학습용 임시 서버에서만 DB를 지우고 다시 만든다.
- 페이지 코드는 basic 완성본(PM05)에서 오늘 개념 밖의 장치를 걷어낸 것이다. Migration은 완성본 폴더 그대로 쓴다.
- nvidia_camp의 오전 DB 준비 SQL과 완성본은 읽기만 하고, 임시 폴더에 복사해 실행한다.
- POST B는 실제 /docs 화면에서 보내고 화면을 shots/에 저장한다(시스템 Chrome, 환경 변수 CHROME).
- 순서: 서버 실행 → 다섯 API와 SQL 대조 → 실패 요청 → 재시작 → Session 실험 → Migration.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

import psycopg
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
CAMP = HERE.parents[4]
READY_SQL = CAMP / "05_LLM_RAG/20261112/Day19_01/mentor/01_basic/02_PostgreSQL/B_CRUD/00_ready_database.sql"
APP_SRC = CAMP / "05_LLM_RAG/20261112/Day19_02/mentor/01_basic/05_PM05_일일프로젝트"
DB, MIG_DB = "day19_crud_b", "day19_migration_b"
PAGE_APP = HERE.parent / "code" / "app"
SHOTS = HERE / "shots"
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
PORT = 8765
BASE = f"http://127.0.0.1:{PORT}"
PG = dict(host=os.environ["PGHOST"], port=int(os.environ["PGPORT"]), user=os.environ.get("PGUSER", "postgres"))
assert PG["port"] != 5432, "사용자 서버(5432)에서는 실행하지 않습니다"


def fresh_db(name, sql=None):
    with psycopg.connect(dbname="postgres", autocommit=True, **PG) as conn:
        conn.execute(f"DROP DATABASE IF EXISTS {name} WITH (FORCE)")
        conn.execute(f"CREATE DATABASE {name}")
    if sql:
        with psycopg.connect(dbname=name, autocommit=True, **PG) as conn:
            conn.execute(sql)


def sql(query, db=DB):
    with psycopg.connect(dbname=db, autocommit=True, **PG) as conn:
        cur = conn.execute(query)
        return {"cols": [d.name for d in cur.description], "rows": [list(r) for r in cur.fetchall()]}


def count(table, db=DB):
    return sql(f"SELECT count(*) FROM {table}", db)["rows"][0][0]


ROW_SQL = ("SELECT k.id, k.title, k.content, c.name AS category FROM knowledge AS k "
           "JOIN categories AS c ON c.id = k.category_id WHERE k.id = {id}")
ALL_SQL = ("SELECT k.id, k.title, k.content, c.name AS category FROM knowledge AS k "
           "JOIN categories AS c ON c.id = k.category_id ORDER BY k.id")


def call(method, path, body=None):
    data = json.dumps(body, ensure_ascii=False).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            raw, status = r.read(), r.status
    except urllib.error.HTTPError as e:
        raw, status = e.read(), e.code
    return {"request": f"{method} {path}", "body": body, "status": status, "size": len(raw),
            "response": json.loads(raw) if raw else None}


def start_server(work):
    proc = subprocess.Popen([sys.executable, "-m", "uvicorn", "app.main:app", "--port", str(PORT)],
                            cwd=work, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(60):
        try:
            urllib.request.urlopen(BASE + "/health")
            return proc
        except Exception:
            time.sleep(0.25)
    raise RuntimeError("서버가 뜨지 않았습니다")


def docs_post(body):
    """/docs에서 POST /api/knowledge를 펼쳐 Try it out → Body 입력 → Execute. 입력·응답 화면을 저장한다."""
    SHOTS.mkdir(exist_ok=True)
    op = "operations-default-create_knowledge_api_knowledge_post"
    text_body = json.dumps(body, ensure_ascii=False, indent=2)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME)
        page = browser.new_page(viewport={"width": 640, "height": 900}, device_scale_factor=2)
        page.goto(BASE + "/docs"); page.wait_for_selector(f"#{op}")
        block = page.locator(f"#{op}")
        block.locator(".opblock-summary").first.click()
        block.locator(".try-out__btn").click()
        area = block.locator("textarea.body-param__text")
        area.fill(text_body)
        area.evaluate("el => { el.style.height = '7.5em'; el.style.minHeight = '0'; }")
        block.locator(".execute").click()
        live = block.locator(".live-responses-table"); live.wait_for(); time.sleep(0.5)
        status = int(live.locator("tbody .response-col_status").first.inner_text().strip())
        body_el = live.locator(".response-col_description div:has(> h5:text-is(\"Response body\")) pre").first
        response = json.loads(body_el.inner_text())
        sy = page.evaluate("window.scrollY")
        top = block.locator(".opblock-section-request-body").first.bounding_box()
        bottom = block.locator("button.execute").first.bounding_box()
        page.screenshot(path=str(SHOTS / "post_input.png"), full_page=True,
                        clip={"x": top["x"], "y": top["y"] + sy, "width": top["width"], "height": bottom["y"] + bottom["height"] - top["y"] + 8})
        box, end = live.bounding_box(), body_el.bounding_box()
        page.screenshot(path=str(SHOTS / "post_response.png"), full_page=True,
                        clip={"x": box["x"], "y": box["y"] + sy, "width": box["width"], "height": end["y"] + end["height"] - box["y"] + 6})
        browser.close()
    return {"request": "POST /api/knowledge (/docs)", "body": body, "status": status, "response": response,
            "shots": ["shots/post_input.png", "shots/post_response.png"]}


def main():
    out = {}
    work = Path(tempfile.mkdtemp(prefix="day19pm_"))
    shutil.copytree(PAGE_APP, work / "app", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(APP_SRC / "migration_lab", work / "migration_lab")
    (work / ".env").write_text(
        f"DB_USER={PG['user']}\nDB_PASSWORD=capture\nDB_HOST={PG['host']}\nDB_PORT={PG['port']}\nDB_NAME={DB}\n")
    fresh_db(DB, READY_SQL.read_text(encoding="utf-8"))
    out["start"] = {"knowledge": sql(ALL_SQL), "categories": sql("SELECT id, name FROM categories ORDER BY id")}

    # ---- 1교시: 연결과 첫 조회
    server = start_server(work)
    api = out["api"] = {}
    api["health"] = call("GET", "/health")
    api["list"] = call("GET", "/api/knowledge")
    api["filter_learning"] = call("GET", "/api/knowledge?category=learning")
    api["filter_none"] = call("GET", "/api/knowledge?category=nothing")

    # ---- 2교시: CRUD (일일프로젝트 A·B·C와 같은 순서)
    N = count("knowledge")
    api["post_a"] = call("POST", "/api/knowledge", {"title": "실습 질문 채널", "content": "막히면 팀 채널에 질문을 남깁니다.", "category": "learning"})
    api["post_b"] = docs_post({"title": "가상환경 정책", "content": "새 프로젝트는 uv로 가상환경을 만듭니다.", "category": "policy"})
    b = api["post_b"]["response"]["id"]
    out["sql_b_after_post"] = sql(ROW_SQL.format(id=b))
    out["sql_b_category_id"] = sql(f"SELECT id, title, category_id FROM knowledge WHERE id = {b}")
    out["categories_after_post"] = sql("SELECT id, name FROM categories ORDER BY id")
    api["get_b"] = call("GET", f"/api/knowledge/{b}")
    api["get_missing"] = call("GET", "/api/knowledge/9999")
    api["get_not_int"] = call("GET", "/api/knowledge/abc")
    api["put_b"] = call("PUT", f"/api/knowledge/{b}", {"title": "가상환경 정책", "content": "새 프로젝트는 uv init으로 시작합니다.", "category": "environment"})
    out["sql_b_after_put"] = sql(ROW_SQL.format(id=b))
    api["post_c"] = call("POST", "/api/knowledge", {"title": "임시 공지", "content": "오늘만 쓰는 안내입니다.", "category": "reference"})
    c = api["post_c"]["response"]["id"]
    api["delete_c"] = call("DELETE", f"/api/knowledge/{c}")
    api["get_c"] = call("GET", f"/api/knowledge/{c}")
    out["sql_c_after_delete"] = sql(f"SELECT count(*) AS rows FROM knowledge WHERE id = {c}")

    # ---- 3교시: 실패한 요청은 DB를 바꾸지 않는다
    before = {"knowledge": count("knowledge"), "categories": count("categories")}
    api["post_empty"] = call("POST", "/api/knowledge", {"title": "빈 본문", "content": "", "category": "learning"})
    api["put_partial"] = call("PUT", f"/api/knowledge/{b}", {"content": "본문만 보냄"})
    api["put_missing_newcat"] = call("PUT", "/api/knowledge/9999", {"title": "없는 지식", "content": "새 분류도 생기면 안 됩니다.", "category": "brandnew"})
    after = {"knowledge": count("knowledge"), "categories": count("categories")}
    out["fail_counts"] = {"before": before, "after": after,
                          "brandnew": count("categories WHERE name = 'brandnew'")}
    out["project"] = {"N": N, "a": api["post_a"]["response"]["id"], "b": b, "c": c, "final": count("knowledge")}

    # ---- 재시작 뒤에도 남는가
    server.terminate(); server.wait()
    out["down"] = True
    try:
        urllib.request.urlopen(BASE + "/health", timeout=1); out["down"] = False
    except Exception:
        pass
    server = start_server(work)
    api["list_after_restart"] = call("GET", "/api/knowledge")
    server.terminate(); server.wait()
    out["sql_after_restart"] = sql(ALL_SQL)

    # ---- 3교시: Session 실험 (같은 앱 코드를 직접 import)
    os.chdir(work)
    sys.path.insert(0, str(work))
    from sqlalchemy import String, select, text
    from sqlalchemy.orm import mapped_column
    from app.db import SessionLocal, engine, transaction
    from app.models import Category, Knowledge

    def other(table):  # 다른 연결 = 다른 요청이 보는 DB
        with engine.connect() as conn:
            return conn.execute(text(f"SELECT count(*) FROM {table}")).scalar()

    tx = out["session"] = {}
    db = SessionLocal()
    item = Knowledge(title="flush 확인", content="아직 확정 전", category_id=1)
    db.add(item); tx["add"] = {"id": item.id, "other": other("knowledge")}
    db.flush();   tx["flush"] = {"id": item.id, "other": other("knowledge")}
    db.commit();  tx["commit"] = {"id": item.id, "other": other("knowledge")}
    db.delete(item); db.commit(); db.close()

    def try_save(together):
        start = other("categories")
        db = SessionLocal()
        name = "together-demo" if together else "split-demo"
        err = None
        try:
            if together:
                with transaction(db):
                    cat = Category(name=name); db.add(cat); db.flush()
                    db.add(Knowledge(title="길이 초과", content="가" * 2001, category_id=cat.id)); db.flush()
            else:
                cat = Category(name=name); db.add(cat); db.commit()
                try:
                    db.add(Knowledge(title="길이 초과", content="가" * 2001, category_id=cat.id)); db.commit()
                except Exception:
                    db.rollback(); raise
        except Exception as e:
            err = {"type": type(e).__name__, "constraint": e.orig.diag.constraint_name}
        db.close()
        left = other(f"categories WHERE name = '{name}'")
        with engine.begin() as conn:
            conn.execute(text(f"DELETE FROM categories WHERE name = '{name}'"))
        return {"categories_before": start, "error": err, "category_left": left}

    tx["together"] = try_save(True)
    tx["split"] = try_save(False)

    Knowledge.source = mapped_column(String(120), nullable=True)  # ORM에만 열을 적는다
    with SessionLocal() as db:
        try:
            db.scalars(select(Knowledge)).all(); out["orm_only"] = {"ok": True}
        except Exception as e:
            out["orm_only"] = {"ok": False, "type": type(e).__name__, "message": str(e.orig).splitlines()[0]}

    # ---- 4교시: Migration (주 DB와 다른 연습 DB)
    fresh_db(MIG_DB)
    env = dict(os.environ, MIGRATION_DATABASE_URL=f"postgresql+psycopg://{PG['user']}:capture@{PG['host']}:{PG['port']}/{MIG_DB}")

    def alembic(*args):
        r = subprocess.run([sys.executable, "-m", "alembic", *args], cwd=work / "migration_lab", env=env,
                           capture_output=True, text=True, check=True)
        lines = (r.stdout + r.stderr).splitlines()
        return [l.replace("INFO  [alembic.runtime.migration] ", "") for l in lines
                if l.strip() and "Context impl" not in l and "Will assume" not in l]

    cols = ("SELECT column_name, data_type, character_maximum_length AS max_length, is_nullable "
            "FROM information_schema.columns WHERE table_name = 'knowledge' ORDER BY ordinal_position")
    mig = out["migration"] = {}
    mig["current_0"] = alembic("current")
    mig["history"] = alembic("history")
    mig["up_001"] = alembic("upgrade", "001_initial")
    mig["current_1"] = alembic("current")
    mig["tables_1"] = sql("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' "
                          "AND table_name <> 'alembic_version' ORDER BY table_name", MIG_DB)
    with psycopg.connect(dbname=MIG_DB, autocommit=True, **PG) as conn:
        conn.execute("INSERT INTO categories(name) VALUES ('learning')")
        conn.execute("INSERT INTO knowledge(title, content, category_id) VALUES ('기준 지식', 'Migration 전부터 있던 행', 1)")
    mig["cols_1"] = sql(cols, MIG_DB)
    mig["up_head"] = alembic("upgrade", "head")
    mig["current_2"] = alembic("current")
    mig["cols_2"] = sql(cols, MIG_DB)
    mig["rows_2"] = sql("SELECT id, title, content, source FROM knowledge", MIG_DB)
    mig["down_001"] = alembic("downgrade", "001_initial")
    mig["cols_3"] = sql(cols, MIG_DB)
    mig["rows_3"] = sql("SELECT id, title, content FROM knowledge", MIG_DB)
    mig["up_again"] = alembic("upgrade", "head")
    mig["current_4"] = alembic("current")

    import fastapi, sqlalchemy, pydantic, alembic as alembic_pkg
    out["env"] = {"postgresql": sql("SHOW server_version")["rows"][0][0], "fastapi": fastapi.__version__,
                  "sqlalchemy": sqlalchemy.__version__, "psycopg": psycopg.__version__,
                  "pydantic": pydantic.__version__, "alembic": alembic_pkg.__version__,
                  "python": sys.version.split()[0]}
    os.chdir(HERE)
    shutil.rmtree(work, ignore_errors=True)
    (HERE / "capture.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    print("capture.json 기록 완료")


if __name__ == "__main__":
    main()
