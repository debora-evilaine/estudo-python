import discord
from decouple import config
from discord.ext import commands
import tracemalloc
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

 
tracemalloc.start()



intents = discord.Intents.default()

intents.messages = True
intents = discord.Intents.default()
intents.members = True
intents.presences = True


bot = commands.Bot(command_prefix='!', intents=intents)


bot.load_extension('manager')
bot.load_extension('commands.images')
bot.load_extension('commands.maths')
bot.load_extension('commands.reactions')
bot.load_extension('tasks.dates')
bot.load_extension('commands.talks')
bot.load_extension('commands.listar_arquivo')
bot.load_extension('commands.listar_alunos')
bot.load_extension('commands.cadastro')
tracemalloc.stop()

  




       

       




TOKEN = config("TOKEN")
bot.run(TOKEN)