from __future__ import annotations


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


def classify(message: str) -> dict:
    text = message.lower()
    rules = [
        ("human", ["投诉升级", "食品安全", "律师", "法院", "大额赔付"]),
        ("order_query", ["订单", "物流", "发货", "改地址", "ord"]),
        ("aftersale", ["退款", "退货", "破损", "错发", "补发", "质量", "售后"]),
        ("inventory", ["库存", "断货", "补货", "滞销", "临期", "sku快"]),
        ("marketing", ["文案", "小红书", "抖音", "脚本", "活动", "直播", "私域"]),
        ("reporting", ["gmv", "销售", "报表", "转化率", "利润", "sku表现", "本周"]),
        ("recommendation", ["推荐", "买什么", "送礼", "预算", "自饮", "客户", "长辈"]),
        ("kb_qa", ["怎么泡", "冲泡", "区别", "发票", "政策", "保质期", "龙井"]),
    ]
    for intent, keywords in rules:
        if any(k in text for k in keywords):
            return {"intent": intent, "confidence": 0.88, "reason": f"命中 {intent} 关键词", "required_slots": [], "next_agent": ROUTES[intent]}
    return {"intent": "unknown", "confidence": 0.35, "reason": "未命中明确业务关键词", "required_slots": [], "next_agent": "kb"}
