import os
import discord
from discord.ext import commands

import src.message as msg


# env setting
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# bot setting
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)


# discord commands
@bot.command()
async def ping(ctx):
    await msg.get_pong(ctx)


@bot.command()
async def GPT(ctx, *, query: str):
    await msg.get_gpt_answer(ctx, query)


@bot.event
async def on_message(message):
    # Except bot answer
    if message.author == bot.user:
        return

    # Except not command
    if not message.content.startswith("!"):
        return

    # Command
    if message.content.startswith("!GPT"):
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)
    elif message.content.startswith("!ping"):
        await bot.process_commands(message)
    else:
        await message.channel.send("Unknown command!!")


# discord setting
def run_bot():
    return bot.run(DISCORD_TOKEN)
