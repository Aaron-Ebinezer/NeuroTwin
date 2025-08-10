from fastapi import APIRouter, Depends
from backend.agents.profiler.feedback import process_feedback
from backend.services.database.session import AsyncSession, get_db

router = APIRouter()

@router.post("/feedback")
async def submit_feedback(
    user_id: int,
    rating: int,
    comment: str = None,
    db: AsyncSession = Depends(get_db)
):
    new_tier = await process_feedback(db, user_id, rating, comment)
    return {"new_tier": new_tier}