import discord
import time
import datetime

@bot.command(pass_context=True)
async def ping(ctx, *args):
    '''see the bots ping time'''
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    embed = discord.Embed(description = ":ping_pong: **Pong!** ```{}ms```".format(round((t2 - t1) * 1000)) , color = 0xcd6800)
    return await bot.say(embed = embed)
    
 @bot.command(pass_context=True)
async def fortnite(self):
    '''sends a link to fortnite'''
    embed = discord.Embed(text="click this", description="")
    embed.set_author(name="fornite (click)", url="https://www.epicgames.com/fortnite/en-US/buy-now/battle-royale", icon_url=self.bot.user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def roblox(self):
    '''sends a link to roblox'''
    embed = discord.Embed(text="click this", description="click this")
    embed.set_author(name="roblox (click)", url="https://www.roblox.com/?v=rc&rbx_source=5&rbx_medium=cpa&rbx_campaign=27715_RB15", icon_url=self.bot.user.avatar_url)
    await bot.say(embed=embed)
