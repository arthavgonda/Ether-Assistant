import psutil
import os

class MemoryMonitor:
    def __init__(self, max_mb: int = 100):
        self._max_bytes = max_mb * 1024 * 1024
        self._process = psutil.Process(os.getpid())
    
    def get_usage(self) -> int:
        # Returns memory usage in bytes
        return self._process.memory_info().rss
    
    def get_usage_mb(self) -> float:
        return self.get_usage() / (1024 * 1024)
    
    def is_under_pressure(self) -> bool:
        # Returns True if using >80% of budget
        return self.get_usage() > (self._max_bytes * 0.8)
    
    def get_percentage(self) -> float:
        return (self.get_usage() / self._max_bytes) * 100