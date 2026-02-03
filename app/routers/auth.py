from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user_schema import UserCreate
from app.db.mongodb import users_collection
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


# 📝 REGISTER — OCHIQ
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    existing = await users_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    user_dict = {
        "email": user.email,
        "password": hash_password(user.password.strip()),
        "role": user.role
    }

    await users_collection.insert_one(user_dict)
    return {"msg": "registered"}


# 🔐 LOGIN — OAUTH2 STANDARD
@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    # ⚠️ OAuth2 da username ishlatiladi (bizda email)
    user = await users_collection.find_one(
        {"email": form_data.username}
    )

    if not user or not verify_password(
        form_data.password.strip(),
        user["password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({
        "user_id": str(user["_id"]),
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
