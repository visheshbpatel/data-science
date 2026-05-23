import os
import httpx
import asyncio
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")


async def ask_groq(prompt):

    url = f"{base_url}/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": model,

        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            url,
            headers=headers,
            json=json_data
        )

        if response.status_code != 200:

            print("Request Failed")
            print(response.json())

            return

        data = response.json()

        print(data['choices'][0]['message']['content'])
        print()



async def main():

    await asyncio.gather(
        ask_groq("What is AI in 2 lines"),
        ask_groq("What is ML in 2 lines"),
        ask_groq("What is DL in 2 lines")
    )

asyncio.run(main())

