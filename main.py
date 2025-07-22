import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

# load token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# setup logging
logging.basicConfig(filename='discord.log', encoding='utf-8', level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

# loads extensions from "./commands"
async def load():
    count = 0;
    for file in os.listdir("./commands"):
        if file.endswith(".py") and not file.startswith("__"):
            await bot.load_extension(f"commands.{file[:-3]}")
            count += 1;
    print(f"Loaded {count} cogs")

async def setup_hook():
    # load cogs
    await load()
    # sync commands
    #for cmd in bot.tree.get_commands():
    #    print(cmd.name)

    #await bot.tree.sync()
    #guild = discord.Object(id=1390429149512077383)  # your server ID
    #await bot.tree.sync(guild=guild)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.setup_hook = setup_hook
bot.run(TOKEN)
