from fastapi import APIRouter, Depends, HTTPException
from backend.services.llm.groq import GroqService
from backend.agents.prompt_engineer.templates import generate_prompt
from backend.services.database.session import AsyncSession, get_db
from backend.models.user import User

router = APIRouter()

@router.post("/ask")
async def ask_question(
    question: str,
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    prompt = generate_prompt(question, user.tier)
    response = await GroqService().get_response(prompt)
    
    return {
        "answer": response,
        "tier": user.tier
    }