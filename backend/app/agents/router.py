from __future__ import annotations

import re


ROUTES = {
    "kb_qa": "kb",
    "recommendation": "recommendation",
    "order_query": "order",
    "aftersale": "aftersale",
    "inventory": "inventory",
    "marketing": "marketing",
    "reporting": "reporting",
    "human": "human",
    "unknown": "kb",
}


RULES: list[tuple[str, list[str]]] = [
    ("human", ["投诉升级", "食品安全", "律师", "法院", "大额赔付", "监管", "索赔"]),
    ("order_query", ["订单", "物流", "快递", "发货", "改地址", "地址", "签收", "ord"]),
    ("aftersale", ["退款", "退货", "换货", "破损", "错发", "漏发", "补发", "质量", "售后", "坏了"]),
    ("inventory", ["库存", "断货", "补货", "滞销", "临期", "周转", "清仓", "sku快", "sku 快"]),
    ("marketing", ["文案", "小红书", "抖音", "脚本", "活动", "直播", "私域", "朋友圈", "短信", "邮件标题"]),
    ("reporting", ["gmv", "销售", "报表", "转化率", "利润", "毛利", "sku表现", "本周", "今天", "同比", "环比", "roi"]),
    ("recommendation", ["推荐", "买什么", "送礼", "预算", "自饮", "客户", "长辈", "办公室喝", "入门"]),
    ("kb_qa", ["怎么泡", "冲泡", "区别", "发票", "政策", "保质期", "龙井", "普洱", "白茶", "乌龙"]),
]


def classify(message: str) -> dict:
    text = (message or "").strip().lower()
    if not text:
        return {"intent": "unknown", "confidence": 0.1, "reason": "空消息", "required_slots": [], "next_agent": "kb"}

    if re.search(r"\bord\d+\b", text, re.I):
        return {"intent": "order_query", "confidence": 0.95, "reason": "识别到订单号", "required_slots": [], "next_agent": "order"}

    scores: dict[str, int] = {}
    for intent, keywords in RULES:
        score = sum(1 for keyword in keywords if keyword.lower() in text)
        if score:
            scores[intent] = score

    if not scores:
        return {"intent": "unknown", "confidence": 0.35, "reason": "未命中明确业务关键词", "required_slots": [], "next_agent": "kb"}

    intent = max(scores, key=lambda key: (scores[key], -list(ROUTES).index(key) if key in ROUTES else 0))
    confidence = min(0.95, 0.62 + scores[intent] * 0.12)
    return {
        "intent": intent,
        "confidence": confidence,
        "reason": f"命中 {intent} 业务关键词",
        "required_slots": [],
        "next_agent": ROUTES[intent],
    }
