from .base import AgentResult


KNOWLEDGE = {
    "龙井": "龙井建议用 85°C 左右热水冲泡，先温杯，再投茶，前两泡 10-20 秒出汤，避免沸水久闷。",
    "发票": "订单完成后可申请电子发票，抬头和税号需以实际订单信息为准。",
    "退换货": "食品类茶叶售后需结合是否拆封、签收时间和证据图片人工确认。",
}


def run(message: str, context: dict | None = None) -> AgentResult:
    for key, answer in KNOWLEDGE.items():
        if key in message:
            output = {"action": "answer", "reply": answer, "sources": [f"mock_kb:{key}"], "confidence": 0.82, "need_human": False}
            return AgentResult(answer, "kb_qa", "kb", output, sources=output["sources"])
    reply = "暂未查到可靠信息，建议转人工确认后再回复客户。"
    output = {"action": "handoff", "reply": reply, "sources": [], "confidence": 0.3, "need_human": True}
    return AgentResult(reply, "kb_qa", "kb", output, need_human=True)
