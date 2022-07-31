from spambot import *
from spambot import D3vilBot1, D3vilBot2, D3vilBot3, D3vilBot4, D3vilBot5
from spambot.help import *
from spambot.helpers.commands import *
from telethon import events


@D3vilBot1.on(events.CallbackQuery(data=b'alive'))
@D3vilBot2.on(events.CallbackQuery(data=b'alive'))
@D3vilBot3.on(events.CallbackQuery(data=b'alive'))
@D3vilBot4.on(events.CallbackQuery(data=b'alive'))
@D3vilBot5.on(events.CallbackQuery(data=b'alive'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)

@D3vilBot1.on(events.CallbackQuery(data=b'ping'))
@D3vilBot2.on(events.CallbackQuery(data=b'ping'))
@D3vilBot3.on(events.CallbackQuery(data=b'ping'))
@D3vilBot4.on(events.CallbackQuery(data=b'ping'))
@D3vilBot5.on(events.CallbackQuery(data=b'ping'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)

@D3vilBot1.on(events.CallbackQuery(data=b'raid'))
@D3vilBot2.on(events.CallbackQuery(data=b'raid'))
@D3vilBot3.on(events.CallbackQuery(data=b'raid'))
@D3vilBot4.on(events.CallbackQuery(data=b'raid'))
@D3vilBot5.on(events.CallbackQuery(data=b'raid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK)

@D3vilBot1.on(events.CallbackQuery(data=b'replyraid'))
@D3vilBot2.on(events.CallbackQuery(data=b'replyraid'))
@D3vilBot3.on(events.CallbackQuery(data=b'replyraid'))
@D3vilBot4.on(events.CallbackQuery(data=b'replyraid'))
@D3vilBot5.on(events.CallbackQuery(data=b'replyraid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)

@D3vilBot1.on(events.CallbackQuery(data=b'spam'))
@D3vilBot2.on(events.CallbackQuery(data=b'spam'))
@D3vilBot3.on(events.CallbackQuery(data=b'spam'))
@D3vilBot4.on(events.CallbackQuery(data=b'spam'))
@D3vilBot5.on(events.CallbackQuery(data=b'spam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)

@D3vilBot1.on(events.CallbackQuery(data=b'pspam'))
@D3vilBot2.on(events.CallbackQuery(data=b'pspam'))
@D3vilBot3.on(events.CallbackQuery(data=b'pspam'))
@D3vilBot4.on(events.CallbackQuery(data=b'pspam'))
@D3vilBot5.on(events.CallbackQuery(data=b'pspam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)

@D3vilBot1.on(events.CallbackQuery(data=b'extras'))
@D3vilBot2.on(events.CallbackQuery(data=b'extras'))
@D3vilBot3.on(events.CallbackQuery(data=b'extras'))
@D3vilBot4.on(events.CallbackQuery(data=b'extras'))
@D3vilBot5.on(events.CallbackQuery(data=b'extras'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)

@D3vilBot1.on(events.CallbackQuery(data=b'back'))
@D3vilBot2.on(events.CallbackQuery(data=b'back'))
@D3vilBot3.on(events.CallbackQuery(data=b'back'))
@D3vilBot4.on(events.CallbackQuery(data=b'back'))
@D3vilBot5.on(events.CallbackQuery(data=b'back'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit("This Is Help Command!!!", buttons=Buttons)
 