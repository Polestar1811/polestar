import re

from ..tools.product_tools import list_recommendable_products
from .base import AgentResult


def _budget(message: str) -> float | None:
    match = re.search(r"(\d+)\s*元?", message)
    return float(match.group(1)) if match else None


def run(message: str, context: dict | None = None) -> AgentResult:
    scene = "送礼" if any(k in message for k in ["送礼", "长辈", "客户"]) else "自饮"
    tool = list_recommendable_products(scene=scene, budget=_budget(message))
    products = tool["data"]
    skus = [
        {"sku_id": p["sku_id"], "name": p["name"], "price": p["price"], "reason": f"适合{scene}，库存充足，风味标签：{'/'.join(p['tags'])}", "suitable_scene": scene, "giftable": "礼盒" in p["tags"] or "送礼" in p["scene"], "stock_status": "有货"}
        for p in products
    ]
    reply = "推荐这几款：" + "、".join(p["name"] for p in products)
    output = {"reply": reply, "recommended_skus": skus, "upsell_skus": [], "need_clarify": False, "clarify_question": ""}
    return AgentResult(reply, "recommendation", "recommendation", output, [tool])
