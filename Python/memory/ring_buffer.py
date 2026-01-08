import time
from typing import Optional, Dict, List, Any


class CommandEntry:
    __slots__ = ['command', 'result', 'timestamp', 'metadata', '_cached_dict']
    
    def __init__(self, command: str = "", result: str = "", timestamp: int = 0, metadata: Optional[Dict] = None):
        self.command = command[:100] if command else ""
        self.result = result[:200] if result else ""
        self.timestamp = timestamp
        self.metadata = metadata or {}
        self._cached_dict = None  # Cache serialization
    
    def to_dict(self) -> Dict:
        if self._cached_dict is None:
            self._cached_dict = {
                'command': self.command,
                'result': self.result,
                'timestamp': self.timestamp,
                'metadata': self.metadata
            }
        return self._cached_dict
    
    def __sizeof__(self) -> int:
        return (len(self.command) + len(self.result) + 8 + sum(len(str(k)) + len(str(v)) for k, v in self.metadata.items()))
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'CommandEntry':
        return cls(
            command=data.get('command', ''),
            result=data.get('result', ''),
            timestamp=data.get('timestamp', 0),
            metadata=data.get('metadata', {})
        )


class CommandRingBuffer:
    def __init__(self, size: int = 50):
        self._size = size
        self._buffer: List[Optional[CommandEntry]] = [None] * size
        self._head = 0
        self._count = 0
    
    def add(self, command: str, result: str = "", metadata: Optional[Dict] = None) -> None:
        entry = CommandEntry(
            command=command,
            result=result,
            timestamp=int(time.time()),
            metadata=metadata
        )
        self._buffer[self._head] = entry
        self._head = (self._head + 1) % self._size
        if self._count < self._size:
            self._count += 1
    
    def get_recent(self, count: int = 10) -> List[CommandEntry]:
        result = []
        actual_count = min(count, self._count)
        for i in range(actual_count):
            idx = (self._head - 1 - i) % self._size
            entry = self._buffer[idx]
            if entry:
                result.append(entry)
        return result
    
    def get_all(self) -> List[CommandEntry]:
        return self.get_recent(self._count)
    
    def search(self, keyword: str) -> List[CommandEntry]:
        keyword_lower = keyword.lower()
        results = []
        for entry in self.get_all():
            if keyword_lower in entry.command.lower():
                results.append(entry)
        return results
    
    def get_by_app(self, app_name: str) -> List[CommandEntry]:
        app_lower = app_name.lower()
        results = []
        for entry in self.get_all():
            if entry.metadata.get('app_name', '').lower() == app_lower:
                results.append(entry)
        return results
    
    def clear(self) -> None:
        self._buffer = [None] * self._size
        self._head = 0
        self._count = 0
    
    def to_list(self) -> List[Dict]:
        entries = self.get_all()
        return [entry.to_dict() for entry in reversed(entries)]
    
    def from_list(self, data: List[Dict]) -> None:
        self.clear()
        for item in data[-self._size:]:
            entry = CommandEntry.from_dict(item)
            self._buffer[self._head] = entry
            self._head = (self._head + 1) % self._size
            if self._count < self._size:
                self._count += 1
    
    @property
    def count(self) -> int:
        return self._count
    
    @property
    def is_full(self) -> bool:
        return self._count >= self._size
    
    def add_batch(self, commands: List[tuple]) -> None:
        """Add multiple commands at once - more efficient"""
        timestamp = int(time.time())
        for cmd, result, metadata in commands:
            entry = CommandEntry(cmd, result, timestamp, metadata)
            self._buffer[self._head] = entry
            self._head = (self._head + 1) % self._size
            if self._count < self._size:
                self._count += 1
            timestamp += 1
