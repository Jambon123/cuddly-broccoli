#Accreditation (Do not Remove)

#Original Creator of Software Jambon(https://github.com/Jambon123)

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

class mathscog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fib', aliases=['fibonacci'])
    async def fib(self, ctx, arg1, arg2, arg3):
        try:
            FibArgs = []
            FibArgs.append(int(arg1))
            FibArgs.append(int(arg2))
            for n in int(arg3):
                n1 = n - 1
                n2 = n - 2
                x = n1 + n2
                await ctx.send (x)
            FibArgs.clear()
        except: 
            await ctx.send ("Error in command")

def setup(bot):
    bot.add_cog(mathscog(bot))
