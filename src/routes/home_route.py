# routes/home_route.py

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.get(
    "/",
    response_class=PlainTextResponse,
    tags=["Root"],
    summary="Home endpoint",
    description="Simple health probe for root access.",
    responses={200: {"description": "Service is up"}},
)
def home():
    return "ok"
