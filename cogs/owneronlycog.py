#Accreditation (Do not Remove)

#Original Creator of Software Jambon(https://github.com/Jambon123)

#Imports
from dotenv import load_dotenv
import discord, discord.utils #Discord Imports
from discord.ext import tasks, commands
from nationstates import Shard
from datetime import datetime

class owneronlycog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setstatus')
    @commands.is_owner()
    async def setstatus(self, ctx, *, args):

        try:
            game = discord.Game(str(args))
            await self.bot.change_presence(status=discord.Status.online, activity=game)
            await ctx.send("Status Changed to " + str(game))
            print("Status Changed to " + str(game))
        except Exception as e:
            await ctx.send ("Error in command " + str(e))

def setup(bot):
    bot.add_cog(owneronlycog(bot))