import json

from ..config import settings
from ..tools.ticket_tools import create_ticket
from .ai import generate_json
from .base import AgentResult


def _normalize_output(output: dict, fallback: dict) -> dict:
    if output.get("action") not in {"collect_evidence", "propose_solution", "handoff"}:
        output["action"] = fallback["action"]
    if not isinstance(output.get("required_evidence"), list):
        output["required_evidence"] = fallback["required_evidence"]
    if not isinstance(output.get("proposal"), dict):
        output["proposal"] = fallback["proposal"]
    if output.get("risk_level") not in {"low", "medium", "high"}:
        output["risk_level"] = fallback["risk_level"]
    output["reply"] = str(output.get("reply") or fallback["reply"])
    output["case_type"] = str(output.get("case_type") or fallback["case_type"])
    output["need_human"] = bool(output.get("need_human", True))
    return output


def run(message: str, context: dict | None = None) -> AgentResult:
    case_type = "damaged_package" if "破损" in message else "quality_issue" if "质量" in message else "refund"
    required = ["外包装照片", "商品破损照片", "订单号"] if case_type == "damaged_package" else ["订单号", "问题描述", "证据图片"]
    proposal = {"type": "manual_review", "reason": "食品类售后需结合证据和订单状态审核，Agent 只给建议。", "amount": None}
    fallback = {
        "action": "collect_evidence",
        "reply": "已生成售后建议：请先补充订单号和证据图片，人工审核后再决定退款、补发或换货。",
        "case_type": case_type,
        "required_evidence": required,
        "proposal": proposal,
        "risk_level": "medium",
        "need_human": True,
    }
    system = """你是企业售后处理 Agent。
你只给建议和证据清单，不直接承诺退款、补发、赔偿。
高金额、食品安全、批量异常、恶意投诉、差评威胁必须 need_human=true。
输出严格 JSON：action、reply、case_type、required_evidence、proposal、risk_level、need_human。"""
    user = json.dumps({"customer_message": message, "detected_case_type": case_type, "required_evidence": required}, ensure_ascii=False)
    output = _normalize_output(generate_json(system, user, fallback, model=settings.default_reasoning_model), fallback)
    ticket = create_ticket(output.get("case_type", case_type), {"message": message, "agent_output": output})
    return AgentResult(output.get("reply", fallback["reply"]), "aftersale", "aftersale", output, [ticket], need_human=bool(output.get("need_human", True)))
