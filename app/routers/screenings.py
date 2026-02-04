from fastapi import APIRouter, HTTPException, BackgroundTasks
from bson import ObjectId
from datetime import datetime

from app.schemas.screening_schema import ScreeningCreate
from app.services.screening_service import create_screening
from app.services.background import process_screening
from app.db.mongodb import screenings_collection

router = APIRouter(
    prefix="/screenings",
    tags=["Screenings"]
)

# ==================================================
# CREATE SCREENING (POST) — AI BACKGROUND ISHLAYDI
# ==================================================
@router.post("/", status_code=201)
async def create_screening_endpoint(
    screening: ScreeningCreate,
    background_tasks: BackgroundTasks
):
    # 1. Screening yaratamiz
    screening_id = await create_screening(screening.dict())

    # 2. AI processing'ni background'da ishga tushiramiz
    background_tasks.add_task(
        process_screening,
        screening_id
    )

    return {
        "id": screening_id
    }


# ==================================================
# GET SCREENING BY ID (GET)
# ==================================================
@router.get("/{id}")
async def get_screening(id: str):
    # 1. ObjectId tekshiruvi
    try:
        oid = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid screening id")

    # 2. DB dan olish
    screening = await screenings_collection.find_one({"_id": oid})
    if not screening:
        raise HTTPException(status_code=404, detail="Screening not found")

    # 3. Datetime serializer
    def serialize_dt(value):
        if isinstance(value, datetime):
            return value.isoformat()
        return value

    # 4. Response
    return {
        "id": str(screening["_id"]),
        "resume_id": str(screening.get("resume_id")),
        "status": screening.get("status"),
        "ai_department": screening.get("ai_department"),
        "ai_department_score": screening.get("ai_department_score"),
        "created_at": serialize_dt(screening.get("created_at")),
        "scored_at": serialize_dt(screening.get("scored_at")),
    }
