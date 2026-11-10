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
MAKE = (HERE / "code" / "make_data.py").read_text(encoding="utf-8")
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


def json_view(rec, new_ids=()):
    """주소창으로 연 JSON 화면. 목록은 항목마다 한 줄, 그 밖은 들여쓰기."""
    value = json.loads(rec["text"])
    if isinstance(value, list):
        rows = [{"text": "  " + json.dumps(e, ensure_ascii=False) + ",", "new": e["id"] in new_ids} for e in value]
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
expect(json.loads(CAP["get_2"]["text"])["title"] == "서버 실행", "get_2")
expect(CAP["get_foo"]["status"] == 422 and "int_parsing" in CAP["get_foo"]["text"], "get_foo")
expect(ids(CAP["list_before"]) == [1, 2, 3] and ids(CAP["list_after"]) == [1, 2, 3, 4], "post list")
expect(CAP["post"]["status"] == "201" and CAP["post"]["file"] == {"ids": [1, 2, 3, 4], "next_id": 5}, "post")
expect(CAP["no_title"]["status"] == "422" and ids(CAP["list_after_no_title"]) == [1, 2, 3, 4], "no_title")
expect(CAP["nw_post"]["status"] == "201" and CAP["nw_get_4"]["status"] == 404, "no_write")
expect(ids(CAP["nw_list"]) == [1, 2, 3] and CAP["nw_post"]["file"]["ids"] == [1, 2, 3], "no_write list")
print("기록과 기대값 대조: 모두 일치")

seed = {"next_id": 4, "entries": [
    {"id": 1, "title": "가상환경", "category": "setup", "content": "프로젝트별 패키지를 분리한다."},
    {"id": 2, "title": "서버 실행", "category": "api", "content": "uvicorn으로 개발 서버를 켠다."},
    {"id": 3, "title": "입력 오류", "category": "api", "content": "422이면 입력값을 확인한다."}]}
seed_text = json.dumps(seed, ensure_ascii=False, indent=2)
write_line = find_line(MAIN, "write_data(data)", find_line(MAIN, "def create_knowledge"))
get_span = span(MAIN, "@app.get(\"/api/knowledge/{knowledge_id}\")", "return data[\"entries\"][index]")

