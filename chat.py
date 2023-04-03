from dotenv import load_dotenv
import openai
import os

load_dotenv("C_TOKEN")
key = os.getenv("C_TOKEN")

openai.api_key = key


messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "can you help me"},
        {"role": "assistant", "content": "bruh ok"},
    ]

def chat(inp):
    messages.append({"role": "user", "content": inp})
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
    )
    messages.append(response.choices[0].message)
    return response.choices[0].message.content

print(chat("What's the meaning of drug stimulant methamphetamine?"))
print(chat("why do people often abuse meth out of all other drugs?"))