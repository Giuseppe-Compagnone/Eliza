# src/utils/text_utils.py
"""
Text utility functions for ELIZA.
Contains generic text processing functions: cleaning, tokenization, sentence splitting.
"""

import re

def clean_text(text):
    """
    Lowercase, strip leading/trailing spaces, remove extra spaces.
    """
    text = text.lower().strip()
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    return text

def split_sentences(text):
    """
    Split text into sentences using punctuation as delimiters.
    Returns a list of cleaned, non-empty sentences.
    """
    # Split on ., !, ?
    sentences = re.split(r'[.!?]+', text)
    # Remove empty strings and strip spaces
    return [s.strip() for s in sentences if s.strip()]

def tokenize(text):
    """
    Split text into words, removing punctuation.
    Returns a list of words.
    """
    # Remove punctuation (keep only letters, numbers, whitespace)
    text = re.sub(r'[^\w\s]', '', text)
    # Split by whitespace
    return text.split()
