import discord
from discord.ext import commands

import random

class M8ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready():
        print("8ball is ready")

    @commands.command(aliases=['шар', '8ball'])
    async def m8ball(ctx, *, question):
        with open("assets/command_files/8ballresponces.txt", encoding='utf-8') as f:
            responces = f.readlines()
            responce = random.choice(responces)
        await ctx.reply(f"Мой ответ - {responce}")


async def setup(client):
    await client.add_cog(M8ball(client))