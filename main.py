#The Rancher Rewrite
#Created by Hunter Berg

import discord
import asyncio
import os
from dotenv import load_dotenv
import youtube_dl
import math
from discord.utils import get
from discord.ext import commands


load_dotenv()
token = os.environ['TOKEN'] 

Bot = commands.Bot(
	command_prefix=commands.when_mentioned_or("*"),
	description='The Master of 18 naked cowboys '
)

@Bot.command() # *ping command
async def ping(ctx): #shows latency of bot in ms 
	"""Shows the ping of the bot ton the Discord servers in ms"""
	await ctx.send(f'Pong! `{math.floor(Bot.latency * 1000)}` ms')

@Bot.command() #speak command (*speak)
async def speak(ctx, *, text):
	"""A command only Hunter can use. It allows him to speak through the bot."""
	if ctx.message.author.id == 355099018113843200:
		message = ctx.message 
		await message.delete()

		await ctx.send(text)
	else:
		await ctx.send("this is not a command you can use")

@Bot.command()
async def lick(ctx): #tounge command (*lick)
	"""Sends a gif in chat :)"""
	await ctx.send("https://tenor.com/view/licktung-pokemon-wiggle-tongue-tongue-out-bleh-gif-17629715")

@Bot.event #bot status
async def on_ready():
	await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))
	print('Rancher is Online') #prints this in the consle when the bot is running 