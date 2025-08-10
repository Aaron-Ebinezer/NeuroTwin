TIER_PROMPTS = {
    "basic": "Explain this in simple terms suitable for a beginner: {question}",
    "intermediate": """Provide a detailed explanation of {question} with:
    - Key concepts
    - 1 practical example
    - Common misconceptions""",
    "advanced": """Analyze {question} with:
    - Current research trends
    - Mathematical formulations
    - Comparative approaches"""
}

def generate_prompt(question: str, tier: str) -> str:
    base_prompt = TIER_PROMPTS.get(tier, TIER_PROMPTS["basic"])
    return base_prompt.format(question=question)