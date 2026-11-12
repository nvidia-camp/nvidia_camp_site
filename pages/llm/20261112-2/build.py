"""Day19-2 오후 FastAPI–PostgreSQL 연동: template.html + 페이지 코드(code/app) + 실행 기록(capture/capture.json) → index.html

- 화면의 코드는 code/app 의 실제 파일에서 함수 단위로 잘라 온다(capture.py가 이 코드를 실행했다).
- 화면의 숫자·행은 모두 capture.json 에서 읽고, 아래 expect()로 기대값과 대조한다.
기록을 새로 만들 때: cd capture && PGHOST=localhost PGPORT=55433 PGUSER=postgres uv run capture.py
실행: python3 build.py
"""
import base64
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAMP = HERE.parents[3]
CAP = json.loads((HERE / "capture" / "capture.json").read_text(encoding="utf-8"))
APP = HERE / "code" / "app"
MIG = CAMP / "05_LLM_RAG/20261112/Day19_02/mentor/01_basic/05_PM05_일일프로젝트/migration_lab/migrations/versions/002_source.py"
API = CAP["api"]


def expect(cond, msg):
    assert cond, msg


# ── 기록과 기대값 대조 (화면에는 보이지 않음) ──
P = CAP["project"]
B, C = P["b"], P["c"]
expect(API["health"]["status"] == 200, "health")
expect([x["id"] for x in API["list"]["response"]] == [1, 2, 3], "list")
expect([x["id"] for x in API["filter_learning"]["response"]] == [1, 3] and API["filter_none"]["response"] == [], "filter")
expect(API["post_a"]["status"] == 201 and API["post_a"]["response"]["category"] == "learning", "post a")
expect(API["post_b"]["status"] == 201 and B == 5, "post b")
expect(CAP["sql_b_category_id"]["rows"][0][2] == 4, "b category_id")
expect(API["get_missing"]["status"] == 404 and API["get_not_int"]["status"] == 422, "get errors")
expect(API["put_b"]["status"] == 200 and API["put_b"]["response"]["id"] == B, "put")
expect(CAP["sql_b_after_put"]["rows"][0][3] == "environment", "put sql")
expect(API["delete_c"]["status"] == 204 and API["delete_c"]["size"] == 0, "delete")
expect(API["get_c"]["status"] == 404 and CAP["sql_c_after_delete"]["rows"][0][0] == 0, "after delete")
F = CAP["fail_counts"]
expect(F["before"] == F["after"] and F["brandnew"] == 0, "fail keeps db")
expect([API[k]["status"] for k in ("post_empty", "put_partial", "put_missing_newcat")] == [422, 422, 404], "fail status")
expect(P["final"] == P["N"] + 2 and CAP["down"], "project")
expect([x["id"] for x in API["list_after_restart"]["response"]] == [1, 2, 3, 4, 5], "restart")
S = CAP["session"]
expect(S["add"]["id"] is None and S["flush"]["other"] == S["add"]["other"] and S["commit"]["other"] == S["add"]["other"] + 1, "flush/commit")
expect(S["together"]["category_left"] == 0 and S["split"]["category_left"] == 1, "together/split")
expect(not CAP["orm_only"]["ok"], "orm only")
M = CAP["migration"]
expect(M["current_0"] == [] and M["current_2"] == ["002_source (head)"], "migration current")
expect(M["cols_2"]["rows"][-1][0] == "source" and M["rows_2"]["rows"][0][3] is None, "migration column")
expect([r[0] for r in M["cols_3"]["rows"]] == ["id", "title", "content", "category_id"], "downgrade")
print("기록과 기대값 대조: 모두 일치")


# ── 도구 ──
def e(s):
    return html.escape(str(s), quote=True)


PY_KW = set("import from def class return if else elif for in is None not and or with as raise try except yield True False".split())
SQL_KW = set("SELECT FROM WHERE JOIN ON AS AND ORDER BY INSERT INTO VALUES UPDATE SET DELETE COUNT".split())


def hl(line, lang):
    """주석 → 문자열 → 키워드 순서로 칠한다(주석 안 단어가 키워드 색이 되지 않게)."""
    com = r"#.*$" if lang == "py" else r"--.*$"
    kws = PY_KW if lang == "py" else SQL_KW
    out, last = "", 0
    for m in re.finditer(rf"({com})|(\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*')|\b([A-Za-z_]\w*)\b", line):
        out += e(line[last:m.start()])
        if m.group(1):
            out += f'<span class="c">{e(m.group(1))}</span>'
        elif m.group(2):
            out += f'<span class="s">{e(m.group(2))}</span>'
        elif m.group(3) in kws:
            out += f'<span class="k">{e(m.group(3))}</span>'
        else:
            out += e(m.group(3))
        last = m.end()
    return out + e(line[last:])


