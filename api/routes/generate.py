from fastapi import APIRouter, Body
from services.copygen import generate_copy

router = APIRouter()

@router.post("/generate-copy")
def generate(data: dict = Body(...)):
    return generate_copy(data)