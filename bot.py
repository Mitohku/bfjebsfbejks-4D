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
	embed3.description = f"Savy **-** Ascian **-** Khalyte\nㅤ"
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

@bot.command()
async def radio(ctx):
	embed = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed.set_author(name = "FirstStation - Une Nouvelle WebRadio") 
	embed.description = f"Vous vous ennuyez? Vous voulez juste écouter de la musique?\nEcoutez **FirstStation** en direct!\n\n**__http://firststation.fr/__**\nㅤ"
	embed.set_footer(text = "| ©  FirstStation")

	await ctx.send(embed = embed)

@bot.command(aliases = ['anim', 'animation', 'evenement'])
async def event(ctx):
	imitation = "EVENT IMITATION JENI ASHLEY"
	karaoke = "KARAOKE ALONE-K-REYSS🎶"

	embed = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed.set_author(name = "PLANIFICATION DES EVENEMENTS") 
	embed.description = f"ㅤ"
	embed.add_field(name="Gaming'Actu", value= f"Samedi 31 Mars, 17h-18h, **(FirstStation)**\n*Animé par **Say' [ Hypesia.net ]***\nㅤ", inline=False)
	embed.add_field(name="Karaoké", value= f"Tous les Samedis, 21h, **({karaoke})**\n*Animé par **Say'**, **tricksterGoddess***\nㅤ", inline=False)
	embed.add_field(name="Imitations Vocales", value= f"Dimanche 1 Avril, 21h, **({imitation})**\n*Animé par **J.Ɛ.Ɲ.I.**, **Ashley***", inline=False)
	embed.set_footer(text = "| ©  Say'")

	await ctx.send(embed = embed)

@bot.command(aliases = ['bd', 'bday', 'anniversaire', 'birthday'])
async def anniv(ctx, *, member: discord.Member = None):
	staff = [288357574607110146, 207959196870770698, 221040142788329483, 287973799423377408, 200299673586499584, 268422888699199488, 287936701626580992, 213014237075734530, 311063007809765376, 211850949801672706, 204045143571955715, 260434985364881409, 263755586418507777, 332987567362539522, 282868217997819904, 286573704949792770, 265228969098477568, 385419569558323202]
	
	if member is None:
		member = ctx.author

	if member.id in staff:
		embed = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed.set_author(name = "DATES D'ANNIVERSAIRES DU STAFF") 
		embed.description = f"ㅤ"
		#embed.add_field(name="Bodhi", value= f"???", inline=False)
		#embed.add_field(name="Ashley", value= f"???", inline=False)
		embed.add_field(name="NONOXX", value= f"8 Juillet\n--------------------------", inline=False)
		#embed.add_field(name="Skippy", value= f"???", inline=False)
		#embed.add_field(name="Cancer", value= f"???\n--------------------------", inline=False)
		embed.add_field(name="Jeni", value= f"27 Mars\n--------------------------", inline=False)
		#embed.add_field(name="Dom", value= f"???\n--------------------------", inline=False)
		embed.add_field(name="Ascian", value= f"4 Juin", inline=False)
		embed.add_field(name="Khalyte", value= f"29 Décembre\n--------------------------", inline=False)
		#embed.add_field(name="Savy", value= f"???\n--------------------------", inline=False)
		embed.add_field(name="Lurewing", value= f"16 Janvier", inline=False)
		embed.add_field(name="K", value= f"4 Décembre", inline=False)
		#embed.add_field(name="Alone", value= f"???", inline=False)
		embed.add_field(name="Reyss", value= f"24 Avril\n--------------------------", inline=False)
		embed.add_field(name="Say'", value= f"15 Novembre", inline=False)
		embed.set_footer(text = "| ©  Say'")

		await ctx.send(embed = embed)
	else:
		return

@bot.group()
async def game(self):

	if game == None:
		await self.send(f"Merci d'utiliser un des paramètres: `on`, `off`")

@game.command()
async def game_on(self, *, game = None):
	author = ctx.message.author.mention

	if not game:
		await self.send(f"Merci de mettre une raison!")
	else:
		embed1 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed1.description = f"{author} est désormais AFK pour **{game}** !"
		embed1.set_footer(text = "| ©  Say'")

@game.command()
async def game_off(self, *, game = None):
	author = ctx.message.author.mention

	if not game:
		embed2 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed2.description = f"{author} n'est plus AFK !"
		embed2.set_footer(text = "| ©  Say'")
	else:
		return



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
