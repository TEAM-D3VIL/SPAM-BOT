from spambot import *
from spambot import D3vilBot1, D3vilBot2, D3vilBot3, D3vilBot4, D3vilBot5
from telethon import events

a = False

@D3vilBot1.on(events.NewMessage(incoming=True, pattern='/spam'))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern='/spam'))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern='/spam'))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern='/spam'))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern='/spam'))
async def spam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[6:8])
            spam = text[8:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                    await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@D3vilBot1.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern='/bigspam'))
async def bigspam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[9:15])
            spam = text[15:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                            await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@D3vilBot1.on(events.NewMessage(incoming=True, pattern='/mspam'))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern='/mspam'))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern='/mspam'))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern='/mspam'))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern='/mspam'))
async def mspam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[7:13])
            if e.is_reply == False:
                await e.client.send_message(e.chat_id, "Please reply to a media and enter how many times you want send that media!")
            elif e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.media
                for i in range(counts):
                    await e.client.send_file(e.chat_id, replied_message)
            else:
                await e.client.send_message(e.chat_id, "Some thing went wrong! Please reply to a media and enter how many times you want send that media!")
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Please enter how many times you want to spam in reply of media!")

@D3vilBot1.on(events.NewMessage(incoming=True, pattern="/uspam"))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern="/uspam"))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern="/uspam"))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern="/uspam"))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        
@D3vilBot1.on(events.NewMessage(incoming=True, pattern="/ustop"))
@D3vilBot2.on(events.NewMessage(incoming=True, pattern="/ustop"))
@D3vilBot3.on(events.NewMessage(incoming=True, pattern="/ustop"))
@D3vilBot4.on(events.NewMessage(incoming=True, pattern="/ustop"))
@D3vilBot5.on(events.NewMessage(incoming=True, pattern="/ustop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.client.send_message(e.chat_id, "U Spam Stopped Successfully")