def pane(label, src, marks=(), lang="py"):
    rows = []
    for line in src.rstrip("\n").split("\n"):
        cls = "ln mark" if any(mk in line for mk in marks) else "ln"
        rows.append(f'<span class="{cls}">{hl(line, lang) if lang != "text" else e(line)}</span>')
    return f'<div class="pane"><div class="pane-head">{e(label)}</div><pre><code>{"".join(rows)}</code></pre></div>'


def read(name):
    return (APP / name).read_text(encoding="utf-8")


def block(src, name):
    """최상위 def/class 하나(위 데코레이터 포함)를 잘라 온다."""
    lines = src.split("\n")
    head = next(i for i, l in enumerate(lines) if re.match(rf"(def|class) {name}\b", l))
    start = head
    while start > 0 and lines[start - 1].startswith("@"):
        start -= 1
    end = head + 1
    while end < len(lines) and (lines[end] == "" or lines[end][0] in " \t"):
        end += 1
    return "\n".join(lines[start:end]).rstrip()


def resp(rec, label=None, trim=None):
    body = rec["response"]
    if body is None:
        text = f'(본문 없음 · {rec["size"]}바이트)'
    else:
        text = json.dumps(body, ensure_ascii=False, indent=2 if isinstance(body, dict) and "detail" not in body else None)
        if trim and len(text) > trim:
            text = text[:trim] + " …"
    return (f'<div class="resp"><div class="resp-bar"><span>{e(label or rec["request"])}</span><b>{rec["status"]}</b></div>'
            f'<pre>{e(text)}</pre></div>')


def table(cols, rows, caption=None, classes=None, num=()):
    classes = classes or [""] * len(rows)
    head = "".join(f'<th class="{"num" if i in num else ""}">{c}</th>' for i, c in enumerate(cols))
    body = "".join(
        f'<tr class="{cl}">' + "".join(f'<td class="{"num" if i in num else ""}">{v}</td>' for i, v in enumerate(r)) + "</tr>"
        for r, cl in zip(rows, classes))
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'<div class="table-wrap"><table>{cap}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def no_comments(src):
    return "\n".join(l for l in src.split("\n") if not l.strip().startswith("#"))


def webp(name, w, h):
    data = base64.b64encode((HERE / "img" / f"{name}.webp").read_bytes()).decode("ascii")
    return f'<img src="data:image/webp;base64,{data}" width="{w}" height="{h}"'


def img(rel):
    data = base64.b64encode((HERE / "capture" / rel).read_bytes()).decode("ascii")
    return f"data:image/png;base64,{data}"


def none(v):
    return "NULL" if v is None else e(v)


# ── 코드 원본 ──
SETTINGS, DB, MODELS, SCHEMAS, MAIN = (read(n) for n in ("settings.py", "db.py", "models.py", "schemas.py", "main.py"))
MIG_SRC = MIG.read_text(encoding="utf-8")
body_b = API["post_b"]["body"]
cat_b = CAP["sql_b_category_id"]["rows"][0][2]

# ── 머리말 ──
out = [f"""<header class="head">
  <p class="eyebrow">Day19-2 · 11/12 오후 · 생성형 AI·LLM 및 RAG 엔지니어링</p>
  <h1>FastAPI–PostgreSQL 연동</h1>
  <p class="lead">오전에 따로 만든 FastAPI와 PostgreSQL을 잇습니다. 이제 API로 지식을 하나 등록하면 DB에 행이 하나 생깁니다.</p>
  <div class="level">
    <span class="level-tag">basic</span>
    <p><b>basic(기본필수) 실습 기준입니다.</b> 코드는 basic 완성본에서 오늘 배우는 부분만 남겼습니다. 노란 <span class="todo">B01</span> 표시는 실습에서 직접 채우는 곳입니다.</p>
  </div>
</header>"""]

