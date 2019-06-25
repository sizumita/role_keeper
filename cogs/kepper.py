from discord.ext import commands
import discord
import database


class KeeperCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener(name='on_ready')
    async def on_ready(self):
        await database.setup()
        await self.bot.change_presence(activity=discord.Game(name='::help'))

    @commands.Cog.listener(name='on_member_join')
    async def on_member_join(self, member):
        roles = await database.get_roles(member.id, member.guild.id)
        if not member.guild.me.guild_permissions.manage_roles:
            return

        if roles:
            for _id in roles:
                role = member.guild.get_role(_id)
                if roles is None:
                    continue
                await member.add_roles(role)

    @commands.Cog.listener(name='on_member_remove')
    async def on_member_remove(self, member):
        roles = [i.id for i in member.roles]
        await database.add_roles(member.id, member.guild.id, roles)


def setup(bot):
    return bot.add_cog(KeeperCog(bot))
