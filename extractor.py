#!/usr/bin/env python3

import re
import json

class DataExtractor:
    """Robust data extraction regexes for common patterns."""
    def __init__(self):
        # Pre-compiled regex patterns for different data types
        self.patterns = {
            # Matches emails like user@example.com
            'email': re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}\b'),
            # Matches http and https URLs
            'url': re.compile(r'https?://[^\s\)\]\}\,>"\']+'),
            # Matches phone numbers in different formats: (123) 456-7890, 123-456-7890, 123.456.7890
            'phone': re.compile(r'(?:\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\b\d{10}\b)'),
            # Matches credit card numbers (with space or dash separators)
            'credit_card': re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b'),
            # Matches 24-hour times like 14:30
            'time_24h': re.compile(r'\b(?:[01][0-9]|2[0-3]):[0-5][0-9](?!\s?(?:AM|PM))\b', re.IGNORECASE),
            # Matches 12-hour times like 2:30 PM or 09:15 am
            'time_12h': re.compile(r'\b(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM)\b', re.IGNORECASE),
            # Matches hashtags like #Example, #Data_Extraction
            'hashtag': re.compile(r'(?<!#)#[A-Za-z0-9_]+\b'),
            # Matches currency values like $19.99, $1,234.56
            'currency': re.compile(r'\$(?:\d{1,3}(?:,\d{3})+|\d+(?!,))(?:\.\d{2})?(?![\d,])')
        }

    def _unique_sorted(self, items):
        # Remove duplicate items from the list while preserving the original order
        return sorted(list(dict.fromkeys(items)), key=lambda s: (len(s), s))

    def extract_all(self, text):
        """Extract all supported data types from a given text string."""
        return {
            'emails': self.patterns['email'].findall(text),
            'urls': self.patterns['url'].findall(text),
            'phone_numbers': self._unique_sorted(self.patterns['phone'].findall(text)),
            'credit_cards': self._unique_sorted(self.patterns['credit_card'].findall(text)),
            'time_12h': self._unique_sorted(self.patterns['time_12h'].findall(text)),
            'time_24h': self._unique_sorted(self.patterns['time_24h'].findall(text)),
            'hashtags': self._unique_sorted(self.patterns['hashtag'].findall(text)),
            'currency': self._unique_sorted(self.patterns['currency'].findall(text))
        }