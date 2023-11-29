import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import hupper

from utils import construct_reply

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    reply = await construct_reply(message=message)
    await message.reply(reply)

def run_bot():
    asyncio.run(bot.start(BOT_TOKEN))

if __name__ == "__main__":
    if os.getenv('ENVIRONMENT') == "local":
        hupper.start_reloader("bot.run_bot")
    else:
        run_bot()