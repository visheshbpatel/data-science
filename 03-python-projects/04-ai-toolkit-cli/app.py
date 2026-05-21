import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")

client = OpenAI(
    api_key = api_key,
    base_url=base_url)


response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role":'user',
            "content": "Hello AI"
        }
    ]
)

print(response.choices[0].message.content)
