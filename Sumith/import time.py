import time

request = []
LIMIT = 5
TIME_WINDOW = 60

def is_allowed(user_id):
    current_time = time.time

    if user_id not in request:
        request[user_id] = []

    request[user_id] = [
        t for t in request[user_id]
        if current_time -t < TIME_WINDOW
    ]

    if len(request[user_id]) < LIMIT:
        
