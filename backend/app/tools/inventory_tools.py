from ..mock_data import DB
from .common import ok


def _status(product: dict):
    stock = product["stock"]
    if stock <= 0:
        return "out_of_stock", "high"
    if stock < 40:
        return "low_stock", "medium"
    if product["sku_id"] == "SKU-HC-001":
        return "aging", "medium"
    return "healthy", "low"


def get_inventory_snapshot(sku_ids: list[str] | None = None):
    DB.ensure_seeded()
    rows = [p for p in DB.products if not sku_ids or p["sku_id"] in sku_ids]
    return ok(rows)


def list_low_stock():
    DB.ensure_seeded()
    alerts = []
    for p in DB.products:
        stock_status, risk_level = _status(p)
        if stock_status != "healthy":
            alerts.append({"sku_id": p["sku_id"], "name": p["name"], "stock": p["stock"], "stock_status": stock_status, "risk_level": risk_level})
    return ok(alerts)


def list_aging_stock(days_threshold: int = 30):
    DB.ensure_seeded()
    return ok([p for p in DB.products if p["sku_id"] == "SKU-HC-001"])


def compute_reorder_suggestion(sku_id: str):
    product = next((p for p in DB.products if p["sku_id"] == sku_id), None)
    if not product:
        return ok({"type": "manual_review", "reason": "缺少 SKU 数据", "qty": None})
    stock_status, _ = _status(product)
    if stock_status in {"low_stock", "out_of_stock"}:
        return ok({"type": "replenish", "reason": "库存低于安全线，建议补货", "qty": 100})
    if stock_status == "aging":
        return ok({"type": "promote", "reason": "近 30 日动销下降，建议做办公室场景组合促销", "qty": None})
    return ok({"type": "hold", "reason": "库存健康，暂不补货", "qty": None})
