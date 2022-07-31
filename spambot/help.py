from spambot import *
from spambot import D3vilBot1, D3vilBot2, D3vilBot3, D3vilBot4, D3vilBot5
from spambot.helpers.commands import *
from telethon import events, Button


Buttons = [
    Button.inline("Alive", b'alive'),
    Button.inline("Ping", b'ping')
], [
    Button.inline("Raid", b'raid'),
    Button.inline("Reply Raid", b'replyraid')
], [
    Button.inline("Spam", b'spam'),
    Button.inline("Pspam", b'pspam')
], [
    Button.inline("Extras", b'extras')
], [
    Button.url("Channel", "t.me/D3VIL_BOT_SUPPORT"),
    Button.url("Group", "D3VIL_BOT_OFFICIAL")
]

BACK = [
    Button.inline("Back", b'back')
]

@D3vilBot1.on(events.NewMessage(incoming=True, pattern='/help'))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern='/help'))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern='/help'))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern='/help'))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="This Is Help Command!!!", buttons=Buttons)

        

