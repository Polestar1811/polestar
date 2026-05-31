from app.agents.inventory_agent import run


def test_inventory_alerts_have_trace():
    result = run("哪些SKU快断货了")
    assert result.tool_traces[0]["trace_id"]
    assert result.structured_output["stock_status"] in {"low_stock", "aging", "out_of_stock", "healthy"}
