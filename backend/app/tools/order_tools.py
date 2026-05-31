from ..mock_data import DB
from .common import fail, ok


def verify_customer(order_no: str, phone_tail: str | None = None, customer_id: str | None = None):
    DB.ensure_seeded()
    order = next((o for o in DB.orders if o["order_no"] == order_no), None)
    if not order:
        return fail("NOT_FOUND", "订单不存在")
    if phone_tail and order["phone_tail"] == phone_tail:
        return ok({"verified": True})
    if customer_id and order["customer_id"] == customer_id:
        return ok({"verified": True})
    return fail("VERIFY_FAILED", "身份校验未通过")


def get_order(order_no: str):
    DB.ensure_seeded()
    order = next((o for o in DB.orders if o["order_no"] == order_no), None)
    return ok(order) if order else fail("NOT_FOUND", "订单不存在")


def get_tracking(order_no: str):
    order = get_order(order_no)
    if not order["ok"]:
        return order
    return ok(order["data"].get("tracking", {}))


def check_order_mutability(order_no: str):
    order = get_order(order_no)
    if not order["ok"]:
        return order
    return ok({"order_no": order_no, "mutable": order["data"]["mutable"]})
