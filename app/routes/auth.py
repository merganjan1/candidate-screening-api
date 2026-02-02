from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserLogin
from app.db.database import db
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])
users = db["users"]

@router.post("/register")
async def register(user: UserCreate):
    user.password = hash_password(user.password)
    await users.insert_one(user.dict())
    return {"msg": "registered"}

@router.post("/login")
async def login(data: UserLogin):
    user = await users.find_one({"email": data.email})
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({
        "user_id": str(user["_id"]),
        "role": user["role"]
    })
    return {"access_token": token}
