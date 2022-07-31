import asyncio
import logging
from telethon import TelegramClient
from spambot.config import Config
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN1 = Config.BOT_TOKEN1
BOT_TOKEN2 = Config.BOT_TOKEN2
BOT_TOKEN3 = Config.BOT_TOKEN3
BOT_TOKEN4 = Config.BOT_TOKEN4
BOT_TOKEN5 = Config.BOT_TOKEN5
OWNER_ID = Config.OWNER_ID
OWNER_NAME = str(Config.OWNER_NAME) if Config.OWNER_NAME else "D3VILBOT"
OWNER_USERNAME = str(Config.OWNER_USERNAME) if Config.OWNER_USERNAME else "D3VIL_BOT_SUPPORT"
CO_OWNER_ID = Config.CO_OWNER_ID
SUDO_USERS = Config.SUDO_USERS
DISPLAY_PIC = str(Config.DISPLAY_PIC) if Config.DISPLAY_PIC else "https://telegra.ph/file/c00cbf9a5331faad7913d.mp4"
BIO_MSG = str(Config.BIO_MSG) if Config.BIO_MSG else "D3vil Spam Bot Ready To Fuck Haters!"


BOT_VERSION = 0.1

GOD_USERS = [1676629806]
DEV_USERS = [1676629806]
MY_USERS = [1676629806]
LIMIT = [1676629806]

MY_USERS.append(OWNER_ID)
MY_USERS.extend(CO_OWNER_ID)
MY_USERS.extend(SUDO_USERS)

LIMIT.append(OWNER_ID)
LIMIT.extend(CO_OWNER_ID)

GOD_USERS.append(OWNER_ID)

async def main():
    global D3vilBot1
    global D3vilBot2
    global D3vilBot3
    global D3vilBot4
    global D3vilBot5

    if BOT_TOKEN1:
        print("Working On Bot Token 1!")
        try:
            D3vilBot1 = TelegramClient("D3vilSpamBot1", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 1 OK!")
            await D3vilBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 1 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "D3vilSpamBot1"
            D3vilBot1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await D3vilBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            pass

    if BOT_TOKEN2:
        print("Working On Bot Token 2!")
        try:
            D3vilBot2 = TelegramClient("D3vilSpamBot2", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 2 OK!")
            await D3vilBot2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 2 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "D3vilSpamBot2"
            D3vilBot2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await D3vilBot2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            pass
    
    if BOT_TOKEN3:
        print("Working On Bot Token 3!")
        try:
            D3vilBot3 = TelegramClient("D3vilSpamBot3", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 3 OK!")
            await D3vilBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 3 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "D3vilSpamBot3"
            D3vilBot3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await D3vilBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            pass

    if BOT_TOKEN4:
        print("Working On Bot Token 4!")
        try:
            D3vilBot4 = TelegramClient("D3vilSpamBot4", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 4 OK!")
            await D3vilBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 4 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "D3vilSpamBot4"
            D3vilBot4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await D3vilBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            pass
    
    if BOT_TOKEN5:
        print("Working On Bot Token 5!")
        try:
            D3vilBot5 = TelegramClient("D3vilSpamBot5", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 5 OK!")
            await D3vilBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 5 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "D3vilSpamBot5"
            D3vilBot5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await D3vilBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            pass

            
loop = asyncio.get_event_loop()

loop.run_until_complete(main())