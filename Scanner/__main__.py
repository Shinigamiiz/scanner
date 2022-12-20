import asyncio
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport
import os
import requests

from pyrogram import Client
from pyrogram.enums import ParseMode

from Scanner import LOGGER, pbot, ubot, tbot
from Scanner.db.global_bans_db import num_gbanned_users
from Scanner.vars import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL_ID

DOWNLOAD_DIRECTORY = "/tmp"

def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper
 
_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
"""fix yelling at me error end"""

async def load_start():
    count = num_gbanned_users()
    LOGGER.info(f"Current Gbanned Users: {count}")
    LOGGER.info("[INFO]: STARTED")
    LOGGER.info(f"LOG CHANNELS: {int(LOG_CHANNEL_ID)}")
    try:
        await pbot.send_message(
            int(LOG_CHANNEL_ID), f"**Pyrogram Client Started Successfully !!**\nCurrent Gbanned Users: `{count}`"
        )
        LOGGER.info("[INFO]: PYROGRAM BOT STARTED")
    except Exception as e:
        LOGGER.info(f"Bot wasn't able to semd message in your log channel.\n\nERROR: {e}")
    try:
        await ubot.send_message(
            int(LOG_CHANNEL_ID), "**Assistant Started Successfully !!**"
        )
        LOGGER.info("[INFO]: PYROGRAM UserBOT STARTED")
    except Exception as e:
        LOGGER.info(f"UserBot wasn't able to semd message in your log channel.\n\nERROR: {e}")
    

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)

Client(
    name="SOME-1HING",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=min(32, os.cpu_count() + 4),
    parse_mode=ParseMode.DEFAULT,
    workdir=DOWNLOAD_DIRECTORY,
    sleep_threshold=60,
    in_memory=True,
    plugins={"root": "Scanner.plugins"},
).start()

loop.close()
