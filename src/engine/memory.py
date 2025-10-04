# src/engine/memory.py
"""
Memory module for ELIZA.
Stores and retrieves sentences to simulate 'memory' from the original DOCTOR script.
"""

import random
from collections import deque

class Memory:
    def __init__(self, max_size=50):
        """
        Initialize memory with optional maximum size.
        """
        self.max_size = max_size
        self.store = deque(maxlen=max_size)  # automatic discard of oldest

    def remember(self, sentence):
        """
        Add a sentence to memory.
        """
        sentence = sentence.strip()
        if sentence:
            self.store.append(sentence)

    def recall(self):
        """
        Retrieve a random sentence from memory.
        Returns None if memory is empty.
        """
        if not self.store:
            return None
        return random.choice(self.store)
