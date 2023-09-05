import openai


def get_it(message, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    responses = openai.ChatCompletion.create(
        messages=message,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens

    )
    return responses.choices[0].message['content']


messages = [{'role': 'user', 'content': 'who is narendra modi'}]
response=get_it(messages,temperature=1)
print(response)

