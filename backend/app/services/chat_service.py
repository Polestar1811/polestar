from ..agents import aftersale_agent, inventory_agent, kb_agent, marketing_agent, order_agent, recommendation_agent, reporting_agent
from ..agents.router import classify
from ..mock_data import DB
from .audit_service import audit


AGENTS = {
    "kb": kb_agent.run,
    "recommendation": recommendation_agent.run,
    "order": order_agent.run,
    "aftersale": aftersale_agent.run,
    "inventory": inventory_agent.run,
    "marketing": marketing_agent.run,
    "reporting": reporting_agent.run,
}


def chat(message: str, agent_type: str = "auto", context: dict | None = None) -> dict:
    context = context or {}
    actor = context.get("actor", {"email": "anonymous", "role": "viewer"})
    route = classify(message) if agent_type == "auto" else {"intent": agent_type, "next_agent": agent_type}
    agent_name = route["next_agent"]
    DB.append_log(
        "llm_logs",
        {
            "provider": "router",
            "model": "deterministic-router",
            "agent": agent_name,
            "intent": route.get("intent"),
            "usage": {"input_chars": len(message), "output_chars": 0},
            "latency_ms": 0,
            "error": None,
        },
    )
    if agent_name == "human":
        audit("human_handoff", actor["email"], {"message": message, "reason": route.get("reason")})
        return {
            "reply": "该问题涉及高风险场景，建议人工接管。",
            "intent": "human",
            "agent": "human",
            "structured_output": route,
            "tool_traces": [],
            "sources": [],
            "need_human": True,
        }
    runner = AGENTS.get(agent_name, kb_agent.run)
    result = runner(message, context)
    if result.intent in {"aftersale", "inventory", "marketing", "reporting"}:
        audit(f"{result.intent}_agent_suggestion", actor["email"], result.structured_output)
    return {
        "reply": result.reply,
        "intent": route.get("intent", result.intent),
        "agent": result.agent,
        "structured_output": result.structured_output,
        "tool_traces": result.tool_traces,
        "sources": result.sources,
        "need_human": result.need_human,
    }
