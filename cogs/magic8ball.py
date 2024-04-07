import discord
from discord.ext import commands

import random

class M8Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("8ball is ready")

    @commands.command()
    async def M8B(self, ctx):
        ctx.send("work")


async def setup(client):
    await client.add_cog(M8Ball(client))