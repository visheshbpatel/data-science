import asyncio

from clients.groq_clients import ask_groq
from clients.gemini_clients import ask_gemini
from utils.display import display_results


async def main():

    prompt = "Explain AI in 2 lines"

    results = await asyncio.gather(
        ask_groq(prompt),
        ask_gemini(prompt)
    )

    display_results(results)


asyncio.run(main())