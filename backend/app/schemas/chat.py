from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str
    agent_type: str = "auto"
    context: dict = Field(default_factory=dict)


class ChatResponse(BaseModel):
    reply: str
    intent: str
    agent: str
    structured_output: dict
    tool_traces: list[dict]
    sources: list[str] = []
    need_human: bool = False
