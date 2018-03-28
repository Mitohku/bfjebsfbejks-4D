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
async def quickpoll(ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await reaction.emoji(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await ctx.bot.edit_message(react_message, embed=embed)

		
@bot.command()
async def test(ctx):
	embed = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed.set_author(name = "TEST")
	embed.description = f"CECI EST UNE COMMANDE DE TEST"
	embed.set_footer(text = "TEST")
	await ctx.send(embed=embed)

@bot.command(aliases = ['team'])
async def staff(ctx):


		text1 = discord.Embed(colour = discord.Colour(0xC21C1C))
		text2 = discord.Embed(colour = discord.Colour(0xC21C1C))

		await add_reaction(message(ctx.author(bot)))
		


		embed1 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed2 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed3 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed4 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed5 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed6 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed7 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed8 = discord.Embed(colour = discord.Colour(0xC21C1C))
		embed9 = discord.Embed(colour = discord.Colour(0xC21C1C))
		texte1 = "***/!\ ROLES & DESCRIPTION DU STAFF /!\***"
		texte2 = "***/!\ ROLES & DESCRIPTION DU NOYAU DUR /!\***"
	

		await ctx.send(texte1)
		embed1.set_author(name = "Foreigners 4D")
		embed1.description = f"Say\nㅤ"
		embed1.add_field(name="Description", value= f"- **__Rôle Principal:__** Ils sont intégrés au sein du staff en statut de formation, avec une attente d'une semaine maximum. Jeni *(Responsable des **Animateurs**/**Helpers***)* valide ou non l'intégration définitive.\n- **__Les attentes:__** s'occuper des **Sans Papiers** (accueillir les nouveaux), dynamiser le serveur, faire des invitations de masse.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles.", inline=False)
		embed1.set_footer(text = "| ©  Say'  1-(1/5)")
		embed2.set_author(name = "Animators / Helpers")
		embed2.description = f"Alone **-** Lurewing **-** Reyss **-** K\nㅤ"
		embed2.add_field(name="Description", value= f"- **__Rôle Principal:__** Ce sont des **Animateurs**/**Helpers** confirmés\n- **__Les attentes:__** Ils doivent s'occuper des **Sans Papiers** (accueillir les nouveaux), dynamiser le serveur, faire des invitations de masse.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles, expulser un membre.", inline=False)
		embed2.set_footer(text = "| ©  Say'  1-(2/5)")
		embed3.set_author(name = "Moderators")
		embed3.description = f"Savy **-** Ascian\nㅤ"
		embed3.add_field(name="Description", value= f"- **__Rôle Principal:__** Ils encadrent les **Animateurs** et les **Foreigners** de manière technique et relationnelle.\n- **__Les attentes:__** Ils doivent dynamiser le serveur, faire des invitations de masse. Ils jouent le rôle de médiateur entre membres, **Foreigners** et **Animateurs**\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser un membre.", inline=False)
		embed3.set_footer(text = "| ©  Say'  1-(3/5)")
		embed4.set_author(name = "Operators")
		embed4.description = f"Dom **-** Jeni\nㅤ"
		embed4.add_field(name="Description", value= f"- **__Rôle Principal:__** Dom gère la zone +18 *(trash, section adulte, etc..)*\n- **__Les attentes:__** Ils sont autant proches des nouveaux membres que du Fondateur. La prise du recul et la priorisation sont leurs armes.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser un membre.", inline=False)
		embed4.set_footer(text = "| ©  Say'  1-(4/5)")
		embed5.set_author(name = "Administrators")
		embed5.description = f"Cancer **-** NONOXX **-** Skippy **-** Ashley\nㅤ"
		embed5.add_field(name="Description", value= f"- **__Rôle Principal:__** ???\n- **__Les attentes:__** Ils encadrent les **Modérateurs**, les **Animateurs**/**Helpers** et les **Foreigners** de manière technique et relationnelle.\n- **__Droits:__** mute/unmute sur les salons vocaux, ajouts de rôles *(**+18 NSFW**)*, expulser/bannir un membre.", inline=False)
		embed5.set_footer(text = "| ©  Say'  1-(5/5)")
	
		await ctx.send(embed = embed1)
		await ctx.send(embed = embed2)
		await ctx.send(embed = embed3)
		await ctx.send(embed = embed4)
		await ctx.send(embed = embed5)
	
	
		await ctx.send(texte2)
		embed6.set_author(name = "Cancer")
		embed6.add_field(name="ㅤ", value= f"Gère la zone vocal du serveur", inline=False)
		embed6.set_footer(text = "| ©  Say'  2-(1/4)")
		embed7.set_author(name = "Skippy")
		embed7.add_field(name="ㅤ", value= f"Valide  les recrutements (candidatures / évolutions rôles)  du staff.", inline=False)
		embed7.set_footer(text = "| ©  Say'  2-(2/4)")
		embed8.set_author(name = "NONOXX")
		embed8.add_field(name="ㅤ", value= f"Gère tout ce qui est interface graphique du serveur (logos/emojis/etc..)", inline=False)
		embed8.set_footer(text = "| ©  Say'  2-(3/4)")
		embed9.set_author(name = "Ashley")
		embed9.add_field(name="ㅤ", value= f"Gère la planification des évènements, les réseaux sociaux, le règlement. (back-up Fondatrice).", inline=False)
		embed9.set_footer(text = "| ©  Say'  2-(4/4)")
	
		await ctx.send(embed = embed6)
		await ctx.send(embed = embed7)
		await ctx.send(embed = embed8)
		await ctx.send(embed = embed9)
		


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
