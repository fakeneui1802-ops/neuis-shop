from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthResponse(BaseModel):
    status: str

@router.get("/", tags=["root"])
async def read_root():
    return {"message": "Hello from fastapi-starter-de!"}

@router.get("/health", response_model=HealthResponse, tags=["health"])
async def health():
    return HealthResponse(status="ok")
