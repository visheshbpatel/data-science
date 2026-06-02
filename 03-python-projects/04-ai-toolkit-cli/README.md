# AI Toolkit CLI

A simple AI-powered command-line toolkit built with Python.

This CLI application performs:

* Text Summarization
* Translation
* Sentiment Analysis

using an OpenAI-compatible API such as Groq or OpenAI.

---

## Features

* Summarize text into 3 concise bullet points
* Translate text into any language
* Analyze sentiment of text
* Logging support with `app.log`
* Environment variable configuration using `.env`
* Clean command-line interface with `argparse`

---

## Project Structure

```bash
04-ai-toolkit-cli/
│
├── app.py
├── app.log
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd 04-ai-toolkit-cli
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
API_KEY=your_api_key
BASE_URL=your_base_url
MODEL=your_model_name
```

Example:

```env
API_KEY=xxxxxxxxxxxxxxxx
BASE_URL=https://api.groq.com/openai/v1
MODEL=llama-3.3-70b-versatile
```

---

## Usage

### Help Menu

```bash
python app.py --help
```

Output:

```text
usage: app.py [-h] [--language LANGUAGE] {summarize,translate,sentiment-analysis} text

AI-powered CLI toolkit for summarization, translation, and sentiment analysis

positional arguments:
  {summarize,translate,sentiment-analysis}
                        Task to perform
  text                  Text input for processing

options:
  -h, --help            show this help message and exit
  --language LANGUAGE   Language for translation
```

---

### Text Summarization

Command:

```bash
python app.py summarize "Artificial Intelligence automates repetitive tasks, improves decision-making, and increases productivity across industries."
```

Output:

```text
* Artificial Intelligence automates repetitive tasks.
* AI improves decision-making.
* AI increases productivity across various sectors.
```

---

### Text Translation

Command:

```bash
python app.py translate "How are you today?" --language french
```

Output:

```text
Comment allez-vous aujourd'hui ?
```

---

### Default Language Translation

Command:

```bash
python app.py translate "How are you today?"
```

Output:

```text
आप आज कैसे हैं?
```

---

### Sentiment Analysis

Command:

```bash
python app.py sentiment-analysis "I absolutely loved this project. It was fun and very useful."
```

Output:

```text
The sentiment is Positive. The reason is the use of enthusiastic language, such as "absolutely loved", "fun", and "very useful", which indicates a strong positive emotion.
```

---

## Logging

Application logs are stored in:

```bash
app.log
```

Example log output:

```text
2026-06-01 12:10:14 | INFO | --------------------------------------------------
2026-06-01 12:10:14 | INFO | Starting AI Toolkit CLI Session
2026-06-01 12:10:15 | INFO | Initializing AI client
2026-06-01 12:10:16 | INFO | Sending request to AI model
2026-06-01 12:10:17 | INFO | Received response from AI model
```

## Notes

A sample `app.log` file is included to showcase the logging functionality implemented in the project.

---

## Tech Stack

* Python
* OpenAI Python SDK
* python-dotenv
* argparse
* logging
* Groq / OpenAI-compatible APIs

---

## Future Improvements

* Interactive chat mode
* Save output to files
* Rich terminal UI
* Support additional NLP tasks
* Multi-model support

---

## Author

**Vishesh Patel**

GitHub: https://github.com/visheshbpatel
