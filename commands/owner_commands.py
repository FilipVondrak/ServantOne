import discord
from discord.ext import commands

class OwnerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sync")
    @commands.is_owner()
    async def sync(self, ctx: commands.Context) -> None:
        synced_gl = await ctx.bot.tree.sync()

        guild = discord.Object(id=1390429149512077383)  # your server ID
        synced_test = await ctx.bot.tree.sync(guild=guild)

        print(f"Synced {len(synced_gl)} commands globally ({synced_test} totally).")
        await ctx.send(f"Synced {len(synced_gl)} commands globally ({synced_test} totally)")

async def setup(bot):
    await bot.add_cog(OwnerCommands(bot))