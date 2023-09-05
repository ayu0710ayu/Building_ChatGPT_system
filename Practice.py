import os
import openai as openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


def get_completion_from_messages(message, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    responses = openai.ChatCompletion.create(
        model=model,
        messages=message,
        temperature=temperature,  # this is the degree of randomness of the model's output
        max_tokens=max_tokens,  # the maximum number of tokens the model can output
    )
    return responses.choices[0].message["content"]


messages = [{'role': 'system', 'content': """You are an assistant who\
 responds in the style of spiderman."""}, {'role': 'user',
                                           'content': """write me a very short poem\
 about a happy carrot in one sentence"""}, ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
