#Accreditation (Do not Remove)

#Original Creator of Software Jambon(https://github.com/Jambon123)
#For Help on the Original Software droplt(https://github.com/drop-lt)
#For Help on the Original Software MrTurtle(https://github.com/Mr-Turtle)

#Imports
import os, sys #System Imports
from dotenv import load_dotenv
import discord, discord.utils #Discord Imports
from discord.ext import tasks, commands
import math
import nationstates #Nationstates Imports
from nationstates import Shard
import traceback #Error Handling
import json, aiofiles #File Imports
import asyncio #Async Imports
import httpx #Web-Connection Imports
import re #Misc Imports

#Config 
bot = commands.Bot(command_prefix='=') #Discord Bot Prefix
cogs = ["cogs.owneronlycog", "cogs.recruitmentcog", "cogs.nsapicog", "cogs.misccog", "cogs.mathscog"]

#Loading
load_dotenv()
USERAGENT = os.getenv('API')
TOKEN = os.getenv('DISCORD_TOKEN')
clientkey = os.getenv('CLIENTKEY')
tgid = os.getenv('TGID')
secretkey = os.getenv('SECRETKEY')
api = nationstates.Nationstates(USERAGENT) #NSAPI UserAgent
intents = discord.Intents.default()
client = discord.Client()
world = api.world()

#Startup
@bot.event
async def on_ready():
    print ("-----")
    print ("Booting up your system")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + str(bot.user.id))
    print("Loading cogs . . .")
    print ("-----")
    for cog in cogs:
        try:
        	bot.load_extension(cog)
        	print(cog + " was loaded.")
        except Exception as e:
        	print(e)
    print ("-----")

#Bot Commands (Using the specificied prefix)

@bot.command(name='example')
async def example(ctx):
    response = ("This is an example command for adaptation or removal")
    await ctx.send(f'{response}')




#Run Bot

bot.run(TOKEN)