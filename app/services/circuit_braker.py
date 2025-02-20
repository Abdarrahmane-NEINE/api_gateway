"""
Implements basic circuit breaker logic to prevent overloading backend services.
"""
class CircuitBreaker:
    def __init__(self, failure_threshold: int = 3):
        self.failure_threshold = failure_threshold
        self.failure_count = 0
        self.open = False

    def record_failure(self):
        self.failure_count += 1
        if self.failure_count >= self.failure_threshold:
            self.open = True

    def record_success(self):
        self.failure_count = 0
        self.open = False

    def is_open(self) -> bool:
        return self.open
