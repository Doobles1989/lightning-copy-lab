from fastapi import APIRouter, Body
from services.copygen import generate_copy

router = APIRouter()

@router.post("/generate-copy")
def generate(data: dict = Body(...)):
    """
    Accepts:
    {
      "template": "landing_page",
      "variables": {
          "product_name": "Lightning Copy Lab",
          "features": "AI speed, human quality, fast turnaround",
          "audience": "freelancers and SaaS founders"
      }
    }
    """
    return generate_copy(data)
