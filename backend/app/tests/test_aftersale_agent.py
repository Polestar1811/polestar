from app.agents.aftersale_agent import run


def test_aftersale_collects_evidence():
    result = run("收到礼盒破损了")
    assert result.structured_output["action"] == "collect_evidence"
    assert result.structured_output["required_evidence"]
