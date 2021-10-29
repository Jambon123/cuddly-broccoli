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
from datetime import datetime

USERAGENT = os.getenv('API')
api = nationstates.Nationstates(USERAGENT)
world = api.world()

class NSAPICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='worldnations')
    async def worldnations(self, ctx):
        try:
            nationnum = world.get_shards('numnations')
            response = ((nationnum.numnations) + (" Nations are in the world"))
            print("worldnations used")
            await ctx.send(f'{response}')
        except Exception as e:
            await ctx.send ("Error in command " + str(e))


def setup(bot):
    bot.add_cog(NSAPICog(bot))