import discord
from dotenv import load_dotenv
import os
from math import * 
from discord.ext import commands 
import openai
import time 
from Bard import Chatbot

chat_timestamp = time.time()

def resetConversationIfExpired():
   global chat_timestamp
   cur_time = time.time()
   if cur_time - chat_timestamp > 300: #reset history message 
      messages = messages[:3]
      print("Resetting conversation history")
   chat_timestamp = cur_time 

load_dotenv("C_TOKEN")
key = os.getenv("C_TOKEN")

load_dotenv("B_TOKEN")
b_token = os.getenv("B_TOKEN")

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

def bard_chat(inp):
   bard_bot = Chatbot(b_token)
   resp = bard_bot.ask(inp)
   return resp('context')
   
   #return "I'll be producing meth in no time"

#create intents
intents = discord.Intents.default()
intents.message_content = True
# read dot token from .env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(help="a very nice greeting to buyers of met- i mean, people")
async def hey(ctx):
   author = ctx.message.author
   await ctx.send("ew it's you again, <@" + str(author.id) + ">")  

@bot.command(help="gives some good words from a good reliable source")
async def echo(ctx, *, arg):
   await ctx.send("my mommy told me " + arg)

@bot.command(help="a nice product for nice buyers")
async def meth(ctx, *, arg):
   await ctx.send("want some of my crystal blue meth? pay me "+ "$" + str(eval(arg)))

@bot.command(help="bot that leads to another bot")
async def ayah(ctx, *, arg):
   await ctx.send(chat(arg)) 

@bot.command(help="Bard answer")
async def copybara(ctx, *, arg):
   await ctx.send(bard_chat(arg)) 

bot.run(token)


