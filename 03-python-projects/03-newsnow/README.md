# NewsNow

A modern desktop news reader built with Python and Tkinter.

NewsNow fetches the latest headlines using NewsAPI and displays them in a clean, mobile-inspired interface with article images, titles, descriptions, and simple navigation.

---

## Features

* Latest news powered by NewsAPI
* Modern Tkinter-based UI
* Fast startup loading screen
* Smooth article navigation
* Open full article in browser
* Image loading with caching
* Clean dark theme for better readability

---

## Tech Stack

* Python 3
* Tkinter
* Requests
* Pillow
* Python Dotenv
* NewsAPI

---

## Project Structure

```bash
NewsNow/
│
├── app.py
├── requirements.txt
├── .env
├── news.ico      # optional
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd NewsNow
```

---

### 2. Create virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Setup API Key

This project uses NewsAPI to fetch the latest news.

Get your free API key from:

[NewsAPI](https://newsapi.org?utm_source=chatgpt.com)

---

### Create `.env`

Create a `.env` file in the project root:

```env
API_KEY=your_newsapi_key_here
```

Example:

```env
API_KEY=abc123xyz456
```

---

## Run the App

```bash
python app.py
```

---

## How It Works

* App opens with a loading screen
* Latest news is fetched from NewsAPI in the background
* Articles are displayed one at a time
* Images are loaded dynamically and cached for smoother navigation
* Use:

  * **Previous** --> go back
  * **Next** --> move forward
  * **Read More** --> open article in browser

---

## Customize News Topic

To change what news is shown, edit this inside `app.py`:

```python
q=india
```

Examples:

```python
q=technology
q=cricket
q=business
q=artificial intelligence
```

---

## Requirements

```txt
requests
Pillow
python-dotenv
```

---

## Notes

* `tkinter` comes pre-installed with Python
* `news.ico` is optional and can be added as the app icon

---
