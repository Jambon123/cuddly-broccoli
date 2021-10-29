#Accreditation (Do not Remove)

#Original Creator of Software Jambon(https://github.com/Jambon123)

#Imports
from dotenv import load_dotenv
import discord, discord.utils #Discord Imports
from discord.ext import tasks, commands
from nationstates import Shard
from datetime import datetime

class mathscog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fib', aliases=['fibonacci'])
    async def fib(self, ctx, *, args):
        try:
            FibArgs = []
            FibArgs.append(int(arg1))
            FibArgs.append(int(arg2))
            for n in (arg3):
                n1 = n - 1
                n2 = n - 2
                x = n1 + n2
                await ctx.send (x)
            FibArgs.clear()
        except Exception as e:
            await ctx.send ("Error in command " + str(e))

def setup(bot):
    bot.add_cog(mathscog(bot))
