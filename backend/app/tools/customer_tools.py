from .common import ok


def get_customer_profile(customer_id: str):
    return ok({"customer_id": customer_id, "level": "regular", "tags": ["送礼偏好"]})


def get_purchase_history(customer_id: str):
    return ok([{"sku_id": "SKU-LJ-001", "order_no": "ORD001"}])


def get_customer_tags(customer_id: str):
    return ok(["绿茶", "礼盒", "高复购"])
