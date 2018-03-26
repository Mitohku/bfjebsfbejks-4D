import discord
from discord.ext import commands
import asyncio
import os
import sys
import time
import random
import datetime as dt
import datetime
import json, asyncio
import copy
import logging
import traceback
import aiohttp
from collections                import Counter


command_prefix = "!" #CHANGE IT TO WHAT YOU WANT
description = "Bot Privé de la 4ème Dimension" #ALSO CHANGE THIS
bot = commands.Bot(command_prefix, description = description)
bot.remove_command('help')
tu = datetime.datetime.now()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def test(ctx):
	embed = discord.Embed(colour = discord.Colour(0xA22121))
	embed.set_author(name = "TEST")
	embed.description = f"CECI EST UNE COMMANDE DE TEST"
	embed.set_footer(text = "TEST")
	await ctx.send(embed=embed)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
