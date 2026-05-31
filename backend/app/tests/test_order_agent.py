from app.agents.order_agent import run


def test_order_agent_does_not_invent_unknown_order():
    result = run("我的 ORD999 订单到哪了")
    assert result.need_human is True
    assert result.structured_output["order_summary"] == {}
