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
	embed1.add_field(name="Description", value= f"- **__Rôle Principal:__** Ils sont intégrés au sein du staff en statut de formation, avec une attente d'une semaine maximum. Jeni *(Responsable des **Animateurs**/**Helpers***)* valide ou non l'intégration définitive.\n- **__Les attentes:__** s'occuper des **Sans Papiers** (accueillir les nouveaux), dynamiser le serveur, faire des invitations de masse.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles.", inline=False)
	embed1.set_footer(text = "| ©  Say' (1/5)")
	embed2.set_author(name = "Animators / Helpers")
	embed2.description = f"Alone **-** Lurewing **-** Reyss **-** K "
	embed2.add_field(name="Description", value= f"- **__Rôle Principal:__** Ce sont des **Animateurs**/**Helpers** confirmés\n- **__Les attentes:__** Ils doivent s'occuper des **Sans Papiers** (accueillir les nouveaux), dynamiser le serveur, faire des invitations de masse.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles, expulser un membre.", inline=False)
	embed2.set_footer(text = "| ©  Say' (2/5)")
	embed3.set_author(name = "Moderators")
	embed3.description = f"Savy **-** Ascian"
	embed3.add_field(name="Description", value= f"- **__Rôle Principal:__** Ils encadrent les **Animateurs** et les **Foreigners** de manière technique et relationnelle.\n- **__Les attentes:__** Ils doivent dynamiser le serveur, faire des invitations de masse. Ils jouent le rôle de médiateur entre membres, **Foreigners** et **Animateurs**\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser un membre.", inline=False)
	embed3.set_footer(text = "| ©  Say' (3/5)")
	embed4.set_author(name = "Operators")
	embed4.description = f"Dom **-** Jeni "
	embed4.add_field(name="Description", value= f"- **__Rôle Principal:__** Dom gère la zone +18 *(trash, section adulte, etc..)*\n- **__Les attentes:__** Ils sont autant proches des nouveaux membres que du Fondateur. La prise du recul et la priorisation sont leurs armes.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser un membre.", inline=False)
	embed4.set_footer(text = "| ©  Say' (4/5)")
	embed5.set_author(name = "Administrators")
	embed5.description = f"Cancer **-** NONOXX **-** Skippy **-** Ashley"
	embed5.add_field(name="Description", value= f"- **__Rôle Principal:__** ???\n- **__Les attentes:__** Ils encadrent les **Modérateurs**, les **Animateurs**/**Helpers** et les **Foreigners** de manière technique et relationnelle.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser/bannir un membre.", inline=False)
	embed5.set_footer(text = "| ©  Say' 1-(5/5)")
	
	await ctx.send(embed1)
	await ctx.send(embed2)
	await ctx.send(embed3)
	await ctx.send(embed4)
	await ctx.send(embed5)
