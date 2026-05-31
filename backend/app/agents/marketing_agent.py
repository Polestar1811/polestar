from ..tools.campaign_tools import create_approval_workitem, create_campaign_brief
from .base import AgentResult


def run(message: str, context: dict | None = None) -> AgentResult:
    hero = "SKU-LJ-001" if "龙井" in message else "SKU-HC-001"
    brief = {"goal": "拉新与转化", "audience": "对茶叶有兴趣的新客和礼赠人群", "channel": ["小红书", "抖音", "私域"], "hero_skus": [hero], "offer": "以后台配置为准", "risk_notes": ["涉及优惠和群发需审批"]}
    campaign = create_campaign_brief(brief)
    approval = create_approval_workitem({"type": "campaign", "brief": brief})
    output = {
        "campaign_brief": brief,
        "copies": {
            "xiaohongshu": "这款龙井适合想把春天清香送进日常的人。香气清爽，礼盒体面，适合拜访客户或长辈。",
            "douyin_script": "镜头一：开盒闻香。镜头二：85°C 水冲泡。镜头三：茶汤清亮。结尾：送礼不夸张，自饮也刚好。",
            "wechat_private": "今天推荐一款清香型茶礼，适合客户拜访和家人节日礼赠，库存以商城页面为准。",
            "sms": "清香茶礼上新，适合节日送礼。优惠以商城展示为准，回复退订。",
            "email_subject": "一份克制、有质感的茶礼推荐",
            "detail_page_outline": ["适用场景", "风味特点", "冲泡建议", "包装规格", "售后说明"],
        },
        "need_approval": True,
    }
    return AgentResult("已生成营销内容草案，涉及优惠和群发前需要审批。", "marketing", "marketing", output, [campaign, approval])
