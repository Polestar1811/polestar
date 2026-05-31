from fastapi import APIRouter, Depends, HTTPException

from ..agents.reporting_agent import run as report_run
from ..services.audit_service import audit
from ..services.auth_service import current_user
from ..services.permission_service import can
from ..tools.report_tools import analyze_uploaded_excel

router = APIRouter()


@router.get("/summary")
def summary(user: dict = Depends(current_user)):
    if not can(user["role"], "reports:read"):
        raise HTTPException(status_code=403, detail="No permission")
    audit("view_report", user["email"], {"report": "summary"})
    return report_run("本周销售情况").structured_output


@router.post("/analyze")
def analyze(file_id: str, user: dict = Depends(current_user)):
    if not can(user["role"], "reports:read"):
        raise HTTPException(status_code=403, detail="No permission")
    return analyze_uploaded_excel(file_id)
