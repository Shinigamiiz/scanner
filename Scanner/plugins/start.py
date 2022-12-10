import logging
import os
import sys, platform
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon import __version__ as tel
from str import startxt2, startxt
#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = getenv("OWNER_ID", None)
OP  = [int(g), int(gg), int(OWNER_ID)]
#TelegramClient..
sree = TelegramClient(
    "Gban",
    api_id=API_ID,
    api_hash=API_HASH
).start(bot_token=BOT_TOKEN)

Owner = "iveL83"
repo = "https://github.com"
@sree.on(events.NewMessage(pattern="^/start"))
async def start(event):
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/NezukoKamado"), Button.url("••ʀєρο••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://te.legra.ph/file/854e06992089ccb64557e.jpg",
            caption=startxt.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await sree.send_file(
            event.chat.id,
            file="https://te.legra.ph/file/854e06992089ccb64557e.jpg",
            caption=startxt2.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
