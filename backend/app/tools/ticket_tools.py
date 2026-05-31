from uuid import uuid4

from ..mock_data import DB
from .common import ok


def create_ticket(ticket_type: str, payload: dict):
    ticket = {"ticket_id": str(uuid4()), "ticket_type": ticket_type, "status": "pending_review", "payload": payload}
    DB.tickets.append(ticket)
    return ok(ticket)


def update_ticket(ticket_id: str, payload: dict):
    ticket = next((t for t in DB.tickets if t["ticket_id"] == ticket_id), None)
    if ticket:
        ticket.update(payload)
    return ok(ticket)


def request_human_review(reason: str, payload: dict):
    return create_ticket("human_review", {"reason": reason, **payload})
