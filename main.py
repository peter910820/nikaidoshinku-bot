import discord, os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

class ShinkuBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = '\\',
            intents = intents
        )

    async def setup_hook(self):
        await self.load_extension('cogs.error_handler')
        await self.load_extension('cogs.basic_commands.general')
        # await self.load_extension("cogs.youtube_player.youtube_player_V3") (old feature)
        await self.load_extension('cogs.youtube_player.youtube_player_V3R')
        await bot.tree.sync(guild = None)

    async def on_ready(self):
        print(f'{self.user} is online.')
        print(f'delay time: {str(round(self.latency*1000, 2))}ms.') # print('logging in as {0.user}'.format(bot))
        game = discord.Game('喵!') # status
        await self.change_presence(status = discord.Status.online, activity = game) # change status to game

bot = ShinkuBot()
bot.run(os.getenv("TOKEN"))