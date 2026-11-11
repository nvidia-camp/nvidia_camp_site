# /// script
# requires-python = ">=3.11"
# dependencies = ["psycopg[binary]"]
# ///
"""카드마다 SQL을 수업 데이터(S0)에서 실제로 실행해 결과를 capture.json에 기록한다.

사용: PGHOST=localhost PGPORT=55432 PGUSER=postgres uv run capture.py
- 수업 준비 SQL(nvidia_camp 05_LLM_RAG/20261111/mentee/00_setup/01_prepare_S0.sql)을 읽기만 한다.
- 카드마다 새 S0 상태에서 시작한다: 변경은 트랜잭션 안에서 실행하고 ROLLBACK한다.
- Auto commit 비교는 새 DB를 하나 더 만들어 실제로 확정되는 것을 확인한다.
"""
import json
from pathlib import Path

import psycopg

HERE = Path(__file__).resolve().parent
PREPARE = HERE.parents[4] / "05_LLM_RAG/20261111/mentee/00_setup/01_prepare_S0.sql"
DB = "knowledge_lab_capture"


def fresh_db(name):
    with psycopg.connect(dbname="postgres", autocommit=True) as conn:
        conn.execute(f"DROP DATABASE IF EXISTS {name}")
        conn.execute(f"CREATE DATABASE {name}")
    with psycopg.connect(dbname=name, autocommit=True) as conn:
        conn.execute(PREPARE.read_text(encoding="utf-8"))


def drop_db(name):
    with psycopg.connect(dbname="postgres", autocommit=True) as conn:
        conn.execute(f"DROP DATABASE IF EXISTS {name}")


def table(cur):
    return {"cols": [d.name for d in cur.description], "rows": [list(r) for r in cur.fetchall()]}


def query(conn, sql):
    return table(conn.execute(sql))


def error_of(conn, sql):
    """실패해야 하는 SQL을 savepoint 안에서 실행하고 위반한 제약조건 종류를 돌려준다."""
    conn.execute("SAVEPOINT s")
    try:
        conn.execute(sql)
    except psycopg.errors.IntegrityError as e:
        conn.execute("ROLLBACK TO SAVEPOINT s")
        return {"sqlstate": e.sqlstate, "constraint": e.diag.constraint_name}
    raise AssertionError(f"거부되지 않음: {sql}")


SQL = {
    "select": "SELECT id, title\nFROM knowledge\nWHERE category_id = 1\nORDER BY id;",
    "join": (
        "SELECT k.id, k.title, c.name AS category\nFROM knowledge AS k\n"
        "JOIN categories AS c\n  ON c.id = k.category_id\nORDER BY k.id;"
    ),
    "left_join": (
        "SELECT c.name AS category, k.title\nFROM categories AS c\n"
        "LEFT JOIN knowledge AS k\n  ON k.category_id = c.id\nORDER BY c.id, k.id;"
    ),
    "group_by": (
        "SELECT c.name AS category,\n       COUNT(k.id) AS knowledge_count\nFROM categories AS c\n"
        "LEFT JOIN knowledge AS k\n  ON k.category_id = c.id\nGROUP BY c.id, c.name\nORDER BY c.id;"
    ),
    "insert": (
        "INSERT INTO knowledge (title, content, category_id)\n"
        "VALUES ('임시 안내', '한 번만 실행합니다.', 1)\nRETURNING id;"
    ),
    "update": (
        "UPDATE knowledge\nSET content = '실행 전에 가상환경을 확인합니다.'\nWHERE id = 2;"
    ),
    "delete": "DELETE FROM knowledge\nWHERE id = 3;",
    "create_table": (
        "CREATE TABLE knowledge (\n"
        "  id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n"
        "  title       VARCHAR(80) NOT NULL\n"
        "              CHECK (char_length(title) BETWEEN 1 AND 80),\n"
        "  content     TEXT NOT NULL\n"
        "              CHECK (char_length(content) BETWEEN 1 AND 2000),\n"
        "  category_id BIGINT NOT NULL\n"
        "              REFERENCES categories (id) ON DELETE RESTRICT\n"
        ");"
    ),
    "tx_category": "INSERT INTO categories (name) VALUES ('api');",
    "tx_knowledge": (
        "INSERT INTO knowledge (title, content, category_id)\nVALUES ('API 문서', '', 4);"
    ),
}

