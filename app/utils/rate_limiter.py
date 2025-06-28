from collections import defaultdict, deque
import time

RATE_LIMIT = 10  # 10 requests
TIME_WINDOW = 60  # 60 seconds
rate_limit_store = defaultdict(deque)

def is_allowed(user_id: str) -> bool:
    now = time.time()
    window = rate_limit_store[user_id]

    while window and window[0] <= now - TIME_WINDOW:
        window.popleft()

    if len(window) < RATE_LIMIT:
        window.append(now)
        return True
    return False