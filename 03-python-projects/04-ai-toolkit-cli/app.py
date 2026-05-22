import os
import argparse
from openai import OpenAI
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
load_dotenv()

parser.add_argument("task")
parser.add_argument("text")
parser.add_argument("--language")

args = parser.parse_args()


def generate_prompt(task,text,language):

    if language is None:
        language="Hindi"

    if task == "summarize":
        prompt = f"Summarize this text: {text}"
        return prompt

    elif task == "translate":
        prompt = f"Translate this text into {language}: {text}"
        return prompt

    elif task == "sentiment-analysis":
        prompt = f"Classify this text as Positive, Negative, or Neutral: {text}"
        return prompt

    else:
        print("Please provide valid task or Text")
        exit()


def generate_response(model,client, prompt):

    try:
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
    
    except Exception as e:
        return f"Error:{e}"


def initialize_client():
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model = os.getenv("MODEL")

    if api_key is None:
        print("Missing API_KEY in .env file")
        exit()

    elif base_url is None:
        print("Missing BASE_URL in .env file")
        exit()

    elif model is None:
        print("Missing MODEL in .env file")
        exit()

    else:
        client = OpenAI(
            api_key = api_key,
            base_url=base_url
            )
        
        return model,client


prompt = generate_prompt(args.task,args.text,args.language)
model,client = initialize_client()
response = generate_response(model,client,prompt)

print(response)
