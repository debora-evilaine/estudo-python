
from discord.ext import commands, tasks
from discord import utils

class Dates(commands.Cog):
    """Works with dates"""
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(hours=1)
    async def current_time(self):
        now = utils.datetime.datetime.now()
        now = now.strftime('%d/%m/%Y as %H:%M:%S')

        channel = self.bot.get_channel(1110680472817778710)
        await channel.send("Data atual: " + now)


def setup(bot):
    bot.add_cog(Dates(bot))
    