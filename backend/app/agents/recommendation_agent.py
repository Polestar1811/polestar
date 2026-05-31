import json
import re

from ..config import settings
from ..tools.product_tools import list_recommendable_products
from .ai import generate_json
from .base import AgentResult


def _normalize_output(output: dict, fallback: dict) -> dict:
    if not isinstance(output.get("recommended_skus"), list):
        output["recommended_skus"] = fallback["recommended_skus"]
    if not isinstance(output.get("upsell_skus"), list):
        output["upsell_skus"] = []
    output["reply"] = str(output.get("reply") or fallback["reply"])
    output["need_clarify"] = bool(output.get("need_clarify", False))
    output["clarify_question"] = str(output.get("clarify_question") or "")
    return output


def _budget(message: str) -> float | None:
    match = re.search(r"(\d+)\s*元?", message)
    return float(match.group(1)) if match else None


def _scene(message: str) -> str:
    if any(k in message for k in ["长辈", "客户", "送礼", "礼盒", "商务"]):
        return "送礼"
    if any(k in message for k in ["办公室", "公司", "员工"]):
        return "办公室"
    if any(k in message for k in ["冷泡", "夏天"]):
        return "冷泡"
    return "自饮"


def run(message: str, context: dict | None = None) -> AgentResult:
    scene = _scene(message)
    tool = list_recommendable_products(scene=scene, budget=_budget(message))
    products = tool["data"] or []
    skus = [
        {
            "sku_id": p["sku_id"],
            "name": p["name"],
            "price": p["price"],
            "reason": f"适合{scene}，库存充足，风味标签：{'/'.join(p['tags'])}",
            "suitable_scene": scene,
            "giftable": "礼盒" in p["tags"] or "送礼" in p["scene"] or "商务" in p["scene"],
            "stock_status": "有货",
        }
        for p in products
    ]
    fallback = {
        "reply": "推荐这几款：" + "、".join(p["name"] for p in products),
        "recommended_skus": skus,
        "upsell_skus": [],
        "need_clarify": False,
        "clarify_question": "",
    }
    system = """你是茶叶电商企业的商品推荐 Agent。
只能基于给定商品数据推荐，禁止推荐缺货商品，禁止编造产地、年份、认证和医疗功效。
输出严格 JSON，字段为 reply、recommended_skus、upsell_skus、need_clarify、clarify_question。"""
    user = json.dumps({"customer_message": message, "scene": scene, "products": products}, ensure_ascii=False)
    output = _normalize_output(generate_json(system, user, fallback, model=settings.default_fast_model), fallback)
    return AgentResult(output.get("reply", fallback["reply"]), "recommendation", "recommendation", output, [tool])
