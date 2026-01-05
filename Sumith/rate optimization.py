import time

class tokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate  # tokens per second
        self.capacity = capacity  # maximum number of tokens
        self.tokens = capacity  # current number of tokens
        self.last_checked = time.time()

    def allow(self):
        now = time.time()
        elapsed = now - self.last_checked
        added_tokens = elapsed * self.rate
        self.tokens = min(self.capacity, self.tokens + added_tokens)
        self.last_checked = now

    def consume(self, tokens=1):
        self._add_tokens()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False
    
    def rate_limited(limiter: RateLimiter):
        """Decorator factory that uses the given RateLimiter"""
    def decorator(func):
        def wrapper(user_id, *args, **kwargs):
            if not limiter.is_allowed(user_id):
                raise PermissionError("Rate limit exceeded")
                return func(user_id, *args, **kwargs)
            return wrapper
        return decorator


# Example usage
if __name__ == "__main__":
    limiter = RateLimiter(limit=3, time_window=10)  # 3 requests per 10 seconds
    user = "alice"

    for i in range(6):
        print(f"Attempt {i+1}: allowed={limiter.is_allowed(user)}")
        time.sleep(1)