REJECT = {
    "not_null": "INSERT INTO knowledge (title, content, category_id) VALUES (NULL, '본문', 1)",
    "check": "INSERT INTO knowledge (title, content, category_id) VALUES ('제목', '', 1)",
    "fk": "INSERT INTO knowledge (title, content, category_id) VALUES ('제목', '본문', 99)",
    "unique": "INSERT INTO categories (name) VALUES ('learning')",
    "restrict": "DELETE FROM categories WHERE name = 'learning'",
}

KNOWLEDGE_ALL = "SELECT id, title, content, category_id FROM knowledge ORDER BY id"
CATEGORIES_ALL = "SELECT id, name FROM categories ORDER BY id"

out = {"sql": SQL, "reject_sql": REJECT}
fresh_db(DB)
with psycopg.connect(dbname=DB) as conn:
    out["version"] = conn.execute("SHOW server_version").fetchone()[0]
    out["categories"] = query(conn, CATEGORIES_ALL)
    out["knowledge"] = query(conn, KNOWLEDGE_ALL)

    for key in ["select", "join", "left_join", "group_by"]:
        out[key] = query(conn, SQL[key])
    conn.rollback()

    for key in ["insert", "update", "delete"]:
        cur = conn.execute(SQL[key])
        out[key] = {"returning": table(cur) if cur.description else None,
                    "rowcount": cur.rowcount, "after": query(conn, KNOWLEDGE_ALL)}
        conn.rollback()

    # 보여 주는 CREATE TABLE이 실제로 실행되는지: 빈 스키마에 만들어 보고 취소
    conn.execute("CREATE SCHEMA ddl_check")
    conn.execute("SET search_path TO ddl_check, public")
    conn.execute("CREATE TABLE ddl_check.categories (id BIGINT PRIMARY KEY)")
    conn.execute(SQL["create_table"])
    out["create_table_ok"] = True
    conn.rollback()

    out["reject"] = {key: error_of(conn, sql) for key, sql in REJECT.items()}
    out["after_reject"] = query(conn, KNOWLEDGE_ALL)
    conn.rollback()

    # 트랜잭션으로 묶은 경우: 두 번째가 실패 → ROLLBACK → 둘 다 없음
    conn.execute("BEGIN")
    cur = conn.execute(SQL["tx_category"] + " ")
    try:
        conn.execute(SQL["tx_knowledge"])
        raise AssertionError("두 번째 INSERT가 실패해야 함")
    except psycopg.errors.CheckViolation:
        pass
    conn.rollback()
    out["tx_rollback"] = query(conn, CATEGORIES_ALL)
    conn.rollback()
drop_db(DB)

# Auto commit: 문장마다 확정 → 첫 INSERT만 남음 (새 DB에서 실제로 확인)
fresh_db(DB)
with psycopg.connect(dbname=DB, autocommit=True) as conn:
    conn.execute(SQL["tx_category"])
    try:
        conn.execute(SQL["tx_knowledge"])
        raise AssertionError("두 번째 INSERT가 실패해야 함")
    except psycopg.errors.CheckViolation:
        pass
    out["tx_autocommit"] = query(conn, CATEGORIES_ALL)
drop_db(DB)

(HERE / "capture.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("server", out["version"])
for key in ["select", "join", "left_join", "group_by"]:
    print(key, out[key]["rows"])
for key in ["insert", "update", "delete"]:
    print(key, out[key]["rowcount"], out[key]["returning"])
print("reject", out["reject"])
print("autocommit", out["tx_autocommit"]["rows"], "rollback", out["tx_rollback"]["rows"])
