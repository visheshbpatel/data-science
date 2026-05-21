import os
import argparse
from openai import OpenAI
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
load_dotenv()

parser.add_argument("task")
parser.add_argument("text")

args = parser.parse_args()

def generate_prompt(task,text):

    if task == "summarize":
        prompt = f"Summerize this text: {text}"
        return prompt

    elif task == "translate":
        prompt = f"translate this text: {text}"
        return prompt

    elif task == "sentiment-analysis":
        prompt = f"sentiment analysis on this text: {text}"
        return prompt

    else:
        print("Please provide valid task or Text")
        exit()


api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
model = os.getenv("MODEL")

client = OpenAI(
    api_key = api_key,
    base_url=base_url)


def generate_response(prompt):

    
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role":'user',
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


prompt = generate_prompt(args.task,args.text)
response = generate_response(prompt)

print(response)