# ── 큰 그림: 연결 지도 ──
LAYERS = [
    ("cli", "/docs", "요청을 보내고 응답을 받는다. /docs 대신 Postman 같은 도구로 보내도 된다", [("브라우저", "127.0.0.1:8000/docs")], [4, 6]),
    ("api", "FastAPI", "주소를 경로 함수에 연결하고, 입력을 검사하고, 응답 모양을 정한다",
     [("main.py", "@app.post(…)"), ("schemas.py", "KnowledgeWrite · KnowledgeRead")], [6, 7, 12]),
    ("orm", "ORM Model", "테이블 한 행 = Python 객체 하나. 분류는 이름과 번호를 서로 바꾼다",
     [("models.py", "Category · Knowledge")], [3, 5]),
    ("ses", "Session", "요청 하나의 작업 공간. 객체를 모으고(add), SQL로 보내고(flush), 확정한다(commit)",
     [("db.py", "get_db() · transaction()")], [2, 10, 11]),
    ("eng", "Engine · Psycopg", "DB 연결을 만들어 두고 빌려준다. Psycopg(Driver)가 SQL을 실제로 보낸다",
     [("db.py", "create_engine(…)"), ("settings.py", "URL.create(…) ← .env")], [1]),
    ("db", "PostgreSQL", "DB day19_crud_b · 테이블 categories, knowledge", [("DB", "localhost:5432")], [14, 15]),
]
LAYER_NAME = {k: n for k, n, *_ in LAYERS}
# 층 사이에서 오가는 것 (내려가는 요청, 올라오는 응답) · 실제 값
WIRES = [
    (f'<code>POST /api/knowledge</code><br>title · content · category <code>"policy"</code>',
     f'<code>201</code> {{…, "category": "policy", "id": <b>{B}</b>}}'),
    ('<code>Knowledge(title=…, category=…)</code><br>객체를 만든다',
     f'<code>to_read(item)</code><br>category_id {cat_b} → <code>"policy"</code>'),
    ("<code>db.add(item)</code><br>Session에 올린다", f"<code>item.id = {B}</code><br>번호가 객체에 채워진다"),
    (f'flush: <code>INSERT</code> 분류 · 지식<br>commit: 둘을 함께 확정', f'DB가 정한 id<br>분류 <b>{cat_b}</b> · 지식 <b>{B}</b>'),
    ("연결 하나를 빌려<br>SQL을 보낸다", "저장된 두 행"),
]


def layer_box(key, name, meaning, files, steps):
    fl = "".join(f'<li><b>{e(f)}</b><code>{e(c)}</code></li>' for f, c in files)
    links = " ".join(f'<a href="#s{n}">{n}</a>' for n in steps)
    return (f'<div class="lbox ly-{key}"><div class="lbox-top"><span class="lname">{e(name)}</span>'
            f'<span class="lsteps">단계 {links}</span></div><p>{e(meaning)}</p><ul class="lfiles">{fl}</ul></div>')


lift = ['<div class="lift-head"><span>요청 ↓ 내려간다</span><span></span><span>↑ 응답이 올라온다</span></div>']
for i, layer in enumerate(LAYERS):
    lift.append(layer_box(*layer))
    if i < len(WIRES):
        down, up = WIRES[i]
        lift.append(f'<p class="down"><span class="dir">요청 ↓</span>{down}</p><span class="wire" aria-hidden="true"></span>'
                    f'<p class="up"><span class="dir">응답 ↑</span>{up}</p>')
lift_html = f'<div class="lift">{"".join(lift)}</div>'

FILES = [
    (".env", "DB_NAME=day19_crud_b<br>DB_USER · DB_PASSWORD …", "접속 정보 다섯 값", 1),
    ("settings.py", "Settings()<br>URL.create(…)", "다섯 값으로 접속 주소를 만든다", 1),
    ("db.py", "engine = create_engine(url)<br>get_db() → Session", "연결 기반 하나 + 요청마다 Session", 2),
    ("main.py", "db: Session = Depends(get_db)", "경로 함수가 db를 받아 쓴다", 2),
]
ARROWS = ["값을 읽는다", "URL을 넘긴다", "Session을 넘긴다"]
wire = []
for i, (f, code, what, no) in enumerate(FILES):
    wire.append(f'<a class="fnode" href="#s{no}"><b>{e(f)}</b><code>{code}</code><span>{e(what)}</span></a>')
    if i < len(ARROWS):
        wire.append(f'<span class="farrow">{e(ARROWS[i])}</span>')
files_html = f'<div class="fwire">{"".join(wire)}</div>'


def here(keys):
    """단계 카드 머리의 '지금 여기' 띠: 연결 지도의 여섯 층 중 이 단계가 다루는 층을 칠한다."""
    items = "".join(f'<li class="ly-{k}{" on" if k in keys else ""}">{e(n)}</li>' for k, n, *_ in LAYERS)
    return f'<div class="here"><span>지금 여기</span><ol>{items}</ol></div>'


