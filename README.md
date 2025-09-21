# DataExtractor 🕵️‍♂️  

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  

A lightweight Python utility for extracting structured data (emails, URLs, phone numbers, credit cards, times, hashtags, and currency values) from text files using **regular expressions (regex)**.  

---

## ✨ Features  
- 📧 Extract **emails**  
- 🌐 Extract **URLs (http/https)**  
- 📱 Extract **phone numbers** (multiple formats)  
- 💳 Extract **credit card numbers**  
- ⏰ Extract **12-hour & 24-hour times**  
- 🏷️ Extract **hashtags**  
- 💲 Extract **currency values**  
- ✅ Removes duplicates & sorts results  
- 💾 Saves results into a **JSON file**  
- 🧪 Includes a **demo mode** with sample data  

---

## 📦 Requirements  
- Python **3.6+**  
- No external libraries required (standard library only 🎉)  

---

## ⚙️ Usage  

### 1. Clone or download this repo  
```bash
git clone <your-repo-url>
cd <your-folder>
2. Run with a text file as input
bash
Copy code
python3 extractor.py yourfile.txt
If no file is provided, the script will:

Prompt you for one, or

Use sample_data.txt (auto-generated) if you press Enter.

📊 Example Output
nginx
Copy code
Processing file: sample_data.txt
EXTRACTION RESULTS
========================================

Emails: 2 found
  • support@company.com
  • sales@business.co.uk

URLs: 2 found
  • https://www.example.com
  • https://blog.example.org/posts

Phones: 3 found
  • (555) 123-4567
  • 555-987-6543
  • 555.111.2222
A JSON file is also generated:

pgsql
Copy code
results_sample_data.json
🧪 Demo Mode
To test quickly, just run:

bash
Copy code
python3 extractor.py
If sample_data.txt doesn’t exist, it will be created automatically.

📂 Project Structure
bash
Copy code
extractor.py        # Main script
sample_data.txt     # Auto-generated demo file (if missing)
results_*.json      # Extraction results in JSON format
🔧 Extending the Extractor
To add new patterns, edit the self.patterns dictionary inside the DataExtractor class. Example:

python
Copy code
'ip_address': re.compile(r'\b\d{1,3}(\.\d{1,3}){3}\b')
👨‍💻 Author
Oladeji Toluwani Jephthae

📌 Licensed under the MIT License.

yaml
Copy code

---

Would you like me to also generate a **LICENSE file (MIT)** and a **.gitignore** so you can turn this into a clean, publishab
