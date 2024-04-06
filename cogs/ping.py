import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready")

    @commands.command(aliases=['пинг'])
    async def ping(self, ctx):
        latency = round(self.client.latency * 1000)
        await ctx.send(f"Pong!\n\nReplied in {latency} ms")

        
async def setup(client):
    await client.add_cog(Ping(client))