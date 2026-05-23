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
        prompt = f"""
                    Summarize the following text into exactly 3 concise bullet points.

                    Rules:
                    - Include only the most important information
                    - Keep each bullet short and clear
                    - Do not add extra explanations

                    Text:
                    {text}
                """
        return prompt
    

    elif task == "translate":
        prompt = f"""
                    Translate the following text into {language}.

                    Rules:
                    - Only return the translated text
                    - Do not add explanations
                    - Do not add notes or extra formatting

                    Text:
                    {text}
                """
        return prompt


    elif task == "sentiment-analysis":
        prompt = f"""
                    Analyze the sentiment of the following text.

                    Instructions:
                    - Identify whether the sentiment is Positive, Negative, or Neutral
                    - Briefly explain the reason for the sentiment
                    - Keep the response concise and clear
                    - Do not add unnecessary information

                    Text:
                    {text}
                """
        return prompt


def generate_response(model,client, prompt):

    try:
        response = client.chat.completions.create(
            model=model,
            temperature=0.3,
            max_tokens=300,
            messages=[
                {
                    "role":"system",
                    "content":"You are a professional AI assistant specialized in summarization, translation, and sentiment analysis. Follow instructions carefully and provide clean, accurate responses."
                },
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
