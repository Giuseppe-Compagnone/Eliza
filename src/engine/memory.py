# src/engine/memory.py
"""
Memory module for ELIZA.
Stores and retrieves sentences in FIFO order, simulating the original DOCTOR memory.
"""

from collections import deque

class Memory:
    def __init__(self, max_size=50):
        """
        Initialize memory with optional maximum size.
        """
        self.max_size = max_size
        self.store = deque(maxlen=max_size)  # oldest sentences discarded automatically

    def remember(self, sentence):
        """
        Add a sentence to memory.
        Strips whitespace and ignores empty strings.
        """
        sentence = sentence.strip()
        if sentence:
            self.store.append(sentence)

    def recall(self):
        """
        Retrieve the oldest sentence from memory.
        Returns None if memory is empty.
        """
        if self.store:
            return self.store.popleft()  # remove from memory when recalled
        return None

    def is_empty(self):
        """
        Check if memory is empty.
        """
        return len(self.store) == 0
