import json

from ..config import settings
from ..tools.campaign_tools import create_approval_workitem, create_campaign_brief
from ..tools.product_tools import search_products
from .ai import generate_json
from .base import AgentResult


COPY_FIELDS = ["xiaohongshu", "douyin_script", "wechat_private", "sms", "email_subject", "detail_page_outline"]


def _safe_copy(value) -> str:
    if isinstance(value, dict):
        value = "\n".join(str(v) for v in value.values() if v)
    elif isinstance(value, list):
        value = "\n".join(str(v) for v in value)
    text = str(value or "")
    replacements = {
        "绝对": "比较",
        "正宗": "资料显示",
        "满分答案": "稳妥选择",
        "超有面子": "体面",
        "性价比超高": "价格友好",
        "仅需": "价格为",
        "必买": "可考虑",
        "天花板": "优选",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def _normalize_output(output: dict, fallback: dict) -> dict:
    if not isinstance(output.get("campaign_brief"), dict):
        output["campaign_brief"] = fallback["campaign_brief"]
    copies = output.get("copies")
    if not isinstance(copies, dict):
        text = "\n".join(str(item) for item in copies) if isinstance(copies, list) else str(copies or "")
        copies = {**fallback["copies"], "xiaohongshu": text or fallback["copies"]["xiaohongshu"]}
    normalized = dict(fallback["copies"])
    for key in COPY_FIELDS:
        if key in fallback["copies"] and key != "detail_page_outline":
            normalized[key] = _safe_copy(copies.get(key, fallback["copies"][key]))
    if isinstance(copies.get("detail_page_outline"), list):
        normalized["detail_page_outline"] = copies["detail_page_outline"]
    if not isinstance(normalized.get("detail_page_outline"), list):
        normalized["detail_page_outline"] = fallback["copies"]["detail_page_outline"]
    output["copies"] = normalized
    output["need_approval"] = bool(output.get("need_approval", True))
    return output


def run(message: str, context: dict | None = None) -> AgentResult:
    products_tool = search_products("龙井" if "龙井" in message else "")
    hero = "SKU-LJ-001" if "龙井" in message else "SKU-HC-001"
    brief = {
        "goal": "拉新与转化",
        "audience": "对茶叶有兴趣的新客和礼赠人群",
        "channel": ["小红书", "抖音", "私域"],
        "hero_skus": [hero],
        "offer": "以后台配置为准",
        "risk_notes": ["涉及优惠和群发需审批", "不得承诺医疗功效"],
    }
    fallback = {
        "campaign_brief": brief,
        "copies": {
            "xiaohongshu": "这款茶适合想把清爽茶香送进日常的人。包装体面，适合拜访客户或长辈，具体库存和价格以商城页面为准。",
            "douyin_script": "镜头一：开盒展示。镜头二：温杯冲泡。镜头三：茶汤清亮。结尾：送礼不夸张，自饮也刚好。",
            "wechat_private": "今天推荐一款有质感的茶礼，适合客户拜访和家人节日礼赠，库存以商城页面为准。",
            "sms": "清香茶礼推荐，适合节日送礼。优惠以商城展示为准，回复退订。",
            "email_subject": "一份克制、有质感的茶礼推荐",
            "detail_page_outline": ["适用场景", "风味特点", "冲泡建议", "包装规格", "售后说明"],
        },
        "need_approval": True,
    }
    system = """你是茶叶电商营销内容 Agent。
输出要适合电商运营真实使用：能直接给运营复制、拆成渠道素材、提醒合规风险。
不得虚假宣传，不得编造认证、奖项、产地、年份，不得承诺医疗功效。
涉及优惠、价格、群发、短信触达时 need_approval=true。
输出严格 JSON：campaign_brief、copies、need_approval。"""
    user = json.dumps({"request": message, "candidate_products": products_tool["data"], "fallback_brief": brief}, ensure_ascii=False)
    output = _normalize_output(generate_json(system, user, fallback, model=settings.default_fast_model), fallback)
    campaign = create_campaign_brief(output.get("campaign_brief", brief))
    approval = create_approval_workitem({"type": "campaign", "output": output})
    return AgentResult("已生成营销内容草案，涉及优惠和群发前需要审批。", "marketing", "marketing", output, [products_tool, campaign, approval])
