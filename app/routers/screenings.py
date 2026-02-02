from fastapi import APIRouter
from app.schemas.screening_schema import ScreeningCreate
from app.services.screening_service import create_screening

router = APIRouter(prefix="/screenings", tags=["Screenings"])

@router.post("/", status_code=201)
async def create(screening: ScreeningCreate):
    screening_id = await create_screening(screening.dict())
    return {"id": screening_id}
