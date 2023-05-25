
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Manages de bot"""
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Estou pronta! Estou conectada como {self.bot.user}")
        
      


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return 
        
        if "palavrão" in message.content:
            await message.channel.send(
                f"Por favor, {message.author.name}, não ofenda os demais usuários!!"
                )
            await message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Por favor envie todos os parâmetros. Ou, se preferir, digite '!help' para obter mais ajuda")
        
        elif isinstance(error, CommandNotFound):
            await ctx.send("Esse comando não existe :( Digite '!help' para descobrir tudo  que posso fazer.")
        
        else:
            raise error

        

def setup(bot):
    bot.add_cog(Manager(bot))
    