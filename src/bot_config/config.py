import os
from discord import Intents
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN   =   os.getenv("BOT_TOKEN")
BOT_GUILD   =   os.getenv("BOT_GUILD")
INTENTS     =   Intents.default()