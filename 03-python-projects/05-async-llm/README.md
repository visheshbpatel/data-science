# Async Multi-LLM Comparison Tool

A Python CLI application that sends the same prompt to multiple LLM providers concurrently using `asyncio` and displays the responses in a Rich-powered terminal interface.

## What It Does

Given a prompt, the application:

1. Sends the prompt to Groq, Gemini, and OpenRouter simultaneously.
2. Waits for all responses using `asyncio.gather()`.
3. Displays the responses side by side in the terminal.

This project was built to learn and demonstrate asynchronous programming, API integration, and terminal UI development in Python.

---

## Tech Stack

* Python
* asyncio
* httpx
* Rich
* python-dotenv

---

## Supported Providers

| Provider   | Model                   |
| ---------- | ----------------------- |
| Groq       | llama-3.3-70b-versatile |
| Gemini     | gemini-flash-latest     |
| OpenRouter | deepseek/deepseek-chat  |

---

## Project Structure

```text
05-async-llm/
│
├── app.py
│
├── clients/
│   ├── groq_clients.py
│   ├── gemini_clients.py
│   └── openrouter_clients.py
│
├── utils/
│   ├── config.py
│   └── display.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file using `.env.example` as reference.

Example:

```env
GROQ_API_KEY=your_api_key
GROQ_BASE_URL=https://api.groq.com/openai/v1
GROQ_MODEL=llama-3.3-70b-versatile

GEMINI_API_KEY=your_api_key
GEMINI_MODEL=gemini-flash-latest

OPENROUTER_API_KEY=your_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=deepseek/deepseek-chat
```

---

## Run

```bash
python app.py
```

Example:

```text
Enter your prompt:

What is asyncio in Python?
```

The application will send the prompt to all configured providers concurrently and display the results in the terminal.

---

## Concepts Demonstrated

### Async Programming

* async / await
* Coroutines
* Event Loop
* asyncio.gather()

### API Integration

* HTTP requests using httpx
* Authentication using API keys
* JSON request/response handling

### Software Engineering

* Modular project structure
* Separation of concerns
* Environment-based configuration
* Error handling

### Terminal UI

* Rich panels
* Rich prompts
* Markdown rendering

---

## Future Improvements

* Retry mechanism with exponential backoff
* Response latency comparison
* Token usage tracking
* Additional providers
* Response export to Markdown or JSON

---

## Author

Vishesh Patel

GitHub: https://github.com/visheshbpatel