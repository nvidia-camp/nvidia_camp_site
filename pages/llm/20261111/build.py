# 실행 기록(capture/capture.json) → index.html
# 사용: python3 build.py   (기록을 새로 만들 때: cd capture && uv run capture.py — PostgreSQL 필요)
# 원칙: 같은 두 테이블을 카드마다 다시 그리고, SQL이 바꾸거나 고르는 칸만 표시한다.
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAP = json.loads((HERE / "capture" / "capture.json").read_text(encoding="utf-8"))
SQL = CAP["sql"]
CAT_NAME = {row[0]: row[1] for row in CAP["categories"]["rows"]}
CAT_ID = {name: cid for cid, name in CAT_NAME.items()}

KEYWORDS = (
    "SELECT FROM WHERE ORDER BY JOIN LEFT ON AS GROUP COUNT INSERT INTO VALUES RETURNING "
    "UPDATE SET DELETE CREATE TABLE BIGINT GENERATED ALWAYS IDENTITY PRIMARY KEY VARCHAR "
    "NOT NULL CHECK TEXT REFERENCES RESTRICT BETWEEN AND BEGIN COMMIT ROLLBACK"
).split()
TOKEN = re.compile(r"(--[^\n]*)|('(?:[^']|'')*')|\b(" + "|".join(KEYWORDS) + r")\b")


def esc(value):
    return html.escape(str(value))


def sql_html(sql):
    out, pos = [], 0
    for m in TOKEN.finditer(sql):
        out.append(esc(sql[pos:m.start()]))
        cls = "cmt" if m.group(1) else "str" if m.group(2) else "kw"
        out.append(f'<span class="{cls}">{esc(m.group(0))}</span>')
        pos = m.end()
    out.append(esc(sql[pos:]))
    return f'<pre class="sql"><code>{"".join(out)}</code></pre>'


def cat_chip(value, show_name=False):
    """분류 id 또는 이름을 같은 색 칩으로. 색만으로 구분하지 않도록 글자를 함께 쓴다."""
    if value is None:
        return '<span class="null">NULL</span>'
    cid = value if isinstance(value, int) else CAT_ID.get(value)
    label = f"{value}" if not show_name else f"{value} {CAT_NAME[cid]}"
    return f'<span class="cat c{cid}">{esc(label)}</span>'


def cell(value):
    return '<span class="null">NULL</span>' if value is None else esc(value)


def mini(cols, rows, row_cls=None, render=None, caption=None, labels=None):
    """cols: 머리글, rows: 값, row_cls: 행마다 클래스, render: (열 이름, 값) → HTML."""
    head = "".join(f"<th>{esc(c)}</th>" for c in cols)
    body = []
    for i, row in enumerate(rows):
        cls = row_cls[i] if row_cls else ""
        tds = "".join(f"<td>{render(c, v) if render else cell(v)}</td>" for c, v in zip(cols, row))
        tag = f'<td class="tag">{labels[i]}</td>' if labels else ""
        body.append(f'<tr class="{cls}">{tds}{tag}</tr>')
    tail = '<th class="tag"></th>' if labels else ""
    cap = f"<caption>{caption}</caption>" if caption else ""
    return f'<table class="mini">{cap}<thead><tr>{head}{tail}</tr></thead><tbody>{"".join(body)}</tbody></table>'


def by_category(col, value):
    if col in ("category_id",) or col == "category":
        return cat_chip(value)
    return cell(value)


def card(key, tag, title, sql, viz, points, wide=False):
    pts = "".join(f"<li>{p}</li>" for p in points)
    cls = "card wide" if wide else "card"
    return f"""
<article class="{cls}" id="{key}">
  <header class="card-head"><span class="tag-kw">{tag}</span><h3>{title}</h3></header>
  {sql}
  <div class="viz">{viz}</div>
  <ul class="points">{pts}</ul>
</article>"""


# ── 큰 그림 ──────────────────────────────────────────────
K = CAP["knowledge"]
k_cols = ["id", "title", "category_id"]
k_rows = [[r[0], r[1], r[3]] for r in K["rows"]]
cat_table = mini(["id", "name"], CAP["categories"]["rows"],
                 render=lambda c, v: cat_chip(v) if c == "id" else esc(v),
                 caption="<code>categories</code> 분류")
know_table = mini(k_cols, k_rows, render=by_category, caption="<code>knowledge</code> 지식")