GROUPS = [
    ("connect", "연결", "Engine · Session", "1교시", [(1, "접속 설정"), (2, "Session"), (3, "ORM Model"), (4, "첫 조회")]),
    ("crud", "CRUD", "ORM으로 다섯 API", "2교시", [(5, "분류 연결"), (6, "POST"), (7, "GET 상세"), (8, "PUT"), (9, "DELETE")]),
    ("tx", "트랜잭션", "Transaction", "3교시", [(10, "flush와 commit"), (11, "함께 확정"), (12, "실패한 요청")]),
    ("mig", "Migration", "Alembic", "4교시", [(13, "ORM만 바꾸면"), (14, "Revision 적용"), (15, "같은 id로 확인")]),
]
out.append(f"""<section id="big" aria-labelledby="big-title">
  <div class="section-head"><h2 id="big-title">큰 그림</h2></div>
  <ol class="band">
    <li><span>Day18</span>SQL · 트랜잭션</li>
    <li><span>오전</span>FastAPI · SQL 따로</li>
    <li class="now"><span>오후 · 오늘</span>둘을 연결</li>
    <li><span>다음</span>LLM · RAG의 원본 지식</li>
  </ol>
  <p class="lead">주소·입력·응답은 오전 그대로입니다. 저장하는 곳만 <code>data.json</code> → PostgreSQL로 바뀝니다.</p>
  <div class="fig">
    <p class="fig-title">연결 지도 · POST 한 번이 DB 행이 되기까지 <small>실제 값</small></p>
    {lift_html}
  </div>
  <div class="fig">
    <p class="fig-title">이 연결을 만드는 파일 · 설정이 이어지는 순서</p>
    {files_html}
  </div>
</section>""")


# ── 단계 카드 ──
STEP_LAYERS = {1: "eng db", 2: "ses", 3: "orm db", 4: "cli api orm ses", 5: "orm ses", 6: "cli api orm ses", 7: "api",
        8: "api orm ses", 9: "api ses", 10: "ses eng", 11: "ses", 12: "cli api", 13: "orm db", 14: "db", 15: "cli db"}
STEP_LAYERS = {k: v.split() for k, v in STEP_LAYERS.items()}


def step(no, title, left, right, key, todo=None, given=False, left_label="코드", extra=""):
    keys = STEP_LAYERS[no]
    badge = "".join(f'<span class="todo">{t}</span>' for t in (todo or []))
    if given:
        badge += '<span class="given">제공 코드 · 읽기만</span>'
    right_html = f'<div><p class="label">실제 결과</p>{right}</div>' if right else ""
    return f"""<article class="step" id="s{no}">
  <div class="step-head"><span class="no">{no}</span><h3>{title}</h3>{badge}</div>
  {here(keys)}
  <p class="mean"><b>핵심</b>{key}</p>
  <div class="two"><div><p class="label">{left_label}</p>{left}</div>{right_html}</div>
  {extra}
</article>"""


def section(gid, steps_html):
    _, name, en, per, _ = next(g for g in GROUPS if g[0] == gid)
    return f"""<section id="{gid}" aria-labelledby="{gid}-title">
  <div class="section-head"><h2 id="{gid}-title">{e(name)}<small>{e(en)} · {e(per)}</small></h2></div>
  <div class="steps">{"".join(steps_html)}</div>
</section>"""


ENV = """# .env  (Git에 올리지 않는다)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=day19_crud_b
DB_USER=postgres
DB_PASSWORD=비밀번호"""
RUN = """$ python -m uvicorn app.main:app --reload
브라우저: http://127.0.0.1:8000/docs"""

get_db_src = block(DB, "get_db")
engine_src = "\n".join(l for l in DB.split("\n") if l.startswith(("engine", "SessionLocal", "# Engine", "# SessionLocal")))
api_b, sql_b = API["get_b"]["response"], CAP["sql_b_category_id"]["rows"][0]

s1 = step(1, "접속 설정 · <code>.env</code>와 <code>URL.create</code>",
          pane(".env", ENV, lang="text") + pane("app/settings.py", block(SETTINGS, "Settings"), marks=("URL.create",)),
          pane("터미널", RUN, lang="text") + resp(API["health"], "GET /health"),
          "접속 정보는 <code>.env</code>에 두고 <code>URL.create</code>로 주소를 만든다. <code>.env</code>의 DB 이름이 pgAdmin에서 본 DB와 같아야 같은 데이터를 본다.",
          todo=["B01"])
