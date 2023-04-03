import discord
from dotenv import load_dotenv
import os
from math import * 
from discord.ext import commands 
import openai

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

@bot.command(help="magic service provided")
async def magic(ctx, *, arg):
   await ctx.send(str(random.choice(magic_list))) 

@bot.command(help="bot that leads to another bot")
async def ayah(ctx, *, arg):
   await ctx.send(chat(arg)) 

bot.run(token)


