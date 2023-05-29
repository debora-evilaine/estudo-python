import discord
from discord.ext import commands
from discord.ui import View, TextInput


class Cadastro(View):
    def __init__(self):
        super().__init__()

        self.prontuario = TextInput(label="Entre com o prontuário do aluno:", placeholder="SP...", style=discord.TextStyle.short)
        self.nome = TextInput(label="Entre com o nome do aluno:", style=discord.TextStyle.short)
        self.email = TextInput(label="Entre com o email do aluno:", style=discord.TextStyle.short)

        self.add_item(self.prontuario)
        self.add_item(self.nome)
        self.add_item(self.email)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.ctx.author:
            return True
        await interaction.response.send_message("Desculpe, você não tem permissão para usar este formulário.")
        return False

    async def on_submit(self, interaction: discord.Interaction):
        nome = self.nome.values[0]
        prontuario = self.prontuario.values[0]
        email = self.email.values[0]

        with open("alunos.txt", "r", encoding="utf-8") as file:
            for line in file:
                line_data = line.strip().split(",")
                line_prontuario = line_data[0].strip()
                line_email = line_data[2].strip()

                if prontuario == line_prontuario or email == line_email:
                    await interaction.response.send_message("Espere! Esse aluno já está cadastrado!")
                    return

        with open("alunos.txt", "a") as file:
            file.write(f"{prontuario}, {nome}, {email}\n")

        await interaction.response.send_message(f'Os dados do aluno cadastrado são: {nome}, {prontuario} e {email}.')

    @staticmethod
    @commands.command(name="modal_de_cadastro")
    async def modal_de_cadastro(ctx: commands.Context):
        view = Cadastro()
        await ctx.send("Cadastro de Alunos", view=view)
