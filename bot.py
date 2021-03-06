import logging
import logging.handlers
import os
import trio

from dotenv import load_dotenv

load_dotenv()

import discord

log_format = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
console_log = logging.StreamHandler()
console_log.setLevel(logging.INFO)
console_log.setFormatter(log_format)
file_log = logging.handlers.RotatingFileHandler(
    "debug.log", maxBytes=10000000, backupCount=5, encoding="utf8"
)
file_log.setLevel(logging.DEBUG)
file_log.setFormatter(log_format)
log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(console_log)
log.addHandler(file_log)

TOKEN = os.environ.get("BOT_TOKEN")
assert isinstance(TOKEN, str)
log.info("Token found. Initializing bot...")
bot = discord.Client(TOKEN)


@bot.slash_command
async def echo(interaction: discord.SlashCommand):
    message = interaction.data["options"][0]["value"]
    await bot.interaction_response(interaction, message)


@bot.slash_command
async def slap(interaction: discord.SlashCommand):
    slapper = str(interaction.member)
    target = str(
        interaction.guild.members[list(interaction.data["resolved"]["users"])[0]]
    )
    message = f"*{slapper} slaps {target} around a bit with a large trout*"
    await bot.interaction_response(interaction, message)


@bot.task
async def test_task():
    while True:
        await bot.send_message("723649270296739882", "hello!")
        await trio.sleep(10)


@bot.task
async def test_task2():
    while True:
        await bot.send_message("723649270296739882", "hi!")
        await trio.sleep(5)


try:
    bot.connect()
except KeyboardInterrupt:
    log.info("Program halted due to keyboard interrupt.")
except Exception as e:
    log.exception("Program halted due to unhandled exception:")
