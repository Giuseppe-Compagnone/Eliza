# src/engine/parser.py
"""
Input parser for ELIZA.
Cleans and tokenizes user input, applies pre-substitutions.
"""

import re
from utils import clean_text, split_sentences

class Parser:
    def __init__(self, pre_subs=None):
        """
        pre_subs: dictionary of pre-substitutions, e.g.
                  {"dont": "don't", "cant": "can't"}
        """
        self.pre_subs = pre_subs or {}

    def clean_input(self, text):
        """Lowercase the text and remove unnecessary punctuation."""
        text = text.lower()
        # Keep basic punctuation needed for sentence splitting
        text = re.sub(r"[^a-z0-9\s']", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def substitute_pre(self, text):
        """Apply pre-substitutions to normalize input."""
        words = text.split()
        substituted = [self.pre_subs.get(word, word) for word in words]
        return " ".join(substituted)

    def parse(self, text):
        """
        Clean text, split sentences, apply pre-substitutions, return normalized string
        """
        text = clean_text(text)
        sentences = split_sentences(text)
        processed = []
        for sentence in sentences:
            words = sentence.split()
            # apply pre-substitutions
            words = [self.pre_subs.get(w, w) for w in words]
            processed.append(" ".join(words))
        return " ".join(processed)
