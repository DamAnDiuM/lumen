import discord
from discord.ext import commands
import random

from assets.env import *

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Working\n-------")

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Pong!\n\nReplied in {latency}ms")

@client.command(aliases=['8ball', 'magic8ball'])
async def шар(ctx, *, question):
    with open("assets/command_files/8ballresponces.txt", encoding='utf-8') as f:
        responces = f.readlines()
        responce = random.choice(responces)
    await ctx.reply(f"Мой ответ - {responce}")
    
@client.command(aliases=['prefix'])
async def префикс(ctx):
    ...
client.run(token)