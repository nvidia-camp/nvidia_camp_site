# Day29 페이지 실측: DB·GPU·API 없이 실행 가능한 Tool 계약만 실행한다.
import json, sys
from pydantic import BaseModel, Field, ValidationError
from langchain_core.tools import tool
from langchain_core.messages import AIMessage, ToolMessage
import langchain_core

class StatusArgs(BaseModel):
    report_id: int = Field(gt=0, description="조회할 보고서 번호")

@tool(args_schema=StatusArgs)
def lookup_status(report_id: int) -> str:
    """보고서의 인덱싱 상태를 조회합니다."""
    return json.dumps({"report_id": report_id, "index_status": "fixture"})

out = {"langchain_core": langchain_core.__version__, "python": sys.version.split()[0]}
out["schema_name"] = lookup_status.name
out["schema_args"] = lookup_status.args
try:
    lookup_status.invoke({"report_id": -1})
except ValidationError as e:
    out["neg_error"] = e.errors()[0]["msg"]

ai = AIMessage(content="", tool_calls=[{"name": "lookup_status", "args": {"report_id": 63}, "id": "call_1"}])
call = ai.tool_calls[0]
tm = lookup_status.invoke({**call, "type": "tool_call"})
out["tool_call"] = {k: call[k] for k in ("name", "args", "id")}
out["tool_message"] = {"type": type(tm).__name__, "tool_call_id": tm.tool_call_id, "content": tm.content}
json.dump(out, open("result.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
