import os
import argparse
from openai import OpenAI
from dotenv import load_dotenv


def setup_parser():

    parser = argparse.ArgumentParser(
        description="AI-powered CLI toolkit for summarization, translation, and sentiment analysis")

    parser.add_argument(
        "task",
        choices=["summarize", "translate", "sentiment-analysis"],
        help="Task to perform"
    )
    parser.add_argument(
        "text",
        help="Text input for processing"
        )
    parser.add_argument(
        "--language",
        default="hindi",
        help="Language for translation"
        )

    return parser


def generate_prompt(task,text,language):

    if task == "summarize":
        prompt = f"Summarize this text: {text}"
        return prompt

    elif task == "translate":
        prompt = f"Translate this text into {language}: {text}"
        return prompt

    elif task == "sentiment-analysis":
        prompt = f"Classify this text as Positive, Negative, or Neutral: {text}"
        return prompt


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

    load_dotenv()

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


def main():

    parser = setup_parser()
    args = parser.parse_args()

    prompt = generate_prompt(args.task,args.text,args.language)
    model,client = initialize_client()
    response = generate_response(model,client,prompt)

    print(response)


if __name__ ==  "__main__":
    main()
