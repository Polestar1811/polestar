import json

from ..config import settings
from .ai import generate_json
from .base import AgentResult


KNOWLEDGE = {
    "龙井": "龙井建议用 85°C 左右热水冲泡，先温杯，再投茶，前两泡 10-20 秒出汤，避免沸水久闷。",
    "发票": "订单完成后可申请电子发票，抬头和税号需以实际订单信息为准。",
    "退换货": "食品类茶叶售后需结合是否拆封、签收时间和证据图片人工确认。",
}


def run(message: str, context: dict | None = None) -> AgentResult:
    hits = [{"title": key, "content": value, "source": f"mock_kb:{key}"} for key, value in KNOWLEDGE.items() if key in message]
    if hits:
        reply = hits[0]["content"]
        fallback = {"action": "answer", "reply": reply, "sources": [hits[0]["source"]], "confidence": 0.82, "need_human": False}
    else:
        reply = "暂未查到可靠信息，建议转人工确认后再回复客户。"
        fallback = {"action": "handoff", "reply": reply, "sources": [], "confidence": 0.3, "need_human": True}
    system = """你是茶叶电商公司的知识库客服 Agent。
只能基于给定知识片段回答，不得编造事实、认证、年份、产地、物流、库存和售后政策。
涉及医疗、保健、减脂、降糖、降压等内容时，只能给一般饮用提醒，不能承诺功效。
输出严格 JSON：action、reply、sources、confidence、need_human。"""
    user = json.dumps({"customer_message": message, "knowledge_hits": hits}, ensure_ascii=False)
    output = generate_json(system, user, fallback, model=settings.default_fast_model)
    return AgentResult(output.get("reply", reply), "kb_qa", "kb", output, sources=output.get("sources", []), need_human=bool(output.get("need_human")))
