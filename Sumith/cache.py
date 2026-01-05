cache = {}

def get_data(key):
    if key in cache:
        return cache[key]
    else:
        # Simulate a time-consuming data retrieval process
        data = f"Data for {key}"
        cache[key] = data
        return data