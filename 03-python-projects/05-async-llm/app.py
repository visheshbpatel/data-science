import os
import httpx
import asyncio
from clients.groq_clients import ask_groq
from clients.gemini_clients import ask_gemini


async def main():

    prompt = "Explain AI in 2 lines"

    results = await asyncio.gather(

        # ask_groq(prompt),

        ask_gemini(prompt)
    )

    for result in results:

        print(result)

        print()


asyncio.run(main())