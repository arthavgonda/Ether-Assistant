import time
from typing import Dict, List, Optional
from collections import Counter


class ContextSummarizer:
    def __init__(self):
        self._app_usage: Counter = Counter()
        self._action_types: Counter = Counter()
        self._hourly_activity: Dict[int, int] = {h: 0 for h in range(24)}
        self._total_commands = 0
        self._last_summary_time = 0
        self._common_patterns: List[str] = []
    
    def analyze_commands(self, commands: List[Dict]) -> Dict:
        self._reset_counters()
        
        for cmd in commands:
            self._total_commands += 1
            
            metadata = cmd.get('metadata', {})
            app_name = metadata.get('app_name', 'unknown')
            action_type = metadata.get('action_type', 'unknown')
            timestamp = cmd.get('timestamp', 0)
            
            self._app_usage[app_name] += 1
            self._action_types[action_type] += 1
            
            if timestamp:
                hour = (timestamp // 3600) % 24
                self._hourly_activity[hour] += 1
        
        self._extract_patterns(commands)
        self._last_summary_time = int(time.time())
        
        return self.get_summary()
    
    def _reset_counters(self) -> None:
        self._app_usage.clear()
        self._action_types.clear()
        self._hourly_activity = {h: 0 for h in range(24)}
        self._total_commands = 0
        self._common_patterns = []
    
    def _extract_patterns(self, commands: List[Dict]) -> None:
        command_texts = [cmd.get('command', '').lower() for cmd in commands]
        
        word_freq: Counter = Counter()
        for text in command_texts:
            words = text.split()
            for word in words:
                if len(word) > 2:
                    word_freq[word] += 1
        
        bigrams: Counter = Counter()
        for text in command_texts:
            words = text.split()
            for i in range(len(words) - 1):
                bigram = f"{words[i]} {words[i+1]}"
                bigrams[bigram] += 1
        
        self._common_patterns = [
            pattern for pattern, count in bigrams.most_common(10) if count >= 2
        ]
    
    def get_summary(self) -> Dict:
        peak_hour = max(self._hourly_activity, key=self._hourly_activity.get) if self._hourly_activity else 0
        
        return {
            'total_commands': self._total_commands,
            'top_apps': dict(self._app_usage.most_common(5)),
            'top_actions': dict(self._action_types.most_common(5)),
            'peak_hour': peak_hour,
            'hourly_distribution': self._hourly_activity,
            'common_patterns': self._common_patterns[:5],
            'summary_time': self._last_summary_time
        }
    
    def get_context_for_command(self, command: str) -> Dict:
        command_lower = command.lower()
        words = command_lower.split()
        
        relevant_apps = []
        relevant_actions = []
        
        for app in self._app_usage:
            if app.lower() in command_lower:
                relevant_apps.append(app)
        
        action_keywords = {
            'open': 'open',
            'close': 'close',
            'search': 'search',
            'find': 'search',
            'create': 'create',
            'delete': 'delete',
            'move': 'move',
            'copy': 'copy',
            'play': 'media',
            'pause': 'media',
            'stop': 'media'
        }
        
        for word in words:
            if word in action_keywords:
                relevant_actions.append(action_keywords[word])
        
        return {
            'relevant_apps': relevant_apps,
            'suggested_actions': relevant_actions,
            'matching_patterns': [p for p in self._common_patterns if any(w in p for w in words)]
        }
    
    def to_dict(self) -> Dict:
        return {
            'app_usage': dict(self._app_usage),
            'action_types': dict(self._action_types),
            'hourly_activity': self._hourly_activity,
            'total_commands': self._total_commands,
            'common_patterns': self._common_patterns,
            'summary_time': self._last_summary_time
        }
    
    def from_dict(self, data: Dict) -> None:
        self._app_usage = Counter(data.get('app_usage', {}))
        self._action_types = Counter(data.get('action_types', {}))
        self._hourly_activity = data.get('hourly_activity', {h: 0 for h in range(24)})
        self._hourly_activity = {int(k): v for k, v in self._hourly_activity.items()}
        self._total_commands = data.get('total_commands', 0)
        self._common_patterns = data.get('common_patterns', [])
        self._last_summary_time = data.get('summary_time', 0)

