from discord.ext import commands
import discord 

class Talks(commands.Cog):
    """Talks with user"""
    def __init__(self, bot):
        self.bot = bot 

    #bot.commands virou commands.command
    @commands.command(name="oi", help ="Envia um 'oi' (Não requer argumentos!)")
    async def send_hello(self, ctx):
        name = ctx.author.name

        response = "Olá, " +name

        await ctx.send(response)

    

    @commands.command(name = "segredo", help = "Te envia um segredo! (não requer argumentos)")
    async def secret(self, ctx):
        try: 
            await ctx.author.send("Essa mensagem é secreta!")
            await ctx.author.send("Essa também!")
            await ctx.author.send("E essa...")
            
        except discord.errors.Forbidden:
            await ctx.send("Ei, eu não posso te contar esse segredo! Mas se você quiser mesmo saber, então habilite receber mensagens de qualquer pessoa do servidor: (Opções > Privacidade)")

def setup(bot):
    bot.add_cog(Talks(bot))
    