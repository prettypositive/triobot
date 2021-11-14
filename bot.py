import logging
import os
import sys
from dotenv import load_dotenv

import discord

console_log = logging.StreamHandler(sys.stdout)
console_log.setLevel(logging.INFO)
console_log.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)

file_log = logging.FileHandler("debug.log")
file_log.setLevel(logging.DEBUG)
file_log.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)

log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(console_log)
log.addHandler(file_log)


def main():
    load_dotenv()
    TOKEN = os.environ.get("BOT_TOKEN")
    assert isinstance(TOKEN, str)
    log.info("Token found. Initializing bot...")
    bot = discord.Client(TOKEN)
    bot.connect()


try:
    main()
except KeyboardInterrupt:
    log.info("Program halted due to keyboard interrupt.")
except Exception as e:
    log.exception("Program halted due to unhandled exception:")
