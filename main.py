import discord
from discord import app_commands
from discord.ext import commands

import logging
from dotenv import load_dotenv
import os

# load token environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# set logging into discord.log
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

# syncs commands on bot start
async def setup_hook() -> None:
    await bot.tree.sync()

bot.setup_hook = setup_hook

@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="echo", description="Echoes a message.")
@app_commands.describe(message="The message to echo.")
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

@bot.tree.command(name="private_echo", description="Echoes a message privately.")
@app_commands.describe(message="The message to echo.")
async def private_echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message, ephemeral=True)

@bot.tree.command()
async def ping(inter: discord.Interaction) -> None:
    await inter.response.send_message(f"> Pong! {round(bot.latency * 1000)}ms")


@bot.command()
@commands.is_owner()
async def sync(ctx: commands.Context) -> None:
    synced = await ctx.bot.tree.sync()

    print(f"Synced {len(synced)} commands globally")
    await ctx.send(f"Synced {len(synced)} commands globally")

bot.run(TOKEN)