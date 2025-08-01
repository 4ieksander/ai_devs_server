# app/routes.py — definicje tras
from fastapi import APIRouter
from app.utils import get_answer_with_position, security_check
from app.models import S04E04_AI_DEVS_INPUT
router = APIRouter()

@router.get("/hello")
async def hello():
    return {"message": "Hello, FastAPI!"}

@router.post("/map_instructions")
async def map_instructions(user_input: S04E04_AI_DEVS_INPUT):
    return get_answer_with_position(user_input)

@router.post("/serce")
async def serce(user_input):
    return security_check(user_input)
