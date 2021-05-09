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

badwords = ["sdfg,sdrfyuio,lkmjnegwefgthk/.jmnhgerwdfgt.;,mjhdestfyjh,kyukyuyhgjt656"]

def replace_all(pattern, repl, string) -> str:
    occurences = re.findall(pattern, string, re.IGNORECASE)
    for occurence in occurences:
        string = string.replace(occurence, repl)

    return string

class misccog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='echo', aliases=['send'])
    async def anonsend(self, ctx, *, args):

        response = str(args)

        for item in badwords:
            response = replace_all(item, "[REDACTED]", response)

        print("Printing... '" + (args) + "' Said by " + str(ctx.author))
        await ctx.send(str(response))

    @commands.command(name='joined')
    async def joined(self, ctx, member: discord.Member):
    #Finds and sends age
        await ctx.send(f'{member.name} joined in {member.joined_at}')

def setup(bot):
    bot.add_cog(misccog(bot))