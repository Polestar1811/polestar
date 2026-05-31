import re

from ..tools.order_tools import check_order_mutability, get_order, get_tracking
from .base import AgentResult


def run(message: str, context: dict | None = None) -> AgentResult:
    match = re.search(r"ORD\d+", message, re.I)
    order_no = match.group(0).upper() if match else None
    if not order_no:
        reply = "请提供订单号，或手机号后四位/会员 ID，以便先做身份校验。"
        output = {"action": "clarify", "reply": reply, "order_summary": {}, "tracking": {}, "allowed_actions": [], "need_human": False}
        return AgentResult(reply, "order_query", "order", output)
    order = get_order(order_no)
    tracking = get_tracking(order_no)
    mutable = check_order_mutability(order_no)
    if not order["ok"]:
        reply = "没有查到该订单，不能编造物流或订单状态，建议人工核查。"
        output = {"action": "handoff", "reply": reply, "order_summary": {}, "tracking": {}, "allowed_actions": [], "need_human": True}
        return AgentResult(reply, "order_query", "order", output, [order], need_human=True)
    allowed = ["修改地址"] if mutable["data"]["mutable"] else ["查看物流", "创建售后工单"]
    reply = f"{order_no} 当前状态：{order['data']['status']}。物流：{tracking['data'].get('status', '暂无物流')}。"
    output = {"action": "answer", "reply": reply, "order_summary": order["data"], "tracking": tracking["data"], "allowed_actions": allowed, "need_human": False}
    return AgentResult(reply, "order_query", "order", output, [order, tracking, mutable])