MAP = [
    ("조회", "행 조회 · 두 테이블 연결 · 집계",
     [("SELECT", "select"), ("JOIN", "join"), ("LEFT JOIN", "left_join"), ("GROUP BY", "group_by")]),
    ("변경", "행 추가 · 수정 · 삭제", [("INSERT", "insert"), ("UPDATE", "update"), ("DELETE", "delete")]),
    ("테이블 정의", "열 · 자료형 · 제약조건", [("CREATE TABLE", "create_table")]),
    ("트랜잭션", "여러 변경을 확정하거나 취소", [("BEGIN · COMMIT · ROLLBACK", "transaction")]),
]
map_rows = "".join(
    f'<li><span class="map-group">{g}</span><span class="map-links">'
    + "".join(f'<a href="#{a}">{esc(t)}</a>' for t, a in links)
    + f'</span><span class="map-desc">{d}</span></li>'
    for g, d, links in MAP
)

# ── 조회 ─────────────────────────────────────────────────
hit = {r[0] for r in CAP["select"]["rows"]}
select_viz = mini(k_cols, k_rows, row_cls=["hit" if r[0] in hit else "dim" for r in k_rows],
                  render=by_category,
                  labels=["남음" if r[0] in hit else "" for r in k_rows],
                  caption=f"결과 {len(hit)}행")
join_viz = mini(CAP["join"]["cols"], CAP["join"]["rows"], render=by_category,
                caption=f"결과 {len(CAP['join']['rows'])}행 · 한 행 = 지식 한 건")
left_rows = CAP["left_join"]["rows"]
left_viz = mini(CAP["left_join"]["cols"], left_rows, render=by_category,
                row_cls=["nullrow" if r[1] is None else "" for r in left_rows],
                caption=f"결과 {len(left_rows)}행")
group_rows = CAP["group_by"]["rows"]
group_viz = mini(CAP["group_by"]["cols"], group_rows, render=by_category,
                 caption=f"결과 {len(group_rows)}행 · 한 행 = 분류 하나")

# ── 변경 ─────────────────────────────────────────────────
before_ids = {r[0] for r in K["rows"]}
ins = CAP["insert"]
new_id = ins["returning"]["rows"][0][0]
ins_rows = [[r[0], r[1], r[3]] for r in ins["after"]["rows"]]
insert_viz = mini(k_cols, ins_rows, render=by_category,
                  row_cls=["new" if r[0] not in before_ids else "" for r in ins_rows],
                  labels=["추가" if r[0] not in before_ids else "" for r in ins_rows],
                  caption=f"RETURNING id → {new_id}")

old_content = {r[0]: r[2] for r in K["rows"]}
upd_rows = [[r[0], r[2]] for r in CAP["update"]["after"]["rows"]]
changed = {r[0] for r in upd_rows if r[1] != old_content[r[0]]}


upd_body = []
for rid, content in upd_rows:
    if rid in changed:
        upd_body.append([rid, f'<del>{esc(old_content[rid])}</del><ins>{esc(content)}</ins>'])
    else:
        upd_body.append([rid, esc(content)])
update_viz = mini(["id", "content"], upd_body, render=lambda c, v: str(v),
                  row_cls=["chg" if r[0] in changed else "" for r in upd_rows],
                  labels=["수정" if r[0] in changed else "" for r in upd_rows],
                  caption=f"UPDATE {CAP['update']['rowcount']} · 바뀐 행 수")

after_ids = {r[0] for r in CAP["delete"]["after"]["rows"]}
del_rows = [[r[0], r[1]] for r in K["rows"]]
delete_viz = mini(["id", "title"], del_rows,
                  row_cls=["del" if r[0] not in after_ids else "" for r in del_rows],
                  labels=["삭제" if r[0] not in after_ids else "" for r in del_rows],
                  caption=f"DELETE {CAP['delete']['rowcount']} · 남은 행 {len(after_ids)}개")

# ── 테이블 정의 ──────────────────────────────────────────
assert CAP["create_table_ok"]
BADGE = lambda *names: " ".join(f'<span class="badge">{n}</span>' for n in names)
cols_table = f"""<table class="mini cols"><caption><code>knowledge</code>의 열</caption>
<thead><tr><th>열</th><th>자료형</th><th>제약조건</th></tr></thead><tbody>
<tr><td>id</td><td><code>BIGINT</code></td><td>{BADGE("PRIMARY KEY", "IDENTITY")}</td></tr>
<tr><td>title</td><td><code>VARCHAR(80)</code></td><td>{BADGE("NOT NULL", "CHECK 1~80자")}</td></tr>
<tr><td>content</td><td><code>TEXT</code></td><td>{BADGE("NOT NULL", "CHECK 1~2,000자")}</td></tr>
<tr><td>category_id</td><td><code>BIGINT</code></td><td>{BADGE("NOT NULL", "FOREIGN KEY")} → <code>categories.id</code></td></tr>
</tbody></table>"""
REJECT_TEXT = [
    ("not_null", "title에 NULL", "NOT NULL", "23502"),
    ("check", "content에 빈 문자열 <code>''</code>", "CHECK", "23514"),
    ("fk", "category_id에 없는 분류 99", "FOREIGN KEY", "23503"),
    ("unique", "분류 learning을 한 번 더 추가", "UNIQUE", "23505"),
    ("restrict", "지식이 있는 분류 learning 삭제", "ON DELETE RESTRICT", "23503"),
]
for key, _, _, state in REJECT_TEXT:
    assert CAP["reject"][key]["sqlstate"] == state, key
