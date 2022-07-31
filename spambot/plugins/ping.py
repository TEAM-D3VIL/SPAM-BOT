from spambot import *
from spambot import D3vilBot1, D3vilBot2, D3vilBot3, D3vilBot4, D3vilBot5
from telethon import events
from datetime import datetime

@D3vilBot1.on(events.NewMessage(incoming=True, pattern='/ping'))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern='/ping'))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern='/ping'))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern='/ping'))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f"Ping Pong!\n\nD3vil Spam Bot\n\nMy Master:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\nPing:- {ms} ms\n\nD3vil Spam Bot On Fire")
