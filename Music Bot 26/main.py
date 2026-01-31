# Jammer26 main
# @author(s) 
# - Karam Mannsi
# - Larry Liu
# - Brian Chong
# - Varin Padroo
# @since dd/mm/26
# Enables Jammer to take commands, message, and play music within the server

import discord
from discord.ext import commands
import logging 
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to go!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "hello" in message.content.lower():
        await message.channel.send(f"Hey, my name is {bot.user.name}, nice to meeet you!")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

# Run the bot!
bot.run(token, log_handler=handler, log_level= logging.DEBUG)