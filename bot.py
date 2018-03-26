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


command_prefix = "!" 
description = "Bot Privé de la 4ème Dimension"
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
	embed = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed.set_author(name = "TEST")
	embed.description = f"CECI EST UNE COMMANDE DE TEST"
	embed.set_footer(text = "TEST")
	await ctx.send(embed=embed)

@bot.command(aliases = ['team'])
async def staff(ctx):
	embed1 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed2 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed3 = discord.Embed(colour = discord.Colour(0xC21C1C))
	texte1 = "***/!\ ROLES & DESCRIPTION DU STAFF /!\***"
	texte2 = "***/!\ ROLES & DESCRIPTION DU NOYAU DUR /!\***"

	await ctx.send(texte1)
	embed1.set_author(name = "Foreigners 4D")
	embed1.description = f"Say"
	embed1.add_field(name="Description", value= f"- **__Rôle Principal:__** Ils sont intégrés au sein du staff en statut de formation, sous une attente d'une semaine maximum. Jeni (Responsable des animateurs/helpers) valide ou non l'intégration définitive.\n- **__Les attentes:__** s'occuper des **Sans Papiers** (accueillir les nouveaux), dynamiser le serveur, faire des invites de masse.\n- **__Droits :__**  mutes/unmute sur les salons vocaux, ajouts de rôles.", inline=False)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
