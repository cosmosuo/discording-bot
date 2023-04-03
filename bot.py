import discord
from dotenv import load_dotenv
import os
from math import * 
import random


user_cmd_count = {}
og_value = 1
db_value = 2*og_value


def userCalling(user):
    if user in user_cmd_count:
        user_cmd_count[user] += 1
    else:
        user_cmd_count[user] = 1

#create intents
intents = discord.Intents.default()
intents.message_content = True

# read dot token from .env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

#create bot client
client = discord.Client(intents=intents)

@client.event 
async def on_ready():
        print(f"{client.user.name} logged in")

@client.event
async def on_message(message):
      global db_value
      global count
      author = message.author
      if author.bot:
             return
      
#log in
client.run(token)