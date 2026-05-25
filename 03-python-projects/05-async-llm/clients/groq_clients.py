import httpx
from utils.config import(groq_api_key, groq_base_url, groq_model)

async def ask_groq(prompt):

    url = f"{groq_base_url}/chat/completions"

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": groq_model,

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
            "response": content
        }