steps = [
    {
        "id": "intro", "period": "시작", "title": "전체 구조", "kind": "intro",
        "task": "오늘 만드는 것: 브라우저의 요청을 받아 지식을 읽고·만들고·바꾸고·지우는 작은 서버",
        "doc": ("First Steps", DOC + "first-steps/"),
    },
    {
        "id": "start", "period": "1교시", "title": "서버 실행", "endpoint": "python -m uvicorn main:app --reload",
        "task": "main.py의 app을 Uvicorn으로 켜고, 브라우저에서 /docs를 연다",
        "success": "터미널에 'Application startup complete.', /docs에 경로 6개",
        "words": [["/docs", "FastAPI가 코드를 보고 자동으로 만든 문서. 여기서 요청도 보낼 수 있다"]],
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "app = FastAPI(", "return {\"status\": \"ok\"}"),
                 "mark": [find_line(MAIN, "app = FastAPI(")]},
        "terminal": {"title": "터미널 · 서버", "lines": ["$ python -m uvicorn main:app --reload", *CAP["start"]["server_log"]]},
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
                 "mark": [find_line(MAIN, "@app.get(\"/health\")")]},
        "views": [json_view(CAP["health"])],
        "server": server_line(CAP["health"]),
        "why": "주소창에 /health를 넣으면 @app.get(\"/health\") 바로 아래 함수가 실행됩니다. 함수가 돌려준 {\"status\": \"ok\"}가 그대로 화면에 나옵니다.",
        "doc": ("First Steps", DOC + "first-steps/"),
    },
    {
        "id": "get2", "period": "2교시", "title": "Path Parameter", "endpoint": "GET /api/knowledge/{knowledge_id}",
        "task": "주소 끝의 숫자로 지식 한 건을 찾는다",
        "success": "id 2, 제목 '서버 실행'",
        "words": [["Path Parameter", "주소 안에 들어간 값. /api/knowledge/2의 2"]],
        "code": {"file": "main.py", "source": MAIN, "focus": get_span,
                 "mark": [find_line(MAIN, "def get_knowledge(knowledge_id: int):")]},
        "views": [json_view(CAP["get_2"])],
        "server": server_line(CAP["get_2"]),
        "why": "주소 끝의 2가 knowledge_id에 들어갑니다. int라고 적어 두었기 때문에 글자 \"2\"가 아니라 숫자 2로 들어와서, 파일의 id 2와 맞춰 볼 수 있습니다.",
        "doc": ("Path Parameters", DOC + "path-params/"),
    },
    {
        "id": "getfoo", "period": "2교시", "title": "Validation", "endpoint": "GET /api/knowledge/foo",
        "task": "숫자 대신 foo를 넣으면 어떻게 되는지 본다",
        "success": "상태코드 422와 int_parsing 오류",
        "words": [["Validation", "보낸 값이 선언한 타입·규칙에 맞는지 FastAPI가 먼저 검사하는 것"], ["422", "검사를 통과하지 못해 거절됨"]],
        "code": {"file": "main.py", "source": MAIN, "focus": get_span,
                 "mark": [find_line(MAIN, "def get_knowledge(knowledge_id: int):")]},
        "views": [json_view(CAP["get_foo"])],
        "server": server_line(CAP["get_foo"]),
        "why": "knowledge_id는 숫자여야 하는데 foo가 들어왔습니다. 그래서 FastAPI가 함수를 실행하기 전에 422로 돌려보냅니다.",
        "doc": ("Path Parameters", DOC + "path-params/#data-validation"),
    },
    {
        "id": "post", "period": "3교시", "title": "Request Body", "endpoint": "POST /api/knowledge",
        "task": "/docs에서 내용을 보내 지식을 하나 등록한다",
        "success": "Code 201, 목록이 3건 → 4건",
        "words": [["Request Body", "새로 저장할 내용을 담아 보내는 JSON"], ["201", "새로 만들어졌다는 상태코드"]],
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "@app.post(", "    return entry"),
                 "mark": [find_line(MAIN, "entry[\"id\"] = data[\"next_id\"]"), write_line]},
        "views": [docs_view(CAP["post"], "POST /api/knowledge → Try it out → Execute")],
        "server": server_line(CAP["post"]),
        "result": {"label": "주소창에 /api/knowledge", "change": "3건 → 4건",
                   "view": json_view(CAP["list_after"], new_ids={4})},
        "why": "보낼 때 id는 넣지 않습니다. 서버가 파일에 적힌 다음 번호(next_id)를 붙이고, write_data(data)가 파일에 저장합니다.",
        "doc": ("Request Body", DOC + "body/"),
        "variant": {
            "label": "write_data(data) 줄을 지우면",
            "remove_line": write_line,
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
        "code": {"file": "main.py", "source": MAIN, "focus": span(MAIN, "class KnowledgeWrite", "category: str = Field("),
                 "mark": [find_line(MAIN, "title: str = Field(")]},
        "views": [docs_view(CAP["no_title"], "Body에서 title 줄을 지우고 Execute")],
        "server": server_line(CAP["no_title"]),
        "result": {"label": "주소창에 /api/knowledge", "change": "4건 그대로",
                   "view": json_view(CAP["list_after_no_title"])},
        "why": "title은 꼭 보내야 하는 값인데 빠져 있습니다. 그래서 FastAPI가 요청을 받자마자 422로 돌려보내고, 아래 등록 코드는 실행되지 않습니다. 목록이 4건 그대로인 이유입니다.",
        "doc": ("Request Body", DOC + "body/"),
        "recap": [["200", "성공"], ["201", "새로 만들어짐"], ["422", "보낸 값의 형식이 틀림"]],
    },
]

template = (HERE / "template.html").read_text(encoding="utf-8")
data = json.dumps(steps, ensure_ascii=False).replace("</", "<\\/")
out = template.replace("/*__STEPS__*/[]", data)
(HERE / "index.html").write_text(out, encoding="utf-8")
print("index.html", round(len(out) / 1024), "KB")
