from fastapi import APIRouter, Depends, HTTPException

from ..llm.provider import LLMProvider
from ..mock_data import DB
from ..services.auth_service import current_user

router = APIRouter()


@router.get("/llm-logs")
def llm_logs(user: dict = Depends(current_user)):
    if user["role"] not in {"owner", "admin"}:
        raise HTTPException(status_code=403, detail="No permission")
    return {"items": DB.llm_logs}


@router.get("/audit-logs")
def audit_logs(user: dict = Depends(current_user)):
    if user["role"] not in {"owner", "admin"}:
        raise HTTPException(status_code=403, detail="No permission")
    return {"items": DB.audit_logs}


@router.post("/model-test")
async def model_test(user: dict = Depends(current_user)):
    if user["role"] not in {"owner", "admin"}:
        raise HTTPException(status_code=403, detail="No permission")
    result = await LLMProvider().chat(
        messages=[
            {"role": "system", "content": "你是 TeaAgent 模型连通性测试助手，只返回一句简短中文。"},
            {"role": "user", "content": "请回复：模型连接正常"},
        ],
        max_tokens=80,
        temperature=0,
    )
    return {
        "provider": result.provider,
        "model": result.model,
        "content": result.content,
        "latency_ms": result.latency_ms,
        "usage": result.usage,
        "mock": result.content == "{}",
    }
