import discord
from discord.ext import commands

from assets.bot_info import bot_info

class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Info is ready")

    @commands.command(aliases=['инфо'])
    async def info(self, ctx):
        embedMsg = discord.Embed(title="Информация", description=f'Бот для сигм\n\nversion {bot_info['version']}')
        await ctx.send(embed=embedMsg)
async def setup(client):
    await client.add_cog(info(client))