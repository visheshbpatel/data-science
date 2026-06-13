import httpx

from utils.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    OPENROUTER_MODEL
)


async def ask_openrouter(prompt):

    url = f"{OPENROUTER_BASE_URL}/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": OPENROUTER_MODEL,

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

            return {
                "provider": "OpenRouter",
                "error": response.json()
            }

        data = response.json()

        content = data["choices"][0]["message"]["content"]

        return {
            "provider": "OpenRouter",
            "model": OPENROUTER_MODEL,
            "response": content
        }