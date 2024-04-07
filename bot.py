import discord
from discord.ext import commands, tasks
import random

from itertools import cycle
import os
import asyncio

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

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            
async def main():
    async with client:
        await load()
        await client.start(token)
@client.event
async def on_ready():
    print("Working\n-------")
    change_status.start()


asyncio.run(main())


@client.command(aliases=['prefix'])
async def префикс(ctx, prefix):
    client.command_prefix = prefix
    await ctx.send(f"Prefix changed to {prefix}")
    