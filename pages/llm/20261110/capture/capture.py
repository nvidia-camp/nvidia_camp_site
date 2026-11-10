# /// script
# dependencies = ["playwright", "fastapi", "uvicorn[standard]", "httpx"]
# ///
# 실제 서버를 띄우고, 학생이 보는 브라우저 화면(/docs·JSON)과 서버 로그를 단계별로 기록한다
# 사용: cd capture && uv run capture.py ../code capture.json   (8000 포트를 비워 두고, Chrome 필요)
import base64, json, os, shutil, signal, subprocess, sys, tempfile, threading, time
from pathlib import Path
from playwright.sync_api import sync_playwright

SRC = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2]).resolve(); SHOTS = OUT.parent / "shots"
SHOTS.mkdir(exist_ok=True)
URL = "http://127.0.0.1:8000"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


import atexit
RUNNING = []


@atexit.register
def _cleanup():
    for proc in RUNNING:
        if proc.poll() is None:
            proc.send_signal(signal.SIGINT)
            proc.wait(timeout=10)


class Server:
    def __init__(self, cwd):
        self.cwd, self.lines = cwd, []

    def start(self):
        self.p = subprocess.Popen([sys.executable, "-m", "uvicorn", "main:app", "--reload"], cwd=self.cwd,
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                  env={**os.environ, "PYTHONUNBUFFERED": "1"})
        RUNNING.append(self.p)
        threading.Thread(target=self._read, daemon=True).start()
        mark = len(self.lines)
        self.wait("Application startup complete")
        return self.clean(self.lines[mark:])

    def _read(self):
        for line in self.p.stdout:
            self.lines.append(line.rstrip("\n"))

    def wait(self, text, timeout=20):
        end = time.time() + timeout
        while time.time() < end:
            if any(text in l for l in self.lines):
                return
            time.sleep(0.05)
        raise RuntimeError(text)

    def clean(self, lines):
        out = []
        for l in lines:
            for prefix in (str(self.cwd.resolve()), str(self.cwd)):
                l = l.replace(prefix, "~/fastapi_knowledge")
            out.append(l)
        return out

    def stop(self):
        mark = len(self.lines)
        self.p.send_signal(signal.SIGINT); self.p.wait(timeout=15); time.sleep(0.2)
        return self.clean(self.lines[mark:])


def project(variant=None):
    root = Path(tempfile.mkdtemp(prefix="cap_")) / "fastapi_knowledge"
    root.mkdir()
    for f in ("main.py", "storage.py", "make_data.py"):
        shutil.copy(SRC / f, root / f)
    if variant:
        text = (root / "main.py").read_text(encoding="utf-8")
        assert text.count(variant[0]) == 1
        (root / "main.py").write_text(text.replace(*variant), encoding="utf-8")
    subprocess.run([sys.executable, "make_data.py"], cwd=root, check=True, capture_output=True)
    return root


def state(root):
    d = json.loads((root / "data" / "knowledge.json").read_text(encoding="utf-8"))
    return {"ids": [e["id"] for e in d["entries"]], "next_id": d["next_id"]}


def shot(locator, name):
    path = SHOTS / f"{name}.png"
    locator.screenshot(path=str(path))
    return f"shots/{path.name}"


def visit(page, server, path, name):
    """주소창에 URL을 넣었을 때: 화면 글자 + 실제 화면 캡처 + 서버 로그"""
    mark = len(server.lines)
    resp = page.goto(URL + path)
    time.sleep(0.4)
    raw = page.locator("pre").first.inner_text()
    box = page.locator("input[type=checkbox]")
    pretty = None
    if box.count():
        box.first.check()
        time.sleep(0.3)
        pretty = page.locator("body").inner_text()
    return {"url": URL + path, "status": resp.status, "text": raw, "pretty": pretty,
            "shot": shot(page.locator("body"), name), "server_log": server.clean(server.lines[mark:])}


def response_shot(page, live, name):
    """Server response 중 Code와 Response body까지만 자른다 (Response headers 제외)."""
    top = live.bounding_box()
    body = live.locator(".response-col_description div:has(> h5:text-is(\"Response body\")) pre")
    target = body.first if body.count() else live.locator("tbody .response-col_status").first
    body_box = target.bounding_box()
    scroll_y = page.evaluate("window.scrollY")
    clip = {"x": top["x"], "y": top["y"] + scroll_y, "width": top["width"],
            "height": body_box["y"] + body_box["height"] - top["y"] + 6}
    path = SHOTS / f"{name}_response.png"
    page.screenshot(path=str(path), clip=clip, full_page=True)
    return f"shots/{path.name}"


