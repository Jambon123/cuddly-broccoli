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
intents.members = True
client = discord.Client()
world = api.world()

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

@bot.command(name='setselfdata')
async def setselfdata(ctx, *, args):
    try:
        user = str(ctx.author.id)
        server = str(ctx.message.guild.id)
        data = json.loads(str(args))

        async with aiofiles.open('datalist.json', mode='r') as f:
            AllDataDictStr = await f.read()

        AllDataDict = json.loads(str(AllDataDictStr))
        
        if server not in AllDataDict.keys():
            AllDataDict[server] = {}
            
        if user not in AllDataDict[server].keys():
            AllDataDict[server][user] = []
            
        if data not in AllDataDict[server][user]:
            AllDataDict[server][user].append(data)
            
        #AllDataDict[server][user].append(data)

        async with aiofiles.open('datalist.json', mode="w") as f:
            await f.write(json.dumps(AllDataDict))

        await ctx.send(("Added ") + str(data) + (" to ") + str(user)) 

    except Exception as e:
        await ctx.send ("Error in command " + str(e))

@bot.command(name='readselfdata')
async def readselfdata(ctx):
    try:
        user = ctx.author.id
        response = str("Data Read: " ("data"+str(user)))
        await ctx.send("data"+str(user))
        print ("data"+str(user))
    except Exception as e:
        await ctx.send ("Error in command " + str(e))

#Run Bot

bot.run(TOKEN)