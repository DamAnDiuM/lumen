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
        if question:
            with open("assets/command_files/8ballresponces.txt", encoding="utf-8") as f:
                responces = f.readlines()
                responce = random.choice(responces)
                embed_message = discord.Embed(title=question, description=responce, color=discord.Color.purple())
                await ctx.reply(embed = embed_message)
            

async def setup(client):
    await client.add_cog(M8Ball(client))