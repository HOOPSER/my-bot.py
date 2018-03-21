 #import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk    
import random
import time
import datetime
import json
import logging
import token
import sys

bot = commands.Bot(command_prefix='g') #change it to what you want

print(discord.__version__)

@bot.event
async def on_ready():
    print("running... ok ready to start")
    print("running the " + bot.user.name)
    print ("With the ID " + bot.user.id)
    print("gaming bot by chris") # change this to what you want
    bot.uptime = datetime.datetime.now()
    print(bot.uptime)
    server = len(bot.servers)
    print(server)
    users = sum(1 for _ in bot.get_all_members())
    print(users)
    while 1==1:
        await bot.change_presence(game=discord.Game(name='with {} servers'.format(server)))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='with {} users'.format(users)))
        await asyncio.sleep(10)                         
        await bot.change_presence(game=discord.Game(name='PREFIX = g')) #change the "g" to your bots prefix
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name='ghelp')) #change the "g to your bots prefix"
        await asyncio.sleep(25)
