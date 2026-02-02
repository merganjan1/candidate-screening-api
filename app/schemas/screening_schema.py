from pydantic import BaseModel

class ScreeningCreate(BaseModel):
    resume_id: str

class ScreeningResponse(BaseModel):
    resume_id: str
    score: float
    decision: str
