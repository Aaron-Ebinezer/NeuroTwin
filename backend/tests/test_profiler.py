# backend/tests/test_profiler.py
import pytest
from backend.agents.profiler.rules import calculate_user_tier
from backend.models.user import User, Feedback

@pytest.mark.asyncio
@pytest.mark.parametrize("initial_score,feedbacks,expected_tier", [
    (1.0, [], "basic"),  # No feedback retains initial tier
    (1.0, [1, 1], "basic"),  # Low scores stay basic
    (3.0, [4, 5], "intermediate"),  # Upgrade threshold
    (4.5, [5, 5], "advanced"),  # Jump to advanced
    (5.0, [1, 2], "intermediate"),  # High initial, low feedback -> downgrade
])
async def test_tier_calculation(initial_score, feedbacks, expected_tier):
    user = User(initial_assessment=initial_score)
    user.feedbacks = [Feedback(rating=r) for r in feedbacks]
    result = await calculate_user_tier(user)
    assert result == expected_tier