from dataclasses import dataclass

@dataclass
class MemoryConfig:
    buffer_size: int
    cache_size: int
    enable_audio_fingerprints: bool
    enable_summarizer: bool
    max_memory_mb: int
    compression_enabled: bool
    
    @classmethod
    def for_slow_device(cls):
        return cls(
            buffer_size=30,
            cache_size=50,
            enable_audio_fingerprints=False,
            enable_summarizer=False,
            max_memory_mb=50,
            compression_enabled=True
        )
    
    @classmethod
    def for_normal_device(cls):
        return cls(
            buffer_size=50,
            cache_size=100,
            enable_audio_fingerprints=True,
            enable_summarizer=True,
            max_memory_mb=100,
            compression_enabled=True
        )
    
    @classmethod
    def for_fast_device(cls):
        return cls(
            buffer_size=100,
            cache_size=200,
            enable_audio_fingerprints=True,
            enable_summarizer=True,
            max_memory_mb=200,
            compression_enabled=False
        )