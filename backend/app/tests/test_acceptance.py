from app.services.chat_service import chat


def test_acceptance_chat_examples():
    cases = [
        ("送长辈300元左右茶叶推荐", "recommendation"),
        ("我的ORD001订单到哪了", "order_query"),
        ("收到礼盒破损了", "aftersale"),
        ("哪些SKU快断货了", "inventory"),
        ("帮我写一篇小红书龙井礼盒文案", "marketing"),
        ("本周销售情况怎么样", "reporting"),
    ]
    for message, intent in cases:
        result = chat(message)
        assert result["intent"] == intent
        assert result["reply"]
        assert isinstance(result["structured_output"], dict)
        if intent != "kb_qa":
            assert result["tool_traces"]
