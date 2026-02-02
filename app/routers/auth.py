from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserLogin
from app.db.mongodb import users_collection
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(user: UserCreate):
    # 1️⃣ email bor-yo‘qligini tekshiramiz
    existing = await users_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    # 2️⃣ passwordni tozalaymiz (MUHIM!)
    password = user.password.strip()

    # 3️⃣ user dict tayyorlaymiz
    user_dict = {
        "email": user.email,
        "password": hash_password(password),
        "role": user.role
    }

    # 4️⃣ DB ga yozamiz
    await users_collection.insert_one(user_dict)

    return {"msg": "registered"}


@router.post("/login")
async def login(data: UserLogin):
    user = await users_collection.find_one({"email": data.email})
    if not user or not verify_password(data.password.strip(), user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "user_id": str(user["_id"]),
        "role": user["role"]
    })

    return {"access_token": token}
