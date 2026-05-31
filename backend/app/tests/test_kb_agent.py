from app.agents.kb_agent import run


def test_kb_agent_cites_source_when_known():
    result = run("龙井怎么泡")
    assert result.sources
    assert result.structured_output["action"] == "answer"