assert len(CAP["after_reject"]["rows"]) == len(K["rows"])
reject_list = "".join(
    f'<li><span class="x" aria-hidden="true">✕</span><span>{what}</span><span class="badge">{rule}</span></li>'
    for _, what, rule, _ in REJECT_TEXT
)
ddl_viz = f"""{cols_table}
<p class="sub"><code>categories</code>: id <code>BIGINT</code> {BADGE("PRIMARY KEY", "IDENTITY")} · name <code>VARCHAR(30)</code> {BADGE("NOT NULL", "UNIQUE")}</p>
<div class="reject"><p class="reject-title">이런 INSERT·DELETE는 거부됩니다</p><ul>{reject_list}</ul>
<p class="sub">거부된 뒤에도 knowledge는 {len(CAP["after_reject"]["rows"])}행 그대로</p></div>"""

# ── 트랜잭션 ─────────────────────────────────────────────
auto_rows = CAP["tx_autocommit"]["rows"]
roll_rows = CAP["tx_rollback"]["rows"]
base_cat = {r[0] for r in CAP["categories"]["rows"]}
assert len(auto_rows) == len(base_cat) + 1 and len(roll_rows) == len(base_cat)
cat_render = lambda c, v: (f'<span class="cat c{min(v, 4)}">{v}</span>' if c == "id" else esc(v))
auto_table = mini(["id", "name"], auto_rows, render=cat_render,
                  row_cls=["new" if r[0] not in base_cat else "" for r in auto_rows],
                  labels=["남음" if r[0] not in base_cat else "" for r in auto_rows],
                  caption=f"categories {len(auto_rows)}행 · 지식 없는 분류 api가 남음")
roll_table = mini(["id", "name"], roll_rows, render=cat_render,
                  caption=f"categories {len(roll_rows)}행 · 둘 다 취소")
tx_auto_sql = "-- ① 바로 확정\n" + SQL["tx_category"] + "\n-- ② CHECK 위반으로 실패\n" + SQL["tx_knowledge"]
tx_roll_sql = ("BEGIN;\n" + SQL["tx_category"] + "\n-- CHECK 위반으로 실패\n" + SQL["tx_knowledge"]
               + "\n-- 실패했으니 둘 다 취소\nROLLBACK;")
tx_viz = f"""<div class="tx">
  <div class="tx-col"><p class="tx-title">BEGIN 없이 (Auto commit)</p>{sql_html(tx_auto_sql)}{auto_table}</div>
  <div class="tx-col"><p class="tx-title">BEGIN으로 묶으면</p>{sql_html(tx_roll_sql)}{roll_table}</div>
</div>"""

CARDS_READ = "".join([
    card("select", "SELECT", "조건에 맞는 행 조회", sql_html(SQL["select"]), select_viz, [
        "<code>WHERE</code>에 맞는 행만 남고, <code>ORDER BY</code> 순서로 나옵니다. <code>LIMIT n</code>은 최대 n행입니다.",
        "읽는 순서: <code>FROM</code> → <code>WHERE</code> → <code>SELECT</code> → <code>ORDER BY</code>",
    ]),
    card("join", "JOIN", "두 테이블 연결", sql_html(SQL["join"]), join_viz, [
        "<code>ON</code>의 값이 같은 분류 행을 지식 행 옆에 붙입니다. <code>k</code>·<code>c</code>는 테이블 별칭입니다.",
    ]),
    card("left_join", "LEFT JOIN", "짝이 없는 행도 남기기", sql_html(SQL["left_join"]), left_viz, [
        "왼쪽(<code>categories</code>)의 행은 모두 남고, 짝이 없으면 <code>NULL</code>입니다.",
    ]),
    card("group_by", "GROUP BY", "분류별 집계", sql_html(SQL["group_by"]), group_viz, [
        "분류마다 한 행으로 묶어 셉니다.",
        "<code>COUNT(k.id)</code>는 NULL을 세지 않아 빈 분류가 0입니다. <code>COUNT(*)</code>를 쓰면 reference가 1로 나옵니다.",
    ]),
])
CARDS_WRITE = "".join([
    card("insert", "INSERT", "행 추가", sql_html(SQL["insert"]), insert_viz, [
        "<code>id</code>는 넣지 않습니다. DB가 발급한 번호를 <code>RETURNING</code>으로 받습니다.",
    ]),
    card("update", "UPDATE", "행 수정", sql_html(SQL["update"]), update_viz, [
        "<code>SET</code>은 바꿀 값, <code>WHERE</code>는 대상입니다. <strong>WHERE를 빼면 모든 행이 바뀝니다.</strong>",
    ]),
    card("delete", "DELETE", "행 삭제", sql_html(SQL["delete"]), delete_viz, [
        "행만 지우고 테이블은 남습니다. <strong>WHERE를 빼면 모든 행이 지워집니다.</strong>",
    ]),
])
CARD_DDL = card("create_table", "CREATE TABLE", "테이블 구조와 제약조건", sql_html(SQL["create_table"]), ddl_viz, [
    "규칙은 <code>CREATE TABLE</code>에서 정하고, DB가 INSERT·UPDATE·DELETE 때마다 검사합니다.",
    "부모 테이블(<code>categories</code>)을 먼저 만듭니다. 관계는 categories 1 : N knowledge입니다.",
], wide=True)
CARD_TX = card("transaction", "BEGIN · COMMIT · ROLLBACK", "여러 변경을 하나로", "", tx_viz, [
    "함께 성공해야 하는 변경은 <code>BEGIN</code>으로 묶습니다. 모두 성공하면 <code>COMMIT</code>, 하나라도 실패하면 <code>ROLLBACK</code>합니다.",
    "pgAdmin Query Tool은 Auto commit이 기본입니다. BEGIN 없이 실행한 문장은 바로 확정됩니다.",
    "내일 FastAPI 코드에서는 성공하면 <code>db.commit()</code>, 예외가 나면 <code>db.rollback()</code>을 호출합니다.",
], wide=True)

