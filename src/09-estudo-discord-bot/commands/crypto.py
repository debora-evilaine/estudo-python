import requests
from discord.ext import commands

class Crypto(commands.Cog):
    """Works with cryptocurrency"""
    def __init__(self, bot):
        self.bot = bot 

    #bot.commands vira commands.command
    @commands.command(help = "Verifica o preço de um par na bilance (precisa dos argumentos 'moeda' e 'base')")
    async def binance(self, ctx, coin, base):
        try: 
            response = requests.get(f"https://api.biance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
            data = response.json()
            price = data.get("price")
            
            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else: 
                await ctx.send(f"O valor do par {coin}/{base} é inválido!")
        
        except Exception as error: 
            await ctx.send("Oops... algo deu errado!")
            print(error)
    
def setup(bot):
    bot.add_cog(Crypto(bot))
    