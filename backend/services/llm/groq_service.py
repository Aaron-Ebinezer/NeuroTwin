import os
from groq import Groq
from typing import Optional
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parents[2] / ".env"
print("Looking for .env at:", env_path)
load_dotenv(dotenv_path=env_path)

# Debug print
print("GROQ_API_KEY loaded:", os.getenv("GROQ_API_KEY"))

class GroqService:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

        self.client = Groq(api_key=api_key)
        self.model = "llama3-8b-8192"

    async def get_response(self, prompt: str, max_tokens: int = 1024) -> Optional[str]:
        try:
            completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model,
                temperature=0.7,
                max_tokens=max_tokens
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Groq API error: {e}")
            return None
