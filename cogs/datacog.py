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

class DATACOG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setselfdata')
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

    @commands.command(name='readselfdata')
    async def readselfdata(ctx):
        try:
            user = ctx.author.id
            response = str("Data Read: " ("data"+str(user)))
            await ctx.send("data"+str(user))
            print ("data"+str(user))
        except Exception as e:
            await ctx.send ("Error in command " + str(e))

def setup(bot):
    bot.add_cog(DATACOG(bot))


