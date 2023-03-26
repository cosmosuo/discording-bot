from dotenv import load_dotenv
import openai
import os

load_dotenv("C_TOKEN")
key = os.getenv("C_TOKEN")

openai.api_key = key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "can you help me"},
        {"role": "assistant", "content": "bruh ok"},
        {"role": "user", "content": "what is dna"}
    ]
)

print(response)