SUMMARY = [
    ("PRIMARY KEY", "행을 구분합니다", "<code>WHERE id = 2</code> — 조회·수정·삭제할 행 하나를 정확히 고름"),
    ("FOREIGN KEY", "부모에 있는 값만 받습니다", "<code>JOIN … ON c.id = k.category_id</code> — 조회할 때 그 값으로 연결"),
    ("제약조건", "잘못된 값을 거부합니다", "INSERT·UPDATE가 실패해도 기존 데이터는 그대로"),
    ("트랜잭션", "여러 변경을 하나로 묶습니다", "<code>COMMIT</code>으로 확정, <code>ROLLBACK</code>으로 취소"),
]
summary_rows = "".join(
    f'<li><span class="badge strong">{a}</span><span class="sum-what">{b}</span><span class="sum-where">{c}</span></li>'
    for a, b, c in SUMMARY
)

MORE = [
    ("HAVING", "<code>GROUP BY … HAVING COUNT(k.id) &gt;= 2</code> — 묶은 뒤의 그룹을 거릅니다. 묶기 전의 행을 거르는 것은 WHERE입니다."),
    ("SUM · MIN · MAX", "<code>SUM(char_length(content))</code>처럼 합계·최솟값·최댓값을 구하는 집계 함수입니다."),
    ("LIKE", "<code>title LIKE '%실습%'</code> — '실습'이 들어간 값. <code>%</code>는 아무 글자 0자 이상입니다."),
    ("NULL과 빈 문자열", "NULL은 값이 없는 상태, <code>''</code>는 길이 0인 값입니다. NULL은 <code>IS NULL</code>로 확인합니다."),
    ("INDEX · EXPLAIN", "<code>CREATE INDEX</code>는 행을 빨리 찾는 구조를 만들고, <code>EXPLAIN</code>은 DB가 행을 찾는 방법을 보여 줍니다. 행이 3개뿐이면 인덱스가 있어도 전부 읽는 <code>Seq Scan</code>이 정상입니다."),
    ("번호 건너뜀", "ROLLBACK하거나 INSERT가 실패해도 발급된 IDENTITY 번호는 돌아오지 않습니다. 다음 번호를 예상하지 말고 RETURNING으로 확인합니다."),
    ("SQL과 HTTP", "SQL은 행과 오류만 돌려줍니다. 200·404 같은 상태코드는 API가 정합니다."),
]
more_rows = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in MORE)

PAGE = (HERE / "template.html").read_text(encoding="utf-8")
for name, value in {
    "CAT_TABLE": cat_table, "KNOW_TABLE": know_table, "MAP": map_rows,
    "CARDS_READ": CARDS_READ, "CARDS_WRITE": CARDS_WRITE, "CARD_DDL": CARD_DDL, "CARD_TX": CARD_TX,
    "SUMMARY": summary_rows, "MORE": more_rows, "VERSION": esc(CAP["version"].split()[0]),
}.items():
    assert "{{" + name + "}}" in PAGE, name
    PAGE = PAGE.replace("{{" + name + "}}", value)
assert "{{" not in PAGE
(HERE / "index.html").write_text(PAGE, encoding="utf-8")
print("index.html", len(PAGE), "bytes")
