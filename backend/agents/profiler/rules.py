TIER_THRESHOLDS = {
    "basic": {"max_score": 2.5},
    "intermediate": {"min_score": 2.5, "max_score": 4.0},
    "advanced": {"min_score": 4.0}
}
async def calculate_user_tier(user) -> str:
    if not user.feedbacks:
        return user.tier
    
    avg_score = sum(fb.rating for fb in user.feedbacks) / len(user.feedbacks)
    adjusted_score = (user.initial_assessment * 0.4) + (avg_score * 0.6)

    if adjusted_score >= TIER_THRESHOLDS["advanced"]["min_score"]:
        return "advanced"
    elif adjusted_score >= TIER_THRESHOLDS["intermediate"]["min_score"]:
        return "intermediate"
    return "basic"