from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv

extensions = [
    'cogs.keeper'
]

bot = commands.Bot("::")

