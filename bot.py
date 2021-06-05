import logging
import json

from pyrogram import Client
from config import *
from data import whispers

plugins = dict(
    root="plugins",
    include=[
        "inline",
        "private"
    ]
)

logging.basicConfig(level=logging.INFO)

app = Client("whisperbot", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)

app.run()
with open('data.json', 'w') as f:
    json.dump(whispers, f)
