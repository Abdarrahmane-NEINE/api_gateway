import time
from threading import Lock

class RateLimiter:
    _instance = None
    _lock: Lock = Lock()
    # Implements the Singleton pattern to ensure a single limiter instance.
    def __new__(cls, limit: int = 100):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.limit = limit
                cls._instance.calls = {}
            return cls._instance

    def is_allowed(self, client_id: str) -> bool:
        current_time = time.time()
        window = 60  # 60 seconds window
        if client_id not in self.calls:
            self.calls[client_id] = []
        # Remove expired calls
        self.calls[client_id] = [call for call in self.calls[client_id] if call > current_time - window]
        if len(self.calls[client_id]) < self.limit:
            self.calls[client_id].append(current_time)
            return True
        return False
