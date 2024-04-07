import discord
from discord.ext import commands

class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Prefix is ready")

    @commands.command(aliases=['префикс'])
    async def prefix(self, ctx, prefix):
        if not prefix:
            await ctx.send(f"Current prefix - {self.client.command_prefix}")
        else:
            self.client.command_prefix = prefix
            await ctx.send(f"Prefix changed to {prefix}")


async def setup(client):
    await client.add_cog(Prefix(client))