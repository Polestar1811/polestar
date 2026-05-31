from app.agents.recommendation_agent import run


def test_recommendation_returns_in_stock_skus():
    result = run("送客户300元左右买什么")
    assert result.structured_output["recommended_skus"]
    assert all(x["stock_status"] == "有货" for x in result.structured_output["recommended_skus"])
