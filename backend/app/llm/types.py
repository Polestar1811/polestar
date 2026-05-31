from pydantic import BaseModel


class LLMResponse(BaseModel):
    content: str
    raw: dict = {}
    usage: dict = {}
    latency_ms: int = 0
    provider: str
    model: str
