# 단계 정의 + 실제 실행 기록(capture/capture.json, capture/shots/) → index.html
# 사용: python3 build.py   (기록을 새로 만들 때: cd capture && uv run capture.py ../code capture.json)
# 원칙: 한 단계에서 볼 곳은 코드 하나, 브라우저 하나. 용어는 처음 나올 때 1~2개만.
import base64
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAP_DIR = HERE / "capture"
CAP = json.loads((CAP_DIR / "capture.json").read_text(encoding="utf-8"))
MAIN = (HERE / "code" / "main.py").read_text(encoding="utf-8")
DOC = "https://fastapi.tiangolo.com/tutorial/"
URL = "http://127.0.0.1:8000"

# 브라우저가 탭 아이콘을 스스로 찾는 요청(favicon.ico)은 데모와 관계없어 로그에서 뺀다
for rec in CAP.values():
    if "server_log" in rec:
        rec["server_log"] = [l for l in rec["server_log"] if "favicon.ico" not in l]


def find_line(source, part, after=1):
    """after 줄 이후에서 part가 들어 있는 첫 줄의 번호."""
    rows = source.splitlines()
    return next(i for i, r in enumerate(rows, 1) if i >= after and part in r)


def span(source, start_part, end_part):
    start = find_line(source, start_part)
    return [start, find_line(source, end_part, start)]


def image(rel):
    data = (CAP_DIR / rel).read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode()


def json_view(rec, tags=None):
    """주소창으로 연 JSON 화면. 목록은 항목마다 한 줄, 그 밖은 들여쓰기. tags={id: "새로 생김"}"""
    tags = tags or {}
    value = json.loads(rec["text"])
    if isinstance(value, list):
        rows = [{"text": "  " + json.dumps(e, ensure_ascii=False) + ",", "tag": tags.get(e["id"])} for e in value]
        rows[-1]["text"] = rows[-1]["text"].rstrip(",")
        lines = [{"text": "["}, *rows, {"text": "]"}]
    else:
        lines = [{"text": l} for l in json.dumps(value, ensure_ascii=False, indent=2).split("\n")]
    return {"kind": "json", "url": rec["url"], "status": rec["status"], "lines": lines}


def docs_view(rec, caption, with_input=True):
    view = {"kind": "docs", "url": URL + "/docs", "caption": caption, "response": image(rec["shot_response"])}
    if with_input:
        view["input"] = image(rec["shot_input"])
    return view


def server_line(rec):
    """그 요청 때 서버 터미널에 찍힌 줄 그대로."""
    return rec["server_log"]


def ids(rec):
    return [e["id"] for e in json.loads(rec["text"])]


def expect(condition, message):
    assert condition, message


# ── 기록과 기대값 대조 (화면에는 보이지 않음) ──
expect(CAP["health"]["status"] == 200 and json.loads(CAP["health"]["text"]) == {"status": "ok"}, "health")
expect(ids(CAP["list_before"]) == [1, 2, 3], "list_before")
expect(json.loads(CAP["get_2"]["text"])["title"] == "서버 실행", "get_2")
expect(CAP["get_9999"]["status"] == 404 and "Knowledge not found" in CAP["get_9999"]["text"], "get_9999")
expect(CAP["get_foo"]["status"] == 422 and "int_parsing" in CAP["get_foo"]["text"], "get_foo")
expect(CAP["post"]["status"] == "201" and CAP["post"]["file"] == {"ids": [1, 2, 3, 4], "next_id": 5}, "post")
expect(ids(CAP["list_after"]) == [1, 2, 3, 4], "list_after")
expect(CAP["no_title"]["status"] == "422" and CAP["no_title"]["file"] == {"ids": [1, 2, 3, 4], "next_id": 5}, "no_title")
expect(CAP["put"]["status"] == "200" and CAP["put"]["file"] == {"ids": [1, 2, 3, 4], "next_id": 5}, "put")
expect(json.loads(CAP["put"]["response_body"])["id"] == 2, "put id")
expect(CAP["delete"]["status"] == "204" and CAP["delete"]["response_body"] == "", "delete")
expect(CAP["delete"]["file"] == {"ids": [1, 2, 4], "next_id": 5}, "delete file")
expect(CAP["get_3_after_delete"]["status"] == 404, "get_3 after delete")
expect(ids(CAP["list_restart"]) == [1, 2, 4] and CAP["get_3_restart"]["status"] == 404, "restart")
expect(json.loads(CAP["list_restart"]["text"])[1]["content"].startswith("python -m uvicorn"), "restart keeps put")
expect(CAP["nw_post"]["status"] == "201" and CAP["nw_get_4"]["status"] == 404, "no_write")
expect(ids(CAP["nw_list"]) == [1, 2, 3] and CAP["nw_post"]["file"]["ids"] == [1, 2, 3], "no_write list")
print("기록과 기대값 대조: 모두 일치")


