import atexit
from typing import Optional, Dict, List, Any
import numpy as np

from .ring_buffer import CommandRingBuffer
from .command_cache import CommandCache
from .persistence import MemoryPersistence
from .context_summary import ContextSummarizer
from .memory_monitor import MemoryMonitor


class MemoryManager:
    _instance: Optional['MemoryManager'] = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, buffer_size: int = 50, cache_size: int = 100, storage_dir: Optional[str] = None, max_memory_mb: int = 100):
        if hasattr(self, '_initialized') and self._initialized:
            return
        
        self._buffer = CommandRingBuffer(size=buffer_size)
        self._cache = CommandCache(max_entries=cache_size)
        self._persistence = MemoryPersistence(storage_dir=storage_dir)
        self._summarizer = None #create when demand
        self._initialized = True
        self._auto_save_enabled = True
        self._monitor = MemoryMonitor(max_memory_mb)
        self._aggressive_mode = False
        
        self._load_from_disk()
        atexit.register(self._save_to_disk)
    
    def add_command(self, command: str, result: str = "", metadata: Optional[Dict] = None, audio_data: Optional[np.ndarray] = None) -> None:
        if self._monitor.is_under_pressure():
            self._enter_aggressive_mode()
        
        self._buffer.add(command, result, metadata)
        if not self._aggressive_mode and audio_data is not None:
            self._cache.cache_command(command, result, audio_data)
        else:
            self._cache.cache_command(command, result, None)
    

    def _enter_aggressive_mode(self) -> None:
        if not self._aggressive_mode:
            self._aggressive_mode = True
            # Clear audio fingerprints (biggest memory users)
            self._cache._fingerprints.clear()
            # Reduce cache size
            self._cache._max_entries = 50
            self._cache._evict_if_needed()
    

    def _exit_aggressive_mode(self) -> None:
        if self._aggressive_mode and not self._monitor.is_under_pressure():
            self._aggressive_mode = False
            self._cache._max_entries = 100
    
    def get_recent_commands(self, count: int = 10) -> List[Dict]:
        entries = self._buffer.get_recent(count)
        return [e.to_dict() for e in entries]
    
    def search_commands(self, keyword: str) -> List[Dict]:
        entries = self._buffer.search(keyword)
        return [e.to_dict() for e in entries]
    
    def get_cached_action(self, command: str) -> Optional[str]:
        return self._cache.get_cached_action(command)
    
    def get_action_by_audio(self, audio_data: np.ndarray) -> Optional[tuple]:
        return self._cache.get_action_by_audio(audio_data)
    
    def get_context(self, command: str) -> Dict:
        recent = self.get_recent_commands(5)
        summary = self._summarizer.get_context_for_command(command)
        cached = self._cache.get_cached_action(command)
        
        return {
            'recent_commands': recent,
            'context_hints': summary,
            'cached_action': cached,
            'command_count': self._buffer.count
        }
    
    def get_summary(self) -> Dict:
        return self._summarizer.get_summary()
    
    def _update_summary(self) -> None:
        commands = self._buffer.to_list()
        self._summarizer.analyze_commands(commands)
    
    def _load_from_disk(self) -> None:
        commands = self._persistence.load_commands()
        if commands:
            self._buffer.from_list(commands)
        
        cache_data = self._persistence.load_cache()
        if cache_data:
            self._cache.from_dict(cache_data)
        
        summary_data = self._persistence.load_summary()
        if summary_data:
            self._summarizer.from_dict(summary_data)
    
    def _save_to_disk(self) -> None:
        if not self._auto_save_enabled:
            return
        
        self._persistence.save_commands(self._buffer.to_list())
        self._persistence.save_cache(self._cache.to_dict())
        self._persistence.save_summary(self._summarizer.to_dict())
    
    def force_save(self) -> None:
        self._save_to_disk()
    
    def clear_all(self) -> None:
        self._buffer.clear()
        self._cache.clear()
        self._persistence.clear_all()
        self._summarizer = ContextSummarizer()
    
    def set_auto_save(self, enabled: bool) -> None:
        self._auto_save_enabled = enabled
    
    @property
    def stats(self) -> Dict:
        return {
            'commands_stored': self._buffer.count,
            'cache_entries': len(self._cache._cache),
            'audio_fingerprints': len(self._cache._fingerprints),
            'buffer_full': self._buffer.is_full,
            'storage_path': self._persistence.storage_path
        }
    
    @property
    def summarizer(self) -> ContextSummarizer:
        """Lazy-load summarizer"""
        if self._summarizer is None:
            self._summarizer = ContextSummarizer()
            summary_data = self._persistence.load_summary()
            if summary_data:
                self._summarizer.from_dict(summary_data)
        return self._summarizer
    
    def get_summary(self) -> Dict:
        return self.summarizer.get_summary()
    
    def _update_summary(self) -> None:
        commands = self._buffer.to_list()
        self.summarizer.analyze_commands(commands)