s2 = step(2, "Session · 요청마다 하나 열고, 끝나면 닫는다",
          pane("app/db.py", no_comments(engine_src + "\n\n\n" + get_db_src), marks=("yield db",)),
          table(["순서", "일어나는 일"], [
              ["1", "요청이 들어온다"],
              ["2", "<code>with SessionLocal() as db</code> → 이 요청 전용 Session"],
              ["3", "<code>yield db</code> → 경로 함수의 <code>db</code> 매개변수로 들어간다"],
              ["4", "함수가 끝나고 응답이 나간다"],
              ["5", "<code>with</code>가 끝나며 Session을 닫는다"],
          ], caption="요청 하나에서 Session의 일생"),
          "<code>Depends(get_db)</code>가 요청마다 Session을 하나 열어 넘기고, 응답이 나가면 닫는다. 닫는 것(close)은 저장(commit)이 아니다.",
          todo=["B02"])
s3 = step(3, "ORM Model · 테이블을 클래스로",
          pane("app/models.py", block(MODELS, "Category") + "\n\n\n" + block(MODELS, "Knowledge"), marks=("category_id", "relationship")),
          table(["", "API 응답 (외부)", "DB 행 (내부)"], [
              ["id", f"<code>{api_b['id']}</code>", f"<code>{sql_b[0]}</code>"],
              ["title", e(api_b["title"]), e(sql_b[1])],
              ["분류", f'<code>"category": "{e(api_b["category"])}"</code>', f"<code>category_id = {sql_b[2]}</code>"],
          ], caption=f"같은 지식 id {B}를 두 쪽에서 본 모습", classes=["", "", "hit"]),
          "클래스는 이미 있는 테이블을 읽는 설계도다. API는 분류를 <b>이름</b>으로, DB는 <b>번호</b>로 다룬다.",
          given=True)
lst = API["list"]["response"]
s4 = step(4, "첫 조회 · SQL로 넣은 지식이 API에 보인다",
          pane("app/main.py", block(MAIN, "to_read") + "\n\n\n" + block(MAIN, "list_knowledge"), marks=("select(", "db.scalars")),
          table(["id", "title", "category"], [[x["id"], e(x["title"]), e(x["category"])] for x in lst],
                caption=f"GET /api/knowledge → {API['list']['status']} · 오전 DB의 {len(lst)}건 그대로")
          + f'<p class="sub"><code>?category=learning</code> → id {", ".join(str(x["id"]) for x in API["filter_learning"]["response"])} · 없는 분류 → <code>[]</code></p>',
          "<code>select</code>로 만든 SQL을 Session이 실행하고, 결과는 <code>Knowledge</code> 객체로 온다. <b>어제 SQL로 넣은 실제 행</b>이 보이면 연결된 것이다.",
          todo=["B03"],
          extra='<div class="extra"><p class="label">같은 요청을 Postman으로 · 수업 중 실제 화면</p>'
                + webp("postman_list", 884, 726) + ' alt="Postman에서 GET /api/knowledge를 보내 200 OK와 지식 목록 JSON을 받은 화면">'
                + '<p class="sub">/docs 대신 Postman 같은 도구로 보내도 결과는 같다. 요청을 Collection으로 저장해 두고 다시 보낼 수 있다. '
                + '화면의 DB는 실습을 진행한 뒤라 행이 더 많다.</p></div>')
out.append(section("connect", [s1, s2, s3, s4]))

cats = CAP["categories_after_post"]["rows"]
s5 = step(5, "분류 연결 · 이름으로 찾고, 없으면 만든다",
          pane("app/main.py", block(MAIN, "get_or_create_category"), marks=("db.flush()",)),
          table(["id", "name", ""], [[r[0], f"<code>{e(r[1])}</code>",
                                      '<span class="tag ok">B가 새로 만듦</span>' if r[1] == "policy" else
                                      ('<span class="tag keep">A가 재사용</span>' if r[1] == "learning" else "")] for r in cats],
                caption="POST A(learning) · B(policy) 뒤 categories", classes=["hit" if r[1] == "policy" else "" for r in cats]),
          "<code>add</code>는 Session에 올리기, <code>flush</code>는 SQL을 보내 id 받기, <code>commit</code>은 확정. 분류 번호는 이 함수가 찾거나 새로 받아 온다.",
          todo=["B04"])
