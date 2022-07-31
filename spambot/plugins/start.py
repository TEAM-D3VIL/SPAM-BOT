from spambot import *
from spambot import D3vilBot1, D3vilBot2, D3vilBot3, D3vilBot4, D3vilBot5
from telethon import events, Button


data  = [
    Button.url("Channel", url="t.me/D3VIL_BOT_OFFICIAL"),
    Button.url("Repo", url="https://GitHub.com/TEAM-D3VIL/"),
    Button.url("Group", url="t.me/D3VIL_BOT_SUPPORT")
]


@D3vilBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[D3VIL KRISH](tg://user?id={1676629806})"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
Hey {mention},

This Is D3vil Spam Bot!

Owner:- {myOwner}

Sudo:- {sudo_user}

Creator:- {creator}
    """
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)

