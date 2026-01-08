import json
import os
from typing import Dict, Any, Optional
from pathlib import Path
import gzip

class MemoryPersistence:
    def __init__(self, storage_dir: Optional[str] = None, compress: bool = True):
        if storage_dir:
            self._storage_dir = Path(storage_dir)
        else:
            self._storage_dir = Path(__file__).parent / "data"
        
        self._storage_dir.mkdir(parents=True, exist_ok=True)
        self._commands_file = self._storage_dir / "commands.json"
        self._cache_file = self._storage_dir / "cache.json"
        self._summary_file = self._storage_dir / "summary.json"
        self._compress = compress
        if compress:
            self._commands_file = self._storage_dir / "commands.json.gz"
            self._cache_file = self._storage_dir / "cache.json.gz"
            self._summary_file = self._storage_dir / "summary.json.gz"
    
    def save_commands(self, commands_data: list) -> bool:
        return self._write_json(self._commands_file, commands_data)
    
    def load_commands(self) -> list:
        data = self._read_json(self._commands_file)
        return data if isinstance(data, list) else []
    
    def save_cache(self, cache_data: Dict) -> bool:
        return self._write_json(self._cache_file, cache_data)
    
    def load_cache(self) -> Dict:
        data = self._read_json(self._cache_file)
        return data if isinstance(data, dict) else {}
    
    def save_summary(self, summary_data: Dict) -> bool:
        return self._write_json(self._summary_file, summary_data)
    
    def load_summary(self) -> Dict:
        data = self._read_json(self._summary_file)
        return data if isinstance(data, dict) else {}
    
    def _write_json(self, filepath: Path, data: Any) -> bool:
        try:
            temp_file = filepath.with_suffix('.tmp')
            json_str = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

            if self._compress:
                with gzip.open(temp_file, 'wt', encoding='utf-8', compresslevel=6) as f:
                    f.write(json_str)
            else:
                with open(temp_file, 'w', encoding='utf-8') as f:
                    f.write(json_str)
            temp_file.replace(filepath)
            return True
        except Exception:
            return False
    
    def _read_json(self, filepath: Path) -> Any:
        try:
            if not filepath.exists():
                return None
            
            if self._compress and filepath.suffix == '.gz':
                with gzip.open(filepath, 'rt', encoding='utf-8') as f:
                    return json.load(f)
            else:
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            return None
    
    def clear_all(self) -> None:
        for f in [self._commands_file, self._cache_file, self._summary_file]:
            if f.exists():
                f.unlink()
    
    @property
    def storage_path(self) -> str:
        return str(self._storage_dir)