post_row = CAP["sql_b_after_post"]["rows"][0]
s6 = step(6, "POST · 저장하고 201",
          pane("app/main.py", block(MAIN, "create_knowledge"), marks=("db.add", "db.flush()", "with transaction")),
          '<div class="shots">'
          + f'<img src="{img(API["post_b"]["shots"][0])}" alt="/docs에서 POST Body를 입력한 화면" width="582" height="295">'
          + f'<img src="{img(API["post_b"]["shots"][1])}" alt="/docs의 응답 201과 Response body, id {B}" width="542" height="196">'
          + "</div>"
          + table(["id", "title", "content", "category"], [[e(v) for v in post_row]],
                  caption=f"SQL · WHERE k.id = {B}  →  응답과 같은 행", classes=["hit"]),
          "id는 DB가 정한다(오전의 <code>next_id</code>는 없다). 응답의 id로 SQL을 실행하면 같은 행이 나온다.",
          todo=["B06"])
s7 = step(7, "GET 상세 · 없으면 404",
          pane("app/main.py", block(MAIN, "load_one") + "\n\n\n" + block(MAIN, "read_knowledge"), marks=("raise HTTPException",)),
          '<div class="resps">' + resp(API["get_b"]) + resp(API["get_missing"]) + resp(API["get_not_int"], trim=90) + "</div>",
          "없는 번호는 404, 숫자가 아닌 값은 FastAPI가 먼저 422로 거절한다.",
          todo=["B05"])
put_row = CAP["sql_b_after_put"]["rows"][0]
s8 = step(8, "PUT · id는 그대로, 세 필드를 바꾼다",
          pane("app/main.py", block(MAIN, "update_knowledge"), marks=("item.title", "item.content", "item.category =")),
          resp(API["put_b"]) + table(["id", "title", "content", "category"], [[e(v) for v in put_row]],
                                     caption=f"SQL · WHERE k.id = {B}", classes=["hit"]),
          f"객체의 값을 바꾸면 Session이 UPDATE를 만든다. id {B}와 지식 수는 그대로다.",
          todo=["B07"])
s9 = step(9, "DELETE · 본문 없는 204",
          pane("app/main.py", block(MAIN, "delete_knowledge"), marks=("db.delete",)),
          '<div class="resps">' + resp(API["delete_c"]) + resp(API["get_c"]) + "</div>"
          + f'<p class="sub">SQL · <code>WHERE id = {C}</code> → {CAP["sql_c_after_delete"]["rows"][0][0]}행</p>',
          "<code>db.delete</code>는 삭제 표시, 실제 삭제는 commit 때. 삭제 뒤 API는 404, DB는 0행이다.",
          todo=["B08"])
out.append(section("crud", [s5, s6, s7, s8, s9]))

FLUSH_DEMO = """db = SessionLocal()
item = Knowledge(title="flush 확인", content="아직 확정 전", category_id=1)
db.add(item)
db.flush()
db.commit()
# 단계마다 다른 연결에서 SELECT count(*) FROM knowledge"""
s10 = step(10, "flush와 commit · 언제 다른 요청에게 보이나",
           pane("실험 · 같은 앱 코드로", FLUSH_DEMO, marks=("db.flush()", "db.commit()")),
           table(["이 Session에서", "item.id", "다른 연결이 본 knowledge 수"], [
               ["<code>db.add(item)</code>", "None (아직 없음)", S["add"]["other"]],
               ["<code>db.flush()</code>", S["flush"]["id"], f'<span class="big">{S["flush"]["other"]}</span> 아직 안 보임'],
               ["<code>db.commit()</code>", S["commit"]["id"], f'<span class="big">{S["commit"]["other"]}</span> 이제 보임'],
           ], classes=["", "", "hit"]),
           "flush 뒤에 id가 생겨도 commit 전에는 다른 요청에게 보이지 않는다. 그래서 201은 commit 뒤에 보낸다.")
T, SP = S["together"], S["split"]
s11 = step(11, "함께 확정 · 새 분류만 남는 반쪽 저장을 막는다",
           pane("app/db.py", block(DB, "transaction"), marks=("db.commit()", "db.rollback()")),
           table(["저장 방식", "지식 저장", "새 분류"], [
               ["분류 먼저 commit → 그다음 지식", '<span class="tag bad">실패</span>',
                f'<span class="tag bad">{SP["category_left"]}건 남음</span> 지식 없는 분류'],
               ["<code>with transaction(db):</code> 안에서 함께", '<span class="tag bad">실패</span>',
                f'<span class="tag ok">{T["category_left"]}건</span> 함께 취소'],
           ], caption="새 분류를 만든 뒤 지식 저장이 DB 규칙(본문 2,000자 이하)에 걸려 실패하게 했다", classes=["bad", "hit"]),
           "어제의 COMMIT·ROLLBACK이 코드에서는 이 함수다. 함께 맞아야 하는 변경은 한 번에 확정하고, 하나라도 실패하면 전부 취소한다.",
           todo=["B09"])