def docs_execute(page, server, op_id, body, name, path_param=None):
    """/docs에서 해당 경로를 펼치고 Try it out → (값 입력) → Execute"""
    page.goto(URL + "/docs")
    page.wait_for_selector(f"#{op_id}")
    block = page.locator(f"#{op_id}")
    block.locator(".opblock-summary").first.click()
    block.locator(".try-out__btn").click()
    if path_param is not None:
        block.locator("input[placeholder='knowledge_id']").fill(str(path_param))
    if body is not None:
        area = block.locator("textarea.body-param__text")
        area.fill(body)
        area.evaluate("el => { el.style.height = '8.5em'; el.style.minHeight = '0'; }")
    mark = len(server.lines)
    block.locator(".execute").click()
    block.locator(".live-responses-table").wait_for()
    time.sleep(0.5)
    live = block.locator(".live-responses-table")
    code = live.locator("tbody .response-col_status").first.inner_text().strip()
    body_el = live.locator(".response-col_description div:has(> h5:text-is(\"Response body\")) pre")
    resp_body = body_el.first.inner_text() if body_el.count() else ""
    # 입력 영역: 매개변수/Request body 시작부터 Execute 버튼까지
    first = block.locator(".opblock-section-request-body" if path_param is None else ".parameters-container").first
    top = first.bounding_box()
    bottom = block.locator("button.execute").first.bounding_box()
    scroll_y = page.evaluate("window.scrollY")
    page_box = {"x": top["x"], "y": top["y"] + scroll_y, "width": top["width"],
                "height": bottom["y"] + bottom["height"] - top["y"] + 8}
    input_path = SHOTS / f"{name}_input.png"
    page.screenshot(path=str(input_path), clip=page_box, full_page=True)
    return {"op": op_id, "request_body": body, "status": code, "response_body": resp_body,
            "shot_input": f"shots/{input_path.name}", "shot_response": response_shot(page, live, name),
            "server_log": server.clean(server.lines[mark:])}


NEW = '{\n  "title": "실습 환경 안내",\n  "content": "Python 3.10 이상을 사용한다.",\n  "category": "setup"\n}'
NO_TITLE = '{\n  "content": "Python 3.10 이상을 사용한다.",\n  "category": "setup"\n}'
PUT_BODY = '{\n  "title": "서버 실행",\n  "content": "python -m uvicorn main:app --reload로 켠다.",\n  "category": "api"\n}'
POST_OP = "operations-default-create_knowledge_api_knowledge_post"
PUT_OP = "operations-default-update_knowledge_api_knowledge__knowledge_id__put"
DELETE_OP = "operations-default-delete_knowledge_api_knowledge__knowledge_id__delete"

rec = {}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME)
    page = browser.new_page(viewport={"width": 620, "height": 900}, device_scale_factor=2)

    root = project()
    server = Server(root)
    rec["start"] = {"server_log": server.start()}
    mark = len(server.lines)
    page.goto(URL + "/docs"); page.wait_for_selector(".opblock"); time.sleep(0.5)
    rec["docs_home"] = {"shot": shot(page.locator(".opblock-tag-section").first, "docs_home"),
                        "server_log": server.clean(server.lines[mark:])}
    rec["health"] = visit(page, server, "/health", "health")
    rec["get_2"] = visit(page, server, "/api/knowledge/2", "get_2")
    rec["get_9999"] = visit(page, server, "/api/knowledge/9999", "get_9999")
    rec["get_foo"] = visit(page, server, "/api/knowledge/foo", "get_foo")
    rec["list_before"] = visit(page, server, "/api/knowledge", "list_before")
    rec["post"] = docs_execute(page, server, POST_OP, NEW, "post_docs")
    rec["post"]["file"] = state(root)
    rec["list_after"] = visit(page, server, "/api/knowledge", "list_after")
    rec["get_4"] = visit(page, server, "/api/knowledge/4", "get_4")
    rec["no_title"] = docs_execute(page, server, POST_OP, NO_TITLE, "no_title_docs")
    rec["no_title"]["file"] = state(root)
    rec["list_after_no_title"] = visit(page, server, "/api/knowledge", "list_after_no_title")
    rec["put"] = docs_execute(page, server, PUT_OP, PUT_BODY, "put_docs", path_param=2)
    rec["put"]["file"] = state(root)
    rec["list_after_put"] = visit(page, server, "/api/knowledge", "list_after_put")
    rec["delete"] = docs_execute(page, server, DELETE_OP, None, "delete_docs", path_param=3)
    rec["delete"]["file"] = state(root)
    rec["get_3_after_delete"] = visit(page, server, "/api/knowledge/3", "get_3_after_delete")
    rec["list_after_delete"] = visit(page, server, "/api/knowledge", "list_after_delete")
    rec["stop"] = {"server_log": server.stop()}
    # 같은 폴더·같은 명령으로 다시 켠다
    server = Server(root)
    rec["restart"] = {"server_log": server.start()}
    rec["list_restart"] = visit(page, server, "/api/knowledge", "list_restart")
    rec["get_3_restart"] = visit(page, server, "/api/knowledge/3", "get_3_restart")
    rec["restart_file"] = state(root)
    server.stop()
    shutil.rmtree(root.parent)

    root = project(("    data[\"next_id\"] += 1\n    write_data(data)\n", "    data[\"next_id\"] += 1\n"))
    server = Server(root)
    server.start()
    rec["nw_post"] = docs_execute(page, server, POST_OP, NEW, "nw_post_docs")
    rec["nw_post"]["file"] = state(root)
    rec["nw_get_4"] = visit(page, server, "/api/knowledge/4", "nw_get_4")
    rec["nw_list"] = visit(page, server, "/api/knowledge", "nw_list")
    server.stop()
    shutil.rmtree(root.parent)
    browser.close()

OUT.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
for k, v in rec.items():
    print("##", k, v.get("status", ""), v.get("url", ""))
    for l in v.get("server_log", []):
        print("   LOG|", l)
    if "text" in v:
        print("   TXT|", v["text"][:200].replace("\n", " ⏎ "))
    if "response_body" in v:
        print("   RES|", v["response_body"][:160].replace("\n", " "))
