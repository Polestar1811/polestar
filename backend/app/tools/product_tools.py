from ..mock_data import DB
from .common import fail, ok


def search_products(query: str = "", filters: dict | None = None):
    DB.ensure_seeded()
    q = query.lower()
    items = [p for p in DB.products if not q or q in p["name"].lower() or q in " ".join(p["tags"])]
    return ok(items)


def get_product_detail(sku_id: str):
    DB.ensure_seeded()
    item = next((p for p in DB.products if p["sku_id"] == sku_id), None)
    return ok(item) if item else fail("NOT_FOUND", "商品不存在")


def get_product_stock(sku_id: str):
    detail = get_product_detail(sku_id)
    if not detail["ok"]:
        return detail
    return ok({"sku_id": sku_id, "stock": detail["data"]["stock"]})


def list_recommendable_products(scene: str = "", budget: float | None = None, tags: list[str] | None = None):
    DB.ensure_seeded()
    tags = tags or []
    items = []
    for p in DB.products:
        if not p["recommendable"] or p["stock"] <= 0:
            continue
        if budget and p["price"] > budget:
            continue
        score = int(scene in p["scene"]) + len(set(tags) & set(p["tags"])) + p["margin"]
        items.append({**p, "score": score})
    return ok(sorted(items, key=lambda x: x["score"], reverse=True)[:3])
