import discord
import re
import asyncio
from discord import app_commands
from discord.ext import commands


class RandomCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joined(self, ctx, member: discord.Member = None):
        if member == None: member = ctx.author
        try:
            await ctx.send(f'{member} joined on {member.joined_at}')
        except discord.ext.commands.errors.MemberNotFound:
            await ctx.send("Please specify a valid member")

    @commands.command()
    async def remind(self, ctx, time: str = "", task: str = "You have been reminded"):
        time = time.strip().lower()

        if time == "help" or time == "":
            await ctx.send("Use format like: `1d2h30m10s Task description`")
            return

        pattern = r'(?:(\d+)d)?(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?'
        match  = re.fullmatch(pattern, time)
        days, hours, minutes, seconds = [int(x) if x else 0 for x in match.groups()]
        total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds

        if total_seconds == 0:
            await ctx.send("You need to specify at least one time unit (e.g., `10s`, `2m`).")
            return

        await asyncio.sleep(total_seconds)
        await ctx.send(f"{ctx.author.mention}\n⏰ Reminder: {task}")


    @commands.command()
    async def avatar(self, ctx, member: str = None):
        if member is None:
            user = ctx.author
        elif member.isdigit():
            try:
                user = await ctx.bot.fetch_user(int(member))
            except discord.NotFound:
                await ctx.send("User not found.")
                return
            except discord.HTTPException:
                await ctx.send("Failed to fetch user. Try again later.")
                return
            except Exception as e:
                await ctx.send("Failed to fetch user.")
                # Optional: log the error if needed
                print(f"Error fetching user: {e}")
                return
        else:
            try:
                user = await commands.MemberConverter().convert(ctx, member)
            except commands.MemberNotFound:
                await ctx.send("Please specify a valid member.")
                return

        await ctx.send(user.avatar.url)

async def setup(bot):
    await bot.add_cog(RandomCommands(bot))