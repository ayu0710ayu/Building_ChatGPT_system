import os
import openai as openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


def get_completion_from_messages(message, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=message,
        temperature=temperature,  # this is the degree of randomness of the model's output
        max_tokens=max_tokens,  # the maximum number of tokens the model can output
    )
    return response.choice[0].message['content']
response = openai.Moderation.create(
    input="""
Here's the plan.  We get the warhead, 
and we hold the world ransom...
...FOR ONE MILLION DOLLARS!
"""
)
moderation_output = response["results"][0]
print(moderation_output)

