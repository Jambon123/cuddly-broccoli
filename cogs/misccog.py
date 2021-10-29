#Accreditation (Do not Remove)

#Original Creator of Software Jambon(https://github.com/Jambon123)

#Imports
import os, sys #System Imports
from dotenv import load_dotenv
import discord, discord.utils #Discord Imports
from discord.ext import tasks, commands
from nationstates import Shard
import re #Misc Imports
from datetime import datetime

badwords = ["sdfg,sdrfyuio,lkmjnegwefgthk/.jmnhgerwdfgt.;,mjhdestfyjh,kyukyuyhgjt656", "sus", "cringe", "cring", "imposter", "jesus", "sussy"]

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
        try: 
            response = str(args)

            for item in badwords:
                response = replace_all(item, "[REDACTED]", response)

            print("Printing... '" + (args) + "' Said by " + str(ctx.author))
            await ctx.send(str(response))
        except Exception as e:
            await ctx.send ("Error in command " + str(e))

    @commands.command(name='joined')
    async def joined(self, ctx, member: discord.Member):
    #Finds and sends age
        try: 
            await ctx.send(f'{member.name} joined at {member.joined_at}')
        except Exception as e:
            await ctx.send ("Error in command " + str(e))

def setup(bot):
    bot.add_cog(misccog(bot))