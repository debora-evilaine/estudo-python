import discord
from discord.ext import commands

class Images(commands.Cog):
    """Works with images"""
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name = "foto", help = "Te envia uma foto aleatória (não requer argumentos)")
    async def get_random_image(self, ctx):
        url_image = "https://picsum.photos/1920/1080"
        
        embed = discord.Embed(
        title = "Resultado da busca de imagem",
        description = "Atenção: a busca é totalmente aleatória!",
        color = 0x0000FF
        )
        
        embed.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = "Feito por:" + self.bot.user.name, icon_url = self.bot.user.avatar_url)    
        
        embed.add_field(name = "API", value = "Usamos a API do https://picsum.photos/1920/1080")
        embed.add_field(name = "Parâmetros", value = "{largura}/{altura}")
        
        embed.add_field(name = "Exemplo", value = url_image, inline = False)
        
        embed.set_image(url = url_image)
        
        await ctx.send(embed =  embed)
        
def setup(bot):
    bot.add_cog(Images(bot))
