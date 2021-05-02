#Accreditation (Do not Remove)

#Original Creator of Software Jambon(https://github.com/Jambon123)
#For Help on the Original Software droplt(https://github.com/drop-lt)
#For Help on the Original Software MrTurtle(https://github.com/Mr-Turtle)

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

clientkey = os.getenv('CLIENTKEY')
tgid = os.getenv('TGID')
secretkey = os.getenv('SECRETKEY')
USERAGENT = os.getenv('API')
api = nationstates.Nationstates(USERAGENT)
world = api.world()

bot = None
def SetBot(_bot):
  global bot
  bot = bot

def get_youngest(nations_dict, num):
    youngest = []
    nation_temp = nations_dict.copy()
    
    for _ in range(num):
        x = 20
        y = ""
        for nation in nation_temp.copy():
            if nation_temp[nation] < x:
                x = nation_temp[nation]
                y = nation
                nation_temp.pop(nation)
                break
        youngest.append(y)
    
    return youngest

class NationLogger:
    def __init__(self):
        self.nations = {}
        self.blacklist = []

    async def RecordNations(self):
        print("Grabbing Nations")
        content = dict(world.get_shards('newnations'))
        content["newnations"] = content["newnations"].split(",")
        
        for nation in content["newnations"].copy():
            if nation not in self.nations and nation not in self.blacklist:
                self.nations[nation] = -1
        
        for nation in self.nations.copy():
            self.nations[nation] += 1
            if self.nations[nation] >= 14:
                del self.nations[nation]
                self.blacklist.append(nation)
                
        file = open("newnations.json", "w+")
        file.write(json.dumps(self.nations))
        file.close()

class BackgroundCounter(commands.Cog):
    def __init__(self, bot, NationLogger):
        self.nationLogger = NationLogger
        self.bot = bot
        self.printer.start()

    def cog_unload(self, nationLogger):
        self.printer.cancel()

    @tasks.loop(seconds=60.0)
    async def printer(self):
        print("Tick")
        await self.nationLogger.RecordNations()

async def TGSend():
    print ("Tack")
    recruitpick = get_youngest(nationlogger.nations, int("1"))
    for item in recruitpick.copy():
        nationlogger.blacklist.append(item)
        nationlogger.nations.pop(item)

    async with httpx.AsyncClient() as client:
        payload = {'client': (clientkey), 'tgid': (tgid), 'key': (secretkey), 'to': (recruitpick), } 
        await client.get(f'https://www.nationstates.net/cgi-bin/api.cgi?a=sendTG', params = payload)

class AutoTG(commands.Cog):
    def __init__(self, bot, TGSend):
        self.bot = bot
        self.printer.start()

    def cog_unload(self, TGSend):
        self.printer.cancel()

    @tasks.loop(seconds=180.0)
    async def printer(self):
        await asyncio.sleep(1)
        print("Tock")
        await TGSend()

AutoTG(TGSend, bot)
nationlogger = NationLogger()
BackgroundCounter(bot, nationlogger)

class recruitmentcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name='recruit')
    async def recruit(self, ctx, arg):
        global nationlogger
        #Check Value
        if int(arg) == int("0"):
            response =  ("Error, 0 invalid")
        elif int(arg) >= int("9"):
            response = ("Error, 9 or higher too large")
        else:
            recruitno = arg
            print (recruitno)

        #Get nation list equal to recruitno    
        rlist = get_youngest(nationlogger.nations, int(recruitno))

        #Combine Strings, Blacklist
        stringList = ' '.join([str("nation: " + (item)) for item in rlist.copy() ])
        for item in rlist.copy():
            nationlogger.blacklist.append(item)
            nationlogger.nations.pop(item)


        print(stringList)

        response = str(stringList)
        await ctx.send(f'{str(response)}')


def setup(bot):
    bot.add_cog(recruitmentcog(bot))