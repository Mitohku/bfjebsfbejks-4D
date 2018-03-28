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

def to_emoji(c):
    base = 0x1f1e6
    return chr(base + c)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    command_name = bot.command_prefix + 'strawpoll'
    messageContent = message.content
    if message.content.startswith(command_name):
        pollURL = await createStrawpoll(messageContent)
        await message.channel.send(pollURL)
    else:
        await bot.process_commands(message)

		
@bot.command()
async def test(ctx):
	embed = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed.set_author(name = "TEST")
	embed.description = f"CECI EST UNE COMMANDE DE TEST"
	embed.set_footer(text = "TEST")

	await ctx.send(embed = embed)

	try:
		await ctx.message.delete()
	except:
		pass

@bot.command(aliases = ['team'])
async def staff(ctx):
	embed1 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed2 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed3 = discord.Embed(colour = discord.Colour(0xC21C1C))	
	embed4 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed5 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed6 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed7 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed8 = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed9 = discord.Embed(colour = discord.Colour(0xC21C1C))
	texte1 = "***/!\ ROLES & DESCRIPTION DU STAFF /!\***\nㅤ"
	texte2 = "ㅤ\nㅤ\nㅤ\n***/!\ ROLES & DESCRIPTION DU NOYAU DUR /!\***\nㅤ"
	

	await ctx.send(texte1)
	embed1.set_author(name = "Foreigners 4D")
	embed1.description = f"Say\nㅤ"
	embed1.add_field(name="Description", value= f"- **__Rôle Principal:__** Ils sont intégrés au sein du staff en statut de formation, avec une attente d'une semaine maximum. Jeni *(Responsable des **Animateurs**/**Helpers***)* valide ou non l'intégration définitive.\n- **__Les attentes:__** Ils doivent s'occuper des **Sans Papiers** (accueillir les nouveaux), dynamiser le serveur, faire des invitations de masse.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles.", inline=False)
	embed1.set_footer(text = "| ©  Say'ㅤ1-(1/5)")
	embed2.set_author(name = "Animators / Helpers")
	embed2.description = f"Alone **-** Lurewing **-** Reyss **-** K\nㅤ"
	embed2.add_field(name="Description", value= f"- **__Rôle Principal:__** Ce sont des **Animateurs**/**Helpers** confirmés\n- **__Les attentes:__** Ils doivent s'occuper des **Sans Papiers** (accueillir les nouveaux), dynamiser le serveur, faire des invitations de masse.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles, expulser un membre.", inline=False)
	embed2.set_footer(text = "| ©  Say'ㅤ1-(2/5)")
	embed3.set_author(name = "Moderators")
	embed3.description = f"Savy **-** Ascian\nㅤ"
	embed3.add_field(name="Description", value= f"- **__Rôle Principal:__** Ils encadrent les **Animateurs** et les **Foreigners** de manière technique et relationnelle.\n- **__Les attentes:__** Ils doivent dynamiser le serveur, faire des invitations de masse. Ils jouent le rôle de médiateur entre membres, **Foreigners** et **Animateurs**\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser un membre.", inline=False)
	embed3.set_footer(text = "| ©  Say'ㅤ1-(3/5)")
	embed4.set_author(name = "Operators")
	embed4.description = f"Dom **-** Jeni\nㅤ"
	embed4.add_field(name="Description", value= f"- **__Rôle Principal:__** Dom gère la zone +18 *(trash, section adulte, etc..)*\n- **__Les attentes:__** Ils sont autant proches des nouveaux membres que du Fondateur. La prise du recul et la priorisation sont leurs armes.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser un membre.", inline=False)
	embed4.set_footer(text = "| ©  Say'ㅤ1-(4/5)")
	embed5.set_author(name = "Administrators")
	embed5.description = f"Cancer **-** NONOXX **-** Skippy **-** Ashley\nㅤ"
	embed5.add_field(name="Description", value= f"- **__Rôle Principal:__** ???\n- **__Les attentes:__** Ils encadrent les **Modérateurs**, les **Animateurs**/**Helpers** et les **Foreigners** de manière technique et relationnelle.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser/bannir un membre.", inline=False)
	embed5.set_footer(text = "| ©  Say'ㅤ1-(5/5)")
	
	await ctx.send(embed = embed1)
	await ctx.send(embed = embed2)
	await ctx.send(embed = embed3)
	await ctx.send(embed = embed4)
	await ctx.send(embed = embed5)
	
	
	await ctx.send(texte2)
	embed6.set_author(name = "Cancer")
	embed6.add_field(name="ㅤ", value= f"Gère la zone vocal du serveur", inline=False)
	embed6.set_footer(text = "| ©  Say'ㅤ2-(1/4)")
	embed7.set_author(name = "Skippy")
	embed7.add_field(name="ㅤ", value= f"Valide  les recrutements (candidatures / évolutions rôles)  du staff.", inline=False)
	embed7.set_footer(text = "| ©  Say'ㅤ2-(2/4)")
	embed8.set_author(name = "NONOXX")
	embed8.add_field(name="ㅤ", value= f"Gère tout ce qui est interface graphique du serveur (logos/emojis/etc..)", inline=False)
	embed8.set_footer(text = "| ©  Say'ㅤ2-(3/4)")
	embed9.set_author(name = "Ashley")
	embed9.add_field(name="ㅤ", value= f"Gère la planification des évènements, les réseaux sociaux, le règlement. (back-up Fondatrice).", inline=False)
	embed9.set_footer(text = "| ©  Say'ㅤ2-(4/4)")
	
	await ctx.send(embed = embed6)
	await ctx.send(embed = embed7)
	await ctx.send(embed = embed8)
	await ctx.send(embed = embed9)

	try:
		await ctx.message.delete()
	except:
		pass


@bot.command(aliases=['purge', 'clear', 'cc'])
async def clearchat(ctx, number):
	number = int(number)
	if number > 99 or number < 1:
		await ctx.send("Je ne peux supprimer que jusqu'à 99 messages", delete_after=10)
	else:
		author = ctx.message.author
		authorID = author.id
		mgs = []
		number = int(number)
		channel = ctx.message.channel
		async for x in bot.logs_from((channel), limit = int(number+1)):
			mgs.append(x)
			await delete_messages(mgs)
			msg = "🗑 {} a clear **{}** messages dans *{}*".format(ctx.message.author.mention, number, ctx.message.channel.mention)
			await ctx.send(msg, delete_after=4)
			await ctx.send("💢 Vous n'avez pas la permission de faire cette commande")



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
