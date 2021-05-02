#Accreditation (Do not Remove)

#Original Creator of Software Jambon(https://github.com/Jambon123)
#For Help on the Original Software droplt(https://github.com/drop-lt)
#For Help on the Original Software MrTurtle(https://github.com/Mr-Turtle)

#Imports
import os, sys #System Imports
from dotenv import load_dotenv
import discord, discord.utils #Discord Imports
from discord.ext import tasks, commands
import nationstates #Nationstates Imports
from nationstates import Shard
import traceback #Error Handling
import json, aiofiles #File Imports
import asyncio #Async Imports
import httpx #Web-Connection Imports
import re #Misc Imports

class owneronlycog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setstatus')
    @commands.is_owner()
    async def setstatus(self, ctx, *, args):

        game = discord.Game(str(args))
        await self.bot.change_presence(status=discord.Status.online, activity=game)
        await ctx.send("Status Changed to " + str(game))
        print("Status Changed to " + str(game))

def setup(bot):
    bot.add_cog(owneronlycog(bot))