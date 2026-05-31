from fastapi import APIRouter, Depends, HTTPException

from ..services.auth_service import current_user
from ..services.permission_service import can
from ..tools.order_tools import get_order, get_tracking

router = APIRouter()


@router.get("/{order_no}")
def order_detail(order_no: str, user: dict = Depends(current_user)):
    if not can(user["role"], "orders:read"):
        raise HTTPException(status_code=403, detail="No permission")
    return get_order(order_no)


@router.get("/{order_no}/tracking")
def tracking(order_no: str, user: dict = Depends(current_user)):
    if not can(user["role"], "orders:read"):
        raise HTTPException(status_code=403, detail="No permission")
    return get_tracking(order_no)
