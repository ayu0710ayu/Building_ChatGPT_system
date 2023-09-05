import os

import openai as openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']


# openai.api_key = "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" (optional)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


response = get_completion("What is the capital of France?")
print(response)
