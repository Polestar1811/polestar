from fastapi import APIRouter, Depends, HTTPException

from ..services.auth_service import current_user
from ..services.permission_service import can
from ..tools.inventory_tools import list_low_stock

router = APIRouter()


@router.get("/alerts")
def alerts(user: dict = Depends(current_user)):
    if not can(user["role"], "inventory:read") and user["role"] not in {"owner", "operations"}:
        raise HTTPException(status_code=403, detail="No permission")
    return list_low_stock()
