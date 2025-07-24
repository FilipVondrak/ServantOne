import discord
import subprocess
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

        print(f"Synced {len(synced_gl)} commands globally ({len(synced_test)} totally).")
        await ctx.send(f"Synced {len(synced_gl)} commands globally ({len(synced_test)} totally)")


    @commands.command(name="script")
    @commands.is_owner()
    async def script(self, ctx: commands.Context, script: str, *args: str) -> None:
        script_path = f"./scripts/{script}.sh"

        # tries to run the script selected by user
        # the output is printed to console and also sent back to user
        try:
            result = subprocess.run([script_path, *args], capture_output=True, text=True, check=True)
            print(result.stdout)
            await ctx.reply(result.stdout)
        except FileNotFoundError:
            await ctx.reply("Script not found / invalid script")
        except FileExistsError:
            await ctx.reply("Script not executable!")
        except PermissionError:
            await ctx.reply("You don't have permission execute this script.")
        except Exception as e:
            print("Unexpected error:", e)
            await ctx.reply("That didnt work :(")


async def setup(bot):
    await bot.add_cog(OwnerCommands(bot))