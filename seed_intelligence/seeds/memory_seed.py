import time


class MemorySeed:
    """Stores experience with importance and trust."""

    def __init__(self):
        self.memory = {}

    def store(self, key, value, importance=1.0, trust=0.5, source="unknown", private=False):
        self.memory[key] = {
            "value": value,
            "importance": importance,
            "trust": trust,
            "source": source,
            "private": private,
            "timestamp": time.time(),
        }

    def recall(self, key):
        item = self.memory.get(key)
        return item["value"] if item else None

    def recall_all(self):
        return self.memory
