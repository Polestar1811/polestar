from ..tools.ticket_tools import create_ticket
from .base import AgentResult


def run(message: str, context: dict | None = None) -> AgentResult:
    case_type = "damaged_package" if "破损" in message else "quality_issue" if "质量" in message else "refund"
    required = ["外包装照片", "商品破损照片", "订单号"] if case_type == "damaged_package" else ["订单号", "问题描述", "证据图片"]
    proposal = {"type": "manual_review", "reason": "食品类售后需结合证据和订单状态审核，Agent 只给建议。", "amount": None}
    ticket = create_ticket(case_type, {"message": message, "required_evidence": required, "proposal": proposal})
    reply = "已生成售后建议：请先补充订单号和证据图片，人工审核后再决定退款、补发或换货。"
    output = {"action": "collect_evidence", "reply": reply, "case_type": case_type, "required_evidence": required, "proposal": proposal, "risk_level": "medium", "need_human": True}
    return AgentResult(reply, "aftersale", "aftersale", output, [ticket], need_human=True)
