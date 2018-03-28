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

@bot.command(aliases = ['poll'])
async def sondage(ctx, *questions_and_choices: str):
    if len(questions_and_choices) < 3:
        return await ctx.send('Il est nécessaire de donner au moins 1 question et 2 choix.')
    elif len(questions_and_choices) > 21:
        return await ctx.send('Vous ne pouvez mettre que 20 choix.')

    perms = ctx.channel.permissions_for(ctx.me)
    if not (perms.read_message_history or perms.add_reactions):
        return await ctx.send("Je n'ai pas la/les permission(s) **Read Message History** et/ou **Add Reactions**.")

    question = questions_and_choices[0]
    choices = [(to_emoji(e), v) for e, v in enumerate(questions_and_choices[1:])]

    try:
        await ctx.message.delete()
    except:
        pass

    body = "\n".join(f"{key}: {c}" for key, c in choices)
    embed = discord.Embed(title = f"**{ctx.author.name}** vous demandes: ", description = f"{question}", color = discord.Colour(0xC21C1C))
    embed.add_field(name = "Réponses:", value = f"{body}")
    embed.set_thumbnail(url = ctx.author.avatar_url)
    poll = await ctx.send(embed = embed)

    #poll = await ctx.send(f'{ctx.author} asks: {question}\n\n{body}')
    for emoji, _ in choices:
        await poll.add_reaction(emoji)
		
@bot.command()
async def test(ctx):
	embed = discord.Embed(colour = discord.Colour(0xC21C1C))
	embed.set_author(name = "TEST")
	embed.description = f"CECI EST UNE COMMANDE DE TEST"
	embed.set_footer(text = "TEST")

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
