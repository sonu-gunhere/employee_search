from collections import defaultdict, deque
import time
import time
from functools import wraps
from fastapi import Request, HTTPException

RATE_LIMIT = 10  # 10 requests
TIME_WINDOW = 60  # 60 seconds
rate_limit_store = defaultdict(deque)

def is_allowed(user_ip: str) -> bool:
    now = time.time()
    window = rate_limit_store[user_ip]

    while window and window[0] <= now - TIME_WINDOW:
        window.popleft()

    if len(window) < RATE_LIMIT:
        window.append(now)
        return True
    return False


def rate_limit(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        client_ip = request.client.host
        res = is_allowed(client_ip)
        if not res:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        return await func(request, *args, **kwargs)

    return wrapper