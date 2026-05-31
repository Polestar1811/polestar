from ..tools.inventory_tools import compute_reorder_suggestion, list_low_stock
from .base import AgentResult


def run(message: str, context: dict | None = None) -> AgentResult:
    alerts = list_low_stock()
    first = alerts["data"][0] if alerts["data"] else None
    suggestion = compute_reorder_suggestion(first["sku_id"]) if first else {"data": {"type": "hold", "reason": "库存健康", "qty": None}, "trace_id": ""}
    reply = "当前预警：" + ("、".join(f"{a['name']}({a['stock_status']})" for a in alerts["data"]) if alerts["data"] else "暂无明显风险")
    output = {"risk_level": first["risk_level"] if first else "low", "stock_status": first["stock_status"] if first else "healthy", "recommendation": suggestion["data"], "reply": reply, "need_approval": bool(first)}
    return AgentResult(reply, "inventory", "inventory", output, [alerts, suggestion])
