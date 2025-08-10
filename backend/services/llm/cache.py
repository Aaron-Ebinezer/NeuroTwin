from cachetools import TTLCache
from typing import Optional

response_cache = TTLCache(maxsize=1000, ttl=300)  # 5-minute cache

def get_cached_response(prompt: str) -> Optional[str]:
    return response_cache.get(prompt)

def cache_response(prompt: str, response: str):
    response_cache[prompt] = response