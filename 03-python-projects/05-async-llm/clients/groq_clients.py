import httpx
from utils.config import(GROQ_API_KEY, GROQ_BASE_URL, GROQ_MODEL)

async def ask_groq(prompt):

    url = f"{GROQ_BASE_URL}/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": GROQ_MODEL,

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

        content = data['choices'][0]['message']['content']
    
        return {
            "provider": "Groq",
            "model": GROQ_MODEL,
            "response": content
        }
