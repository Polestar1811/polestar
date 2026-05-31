from __future__ import annotations

from uuid import uuid4

from ..mock_data import DB


def ok(data):
    trace_id = str(uuid4())
    result = {"ok": True, "data": data, "error": None, "trace_id": trace_id}
    DB.append_log("tool_logs", {"trace_id": trace_id, "ok": True, "data": data})
    return result


def fail(code: str, message: str):
    trace_id = str(uuid4())
    result = {"ok": False, "data": None, "error": {"code": code, "message": message}, "trace_id": trace_id}
    DB.append_log("tool_logs", {"trace_id": trace_id, "ok": False, "error": result["error"]})
    return result
