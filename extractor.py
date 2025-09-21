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
    

def process_file(filename):
    """Read text from a file and extract all data types using the DataExtractor Class."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        
        extractor = DataExtractor()
        results = extractor.extract_all(text)
        return results
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def demo():
    """Run the demo extraction process using a provided or the default file."""
    import sys
    
    # Checks if user provides filename as command line argument, then uses it
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        # Otherwise, prompts user for filename if not provided use the default: sample_data.txt
        filename = input("Enter filename (or press Enter for 'sample_data.txt'): ").strip()
        if not filename:
            filename = 'sample_data.txt'
    
    print(f"Processing file: {filename}")
    results = process_file(filename)
    
    if not results:
        return
    
    # Print results in a readable format
    print("EXTRACTION RESULTS")
    # Print 40 equal to signs 
    print("=" * 40)
    
    categories = [
        ('Emails', results['emails']),
        ('URLs', results['urls']),
        ('Phones', results['phone_numbers']),
        ('Cards', results['credit_cards']),
        ('12h Time', results['time_12h']),
        ('24h Time', results['time_24h']),
        ('Tags', results['hashtags']),
        ('Currency', results['currency'])
    ]
    
    for name, items in categories:
        print(f"\n{name}: {len(items)} found")
        for item in items:
            print(f"  • {item}")
    
    # Save results in a JSON file with the filename prefix
    output_file = f"results_{filename.replace('.txt', '').replace('/', '_')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_file}")


def create_sample_file():
    """Create a sample text file with test data for extraction."""
    sample_content = """Contact: support@company.com, sales@business.co.uk
Sites: https://www.example.com, https://blog.example.org/posts
Phone: (555) 123-4567, 555-987-6543, 555.111.2222
Cards: 4532 1234 5678 9012, 1234-5678-9012-3456
Time: 9:00 AM, 5:30 PM, 14:30, 09:15
Tags: #WebDev #RegEx #DataExtraction
Price: $19.99, $1,299.50, $49.95"""
    
    with open('sample_data.txt', 'w') as f:
        f.write(sample_content)
    print("Created sample_data.txt for testing")


if __name__ == "__main__":
    # If no sample file exists, create one automatically
    import os
    if not os.path.exists('sample_data.txt'):
        create_sample_file()
    
    # Run the demo
    demo()    