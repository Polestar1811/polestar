from fastapi import APIRouter
from pydantic import BaseModel

from ..services.auth_service import authenticate

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    password: str = ""


@router.post("/login")
def login(payload: LoginRequest):
    user = authenticate(payload.email, payload.password)
    return {"access_token": user["access_token"], "token_type": "bearer", "user": {"email": user["email"], "role": user["role"]}}
