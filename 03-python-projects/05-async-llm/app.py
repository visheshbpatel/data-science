import asyncio

from clients.groq_clients import ask_groq
from clients.gemini_clients import ask_gemini
from clients.openrouter_clients import ask_openrouter
from utils.display import display_results


async def main():

    prompt = "Why is async programming useful in Python?"

    results = await asyncio.gather(
        ask_groq(prompt),
        ask_gemini(prompt),
        ask_openrouter(prompt),
        return_exceptions=True
    )

    display_results(results)


asyncio.run(main())