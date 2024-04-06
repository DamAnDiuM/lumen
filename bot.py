import discord
from discord.ext import commands, tasks
import random
from itertools import cycle

from assets.env import *

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

with open("assets/commands_list.txt", encoding="utf-8") as f:
    bot_statuses = []
    responces = f.readlines()
    for responce in responces:
        bot_statuses.append(client.command_prefix + responce.strip())

bot_status = cycle(bot_statuses)

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))


@client.event
async def on_ready():
    print("Working\n-------")
    change_status.start()


@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Pong!\n\nReplied in {latency} ms")


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