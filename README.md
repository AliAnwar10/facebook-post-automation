# 📢 Facebook Automation Tool

A professional-grade Python automation tool that automates posting to multiple Facebook groups. Built with a modern architecture using **Playwright** for browser automation, **SQLite3** for local data management, and **Tkinter** for a user-friendly GUI.

This tool allows you to:
- Store and manage Facebook credentials
- Save group links and post content (title, description, hashtags, image)
- Select specific post-group combinations for targeted posting
- Automate the entire posting process with Chromium browser using Playwright

---

## 🧰 Features

- 🗂️ GUI with 5-tab interface using Tkinter
- 🔐 Store multiple credentials locally (SQLite)
- 🌐 Manage group names and URLs
- 📝 Save rich post content with title, description, hashtags, and image
- ✅ Assign specific posts to specific groups using checkbox mapping
- 🤖 Full automation via Playwright in Chromium browser
- 🧱 Modular codebase for easy maintenance and scaling

---

## 🚀 Technologies Used

- **Python 3.10+**
- **Tkinter** – GUI Framework
- **SQLite3** – Lightweight local database
- **Playwright (async)** – Browser automation
- **Git** – Version control
- **OS**, **CSV**, **asyncio**, etc. – Standard Python libraries

---

## 🖥️ GUI Overview

| Tab             | Functionality |
|----------------|----------------|
| **Credentials** | Enter and save Facebook email & password |
| **Groups**      | Add group names and URLs |
| **Posts**       | Add post title, description, hashtags, and image |
| **Load Data**   | View stored data and select post-group combinations |
| **Automation**  | Start automation for selected combinations |

---

## 📦 Project Structure

project/test/
├── main.py # GUI application
├── setup_database.py # Creates SQLite tables
├── db_insert.py # DB insert/select/update helpers
├── playwright_runner.py # Playwright automation logic
├── utils.py # Optional: logs/validators
├── facebook_automation.db # SQLite database
├── images/ # Folder for uploaded post images


---

## ⚙️ Installation

### 1. Clone the Repository

git remote add origin https://github.com/AliAnwar10/facebook-post-automation.git

### 2. Create Virtual Environment 

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install playwright
python -m playwright install

### 📋 How to Use
### 1. Setup Database
Run this script once to create all required tables:

python setup_database.py
### 2. Launch the GUI

python main.py
### 3. Fill in All Tabs
Credentials ➝ Save email/password

Groups ➝ Save Facebook group names & URLs

Posts ➝ Add post content + image

Load Data ➝ Select which post goes to which group using checkboxes

Automation ➝ Click Start Automation to begin posting

### ✅ Best Practices
Make sure credentials are valid and 2FA is handled manually if prompted

Use real browser sessions (non-headless) to mimic human behavior

Respect Facebook’s community standards and group posting limits

### 🔐 Security Warning
This tool is for educational and automation learning purposes only.
Do not misuse it to spam or violate Facebook’s Terms of Service. Use it responsibly and ethically.


### 📄 License
This project is licensed under the MIT License. See LICENSE for details.

### 👨‍💻 Author
Ali Anwar
GitHub • Software Engineering Student • Python & Automation Developer

### 🙋‍♂️ Contributing
Pull requests, feature suggestions, and issues are welcome!

### 🌐 Related Projects
Browser Automation Tools
Fiverr Bots and Auto Posters
