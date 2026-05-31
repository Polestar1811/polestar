from fastapi import APIRouter, Depends, HTTPException

from ..agents.marketing_agent import run as marketing_run
from ..mock_data import DB
from ..schemas.campaign import CampaignGenerate
from ..services.audit_service import audit
from ..services.auth_service import current_user
from ..services.permission_service import can

router = APIRouter()


@router.post("/generate")
def generate(payload: CampaignGenerate, user: dict = Depends(current_user)):
    if not can(user["role"], "campaigns:write"):
        raise HTTPException(status_code=403, detail="No permission")
    result = marketing_run(f"{payload.goal} {payload.sku_id or ''}", {"actor": user})
    audit("campaign_generate", user["email"], result.structured_output)
    return result.structured_output


@router.post("/{campaign_id}/approve")
def approve(campaign_id: str, user: dict = Depends(current_user)):
    if user["role"] not in {"owner", "admin"}:
        raise HTTPException(status_code=403, detail="No permission")
    audit("campaign_approve", user["email"], {"campaign_id": campaign_id})
    for item in DB.campaigns:
        if item["campaign_id"] == campaign_id:
            item["status"] = "approved"
            return item
    return {"campaign_id": campaign_id, "status": "approved"}
