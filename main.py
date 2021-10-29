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
from datetime import datetime

#Bot Details
bot = commands.Bot(command_prefix='=') #Discord Bot Prefix
cogs = ["cogs.owneronlycog", "cogs.recruitmentcog", "cogs.nsapicog", "cogs.misccog", "cogs.mathscog", "cogs.datacog"]

load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = discord.Client()

#Startup
@bot.event
async def on_ready():
    print ("-----")
    print ("Starting Bot Up")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + str(bot.user.id))
    AllDataDict = {}
    print ("Ready at " +  str(datetime.now()))
    print ("-----")
    print("Loading cogs . . .")
    print ("-----")
    for cog in cogs:
        try:
        	bot.load_extension(cog)
        	print(cog + " was loaded at " +  str(datetime.now()))
        except Exception as e:
        	print(e)
    print ("Ready at " +  str(datetime.now()))
    print ("-----")

#Bot Commands (Using the specificied prefix)

@bot.command(name='example')
async def example(ctx):
    response = ("This is an example command for adaptation or removal")
    await ctx.send(f'{response}')
#Run Bot

bot.run(os.getenv('DISCORD_TOKEN'))