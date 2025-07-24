import asyncio
import discord
from discord.ext import commands

class SillyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def secret(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.send('Shh! 🤫', delete_after=2)
            asyncio.sleep(2.5)
            await ctx.message.delete()

async def setup(bot):
    await bot.add_cog(SillyCommands(bot))