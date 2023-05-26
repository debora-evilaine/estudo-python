from discord.ext import commands

class Cadastros(commands.Cog):
    """cadastra um aluno por vez"""
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name = "cadastrar_aluno", help = "Cadastra um aluno por vez. Aceita apenas 3 argumentos")
    async def sign_up(self, ctx, *args):
        if len(args)!=3:
            await ctx.send("Opa! Não consigo finalizar o cadastro sem todos os dados necessários! Por favor, forneça apenas o prontuário, nome e email, ou, se preferir, peça ajuda digitando '!help'")
        
        else:
            alunos = []
            dados = ','.join(args)
            await ctx.send(f'{len(args)} dados foram enviados: {dados}')
            alunos.append(dados)
            print(alunos)
            
        arquivo = open("alunos.txt", "a", encoding = "utf-8")
        arquivo.writelines(alunos)
        arquivo.writelines("\n")
        await ctx.send("Eba! O aluno foi cadastrado com sucesso!")
        
        arquivo.close()

def setup(bot):
    bot.add_cog(Cadastros(bot))








