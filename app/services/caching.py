cache_store = {}

# For simplicity, not handling expiry in the v1.
def set_cache(key: str, value, expire: int = 60):
    cache_store[key] = value

def get_cache(key: str):
    return cache_store.get(key)
