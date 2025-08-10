BANNED_WORDS = ["hack", "exploit", "malware"]

def validate_prompt(prompt: str) -> bool:
    lower_prompt = prompt.lower()
    return not any(word in lower_prompt for word in BANNED_WORDS)