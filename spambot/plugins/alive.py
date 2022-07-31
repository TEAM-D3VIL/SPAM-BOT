from spambot import *
from spambot import D3vilBot1, D3vilBot2, D3vilBot3, D3vilBot4, D3vilBot5
from telethon import events
from telethon import version


master = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"


alive_msg = f"""
D3vil Spam Bot Is Alive!

My Master:- {master}

Bot Version:- `{BOT_VERSION}`

Telethon Version:- `{version.__version__}`

{BIO_MSG}
"""

@D3vilBot1.on(events.NewMessage(incoming=True, pattern='/alive'))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern='/alive'))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern='/alive'))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern='/alive'))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern='/alive'))
async def alive(e):
    if e.sender_id in MY_USERS:
        try:
            await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=alive_msg)
        except Exception as e:
            print(e)
