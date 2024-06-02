import discord
from bot_config.config import BOT_TOKEN, INTENTS, BOT_GUILD
from discord import app_commands
from user_commands import Ping
from bot.commands import COMMANDS

class OliTicBot(discord.Client):
    def __init__(self):
        super().__init__(intents=INTENTS)
        self.synced_commands = False
        self.tree = app_commands.CommandTree(self)
        self.__register_commands()
        

    def run(self):
        super().run(BOT_TOKEN)
        
    async def on_ready(self):
        if self.tree and not self.synced_commands:
            await self.tree.sync(guild=discord.Object(id=BOT_GUILD))
            self.synced_commands = True
            print("Command tree is ready!")

    def __register_commands(self):
        for command in COMMANDS:
            @self.tree.command(
                        name=command["name"],
                        description=command["description"],
                        guild=discord.Object(id=BOT_GUILD)
                        )
            async def com(interaction: discord.Interaction):
                await command["handler"](interaction)
            
        

   

client = OliTicBot()

