
import discord
from decouple import config
from discord.ext import commands
import requests



intents = discord.Intents.default()

intents.messages = True

bot = commands.Bot(intents=intents, command_prefix="!")



bot.load_extension("manager")

bot.load_extension("commands.crypto")
bot.load_extension("commands.images")
bot.load_extension("commands.maths")
bot.load_extension("commands.reactions")
bot.load_extension("tasks.dates")
bot.load_extension("commands.talks")
bot.load_extension("commands.cadastro")
bot.load_extension("commands.listar_alunos")

  

TOKEN = config("TOKEN")
bot.run(TOKEN)
