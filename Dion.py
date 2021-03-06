import logging
from telethon import events, TelegramClient


logging.basicConfig(level=logging.INFO)


API_ID = "API_ID" #fill with your API ID, get from my.telegram.org
API_HASH = "API_HASH" #fill with your API HASH, get from my.telegram.org
BOT_TOKEN = "BOT_TOKEN" #fill with your Bot Token, get from t.me/botfather


Dion = TelegramClient("Dion", API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@Dion.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("Hello friends!")


print("Success Started Bot")
Dion.run_until_disconnected()
