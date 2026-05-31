import json

from ..config import settings
from ..tools.inventory_tools import compute_reorder_suggestion, list_low_stock
from .ai import generate_json
from .base import AgentResult


def run(message: str, context: dict | None = None) -> AgentResult:
    alerts = list_low_stock()
    first = alerts["data"][0] if alerts["data"] else None
    suggestion = compute_reorder_suggestion(first["sku_id"]) if first else {"data": {"type": "hold", "reason": "库存健康，暂不补货", "qty": None}, "trace_id": ""}
    fallback = {
        "risk_level": first["risk_level"] if first else "low",
        "stock_status": first["stock_status"] if first else "healthy",
        "recommendation": suggestion["data"],
        "reply": "当前预警：" + ("、".join(f"{a['name']}({a['stock_status']})" for a in alerts["data"]) if alerts["data"] else "暂无明显风险"),
        "need_approval": bool(first),
    }
    system = """你是茶叶电商库存运营 Agent。
基于库存预警数据给出补货、清仓、组合销售或人工复核建议；不得直接修改库存。
输出严格 JSON：risk_level、stock_status、recommendation、reply、need_approval。"""
    user = json.dumps({"question": message, "alerts": alerts["data"], "suggestion": suggestion["data"]}, ensure_ascii=False)
    output = generate_json(system, user, fallback, model=settings.default_fast_model)
    return AgentResult(output.get("reply", fallback["reply"]), "inventory", "inventory", output, [alerts, suggestion])
