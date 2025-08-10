from fastapi import APIRouter, Depends
from backend.services.database.crud import UserCRUD
from backend.services.database.session import AsyncSession, get_db

router = APIRouter()

@router.get("/{user_id}")
async def get_user_profile(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user = await UserCRUD.get_user(db, user_id)
    return user