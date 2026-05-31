from app.agents.router import classify


def test_router_classifies_core_intents():
    cases = {
        "这款龙井怎么泡": "kb_qa",
        "送客户300元左右买什么": "recommendation",
        "我的订单怎么还没到 ORD001": "order_query",
        "收到破损了我要退款": "aftersale",
        "哪些SKU快断货了": "inventory",
        "写一篇小红书文案": "marketing",
        "本周GMV为什么下降": "reporting",
    }
    for text, intent in cases.items():
        assert classify(text)["intent"] == intent
