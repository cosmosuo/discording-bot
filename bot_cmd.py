import discord
from dotenv import load_dotenv
import os
from math import * 
from discord.ext import commands 
import random

magic_list = ["it is certain","It is decidely so","Without a doubt","Yes,definitely","You may rely on it","As i see it, yes","Most likely","Outlook is good","Yes","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict this now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook is not so good","Very doubtful"]

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

bot.run(token)


