import httpx

from utils.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)



async def ask_gemini(prompt):

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent"
    )

    params = {
        "key": GEMINI_API_KEY
    }

    headers = {
        "Content-Type": "application/json"
    }

    json_data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            url,
            params=params,
            headers=headers,
            json=json_data
        )

        if response.status_code != 200:

            return {
                "provider": "Gemini",
                "error": response.json()
            }

        data = response.json()

        content = (
            data["candidates"][0]
            ["content"]["parts"][0]["text"]
        )

        return {
            "provider": "Gemini",
            "response": content
        }
