from fastapi import APIRouter, Depends

from ..schemas.chat import ChatRequest, ChatResponse
from ..services.auth_service import current_user
from ..services.chat_service import chat

router = APIRouter()


@router.post("", response_model=ChatResponse)
def post_chat(payload: ChatRequest, user: dict = Depends(current_user)):
    context = {**payload.context, "actor": user}
    return chat(payload.message, payload.agent_type, context)
