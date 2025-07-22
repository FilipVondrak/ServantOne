import discord
from discord import app_commands
from discord.ext import commands


class RandomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        await ctx.send(f'{member} joined on {member.joined_at}')

async def setup(bot):
    await bot.add_cog(RandomCommands(bot))