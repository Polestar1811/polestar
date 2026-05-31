from __future__ import annotations

from uuid import uuid4

from ..mock_data import DB


def audit(action: str, actor: str, payload: dict) -> dict:
    item = {"id": str(uuid4()), "action": action, "actor": actor, "payload": payload}
    DB.append_log("audit_logs", item)
    return item
