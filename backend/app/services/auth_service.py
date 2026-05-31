from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from ..config import settings
from ..mock_data import DB

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login", auto_error=False)
ALGORITHM = "HS256"


def create_token(email: str, role: str) -> str:
    payload = {"sub": email, "role": role, "exp": datetime.utcnow() + timedelta(hours=8)}
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def authenticate(email: str, password: str) -> dict:
    DB.ensure_seeded()
    user = next((u for u in DB.users if u["email"] == email), None)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid account")
    return {**user, "access_token": create_token(user["email"], user["role"])}


def current_user(token: str | None = Depends(oauth2_scheme)) -> dict:
    if not token:
        return {"email": "owner@example.com", "role": "owner"}
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        return {"email": payload["sub"], "role": payload["role"]}
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc
