import hashlib
import time
from typing import Optional, Dict, Tuple, Callable
import numpy as np


class CommandCache:
    def __init__(self, max_entries: int = 100, ttl_seconds: int = 3600):
        self._max_entries = max_entries
        self._ttl = ttl_seconds
        self._cache: Dict[str, Tuple[str, int, int]] = {}
        self._fingerprints: Dict[str, str] = {}
        self._audio_buffer = np.zeros(1000, dtype=np.float32) # REUSABLE BUFFER
    
    def _compute_audio_fingerprint(self, audio_data: np.ndarray) -> str:
        if audio_data is None or len(audio_data) == 0:
            return ""
        
        step = max(1, len(audio_data) // 100) # getting started with 100 samples
        sample_size = min(100, len(audio_data) // step)

        for i in range(sample_size):
            self._audio_buffer[i] = audio_data[i * step]
        
        mean = np.mean(self._audio_buffer[:sample_size])
        std = np.std(self._audio_buffer[:sample_size]) + 1e-10
        self._audio_buffer[:sample_size] = (self._audio_buffer[:sample_size] - mean) / std

        quantized = np.round(self._audio_buffer[:sample_size] * 10).astype(np.int8)
        return hashlib.md5(quantized.tobytes()).hexdigest()[:16]
    
    def _compute_text_hash(self, text: str) -> str:
        return hashlib.md5(text.lower().strip().encode()).hexdigest()[:16]
    
    def cache_command(self, command_text: str, action_result: str, audio_data: Optional[np.ndarray] = None) -> None:
        text_hash = self._compute_text_hash(command_text)
        timestamp = int(time.time())
        hit_count = 1
        
        if text_hash in self._cache:
            _, _, hit_count = self._cache[text_hash]
            hit_count += 1
        
        self._cache[text_hash] = (action_result, timestamp, hit_count)
        
        if audio_data is not None:
            fingerprint = self._compute_audio_fingerprint(audio_data)
            if fingerprint:
                self._fingerprints[fingerprint] = text_hash
        
        self._evict_if_needed()
    
    def get_cached_action(self, command_text: str) -> Optional[str]:
        text_hash = self._compute_text_hash(command_text)
        return self._get_by_hash(text_hash)
    
    def get_action_by_audio(self, audio_data: np.ndarray) -> Optional[Tuple[str, str]]:
        fingerprint = self._compute_audio_fingerprint(audio_data)
        if not fingerprint or fingerprint not in self._fingerprints:
            return None
        
        text_hash = self._fingerprints[fingerprint]
        action = self._get_by_hash(text_hash)
        if action:
            for cmd_hash, (result, ts, hits) in self._cache.items():
                if cmd_hash == text_hash:
                    return (action, cmd_hash)
        return None
    
    def _get_by_hash(self, text_hash: str) -> Optional[str]:
        if text_hash not in self._cache:
            return None
        
        action, timestamp, hits = self._cache[text_hash]
        if int(time.time()) - timestamp > self._ttl:
            del self._cache[text_hash]
            self._fingerprints = {k: v for k, v in self._fingerprints.items() if v != text_hash}
            return None
        
        self._cache[text_hash] = (action, timestamp, hits + 1)
        return action
    
    def _evict_if_needed(self) -> None:
        if len(self._cache) <= self._max_entries:
            return
        
        current_time = int(time.time())
        expired = [k for k, (_, ts, _) in self._cache.items() if current_time - ts > self._ttl]
        for k in expired:
            del self._cache[k]
        
        if len(self._cache) > self._max_entries:
            sorted_entries = sorted(self._cache.items(), key=lambda x: (x[1][2], x[1][1]))
            to_remove = len(self._cache) - self._max_entries
            for k, _ in sorted_entries[:to_remove]:
                del self._cache[k]
        
        valid_hashes = set(self._cache.keys())
        self._fingerprints = {k: v for k, v in self._fingerprints.items() if v in valid_hashes}
    
    def get_frequent_commands(self, limit: int = 10) -> list:
        sorted_commands = sorted(
            self._cache.items(),
            key=lambda x: x[1][2],
            reverse=True
        )[:limit]
        return [(hash_val, hits) for hash_val, (_, _, hits) in sorted_commands]
    
    def clear(self) -> None:
        self._cache.clear()
        self._fingerprints.clear()
    
    def to_dict(self) -> Dict:
        return {
            'cache': {k: {'action': v[0], 'timestamp': v[1], 'hits': v[2]} for k, v in self._cache.items()},
            'fingerprints': self._fingerprints
        }
    
    def from_dict(self, data: Dict) -> None:
        self.clear()
        cache_data = data.get('cache', {})
        for k, v in cache_data.items():
            self._cache[k] = (v['action'], v['timestamp'], v['hits'])
        self._fingerprints = data.get('fingerprints', {})
        self._evict_if_needed()

