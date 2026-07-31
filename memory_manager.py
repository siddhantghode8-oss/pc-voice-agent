"""Memory Manager - Maintains conversation context"""
import json
import logging
from typing import List, Dict
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class MemoryManager:
    """Manages conversation history for context-aware responses"""
    
    def __init__(self, max_history: int = 20):
        self.history: List[Dict] = []
        self.max_history = max_history
        self.context_file = Path("conversation_history.json")
        self.load_history()
    
    def add_user_message(self, content: str):
        """Add user message to history"""
        message = {
            "role": "user",
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.history.append(message)
        self._trim_history()
        self.save_history()
        logger.info(f"Added user message")
    
    def add_assistant_message(self, content: str):
        """Add assistant message to history"""
        message = {
            "role": "assistant",
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.history.append(message)
        self._trim_history()
        self.save_history()
        logger.info(f"Added assistant message")
    
    def add_system_message(self, content: str):
        """Add system message to history"""
        message = {
            "role": "system",
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.history.append(message)
        self._trim_history()
        self.save_history()
        logger.info(f"Added system message")
    
    def get_history(self) -> List[Dict]:
        """Get conversation history"""
        return self.history
    
    def get_last_n_messages(self, n: int) -> List[Dict]:
        """Get last N messages"""
        return self.history[-n:]
    
    def clear_history(self):
        """Clear conversation history"""
        self.history = []
        self.save_history()
        logger.info("History cleared")
    
    def _trim_history(self):
        """Keep only recent messages"""
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]
    
    def save_history(self):
        """Save history to file"""
        try:
            with open(self.context_file, 'w') as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save history: {e}")
    
    def load_history(self):
        """Load history from file"""
        try:
            if self.context_file.exists():
                with open(self.context_file, 'r') as f:
                    self.history = json.load(f)
                logger.info(f"Loaded {len(self.history)} messages from history")
        except Exception as e:
            logger.warning(f"Could not load history: {e}")
            self.history = []