def L(part, after=1):
    return find_line(MAIN, part, after)


create_at, update_at, delete_at = L("def create_knowledge"), L("def update_knowledge"), L("def delete_knowledge")
write_create = L("write_data(data)", create_at)
write_update = L("write_data(data)", update_at)
write_delete = L("write_data(data)", delete_at)
get_span = span(MAIN, "def find_entry", "return find_entry(read_data(), knowledge_id)")
RUN = "python -m uvicorn main:app --reload"

steps = [
    {
        "id": "intro", "period": "시작", "title": "전체 구조", "kind": "intro",
        "task": "오늘 만드는 것: 브라우저의 요청을 받아 지식을 읽고·만들고·바꾸고·지우는 작은 서버",
        "roles": [["주소 연결", "@app.get(\"/health\")"], ["입력 검사", "knowledge_id: int · Knowledge"], ["저장", "write_data(data)"]],
        "doc": ("First Steps", DOC + "first-steps/"),
    },
    {
        "id": "start", "period": "1교시", "title": "서버 실행", "endpoint": RUN,
        "task": "main.py의 app을 Uvicorn으로 켜고, 브라우저에서 /docs를 연다",
        "success": "터미널에 'Application startup complete.', /docs에 경로 6개",
        "words": [["/docs", "FastAPI가 코드를 보고 자동으로 만든 문서. 여기서 요청도 보낼 수 있다"]],
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "app = FastAPI(", "return {\"status\": \"ok\"}"),
                 "mark": [L("app = FastAPI(")]},
        "terminal": {"title": "터미널 · 서버", "lines": ["$ " + RUN, *CAP["start"]["server_log"]]},
        "views": [{"kind": "shot", "url": URL + "/docs", "img": image(CAP["docs_home"]["shot"])}],
        "why": "main:app은 main.py 파일에 있는 app을 실행하라는 뜻입니다. 서버는 Ctrl+C로 끌 때까지 계속 요청을 기다립니다.",
        "doc": ("First Steps", DOC + "first-steps/"),
    },
    {
        "id": "health", "period": "1교시", "title": "Endpoint", "endpoint": "GET /health",
        "task": "주소창에 /health를 넣어 서버가 답하는지 본다",
        "success": "{\"status\":\"ok\"}와 상태코드 200",
        "words": [["Endpoint", "요청을 받는 주소 하나. Method와 Path로 정해진다"], ["200", "요청이 성공했다는 상태코드"]],
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "@app.get(\"/health\")", "return {\"status\": \"ok\"}"),
                 "mark": [L("@app.get(\"/health\")")]},
        "views": [json_view(CAP["health"])],
        "server": server_line(CAP["health"]),
        "why": "주소창에 /health를 넣으면 @app.get(\"/health\") 바로 아래 함수가 실행됩니다. 함수가 돌려준 {\"status\": \"ok\"}가 그대로 화면에 나옵니다.",
        "doc": ("First Steps", DOC + "first-steps/"),
    },
    {
        "id": "list", "period": "2교시", "title": "JSON Response", "endpoint": "GET /api/knowledge",
        "task": "주소창에 /api/knowledge를 넣어 저장된 지식 목록을 본다",
        "success": "지식 3건이 담긴 배열",
        "words": [["JSON Response", "함수가 돌려준 dict·list를 FastAPI가 JSON 글자로 바꿔 보낸 것"]],
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "@app.get(\"/api/knowledge\")", "return read_data()[\"entries\"]"),
                 "mark": [L("return read_data()[\"entries\"]")]},
        "views": [json_view(CAP["list_before"])],
        "server": server_line(CAP["list_before"]),
        "why": "read_data()가 knowledge.json 파일을 읽어 옵니다. 파일에는 next_id도 들어 있지만 [\"entries\"]만 돌려주기 때문에 화면에는 지식 목록만 나옵니다.",
        "doc": ("First Steps", DOC + "first-steps/#step-4-return-the-content"),
    },
    {
        "id": "get2", "period": "2교시", "title": "Path Parameter", "endpoint": "GET /api/knowledge/{knowledge_id}",
        "task": "주소 끝의 숫자로 지식 한 건을 찾는다",
        "success": "id 2, 제목 '서버 실행'",
        "words": [["Path Parameter", "주소 안에 들어간 값. /api/knowledge/2의 2"]],
        "code": {"file": "main.py", "source": MAIN, "focus": get_span,
                 "mark": [L("if entry[\"id\"] == knowledge_id:"), L("def get_knowledge(knowledge_id: int):")]},
        "views": [json_view(CAP["get_2"])],
        "server": server_line(CAP["get_2"]),
        "why": "주소 끝의 2가 knowledge_id에 들어갑니다. int라고 적어 두었기 때문에 숫자 2로 들어옵니다. find_entry가 목록을 하나씩 보면서 id가 2인 지식을 찾아 돌려줍니다.",
        "doc": ("Path Parameters", DOC + "path-params/"),
    },
    {
        "id": "get9999", "period": "2교시", "title": "HTTPException", "endpoint": "GET /api/knowledge/9999",
        "task": "없는 번호를 넣으면 어떤 답이 오는지 본다",
        "success": "상태코드 404와 Knowledge not found",
        "words": [["HTTPException", "오류 응답을 보내는 FastAPI 도구. return이 아니라 raise로 쓴다"], ["404", "찾는 것이 없다는 상태코드"]],
        "code": {"file": "main.py", "source": MAIN, "focus": get_span, "mark": [L("raise HTTPException")]},
        "views": [json_view(CAP["get_9999"])],
        "server": server_line(CAP["get_9999"]),
        "why": "9999번 지식은 없어서 반복문이 끝까지 돌고 raise 줄에 닿습니다. raise HTTPException이 함수를 멈추고 404와 detail 문구를 돌려줍니다.",
        "doc": ("Handling Errors", DOC + "handling-errors/"),
    },
    {
        "id": "getfoo", "period": "2교시", "title": "Validation", "endpoint": "GET /api/knowledge/foo",
        "task": "숫자 대신 foo를 넣으면 어떻게 되는지 본다",
        "success": "상태코드 422와 int_parsing 오류",
        "words": [["Validation", "보낸 값이 선언한 타입·규칙에 맞는지 FastAPI가 먼저 검사하는 것"], ["422", "검사를 통과하지 못해 거절됨"]],
        "code": {"file": "main.py", "source": MAIN, "focus": get_span,
                 "mark": [L("def get_knowledge(knowledge_id: int):")]},
        "views": [json_view(CAP["get_foo"])],
        "server": server_line(CAP["get_foo"]),
        "why": "knowledge_id는 숫자여야 하는데 foo가 들어왔습니다. 그래서 FastAPI가 함수를 실행하기 전에 422로 돌려보냅니다. 404는 내 코드가 보냈지만, 422는 FastAPI가 알아서 보냅니다.",
        "doc": ("Path Parameters", DOC + "path-params/#data-validation"),
    },
    {
        "id": "post", "period": "3교시", "title": "Request Body", "endpoint": "POST /api/knowledge",
        "task": "/docs에서 내용을 보내 지식을 하나 등록한다",
        "success": "Code 201, 목록이 3건 → 4건",
        "words": [["Request Body", "새로 저장할 내용을 담아 보내는 JSON"], ["201", "새로 만들어졌다는 상태코드"]],
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "class Knowledge", "    return entry"),
                 "mark": [L("def create_knowledge(knowledge: Knowledge):"), L("entry = {\"id\": data[\"next_id\"]"), write_create]},
        "views": [docs_view(CAP["post"], "POST /api/knowledge → Try it out → Execute")],
        "server": server_line(CAP["post"]),
        "result": {"label": "주소창에 /api/knowledge", "change": "3건 → 4건",
                   "view": json_view(CAP["list_after"], {4: "새로 생김"})},
        "why": "knowledge: Knowledge처럼 모델로 받으면 FastAPI가 보낸 JSON을 Body에서 읽어 옵니다. 보낼 때 id는 넣지 않습니다. 서버가 next_id로 번호를 붙이고, write_data(data)가 파일에 저장합니다.",
        "doc": ("Request Body", DOC + "body/"),
        "variant": {
            "label": "write_data(data) 줄을 지우면",
            "remove_line": write_create,
            "success": "Code는 그대로 201인데 목록은 3건 그대로",
            "views": [docs_view(CAP["nw_post"], "같은 내용으로 Execute", with_input=False)],
            "server": server_line(CAP["nw_post"]),
            "result": {"label": "주소창에 /api/knowledge/4", "change": "404, 저장되지 않음",
                       "view": json_view(CAP["nw_get_4"])},
            "why": "응답은 201로 성공처럼 보이지만, 저장하는 줄이 없어서 파일에는 남지 않았습니다. 그래서 등록한 뒤에는 목록을 다시 열어 확인합니다.",
        },
    },
    {
        "id": "notitle", "period": "3교시", "title": "Required Field", "endpoint": "POST /api/knowledge  (title 없이)",
        "task": "title을 빼고 보내면 저장 전에 막히는지 본다",
        "success": "Code 422, 목록은 4건 그대로",
        "words": [["Required Field", "기본값이 없어 꼭 보내야 하는 값. 빠지면 422"]],
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "class Knowledge", "category: str = Field("),
                 "mark": [L("title: str = Field(")]},
        "views": [docs_view(CAP["no_title"], "Body에서 title 줄을 지우고 Execute")],
        "server": server_line(CAP["no_title"]),
        "result": {"label": "주소창에 /api/knowledge", "change": "4건 그대로",
                   "view": json_view(CAP["list_after_no_title"])},
        "why": "title은 꼭 보내야 하는 값인데 빠져 있습니다. 그래서 FastAPI가 요청을 받자마자 422로 돌려보내고, create_knowledge는 실행되지 않습니다. 목록이 4건 그대로인 이유입니다.",
        "doc": ("Request Body", DOC + "body/"),
    },
    {
        "id": "put", "period": "4교시", "title": "PUT", "endpoint": "PUT /api/knowledge/{knowledge_id}",
        "task": "/docs에서 2번 지식의 content를 바꾼다",
        "success": "Code 200, id 2 그대로, 목록 4건 그대로",
        "words": [["PUT", "있는 것을 통째로 바꾸는 요청. 세 값을 모두 보낸다"]],
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "@app.put(", "    return entry"),
                 "mark": [L("entry = find_entry(data, knowledge_id)", update_at), L("entry.update("), write_update]},
        "views": [docs_view(CAP["put"], "PUT /api/knowledge/{knowledge_id} → Try it out → 2 입력 → Execute")],
        "server": server_line(CAP["put"]),
        "result": {"label": "주소창에 /api/knowledge", "change": "2번만 바뀜, 4건 그대로",
                   "view": json_view(CAP["list_after_put"], {2: "바뀜"})},
        "why": "주소의 2로 바꿀 지식을 찾고, Body로 받은 세 값으로 덮어씁니다. 보낸 값에 id가 없어서 id 2는 그대로 남습니다. write_data(data)가 저장하므로 목록을 다시 열어도 바뀐 내용이 보입니다.",
        "doc": ("Body - Updates", DOC + "body-updates/"),
    },
    {
        "id": "delete", "period": "5교시", "title": "DELETE · 204", "endpoint": "DELETE /api/knowledge/{knowledge_id}",
        "task": "/docs에서 3번 지식을 지운다",
        "success": "Code 204, Response body 없음. /api/knowledge/3은 404",
        "words": [["204", "처리했고 돌려줄 내용은 없다는 상태코드"]],
        "code": {"file": "main.py", "source": MAIN, "focus": [L("@app.delete("), write_delete],
                 "mark": [L("@app.delete("), L("data[\"entries\"].remove("), write_delete]},
        "views": [docs_view(CAP["delete"], "DELETE /api/knowledge/{knowledge_id} → Try it out → 3 입력 → Execute")],
        "server": server_line(CAP["delete"]),
        "result": {"label": "주소창에 /api/knowledge/3", "change": "404, 지워짐",
                   "view": json_view(CAP["get_3_after_delete"])},
        "why": "find_entry로 찾은 지식 하나만 목록에서 빼고 저장합니다. status_code=204는 '처리했고 돌려줄 내용은 없다'는 뜻이라 return을 쓰지 않습니다. 다시 열면 없는 번호라서 404가 나옵니다.",
        "doc": ("Response Status Code", DOC + "response-status-code/"),
    },
    {
        "id": "persist", "period": "완성", "title": "Persistence", "endpoint": "Ctrl+C → " + RUN,
        "task": "서버를 껐다 다시 켜고, 지금까지 바꾼 내용이 남아 있는지 본다",
        "success": "4번 추가 · 2번 수정 · 3번 삭제가 그대로",
        "words": [["Persistence", "서버를 껐다 켜도 데이터가 남는 것"]],
        "code": {"file": "main.py", "source": MAIN, "focus": [1, len(MAIN.splitlines())],
                 "mark": [write_create, write_update, write_delete]},
        "terminal": {"title": "터미널 · 서버", "lines": [
            "^C", *CAP["stop"]["server_log"], "$ " + RUN, *CAP["restart"]["server_log"],
            *CAP["list_restart"]["server_log"]]},
        "views": [json_view(CAP["list_restart"], {2: "바뀜", 4: "새로 생김"})],
        "why": "서버를 껐다 켜도 목록이 그대로입니다. 요청마다 read_data()가 파일을 읽고, 바꿀 때마다 write_data(data)가 파일에 저장하기 때문입니다. 이것으로 지식 관리 API가 완성됐습니다.",
        "doc": ("Tutorial - User Guide", DOC),
        "recap": [["200", "성공"], ["201", "새로 만들어짐"], ["204", "처리함, 본문 없음"], ["404", "찾는 것이 없음"], ["422", "보낸 값의 형식이 틀림"]],
    },
]

template = (HERE / "template.html").read_text(encoding="utf-8")
data = json.dumps(steps, ensure_ascii=False).replace("</", "<\\/")
out = template.replace("/*__STEPS__*/[]", data)
(HERE / "index.html").write_text(out, encoding="utf-8")
print("index.html", round(len(out) / 1024), "KB")
