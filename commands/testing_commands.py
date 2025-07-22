import discord
from discord import app_commands
from discord.ext import commands

class TestingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ------ SLASH COMMANDS ------

    @app_commands.command(name="private_echo", description="Echo a message privately.")
    @app_commands.describe(message="The message to echo.")
    async def private_echo(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message, ephemeral=True)

    # ------ HYBRID COMMANDS ------

    @commands.hybrid_command(name="ping", description="Check bot latency.")
    async def ping(self, ctx: commands.Context):
        await ctx.reply(f"Pong! {round(self.bot.latency * 1000)}ms")

async def setup(bot):
    cog = TestingCommands(bot)
    await bot.add_cog(cog)