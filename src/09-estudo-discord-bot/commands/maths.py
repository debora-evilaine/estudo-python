from discord.ext import commands

class Maths(commands.Cog):
    """Works with math and math-related commands"""
    def __init__(self, bot):
        self.bot = bot 

    #bot.command virou: commands.command
    @commands.command(name = "calcular", help = "Calcula uma expressão (precisa do argumento 'expressão')")
    async def calculate_expression(self, ctx, *expression):
        expression = "".join(expression)
        response = eval(expression)
        
        await ctx.send("A resposta é: " + str(response))
    
def setup(bot):
    bot.add_cog(Maths(bot))
    