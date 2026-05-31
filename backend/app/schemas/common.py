from pydantic import BaseModel


class ToolResult(BaseModel):
    ok: bool
    data: dict | list | None
    error: dict | None = None
    trace_id: str
