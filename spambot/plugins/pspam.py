import random
from spambot import *
from spambot import D3vilBot1, D3vilBot2, D3vilBot3, D3vilBot4, D3vilBot5
from spambot.helpers.plinks import PLINKS
from telethon import events

a = False

@D3vilBot1.on(events.NewMessage(incoming=True, pattern='/pspam'))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern='/pspam'))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern='/pspam'))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern='/pspam'))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern='/pspam'))
async def pspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        elif e.raw_text[6:] == "":
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        
@D3vilBot1.on(events.NewMessage(incoming=True, pattern="/pstop"))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern="/pstop"))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern="/pstop"))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern="/pstop"))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern="/pstop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.client.send_message(e.chat_id, "Porn Spam Stopped Successfully")