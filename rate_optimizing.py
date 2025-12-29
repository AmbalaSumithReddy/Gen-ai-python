import time
import requests
from rate_limitng import LIMIT

requests = []

MAX_REQUESTS = 10
WINDOW = 60  

delay = WINDOW / MAX_REQUESTS  

for i in range(MAX_REQUESTS):
    print("Request sent")
    time.sleep(delay)
print("All requests sent within rate limit.")
def is_allowed():
    current_time = time.time()
    while requests and current_time - requests[0] > WINDOW:
        requests.pop(0)
    if len(requests) < LIMIT:
        requests.append(current_time)
        return True
    else:
        return False
for i in range(5):
    if is_allowed():
        print("Request allowed")
    else:
        print("Rate limit exceeded")
    time.sleep(2)