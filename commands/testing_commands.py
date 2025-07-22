import discord
from discord import app_commands
from discord.ext import commands

class TestingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ------ SLASH COMMANDS ------

    @app_commands.guilds(discord.Object(id=1390429149512077383))
    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

    @app_commands.command(name="private_echo", description="Echo a message privately.")
    @app_commands.describe(message="The message to echo.")
    async def private_echo(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message, ephemeral=True)

    # ------ PREFIX COMMANDS ------

    @commands.command(name="prefix_ping")
    async def prefixed_ping(self, ctx: commands.Context):
        await ctx.send("Pong (from prefix command)!")

async def setup(bot):
    cog = TestingCommands(bot)
    await bot.add_cog(cog)