fb, fa = F["before"], F["after"]
s12 = step(12, "실패한 요청은 DB를 바꾸지 않는다",
           table(["보낸 것", "응답"], [
               ['POST · <code>content</code> 빈 문자열', f'<b>{API["post_empty"]["status"]}</b> 입력 거절'],
               [f'PUT <code>/{B}</code> · <code>content</code>만 보냄', f'<b>{API["put_partial"]["status"]}</b> 입력 거절'],
               ['PUT <code>/9999</code> · 새 분류 <code>brandnew</code>', f'<b>{API["put_missing_newcat"]["status"]}</b> 대상 없음'],
           ]),
           table(["", "knowledge", "categories"], [
               ["실패 요청 3개 전", fb["knowledge"], fb["categories"]],
               ["실패 요청 3개 뒤", fa["knowledge"], fa["categories"]],
           ], caption=f'수가 그대로 · brandnew 분류 {F["brandnew"]}건', num=(1, 2), classes=["", "hit"]),
           "422는 입력만 보고 거절(DB까지 가지 않음), 404는 찾아봤는데 없음. 어느 쪽도 DB를 바꾸지 않는다.",
           left_label="요청")
out.append(section("tx", [s10, s11, s12]))

ORM_DEMO = """# models.py의 Knowledge에 한 줄만 더했다 (DB는 그대로)
source: Mapped[str | None] = mapped_column(String(120))

db.scalars(select(Knowledge)).all()"""
s13 = step(13, "ORM만 바꾸면 · DB는 따라오지 않는다",
           pane("실험", ORM_DEMO, marks=("source:",)),
           f'<div class="resp"><div class="resp-bar"><span>조회 결과</span><b>실패</b></div><pre>{e(CAP["orm_only"]["message"])}</pre></div>',
           "클래스에 열을 적어도 실제 테이블은 그대로다. 테이블 구조를 바꾸는 일은 Migration이 한다.")
cols2 = M["cols_2"]["rows"]
s14 = step(14, "Revision 적용 · Alembic",
           pane("migrations/versions/002_source.py", MIG_SRC.replace("branch_labels = None\ndepends_on = None\n", ""),
                marks=("op.add_column", "op.drop_column", "down_revision")),
           table(["명령", "결과"], [
               ["<code>alembic current</code>", "(적용된 것 없음)"],
               ["<code>alembic upgrade 001_initial</code>", "categories · knowledge 생성 → current <code>001_initial</code>"],
               ["기준 지식 1건 INSERT", f'id {M["rows_2"]["rows"][0][0]} <code>{e(M["rows_2"]["rows"][0][1])}</code>'],
               ["<code>alembic upgrade head</code>", f'<code>source</code> 열 추가 → current <code>{e(M["current_2"][0])}</code>'],
               ["기존 행", f'id {M["rows_2"]["rows"][0][0]} 그대로, <code>source</code>는 {none(M["rows_2"]["rows"][0][3])}'],
               ["<code>alembic downgrade 001_initial</code>", f'<code>source</code> 열 삭제, 행 {len(M["rows_3"]["rows"])}건 유지'],
           ], classes=["", "", "", "hit", "", ""])
           + table(["column_name", "data_type", "max_length", "is_nullable"],
                   [[e(c) for c in [r[0], r[1], r[2], r[3]]] for r in cols2 if r[0] == "source"],
                   caption="upgrade head 뒤 knowledge에 생긴 열", classes=["hit"]),
           "구조 변경을 Revision 파일로 남기고 연습 DB에 적용한다. 새 열은 NULL 허용으로 추가해야 기존 행이 깨지지 않는다.",
           todo=["M01", "M02"])
CHECK_SQL = f"""SELECT k.id, k.title, k.content, c.name AS category
FROM knowledge AS k
JOIN categories AS c ON c.id = k.category_id
-- {B}는 POST 응답에서 받은 id
WHERE k.id = {B};"""
s15 = step(15, "같은 id로 확인 · API와 DB가 같은 행을 보는가",
           pane("SQL", CHECK_SQL, lang="sql", marks=("WHERE",)),
           resp(API["get_b"], f"GET /api/knowledge/{B}")
           + table(["id", "title", "content", "category"], [[e(v) for v in put_row]], caption="SQL 결과", classes=["hit"]),
           "응답의 id로 DB를 직접 조회해 같은 값이면 연결이 끝난 것이다.",
           todo=["B11"])
