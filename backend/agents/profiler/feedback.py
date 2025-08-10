from models.user import User, Feedback
from .rules import calculate_user_tier

async def process_feedback(
        session: AsyncSession, user_id: int,
        rating: int, comment: str = None
) -> str:
    feedback = Feedback(
        user_id=user_id,
        rating=rating,
        comment=comment
    )
    session.add(feedback)
    user = await session.get(User, user_id)
    if len(user.feedbacks) % 3 == 0:
        new_tier = await calculate_user_tier(user)
        user.tier = new_tier
    
    await session.commit()
    return user.tier

