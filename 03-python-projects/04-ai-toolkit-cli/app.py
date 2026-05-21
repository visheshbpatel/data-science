import os
import argparse
from openai import OpenAI
from dotenv import load_dotenv

parser = argparse.ArgumentParser()

parser.add_argument("task")
parser.add_argument("text")

args = parser.parse_args()



if args.task == "summarize":
    prompt = f"Summerize this text: {args.text}"

elif args.task == "translate":
    prompt = f"translate this text: {args.text}"

elif args.task == "sentiment-analysis":
    prompt = f"sentiment analysis on this text: {args.text}"

else:
    print("Please provide valid task or Text")


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")

client = OpenAI(
    api_key = api_key,
    base_url=base_url)


response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":'user',
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)