out.append(section("mig", [s13, s14, s15]))

# ── 종합 ──
after = {x["id"]: x for x in API["list_after_restart"]["response"]}
a_id = P["a"]
out.append(f"""<section id="summary" aria-labelledby="summary-title">
  <div class="section-head"><h2 id="summary-title">종합 <small>일일프로젝트 · 5교시</small></h2>
  <p>시작 N = {P["N"]} → POST A·B·C → PUT B → 실패 요청 3개 → DELETE C → 서버를 껐다가 다시 켠 뒤 확인</p></div>
  {table(["지식", "한 일", "재시작 뒤 API", "SQL"], [
      [f"A · id {a_id}", "유지", f'200 · {e(after[a_id]["title"])}', "있음"],
      [f"B · id {B}", "수정", f'200 · {e(after[B]["content"])}', "있음"],
      [f"C · id {C}", "삭제", "404", "0행"],
      ["전체", "", f'<span class="big">{len(after)}건 = N+2</span>', f'{len(CAP["sql_after_restart"]["rows"])}행'],
  ], classes=["", "", "", "hit"])}
  <ol class="summary">
    <li><p>API 약속(주소·입력·응답)은 오전과 같다. 저장하는 곳만 PostgreSQL로 바뀌었다.</p></li>
    <li><p>요청 하나에 Session 하나. 그 안에서 add·flush로 모으고, commit 한 번으로 확정하거나 rollback으로 함께 취소한다.</p></li>
    <li><p>API는 분류를 이름으로, DB는 번호(FK)로 다룬다. 바꾸는 일은 <code>get_or_create_category</code>와 <code>to_read</code>가 한다.</p></li>
    <li><p>테이블 구조를 바꾸는 일은 ORM 코드가 아니라 Migration이 한다. 성공은 응답 id로 DB 행을 다시 찾아 확인한다.</p></li>
  </ol>
</section>""")

# ── 더 알아보기 ──
out.append(f"""<details>
  <summary>더 알아보기</summary>
  <dl>
    <dt>rollback과 id 번호</dt><dd>rollback해도 이미 발급된 번호는 돌아오지 않는다. 10단계에서 id {C}가 지워진 뒤에 {S["flush"]["id"]}가 나온 것도 같은 이유로, 번호는 건너뛸 수 있다.</dd>
    <dt>DB 오류의 응답</dt><dd>입력 오류(422)·없는 대상(404) 말고도, DB 규칙 충돌은 409, DB 연결 실패는 503, 그 밖의 예상 못 한 오류는 500으로 나누어 응답할 수 있다. basic 완성본은 규칙 충돌만 409로 바꾼다.</dd>
    <dt><code>refresh()</code> · <code>close()</code></dt><dd><code>refresh</code>는 DB 값을 객체에 다시 읽어 오고, <code>close</code>는 Session을 정리한다. 둘 다 저장(commit)이 아니다.</dd>
    <dt>autogenerate · stamp</dt><dd><code>alembic revision --autogenerate</code>는 ORM과 DB의 차이로 Revision 초안을 만든다. 초안이라 꼭 읽어 봐야 한다. <code>alembic stamp</code>는 이력 표시만 바꾸고 테이블은 바꾸지 않는다.</dd>
    <dt>intermediate · advanced</dt><dd>같은 기능을 파일로 나눈다: <code>schemas.py</code> 분리(intermediate), Router·Service·Repository 구조와 테스트 DB·<code>dependency_overrides</code>로 자동 검증(advanced).</dd>
  </dl>
</details>""")

env = CAP["env"]
out.append(f"""<footer class="foot">
  <p>pgAdmin 사용법은 <a data-site href="../../setup/postgresql/pgadmin/">PostgreSQL 가이드</a>에 있습니다.</p>
  <p>위 코드는 basic 완성본에서 오늘 배우는 부분만 남긴 것이고, 결과는 이 코드를 PostgreSQL {e(env["postgresql"].split()[0])}에 연결해 실제로 실행한 값입니다 (FastAPI {e(env["fastapi"])} · SQLAlchemy {e(env["sqlalchemy"])} · Psycopg {e(env["psycopg"])} · Alembic {e(env["alembic"])} · Python {e(env["python"])}).</p>
</footer>""")

page = (HERE / "template.html").read_text(encoding="utf-8").replace("{{BODY}}", "\n\n".join(out))
left = re.findall(r"\{\{[^}]+\}\}", page)
assert not left, left
(HERE / "index.html").write_text(page, encoding="utf-8")
print("index.html", len(page) // 1024, "KB")
