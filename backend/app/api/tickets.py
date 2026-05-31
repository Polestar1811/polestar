from fastapi import APIRouter, Depends, HTTPException

from ..mock_data import DB
from ..schemas.ticket import TicketCreate
from ..services.audit_service import audit
from ..services.auth_service import current_user
from ..services.permission_service import can
from ..tools.ticket_tools import create_ticket, update_ticket

router = APIRouter()


@router.get("")
def list_tickets():
    return {"ok": True, "data": DB.tickets, "error": None, "trace_id": "list"}


@router.post("")
def create(payload: TicketCreate, user: dict = Depends(current_user)):
    if not can(user["role"], "tickets:write"):
        raise HTTPException(status_code=403, detail="No permission")
    return create_ticket(payload.ticket_type, payload.payload)


@router.post("/{ticket_id}/approve")
def approve(ticket_id: str, user: dict = Depends(current_user)):
    if not can(user["role"], "tickets:approve"):
        raise HTTPException(status_code=403, detail="No permission")
    audit("ticket_approve", user["email"], {"ticket_id": ticket_id})
    return update_ticket(ticket_id, {"status": "approved"})


@router.post("/{ticket_id}/reject")
def reject(ticket_id: str, user: dict = Depends(current_user)):
    if not can(user["role"], "tickets:approve"):
        raise HTTPException(status_code=403, detail="No permission")
    audit("ticket_reject", user["email"], {"ticket_id": ticket_id})
    return update_ticket(ticket_id, {"status": "rejected"})
