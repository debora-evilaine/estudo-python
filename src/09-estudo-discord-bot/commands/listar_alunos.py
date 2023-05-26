import discord
from discord.ext import commands


class Listas(commands.Cog):
    """cadastra um aluno por vez"""
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name = "listar_alunos", help = "Apresenta os alunos em forma de embed")
    async def student_list(self, ctx):
        arquivo = open("alunos.txt", "r", encoding = "utf-8")
        linhas = []
        for linha in arquivo:
            linha = linha.strip()
            linhas.append(linha)
        resultado = ','.join(linhas)
        #await ctx.send(f"Até o momento, já cadastrei {len(linhas)} alunos: {resultado}")
            
        embed = discord.Embed(
        title = "Resultado da busca de cadastrados",
        description = "Aqui, eu listo todos os alunos cadastrados até o momento.",
        color = 0x0000FF
        )
            
        embed.set_author(name = self.bot.user.name, icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = "Feito por: " + self.bot.user.name, icon_url = self.bot.user.avatar_url)    
            
        embed.add_field(name = "Resultados", value = f"Até o momento, já cadastrei {len(linhas)} alunos: {resultado}")
        embed.add_field(name = "Parâmetros", value = "Prontuário, nome e email")
            
        await ctx.send(embed =  embed)
        
        arquivo.close()

def setup(bot):
    bot.add_cog(Listas(bot))