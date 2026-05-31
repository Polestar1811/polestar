from fastapi.testclient import TestClient

from app.main import app
from app.mock_data import DB


client = TestClient(app)


def test_health_and_chat_api():
    assert client.get("/health").json() == {"status": "ok"}
    response = client.post(
        "/api/chat",
        json={"message": "我的ORD001订单到哪了", "agent_type": "auto", "context": {}},
    )
    body = response.json()
    assert response.status_code == 200
    assert body["intent"] == "order_query"
    assert body["tool_traces"][0]["trace_id"]


def test_login_and_permission_denied_for_warehouse_report():
    login = client.post("/api/auth/login", json={"email": "warehouse@example.com", "password": "demo"}).json()
    response = client.get("/api/reports/summary", headers={"Authorization": f"Bearer {login['access_token']}"})
    assert response.status_code == 403


def test_sensitive_agent_writes_audit_and_llm_log():
    DB.audit_logs.clear()
    DB.llm_logs.clear()
    response = client.post(
        "/api/chat",
        json={"message": "收到礼盒破损了", "agent_type": "auto", "context": {}},
    )
    assert response.status_code == 200
    assert DB.llm_logs
    assert any(item["action"] == "aftersale_agent_suggestion" for item in DB.audit_logs)
