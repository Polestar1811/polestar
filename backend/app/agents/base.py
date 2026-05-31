from dataclasses import dataclass, field


@dataclass
class AgentResult:
    reply: str
    intent: str
    agent: str
    structured_output: dict
    tool_traces: list[dict] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    need_human: bool = False
