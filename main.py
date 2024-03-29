from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
extensions = [
    'cogs.keeper'
]

bot = commands.Bot("::")

for extension in extensions:
    bot.load_extension(extension)

bot.run(os.environ.get("TOKEN"))
