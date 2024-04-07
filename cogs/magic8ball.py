import discord
from discord.ext import commands

import random

class M8Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("8ball is ready")

    @commands.command(aliases=['8ball', 'шар'])
    async def M8B(self, ctx, question):
        print(question)
        if question:
            with open("assets/command_files/8ballresponces.txt", encoding="utf-8") as f:
                responces = f.readlines()
                await ctx.reply(f'Мой ответ - {random.choice(responces)}')
            print(question)
        elif len(question) == 0:
            await ctx.reply('нахуй пошел')

async def setup(client):
    await client.add_cog(M8Ball(client))