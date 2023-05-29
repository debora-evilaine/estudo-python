import discord
from discord.ext import commands
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class Listar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="listar_em_pdf", help="lista os alunos do arquivo alunos.txt em formato pdf")
    async def list_student(self, ctx):
        def create_pdf():
            with open("alunos.txt", "r", encoding="utf-8") as arquivo:
                dados = [linha.strip() for linha in arquivo]
            print("O arquivo foi percorrido!")
            print(dados)

            doc = SimpleDocTemplate("listar-alunos.pdf")
            styles = getSampleStyleSheet()
            paragraph_style = styles['Normal']
            paragraph_style.fontSize = 12

            titulo_paragraph_style = styles['Heading1']
            titulo_paragraph_style.fontSize = 16

            paragraph1 = Paragraph("Alunos Cadastrados", titulo_paragraph_style)
            spacer = Spacer(0, 20)
            paragraph2 = Paragraph(f"Total de alunos: {len(dados)}", paragraph_style)

            header = [["Prontuário", "Nome", "E-mail"]]
            for dado in dados:
                prontuario, nome, email = dado.split(",")
                header.append([prontuario, nome, email])

            table_style = [
                ('BACKGROUND', (0, 0), (-1, 0), 'black'),
                ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), 'white'),
                ('GRID', (0, 0), (-1, -1), 1, 'gray'),
                ('LEFTPADDING', (0, 0), (-1, -1), 60),
                ('RIGHTPADDING', (0, 0), (-1, -1), 60),
            ]

            tabela = Table(header)
            tabela.setStyle(table_style)

            elements = [paragraph1, tabela, spacer, paragraph2]

            doc.build(elements)

            print("PDF criado com sucesso!")

        create_pdf()

        with open("listar-alunos.pdf", "rb") as arquivo_pdf:
            lista_de_alunos = discord.File(arquivo_pdf, filename="listar-alunos.pdf")
            await ctx.send(file=lista_de_alunos)


def setup(bot):
    bot.add_cog(Listar(bot))
