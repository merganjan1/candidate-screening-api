from fastapi import Depends, HTTPException
from jose import jwt
from app.core.jwt import SECRET_KEY, ALGORITHM

def require_admin(token: str = Depends()):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload.get("role") != "admin":
        raise HTTPException(403, "Forbidden")
