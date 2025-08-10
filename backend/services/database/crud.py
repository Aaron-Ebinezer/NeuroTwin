from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User

class UserCRUD:
    @staticmethod
    async def create_user(
        session: AsyncSession, username: str,
        password_hash: str, tier: str 
    ) -> User:
        user = User(
            username = username, password_hash = password_hash,
            tier = tier
            )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    
    @staticmethod
    async def get_user(session: AsyncSession, user_id: int) ->User:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalars().first()
    