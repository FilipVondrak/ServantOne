import discord
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