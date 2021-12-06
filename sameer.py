import asyncio
import os
from os import execl
import sys
import heroku3
import requests
import time
from datetime import datetime
from telethon import TelegramClient
from telethon import events, Button
from telethon import utils
import random
from telethon.tl import functions
from telethon.sessions import StringSession
from telethon.tl.custom import button
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from dossier import API_ID, ALIVE_MEDIA, API_HASH, HEROKU_APP_NAME, HEROKU_API_KEY, SUDO_USERS, DEV_USERS, crew, StartTime, String_Session01, String_Session02, String_Session03, String_Session04, String_Session05, String_Session06, String_Session07, String_Session08, String_Session09, String_Session10, String_Session11, String_Session12, String_Session13, String_Session14, String_Session15, String_Session16, String_Session17, String_Session18, String_Session19, String_Session20, String_Session21, String_Session22, String_Session23, String_Session24, String_Session25, String_Session26, String_Session27, String_Session28, String_Session29, String_Session30, String_Session31, String_Session32, String_Session33, String_Session34, String_Session35, String_Session36, String_Session37, String_Session38, String_Session39, String_Session40, String_Session41, String_Session42, String_Session43, String_Session44, String_Session45, String_Session46, String_Session47, String_Session48, String_Session49, String_Session50, String_Session51, String_Session52, String_Session53, String_Session54, String_Session55, String_Session56, String_Session57, String_Session58, String_Session59, String_Session60, String_Session61, String_Session62, String_Session63, String_Session64, String_Session65, String_Session66, String_Session67, String_Session68, String_Session69, String_Session70
from dossier import HNDLR as hn
from worker.verses import replies, curses
from helpmenu import spam_menu, curse_menu, sudo_menu, dev_menu, acc_menu, help_menu, alive_temxt, deadly_logo, start_caption, start_caption1, devusage, sudousage, spamusage, accusage

deadly_logo = "https://telegra.ph/file/ec3c057fcba5594151601.jpg"

buttons = [
    [
        (Button.url("Cʜᴀɴɴᴇʟ", url="https://t.me/Deadly_spammer")),
        (Button.url("Sᴜᴘᴘᴏʀᴛ", url="t.me/DEADLY_SPAM_BOT"))
    ],
    [
        (Button.url("Rᴇᴘᴏ", url="https://github.com/DEADLY-FIGHTERS/DEADLY-SPAM-BOT")),
        (Button.url("Tᴜᴛᴏʀɪᴀʟ", url="Hah"))
    ]
]

Bot1 = ''
Bot2 = ''
Bot3 = ''
Bot4 = ''
Bot5 = ''
Bot6 = ''
Bot7 = ''
Bot8 = ''
Bot9 = ''
Bot10 = ''
Bot11 = ''
Bot12 = ''
Bot13 = ''
Bot14 = ''
Bot15 = ''
Bot16 = ''
Bot17 = ''
Bot18 = ''
Bot19 = ''
Bot20 = ''
Bot21 = ''
Bot22 = ''
Bot23 = ''
Bot24 = ''
Bot25 = ''
Bot26 = ''
Bot27 = ''
Bot28 = ''
Bot29 = ''
Bot30 = ''
Bot31 = ''
Bot32 = ''
Bot33 = ''
Bot34 = ''
Bot35 = ''
Bot36 = ''
Bot37 = ''
Bot38 = ''
Bot39 = ''
Bot40 = ''
Bot41 = ''
Bot42 = ''
Bot43 = ''
Bot44 = ''
Bot45 = ''
Bot46 = ''
Bot47 = ''
Bot48 = ''
Bot49 = ''
Bot50 = ''
Bot51 = ''
Bot52 = ''
Bot53 = ''
Bot54 = ''
Bot55 = ''
Bot56 = ''
Bot57 = ''
Bot58 = ''
Bot59 = ''
Bot60 = ''
Bot61 = ''
Bot62 = ''
Bot63 = ''
Bot64 = ''
Bot65 = ''
Bot66 = ''
Bot67 = ''
Bot68 = ''
Bot69 = ''
Bot70 = ''



async def DeadlyBot_bots():
    global Bot1
    global Bot2
    global Bot3
    global Bot4
    global Bot5
    global Bot6
    global Bot7
    global Bot8
    global Bot9
    global Bot10
    global Bot11
    global Bot12
    global Bot13
    global Bot14
    global Bot15
    global Bot16
    global Bot17
    global Bot18
    global Bot19
    global Bot20
    global Bot21
    global Bot22
    global Bot23
    global Bot24
    global Bot25
    global Bot26
    global Bot27
    global Bot28
    global Bot29
    global Bot30
    global Bot31
    global Bot32
    global Bot33
    global Bot34
    global Bot35
    global Bot36
    global Bot37
    global Bot38
    global Bot39
    global Bot40
    global Bot41
    global Bot42
    global Bot43
    global Bot44
    global Bot45
    global Bot46
    global Bot47
    global Bot48
    global Bot49
    global Bot50
    global Bot51
    global Bot52
    global Bot53
    global Bot54
    global Bot55
    global Bot56
    global Bot57
    global Bot58
    global Bot59
    global Bot60
    global Bot61
    global Bot62
    global Bot63
    global Bot64
    global Bot65
    global Bot66
    global Bot67
    global Bot68
    global Bot69
    global Bot70
    if String_Session01:
        Bot1 = TelegramClient(StringSession(String_Session01), API_ID, API_HASH)
        try:
            print("Got String Session 01!")
            await Bot1.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot1(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot1(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
            await Bot1(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
        except:
            try:
                print("Got String Session 01!")
                await Bot1.start()
                checkig = await Bot1.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 01!")
        sessn = "DeadlyBot"
        Bot1 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot1.start()
        except:
            pass

    if String_Session02:
        Bot2 = TelegramClient(StringSession(String_Session02), API_ID, API_HASH)
        try:
            print("Got String Session 02!")
            await Bot2.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot2(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot2(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot2(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 02!")
                await Bot2.start()
                checkig = await Bot2.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 02!")
        sessn = "DeadlyBot"
        Bot2 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot2.start()
        except:
            pass
    
    if String_Session03:
        Bot3 = TelegramClient(StringSession(String_Session03), API_ID, API_HASH)
        try:
            print("Got String Session 03!")
            await Bot3.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot3(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot3(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot3(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 03!")
                await Bot3.start()
                checkig = await Bot3.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 03!")
        sessn = "DeadlyBot"
        Bot3 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot3.start()
        except:
            pass
    
    if String_Session04:
        Bot4 = TelegramClient(StringSession(String_Session04), API_ID, API_HASH)
        try:
            print("Got String Session 04!")
            await Bot4.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot4(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot4(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot4(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 04!")
                await Bot4.start()
                checkig = await Bot4.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 04!")
        sessn = "DeadlyBot"
        Bot4 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot4.start()
        except:
            pass

    if String_Session05:
        Bot5 = TelegramClient(StringSession(String_Session05), API_ID, API_HASH)
        try:
            print("Got String Session 05!")
            await Bot5.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot5(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot5(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot5(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 05!")
                await Bot5.start()
                checkig = await Bot5.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 05!")
        sessn = "DeadlyBot"
        Bot5 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot5.start()
        except:
            pass

    if String_Session06:
        Bot6 = TelegramClient(StringSession(String_Session06), API_ID, API_HASH)
        try:
            print("Got String Session 06!")
            await Bot6.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot6(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot6(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot6(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 06!")
                await Bot6.start()
                checkig = await Bot6.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 06!")
        sessn = "DeadlyBot"
        Bot6 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot6.start()
        except:
            pass

    if String_Session07:
        Bot7 = TelegramClient(StringSession(String_Session07), API_ID, API_HASH)
        try:
            print("Got String Session 07!")
            await Bot7.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot7(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot7(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot7(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 07!")
                await Bot7.start()
                checkig = await Bot7.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 07!")
        sessn = "DeadlyBot"
        Bot7 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot7.start()
        except:
            pass

    if String_Session08:
        Bot8 = TelegramClient(StringSession(String_Session08), API_ID, API_HASH)
        try:
            print("Got String Session 08!")
            await Bot8.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot8(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot8(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot8(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 08!")
                await Bot8.start()
                checkig = await Bot8.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 08!")
        sessn = "DeadlyBot"
        Bot8 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot8.start()
        except:
            pass

    if String_Session09:
        Bot9 = TelegramClient(StringSession(String_Session09), API_ID, API_HASH)
        try:
            print("Got String Session 09!")
            await Bot9.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot9(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot9(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot9(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 09!")
                await Bot9.start()
                checkig = await Bot9.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 09!")
        sessn = "DeadlyBot"
        Bot9 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot9.start()
        except:
            pass

    if String_Session10:
        Bot10 = TelegramClient(StringSession(String_Session10), API_ID, API_HASH)
        try:
            print("Got String Session 10!")
            await Bot10.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot10(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot10(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot10(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 10!")
                await Bot10.start()
                checkig = await Bot10.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 10!")
        sessn = "DeadlyBot"
        Bot10 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot10.start()
        except:
            pass

    if String_Session11:
        Bot11 = TelegramClient(StringSession(String_Session11), API_ID, API_HASH)
        try:
            print("Got String Session 11!")
            await Bot11.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot11(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot11(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot11(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 11!")
                await Bot11.start()
                checkig = await Bot11.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 11!")
        sessn = "DeadlyBot"
        Bot11 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot11.start()
        except:
            pass

    if String_Session12:
        Bot12 = TelegramClient(StringSession(String_Session12), API_ID, API_HASH)
        try:
            print("Got String Session 12!")
            await Bot12.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot12(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot12(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot12(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 12!")
                await Bot12.start()
                checkig = await Bot12.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 12!")
        sessn = "DeadlyBot"
        Bot12 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot12.start()
        except:
            pass

    if String_Session13:
        Bot13 = TelegramClient(StringSession(String_Session13), API_ID, API_HASH)
        try:
            print("Got String Session 13!")
            await Bot13.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot13(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot13(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot13(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 13!")
                await Bot13.start()
                checkig = await Bot13.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 13!")
        sessn = "DeadlyBot"
        Bot13 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot13.start()
        except:
            pass

    if String_Session14:
        Bot14 = TelegramClient(StringSession(String_Session14), API_ID, API_HASH)
        try:
            print("Got String Session 14!")
            await Bot14.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot14(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot14(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot14(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 14!")
                await Bot14.start()
                checkig = await Bot14.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 14!")
        sessn = "DeadlyBot"
        Bot14 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot14.start()
        except:
            pass

    if String_Session15:
        Bot15 = TelegramClient(StringSession(String_Session15), API_ID, API_HASH)
        try:
            print("Got String Session 15!")
            await Bot15.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot15(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot15(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot15(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 15!")
                await Bot15.start()
                checkig = await Bot15.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 15!")
        sessn = "DeadlyBot"
        Bot15 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot15.start()
        except:
            pass

    if String_Session16:
        Bot16 = TelegramClient(StringSession(String_Session16), API_ID, API_HASH)
        try:
            print("Got String Session 16!")
            await Bot16.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot16(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot16(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot16(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 16!")
                await Bot16.start()
                checkig = await Bot16.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 16!")
        sessn = "DeadlyBot"
        Bot16 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot16.start()
        except:
            pass

    if String_Session17:
        Bot17 = TelegramClient(StringSession(String_Session17), API_ID, API_HASH)
        try:
            print("Got String Session 17!")
            await Bot17.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot17(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot17(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot17(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 17!")
                await Bot17.start()
                checkig = await Bot17.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 17!")
        sessn = "DeadlyBot"
        Bot17 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot17.start()
        except:
            pass

    if String_Session18:
        Bot18 = TelegramClient(StringSession(String_Session18), API_ID, API_HASH)
        try:
            print("Got String Session 18!")
            await Bot18.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot18(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot18(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot18(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 18!")
                await Bot18.start()
                checkig = await Bot18.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 18!")
        sessn = "DeadlyBot"
        Bot18 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot18.start()
        except:
            pass

    if String_Session19:
        Bot19 = TelegramClient(StringSession(String_Session19), API_ID, API_HASH)
        try:
            print("Got String Session 19!")
            await Bot19.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot19(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot19(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot19(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 19!")
                await Bot19.start()
                checkig = await Bot19.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 19!")
        sessn = "DeadlyBot"
        Bot19 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot19.start()
        except:
            pass

    if String_Session20:
        Bot20 = TelegramClient(StringSession(String_Session20), API_ID, API_HASH)
        try:
            print("Got String Session 20!")
            await Bot20.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot20(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot20(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot20(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 20!")
                await Bot20.start()
                checkig = await Bot20.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 20!")
        sessn = "DeadlyBot"
        Bot20 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot20.start()
        except:
            pass

    if String_Session21:
        Bot21 = TelegramClient(StringSession(String_Session21), API_ID, API_HASH)
        try:
            print("Got String Session 21!")
            await Bot21.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot21(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot21(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot21(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 21!")
                await Bot21.start()
                checkig = await Bot21.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 21!")
        sessn = "DeadlyBot"
        Bot21 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot21.start()
        except:
            pass

    if String_Session22:
        Bot22 = TelegramClient(StringSession(String_Session22), API_ID, API_HASH)
        try:
            print("Got String Session 22!")
            await Bot22.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot22(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot22(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot22(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 22!")
                await Bot22.start()
                checkig = await Bot22.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 22!")
        sessn = "DeadlyBot"
        Bot22 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot22.start()
        except:
            pass

    if String_Session23:
        Bot23 = TelegramClient(StringSession(String_Session23), API_ID, API_HASH)
        try:
            print("Got String Session 23!")
            await Bot23.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot23(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot23(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot23(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 23!")
                await Bot23.start()
                checkig = await Bot23.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 23!")
        sessn = "DeadlyBot"
        Bot23 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot23.start()
        except:
            pass

    if String_Session24:
        Bot24 = TelegramClient(StringSession(String_Session24), API_ID, API_HASH)
        try:
            print("Got String Session 24!")
            await Bot24.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot24(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot24(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot24(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 24!")
                await Bot24.start()
                checkig = await Bot24.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 24!")
        sessn = "DeadlyBot"
        Bot24 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot24.start()
        except:
            pass

    if String_Session25:
        Bot25 = TelegramClient(StringSession(String_Session25), API_ID, API_HASH)
        try:
            print("Got String Session 25!")
            await Bot25.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot25(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot25(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot25(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 25!")
                await Bot25.start()
                checkig = await Bot25.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 25!")
        sessn = "DeadlyBot"
        Bot25 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot25.start()
        except:
            pass

    if String_Session26:
        Bot26 = TelegramClient(StringSession(String_Session26), API_ID, API_HASH)
        try:
            print("Got String Session 26!")
            await Bot26.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot26(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot26(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot26(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 26!")
                await Bot26.start()
                checkig = await Bot26.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 26!")
        sessn = "DeadlyBot"
        Bot26 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot26.start()
        except:
            pass

    if String_Session27:
        Bot27 = TelegramClient(StringSession(String_Session27), API_ID, API_HASH)
        try:
            print("Got String Session 27!")
            await Bot27.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot27(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot27(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot27(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 27!")
                await Bot27.start()
                checkig = await Bot27.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 27!")
        sessn = "DeadlyBot"
        Bot27 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot27.start()
        except:
            pass

    if String_Session28:
        Bot28 = TelegramClient(StringSession(String_Session28), API_ID, API_HASH)
        try:
            print("Got String Session 28!")
            await Bot28.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot28(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot28(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot28(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 28!")
                await Bot28.start()
                checkig = await Bot28.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 28!")
        sessn = "DeadlyBot"
        Bot28 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot28.start()
        except:
            pass

    if String_Session29:
        Bot29 = TelegramClient(StringSession(String_Session29), API_ID, API_HASH)
        try:
            print("Got String Session 29!")
            await Bot29.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot29(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot29(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot29(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 29!")
                await Bot29.start()
                checkig = await Bot29.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 29!")
        sessn = "DeadlyBot"
        Bot29 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot29.start()
        except:
            pass

    if String_Session30:
        Bot30 = TelegramClient(StringSession(String_Session30), API_ID, API_HASH)
        try:
            print("Got String Session 30!")
            await Bot30.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot30(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot30(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot30(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 30!")
                await Bot30.start()
                checkig = await Bot30.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 30!")
        sessn = "DeadlyBot"
        Bot30 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot30.start()
        except:
            pass

    if String_Session31:
        Bot31 = TelegramClient(StringSession(String_Session31), API_ID, API_HASH)
        try:
            print("Got String Session 31!")
            await Bot31.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot31(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot31(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot31(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 31!")
                await Bot31.start()
                checkig = await Bot31.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 31!")
        sessn = "DeadlyBot"
        Bot31 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot31.start()
        except:
            pass

    if String_Session32:
        Bot32 = TelegramClient(StringSession(String_Session32), API_ID, API_HASH)
        try:
            print("Got String Session 32!")
            await Bot32.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot32(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot32(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot32(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 32!")
                await Bot32.start()
                checkig = await Bot32.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 32!")
        sessn = "DeadlyBot"
        Bot32 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot32.start()
        except:
            pass

    if String_Session33:
        Bot33 = TelegramClient(StringSession(String_Session33), API_ID, API_HASH)
        try:
            print("Got String Session 33!")
            await Bot33.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot33(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot33(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot33(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 33!")
                await Bot33.start()
                checkig = await Bot33.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 33!")
        sessn = "DeadlyBot"
        Bot33 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot33.start()
        except:
            pass

    if String_Session34:
        Bot34 = TelegramClient(StringSession(String_Session34), API_ID, API_HASH)
        try:
            print("Got String Session 34!")
            await Bot34.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot34(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot34(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot34(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 34!")
                await Bot34.start()
                checkig = await Bot34.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 34!")
        sessn = "DeadlyBot"
        Bot34 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot34.start()
        except:
            pass

    if String_Session35:
        Bot35 = TelegramClient(StringSession(String_Session35), API_ID, API_HASH)
        try:
            print("Got String Session 35!")
            await Bot35.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot35(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot35(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot35(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 35!")
                await Bot35.start()
                checkig = await Bot35.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 35!")
        sessn = "DeadlyBot"
        Bot35 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot35.start()
        except:
            pass

    if String_Session36:
        Bot36 = TelegramClient(StringSession(String_Session36), API_ID, API_HASH)
        try:
            print("Got String Session 36!")
            await Bot36.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot36(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot36(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot36(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 36!")
                await Bot36.start()
                checkig = await Bot36.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 36!")
        sessn = "DeadlyBot"
        Bot36 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot36.start()
        except:
            pass

    if String_Session37:
        Bot37 = TelegramClient(StringSession(String_Session37), API_ID, API_HASH)
        try:
            print("Got String Session 37!")
            await Bot37.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot37(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot37(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot37(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 37!")
                await Bot37.start()
                checkig = await Bot37.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 37!")
        sessn = "DeadlyBot"
        Bot37 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot37.start()
        except:
            pass

    if String_Session38:
        Bot38 = TelegramClient(StringSession(String_Session38), API_ID, API_HASH)
        try:
            print("Got String Session 38!")
            await Bot38.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot38(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot38(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot38(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 38!")
                await Bot38.start()
                checkig = await Bot38.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 38!")
        sessn = "DeadlyBot"
        Bot38 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot38.start()
        except:
            pass

    if String_Session39:
        Bot39 = TelegramClient(StringSession(String_Session39), API_ID, API_HASH)
        try:
            print("Got String Session 39!")
            await Bot39.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot39(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot39(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot39(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 39!")
                await Bot39.start()
                checkig = await Bot39.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 39!")
        sessn = "DeadlyBot"
        Bot39 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot39.start()
        except:
            pass

    if String_Session40:
        Bot40 = TelegramClient(StringSession(String_Session40), API_ID, API_HASH)
        try:
            print("Got String Session 40!")
            await Bot40.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot40(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot40(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot40(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 40!")
                await Bot40.start()
                checkig = await Bot40.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 40!")
        sessn = "DeadlyBot"
        Bot40 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot40.start()
        except:
            pass
    if String_Session41:
        Bot41 = TelegramClient(StringSession(String_Session41), API_ID, API_HASH)
        try:
            print("Got String Session 41!")
            await Bot41.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot41(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot41(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot41(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 41!")
                await Bot41.start()
                checkig = await Bot41.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 41!")
        sessn = "DeadlyBot"
        Bot41 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot41.start()
        except:
            pass

    if String_Session42:
        Bot42 = TelegramClient(StringSession(String_Session42), API_ID, API_HASH)
        try:
            print("Got String Session 42!")
            await Bot42.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot42(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot42(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot42(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 42!")
                await Bot42.start()
                checkig = await Bot42.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 42!")
        sessn = "DeadlyBot"
        Bot42 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot42.start()
        except:
            pass
    
    if String_Session43:
        Bot43 = TelegramClient(StringSession(String_Session43), API_ID, API_HASH)
        try:
            print("Got String Session 43!")
            await Bot43.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot43(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot43(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot43(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 43!")
                await Bot43.start()
                checkig = await Bot43.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 43!")
        sessn = "DeadlyBot"
        Bot43 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot43.start()
        except:
            pass
    
    if String_Session44:
        Bot44 = TelegramClient(StringSession(String_Session44), API_ID, API_HASH)
        try:
            print("Got String Session 44!")
            await Bot44.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot44(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot44(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot44(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 44!")
                await Bot44.start()
                checkig = await Bot44.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 44!")
        sessn = "DeadlyBot"
        Bot44 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot44.start()
        except:
            pass

    if String_Session45:
        Bot45 = TelegramClient(StringSession(String_Session45), API_ID, API_HASH)
        try:
            print("Got String Session 45!")
            await Bot45.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot45(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot45(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot45(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 45!")
                await Bot45.start()
                checkig = await Bot45.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 45!")
        sessn = "DeadlyBot"
        Bot45 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot45.start()
        except:
            pass

    if String_Session46:
        Bot46 = TelegramClient(StringSession(String_Session46), API_ID, API_HASH)
        try:
            print("Got String Session 46!")
            await Bot46.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot46(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot46(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot46(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 46!")
                await Bot46.start()
                checkig = await Bot46.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 46!")
        sessn = "DeadlyBot"
        Bot46 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot46.start()
        except:
            pass

    if String_Session47:
        Bot47 = TelegramClient(StringSession(String_Session47), API_ID, API_HASH)
        try:
            print("Got String Session 47!")
            await Bot47.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot47(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot47(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot47(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 47!")
                await Bot47.start()
                checkig = await Bot47.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 47!")
        sessn = "DeadlyBot"
        Bot47 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot47.start()
        except:
            pass

    if String_Session48:
        Bot48 = TelegramClient(StringSession(String_Session48), API_ID, API_HASH)
        try:
            print("Got String Session 48!")
            await Bot48.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot48(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot48(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot48(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 48!")
                await Bot48.start()
                checkig = await Bot48.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 48!")
        sessn = "DeadlyBot"
        Bot48 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot48.start()
        except:
            pass

    if String_Session49:
        Bot49 = TelegramClient(StringSession(String_Session49), API_ID, API_HASH)
        try:
            print("Got String Session 49!")
            await Bot49.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot49(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot49(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot49(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 49!")
                await Bot49.start()
                checkig = await Bot49.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 49!")
        sessn = "DeadlyBot"
        Bot49 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot49.start()
        except:
            pass

    if String_Session50:
        Bot50 = TelegramClient(StringSession(String_Session50), API_ID, API_HASH)
        try:
            print("Got String Session 50!")
            await Bot50.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot50(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot50(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot50(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 50!")
                await Bot50.start()
                checkig = await Bot50.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 50!")
        sessn = "DeadlyBot"
        Bot50 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot50.start()
        except:
            pass
    if String_Session51:
        Bot51 = TelegramClient(StringSession(String_Session51), API_ID, API_HASH)
        try:
            print("Got String Session 51!")
            await Bot51.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot51(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot51(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot51(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 51!")
                await Bot51.start()
                checkig = await Bot51.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 51!")
        sessn = "DeadlyBot"
        Bot51 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot51.start()
        except:
            pass

    if String_Session52:
        Bot52 = TelegramClient(StringSession(String_Session52), API_ID, API_HASH)
        try:
            print("Got String Session 52!")
            await Bot52.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot52(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot52(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot52(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 52!")
                await Bot52.start()
                checkig = await Bot52.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 52!")
        sessn = "DeadlyBot"
        Bot52 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot52.start()
        except:
            pass
    
    if String_Session53:
        Bot53 = TelegramClient(StringSession(String_Session53), API_ID, API_HASH)
        try:
            print("Got String Session 53!")
            await Bot53.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot53(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot53(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot53(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 53!")
                await Bot53.start()
                checkig = await Bot53.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 53!")
        sessn = "DeadlyBot"
        Bot53 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot53.start()
        except:
            pass
    
    if String_Session54:
        Bot54 = TelegramClient(StringSession(String_Session54), API_ID, API_HASH)
        try:
            print("Got String Session 54!")
            await Bot54.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot54(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot54(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot54(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 54!")
                await Bot54.start()
                checkig = await Bot54.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 54!")
        sessn = "DeadlyBot"
        Bot54 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot54.start()
        except:
            pass

    if String_Session55:
        Bot55 = TelegramClient(StringSession(String_Session55), API_ID, API_HASH)
        try:
            print("Got String Session 55!")
            await Bot55.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot55(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot55(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot55(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 55!")
                await Bot55.start()
                checkig = await Bot55.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 55!")
        sessn = "DeadlyBot"
        Bot55 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot55.start()
        except:
            pass

    if String_Session56:
        Bot56 = TelegramClient(StringSession(String_Session56), API_ID, API_HASH)
        try:
            print("Got String Session 56!")
            await Bot56.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot56(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot56(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot56(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 56!")
                await Bot56.start()
                checkig = await Bot56.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 56!")
        sessn = "DeadlyBot"
        Bot56 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot56.start()
        except:
            pass

    if String_Session57:
        Bot57 = TelegramClient(StringSession(String_Session57), API_ID, API_HASH)
        try:
            print("Got String Session 57!")
            await Bot57.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot57(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot57(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot57(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 57!")
                await Bot57.start()
                checkig = await Bot57.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 57!")
        sessn = "DeadlyBot"
        Bot57 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot57.start()
        except:
            pass

    if String_Session58:
        Bot58 = TelegramClient(StringSession(String_Session58), API_ID, API_HASH)
        try:
            print("Got String Session 58!")
            await Bot58.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot58(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot58(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot58(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 58!")
                await Bot58.start()
                checkig = await Bot58.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 58!")
        sessn = "DeadlyBot"
        Bot58 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot58.start()
        except:
            pass

    if String_Session59:
        Bot59 = TelegramClient(StringSession(String_Session59), API_ID, API_HASH)
        try:
            print("Got String Session 59!")
            await Bot59.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot59(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot59(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot59(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 59!")
                await Bot59.start()
                checkig = await Bot59.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 59!")
        sessn = "DeadlyBot"
        Bot59 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot59.start()
        except:
            pass

    if String_Session50:
        Bot60 = TelegramClient(StringSession(String_Session60), API_ID, API_HASH)
        try:
            print("Got String Session 60!")
            await Bot60.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot60(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot60(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot60(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 60!")
                await Bot60.start()
                checkig = await Bot60.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 60!")
        sessn = "DeadlyBot"
        Bot60 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot60.start()
        except:
            pass
    if String_Session61:
        Bot61 = TelegramClient(StringSession(String_Session61), API_ID, API_HASH)
        try:
            print("Got String Session 61!")
            await Bot61.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot61(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot61(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot61(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 61!")
                await Bot61.start()
                checkig = await Bot61.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 61!")
        sessn = "DeadlyBot"
        Bot61 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot61.start()
        except:
            pass

    if String_Session62:
        Bot62 = TelegramClient(StringSession(String_Session62), API_ID, API_HASH)
        try:
            print("Got String Session 62!")
            await Bot62.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot62(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot62(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot62(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 62!")
                await Bot62.start()
                checkig = await Bot62.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 62!")
        sessn = "DeadlyBot"
        Bot62 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot62.start()
        except:
            pass
    
    if String_Session63:
        Bot63 = TelegramClient(StringSession(String_Session63), API_ID, API_HASH)
        try:
            print("Got String Session 63!")
            await Bot63.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot63(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot63(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot63(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 63!")
                await Bot63.start()
                checkig = await Bot63.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 63!")
        sessn = "DeadlyBot"
        Bot63 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot63.start()
        except:
            pass
    
    if String_Session64:
        Bot64 = TelegramClient(StringSession(String_Session64), API_ID, API_HASH)
        try:
            print("Got String Session 64!")
            await Bot64.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot64(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot64(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot64(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 64!")
                await Bot64.start()
                checkig = await Bot64.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 64!")
        sessn = "DeadlyBot"
        Bot64 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot64.start()
        except:
            pass

    if String_Session65:
        Bot65 = TelegramClient(StringSession(String_Session65), API_ID, API_HASH)
        try:
            print("Got String Session 65!")
            await Bot65.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot65(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot65(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot65(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 65!")
                await Bot65.start()
                checkig = await Bot65.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 65!")
        sessn = "DeadlyBot"
        Bot65 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot65.start()
        except:
            pass

    if String_Session66:
        Bot66 = TelegramClient(StringSession(String_Session66), API_ID, API_HASH)
        try:
            print("Got String Session 66!")
            await Bot66.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot66(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot66(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot66(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 66!")
                await Bot66.start()
                checkig = await Bot66.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 66!")
        sessn = "DeadlyBot"
        Bot66 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot66.start()
        except:
            pass

    if String_Session67:
        Bot67 = TelegramClient(StringSession(String_Session67), API_ID, API_HASH)
        try:
            print("Got String Session 67!")
            await Bot67.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot67(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot67(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot67(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 67!")
                await Bot67.start()
                checkig = await Bot67.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 67!")
        sessn = "DeadlyBot"
        Bot67 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot67.start()
        except:
            pass

    if String_Session68:
        Bot68 = TelegramClient(StringSession(String_Session68), API_ID, API_HASH)
        try:
            print("Got String Session 68!")
            await Bot68.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot68(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot68(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot68(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 68!")
                await Bot68.start()
                checkig = await Bot68.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 68!")
        sessn = "DeadlyBot"
        Bot68 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot68.start()
        except:
            pass

    if String_Session69:
        Bot69 = TelegramClient(StringSession(String_Session69), API_ID, API_HASH)
        try:
            print("Got String Session 69!")
            await Bot69.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot69(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot69(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot69(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 69!")
                await Bot69.start()
                checkig = await Bot69.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 69!")
        sessn = "DeadlyBot"
        Bot69 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot69.start()
        except:
            pass

    if String_Session70:
        Bot70 = TelegramClient(StringSession(String_Session70), API_ID, API_HASH)
        try:
            print("Got String Session 70!")
            await Bot70.start()
            officialsameer = "https://t.me/DEADLY_fighters"
            await Bot70(functions.channels.JoinChannelRequest(channel=officialsameer))
            await Bot70(functions.channels.JoinChannelRequest(channel="@Deadly_spammer"))
            await Bot70(functions.channels.JoinChannelRequest(channel="@Deadly_spam_bot"))
        except:
            try:
                print("Got String Session 10!")
                await Bot70.start()
                checkig = await Bot70.get_me() 
            except Exception as e:
                print(str(e))
                pass
    else:
        print("Didn't get String Session 70!")
        sessn = "DeadlyBot"
        Bot70 = TelegramClient(sessn, API_ID, API_HASH)
        try:
            await Bot70.start()
        except:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(DeadlyBot_bots())





##########################################################################################################################
# Defining every function here + fellows list

# prettyjson
# TeamArsenic_time
# ifgif

# @DEADLY_SPAM_BOT
##########################################################################################################################


def TeamArsenic_time(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    TeamArsenic_ret = (
        ((str(weeks) + "ᴡ:") if weeks else "")
        + ((str(days) + "ᴅ:") if days else "")
        + ((str(hours) + "ʜ:") if hours else "")
        + ((str(minutes) + "ᴍ:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if TeamArsenic_ret.endswith(":"):
        return TeamArsenic_ret[:-1]
    else:
        return TeamArsenic_ret




async def ifgif(e, gif):
  try:
    await e.client(
      functions.messages.SaveGifRequest(
        id=types.InputDocument(
          id=sandy.media.document.id,
          access_hash=bitxh.media.document.access_hash,
          file_reference=bitxh.media.document.file_reference,
        ),
        unsave=True,
      )
    )
  except:
    pass



##########################################################################################################################
# Defining all vars here


# + Help Menu


# @TeamDeadlyBot
##########################################################################################################################

fellows = {}
@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hn))
async def bot_help(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        gladbot = e.text.split(" ")
        if len(gladbot) > 1:
            helpcll = gladbot[1]
            if helpcll.lower() == "spamcmds":
                await e.reply(spam_menu)
            elif helpcll.lower() == "cursecmds":
                await e.reply(curse_menu)
            elif helpcll.lower() == "sudocmds":
                await e.reply(sudo_menu)
            elif helpcll.lower() == "devcmds":
                await e.reply(dev_menu)
            elif helpcll.lower() == "acccmds":
                await e.reply(acc_menu)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)



##########################################################################################################################
# All commands of spam category

# spam
# bigspam
# packspam
# dspamhang

# @DEADLY_SPAM_BOT
##########################################################################################################################


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hn))
async def spam(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    error = "Use {hn}spam for range less than or equal to 100. For bigger spams use {hn}bigspam."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(gladbot) == 2:
            message = str(gladbot[1])
            counter = int(gladbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            async with e.client.action(e.chat_id, "typing"):
                await asyncio.wait([e.respond(message, reply_to=e.reply_to_msg_id) for i in range(counter)])
        elif e.reply_to_msg_id and bitxh.media:  
            counter = int(gladbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    bitxh = await e.client.send_file(e.chat_id, bitxh, caption=bitxh.text)
                    await ifgif(e, bitxh)  
        elif e.reply_to_msg_id and bitxh.text:
            message = bitxh.text
            counter = int(gladbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            async with e.client.action(e.chat_id, "typing"):
                await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage)




@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hn))
async def bigspam(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(gladbot) == 2:
            msg = str(gladbot[1])
            counter = int(gladbot[0])
            for i in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.respond(msg, reply_to=e.reply_to_msg_id)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and bitxh.media:  
            counter = int(gladbot[0])
            for i in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    bitxh = await e.client.send_file(e.chat_id, bitxh, caption=bitxh.text)
                    await ifgif(e, bitxh) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and bitxh.text:
            message = bitxh.text
            counter = int(gladbot[0])
            for i in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    try:
                        await e.client.send_message(e.chat_id, message)
                    except:
                        pass
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)

@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%suspam(?: |$)(.*)" % hn))
async def uspam(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = e.text.split(" ", 1)
        bitxh = await e.get_reply_message()
        x = 0
        if len(gladbot) == 2:
            msg = str(gladbot[1])
            while x == 0:
                async with e.client.action(e.chat_id, "typing"):
                    await e.respond(msg, reply_to=e.reply_to_msg_id)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and bitxh.media:  
            while x == 0:
                async with e.client.action(e.chat_id, "document"):
                    bitxh = await e.client.send_file(e.chat_id, bitxh, caption=bitxh.text)
                    await ifgif(e, bitxh) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and bitxh.text:
            message = bitxh.text
            while x == 0:
                async with e.client.action(e.chat_id, "typing"):
                    try:
                        await e.client.send_message(e.chat_id, message)
                    except:
                        pass
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)

 
@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%spackspam" % hn))
async def _(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        try:
            x = await e.get_reply_message()
            if not (x and x.media and hasattr(x.media, "document")):
                return await e.reply("`Reply To Sticker Only.`")
            set = x.document.attributes[1]
            sset = await e.client(
                GetStickerSetRequest(
                InputStickerSetID(
                    id=set.stickerset.id,
                    access_hash=set.stickerset.access_hash,
                )
                )
            )
            pack = sset.set.short_name
            docs = [
                utils.get_input_document(x)
                for x in (
                await e.client(GetStickerSetRequest(InputStickerSetShortName(pack)))
                ).documents
            ]
            for xx in docs:
                async with e.client.action(e.chat_id, "document"):
                    await e.client.send_file(e.chat_id, file=(xx))
                    await asyncio.sleep(0.3)
        except Exception as xy:
            print(str(xy))
            await e.reply(f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs.")


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sdspam" % hn))
async def dspam(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        bitxh = await e.get_reply_message()
        gladbot = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        gladbotisop = gladbot[1:]
        if len(gladbotisop) == 2:
            message = str(gladbotisop[1])
            counter = int(gladbotisop[0])
            sleeptime = float(gladbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await bitxh.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and bitxh.media:  
            counter = int(gladbotisop[0])
            sleeptime = float(gladbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    bitxh = await e.client.send_file(e.chat_id, bitxh, caption=bitxh.text)
                    await ifgif(e, bitxh) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and bitxh.text:
            message = bitxh.text
            counter = int(gladbotisop[0])
            sleeptime = float(gladbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%shang" % hn))
async def spam(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(gladbot) == 1:
            counter = int(gladbot[0])
            hangmsg = f"😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟"
            await asyncio.wait([e.respond(hangmsg, reply_to=e.reply_to_msg_id) for i in range(counter)])
        else:
            await e.reply(usage)


##########################################################################################################################
# Curse category:

# curse
# multicurse
# umulticurse
# ucurse
# replycurse
# dreplycurse
# @TeamDeadlyBot
##########################################################################################################################

@Bot1.on(events.NewMessage(incoming=True))
@Bot2.on(events.NewMessage(incoming=True))
@Bot3.on(events.NewMessage(incoming=True))
@Bot4.on(events.NewMessage(incoming=True))
@Bot5.on(events.NewMessage(incoming=True))
@Bot6.on(events.NewMessage(incoming=True))
@Bot7.on(events.NewMessage(incoming=True))
@Bot8.on(events.NewMessage(incoming=True))
@Bot9.on(events.NewMessage(incoming=True))
@Bot10.on(events.NewMessage(incoming=True))
@Bot11.on(events.NewMessage(incoming=True))
@Bot12.on(events.NewMessage(incoming=True))
@Bot13.on(events.NewMessage(incoming=True))
@Bot14.on(events.NewMessage(incoming=True))
@Bot15.on(events.NewMessage(incoming=True))
@Bot16.on(events.NewMessage(incoming=True))
@Bot17.on(events.NewMessage(incoming=True))
@Bot18.on(events.NewMessage(incoming=True))
@Bot19.on(events.NewMessage(incoming=True))
@Bot20.on(events.NewMessage(incoming=True))
@Bot21.on(events.NewMessage(incoming=True))
@Bot22.on(events.NewMessage(incoming=True))
@Bot23.on(events.NewMessage(incoming=True))
@Bot24.on(events.NewMessage(incoming=True))
@Bot25.on(events.NewMessage(incoming=True))
@Bot26.on(events.NewMessage(incoming=True))
@Bot27.on(events.NewMessage(incoming=True))
@Bot28.on(events.NewMessage(incoming=True))
@Bot29.on(events.NewMessage(incoming=True))
@Bot30.on(events.NewMessage(incoming=True))
@Bot31.on(events.NewMessage(incoming=True))
@Bot32.on(events.NewMessage(incoming=True))
@Bot33.on(events.NewMessage(incoming=True))
@Bot34.on(events.NewMessage(incoming=True))
@Bot35.on(events.NewMessage(incoming=True))
@Bot36.on(events.NewMessage(incoming=True))
@Bot37.on(events.NewMessage(incoming=True))
@Bot38.on(events.NewMessage(incoming=True))
@Bot39.on(events.NewMessage(incoming=True))
@Bot40.on(events.NewMessage(incoming=True))
@Bot41.on(events.NewMessage(incoming=True))
@Bot42.on(events.NewMessage(incoming=True))
@Bot43.on(events.NewMessage(incoming=True))
@Bot44.on(events.NewMessage(incoming=True))
@Bot45.on(events.NewMessage(incoming=True))
@Bot46.on(events.NewMessage(incoming=True))
@Bot47.on(events.NewMessage(incoming=True))
@Bot48.on(events.NewMessage(incoming=True))
@Bot49.on(events.NewMessage(incoming=True))
@Bot50.on(events.NewMessage(incoming=True))
@Bot51.on(events.NewMessage(incoming=True))
@Bot52.on(events.NewMessage(incoming=True))
@Bot53.on(events.NewMessage(incoming=True))
@Bot54.on(events.NewMessage(incoming=True))
@Bot55.on(events.NewMessage(incoming=True))
@Bot56.on(events.NewMessage(incoming=True))
@Bot57.on(events.NewMessage(incoming=True))
@Bot58.on(events.NewMessage(incoming=True))
@Bot59.on(events.NewMessage(incoming=True))
@Bot60.on(events.NewMessage(incoming=True))
@Bot61.on(events.NewMessage(incoming=True))
@Bot62.on(events.NewMessage(incoming=True))
@Bot63.on(events.NewMessage(incoming=True))
@Bot64.on(events.NewMessage(incoming=True))
@Bot65.on(events.NewMessage(incoming=True))
@Bot66.on(events.NewMessage(incoming=True))
@Bot67.on(events.NewMessage(incoming=True))
@Bot68.on(events.NewMessage(incoming=True))
@Bot69.on(events.NewMessage(incoming=True))
@Bot70.on(events.NewMessage(incoming=True))
async def _(event):
    global fellows
    gey = fellows.get(event.sender_id)
    if not gey:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".forofficialsameer(random.choice(replies)),
            reply_to=event.message.id,
        )          

@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%scurse" % hn))
async def curse(e):
    usage = f"Usage:\n{hn}curse <count> <Username of User>\n\n{hn}curse <count> <reply to a User>"
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(gladbot) == 2:
            user = str(gladbot[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in crew:
                text = f"I can't betray @TeamDeadlyBot's crew."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(gladbot[0])
                for xd in range(counter):
                    reply = random.choice(curses)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in crew:
                text = f"I can't betray @TeamDeadlyBot's crew."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(gladbot[0])
                username = f"[{c}](tg://user?id={g})"
                for xd in range(counter):
                    reply = random.choice(curses)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%smulticurse" % hn))
async def curse(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help cursecmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴄᴜʀsᴇ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        gladbot = []
        try:
            for i in ("".join(e.text.split(maxsplit=1)[1:])).split(" "):
                if str(i[0]) == '@':
                    gladbot.append(str(i[1:]))
                else:
                    gladbot.append(str(i))
        except:
            return await e.reply(usage, parse_mode=None, link_preview=None)
        if len(gladbot) >= 2:
            demv = 0
            demvs = []
            sumdo = 0
            sumdos = []
            emror = 0
            boom = 0
            booms = []
            counter = int(gladbot[0])
            gladmention = f""
            for ulers in gladbot[1:]:
                try:
                    fuckit = await e.client.get_entity(ulers)
                    ummser = fuckit.id
                    if ummser in crew:
                        demv += 1
                        demvs.append(ummser)
                    elif ummser in SUDO_USERS:
                        sumdo += 1
                        sumdos.append(ummser)
                    else:
                        fname = fuckit.first_name
                        gladmention += f"[{fname}](tg://user?id={ummser})"
                        gladmention += "  "
                        boom += 1
                        booms.append(ummser)
                except:
                    emror += 1
            try:
                if boom != 0:
                    await e.reply(f"Your command contains->\n:{emror} Job faliures:\n:{sumdo} {sumdos} Sudo users id:\n:{demv} {demvs} @TeamDeadlyBot crew member's id:\n\n**:Skipping these:**\n\n**Starting powerfull multi curse on {boom} users for counter {counter}.**\nList of users who are gonna assaulted: {booms}")
                    await asyncio.sleep(3)
                    for i in range(counter):
                        curmse = random.choice(curses)
                        verse = f"{gladmention} {curmse}"
                        async with e.client.action(e.chat_id, "typing"):
                            await e.client.send_message(e.chat_id, verse)
                            await asyncio.sleep(0.3)
                elif demv != 0 or sumdo != 0:
                    await e.reply(f"Your command contains->\n:{emror} Job faliures:\n:{sumdo} {sumdos} Sudo users id:\n:{demv} {demvs} @TeamDeadlyBot crew member's id:\n\n**:Skipping these:**\n\n**Users to assault: {boom}**")
                else:
                    await e.reply(usage)
            except Exception as g:
                await e.reply(usage)
        else:
            await e.reply(usage)


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sumulticurse" % hn))
async def curse(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help cursecmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴄᴜʀsᴇ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = []
        try:
            for i in ("".join(e.text.split(maxsplit=1)[1:])).split(" "):
                if str(i[0]) == '@':
                    gladbot.append(str(i[1:]))
                else:
                    gladbot.append(str(i))
        except:
            return await e.reply(usage, parse_mode=None, link_preview=None)
        if len(gladbot) >= 2:
            demv = 0
            demvs = []
            sumdo = 0
            sumdos = []
            emror = 0
            boom = 0
            booms = []
            gladmention = f""
            for ulers in gladbot:
                try:
                    fuckit = await e.client.get_entity(ulers)
                    ummser = fuckit.id
                    if ummser in crew:
                        demv += 1
                        demvs.append(ummser)
                    elif ummser in SUDO_USERS:
                        sumdo += 1
                        sumdos.append(ummser)
                    else:
                        fname = fuckit.first_name
                        gladmention += f"[{fname}](tg://user?id={ummser})"
                        gladmention += "  "
                        boom += 1
                        booms.append(ummser)
                except:
                    emror += 1
            try:
                if boom != 0:
                    await e.reply(f"Your command contains->\n:{emror} Job faliures:\n:{sumdo} {sumdos} Sudo users id:\n:{demv} {demvs} @TeamDeadlyBot crew member's id:\n\n**:Skipping these:**\n\n**Starting powerfull unlimited multi curse on {boom}.**\nList of users who are gonna assaulted: {booms}")
                    await asyncio.sleep(3)
                    xd = 0
                    while xd == 0:
                        curmse = random.choice(curses)
                        verse = f"{gladmention} {curmse}"
                        async with e.client.action(e.chat_id, "typing"):
                            await e.client.send_message(e.chat_id, verse)
                            await asyncio.sleep(0.3)
                elif demv != 0 or sumdo != 0:
                    await e.reply(f"Your command contains->\n:{emror} Job faliures:\n:{sumdo} {sumdos} Sudo users id:\n:{demv} {demvs} @TeamDeadlyBot crew member's id:\n\n**:Skipping these:**\n\n**Users to assault: {boom}**")
                else:
                    await e.reply(usage)
            except Exception as g:
                await e.reply(str(g))
                #await e.reply(usage)
        else:
            await e.reply(usage)


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sucurse" % hn))
async def ucurse(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help cursecmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴄᴜʀsᴇ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = e.text.split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(gladbot) == 2:
            user = str(gladbot[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in crew:
                text = f"I can't betray @TeamDeadlyBot's crew."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                x = 0
                while x==0:
                    reply = random.choice(curses)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in crew:
                text = f"I can't betray @TeamDeadlyBot's crew."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                username = f"[{c}](tg://user?id={g})"
                x=0
                while x == 0 :
                    reply = random.choice(curses)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sreplycurse" % hn))
async def replycurse(e):
    global fellows
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help cursecmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴄᴜʀsᴇ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(gladbot[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in crew:
                text = f"I can't betray @TeamDeadlyBot's crew."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                fellows[user_id] = []
                gey = fellows.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                name = a.first_name
                text = f"Activated reply and curse on {name}"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in crew:
                text = f"I can't betray @TeamDeadlyBot's crew."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                name = umser.first_name
                fellows[user_id] = []
                gey = fellows.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated Reply Curse on {name}"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)



@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sdreplycurse" % hn))
async def dreplycurse(e):
    global fellows
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help cursecmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴄᴜʀsᴇ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        checkpost = e.text.split(maxsplit=1)
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(gladbot[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in crew:
                text = f"Never started reply and curse on @TeamDeadlyBot's crew."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                try:
                    name = a.first_name
                    gey = fellows.get(user_id)
                    if gey:
                        gey.pop(0)
                    text = f"De-activated reply and curse on {name}"
                    await e.reply(text, parse_mode=None, link_preview=None )
                except Exception as ec:
                    await e.reply(str(ec))
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            name = umser.first_name
            if int(user_id) in crew:
                text = f"Never started reply and curse on @TeamDeadlyBot's crew."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                gey = fellows.get(user_id)
                if gey:
                    gey.pop(0)
                text = f"De-activated reply and curse on {name}"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)

##########################################################################################################################
# All commands of sudo category

# ping
# alive

# @TeamDeadlyBot
##########################################################################################################################



@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hn))
async def gtping(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        if e.reply_to_msg_id:
            v = await e.respond("Pᴏɴɢ!", reply_to=e.reply_to_msg_id)
        else:
            v = await e.reply("Pᴏɴɢ!")
        ping_start = datetime.now()
        ping_end = datetime.now()
        ms = (ping_end-ping_start).microseconds / 1000
        uptime = TeamArsenic_time((time.time() - StartTime) * 1000)
        ping_msg = f"•• Pᴏɴɢ . ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ : {ms}ᴍs\n⏳ Uᴘᴛɪᴍᴇ - {uptime}"
        await v.edit(ping_msg)

@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hn))
async def alive(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        try:
            await e.client.send_file(e.chat_id, ALIVE_MEDIA, caption = alive_temxt, reply_to=e.message.id, link_preview=None)
        except:
            await e.reply(alive_temxt, link_preview=None)



##########################################################################################################################
# All commands of sudo category

# leave
#join
#pjoin
# restart
# logs
# usage


# @TeamDeadlyBot
##########################################################################################################################


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hn))
async def leave(e):
    if e.sender_id in DEV_USERS:
        chamt = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            chamt_id = int(chamt[0])
            await e.reply("*Moves to door...*")
            try:
                await e.client(LeaveChannelRequest(chamt_id))
                await e.edit("*Silently left...*")
            except Exception as eror:
                await e.edit(str(eror))
        else:
            chamt_id = e.chat_id
            await e.reply("*Moves to door...*")
            try:
                await e.client(LeaveChannelRequest(chamt_id))
                await e.edit("*Silently left!*")
            except Exception as eror:
                await e.edit(str(eror))
    elif e.sender_id in SUDO_USERS:
        await e.reply("You ain't a Dev User bish!")


##########################################################################################################################

# Heroku Work

##########################################################################################################################

heroku_api = "https://api.heroku.com"
Heroku = heroku3.from_key(HEROKU_API_KEY)

@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hn))
async def _(dyno):
    if dyno.fwd_from:
        return
    if dyno.sender_id in DEV_USERS:
        pass
    else:
        return
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except:
        return await dyno.reply(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    v = await dyno.reply("Getting Logs....")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    await v.edit("Got the logs wait a sec")
    await dyno.client.send_file(
        dyno.chat_id,
        "logs.txt",
        reply_to=dyno.id,
        force_document=True,
        thumb="resources/DeadlyBot.jpeg",
        caption="@DEADLY_SPAM_BOT spammerbots logs.",
    )

    await asyncio.sleep(5)
    await v.delete()
    return os.remove("logs.txt")


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%susage(?: |$)(.*)" % hn))
async def dyno_usage(dyno):
    if dyno.fwd_from:
        return
    if dyno.sender_id in DEV_USERS:
        pass
    else:
        return
    """
    Get your account Dyno Usage
    """
    die = await dyno.reply("**Processing...**")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await die.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = officialsameerh.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = officialsameerh.floor(minutes_remaining / 60)
    minutes = officialsameerh.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = officialsameerh.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = officialsameerh.floor(AppQuotaUsed / 60)
    AppMinutes = officialsameerh.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await die.edit(
        "**Dyno Usage**:\n\n"
        f" -> `Dyno usage for`  **{HEROKU_APP_NAME}**:\n"
        f"     •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " -> `Dyno hours quota remaining this month`:\n"
        f"     •  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
    )


##########################################################################################################################



# Start bot command



# @TeamDeadlyBot
##########################################################################################################################


@Bot1.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot2.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot3.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot4.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot5.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot6.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot7.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot8.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot9.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot10.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot11.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot12.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot13.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot14.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot15.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot16.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot17.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot18.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot19.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot20.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot21.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot22.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot23.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot24.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot25.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot26.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot27.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot28.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot29.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot30.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot31.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot32.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot33.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot34.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot35.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot36.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot37.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot38.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot39.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot40.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot41.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot42.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot43.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot44.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot45.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot46.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot47.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot48.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot49.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot50.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot51.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot52.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot53.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot54.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot55.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot56.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot57.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot58.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot59.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot60.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot61.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot62.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot63.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot64.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot65.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot66.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot67.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot68.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot69.on(events.NewMessage(incoming=True, pattern="/start"))
@Bot70.on(events.NewMessage(incoming=True, pattern="/start"))
async def alive(e):
    xd = str(e.chat_id)
    if '-' not in xd:
        xd  = await e.client.get_me()
        if not xd.bot:
            await e.client.send_file(e.chat_id, glad_logo, caption = start_caption1, link_preview=None)
        else:
            await e.client.send_message(e.chat_id, start_caption, buttons=buttons)

##########################################################################################################################



# ACCOUNT COMMANDS
#JOIN
#PJOIN
#PROFILEPIC
#NAME
#BIO


# @TeamDeadlyBot
##########################################################################################################################

@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sbio(?: |$)(.*)" % hn))
async def bio(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help devcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in DEV_USERS:
        chckpnt = e.text.split(" ", 1)
        message = chckpnt[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Bio..."
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed bio successfully!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sname(?: |$)(.*)" % hn))
async def bio(e):
    usage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help devcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in DEV_USERS:
        chckpnt = e.text.split(" ", 1)
        message = chckpnt[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed name successfully!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sprofilepic(?: |$)(.*)" % hn))
async def _(event):
    if event.sender_id in DEV_USERS:
        try:
            glad = await event.get_reply_message()
            try:
                media = await glad.download_media( "spammerbots/downloads/")
            except:
                pass
            await client(UploadProfilePhotoRequest(
                await client.upload_file(media)
            ))
            await event.reply("**Changed profile picture successfully!!**")
            try:
                os.remove(media)
            except Excepion as e:
                print(str(e))
        except:
            pass
##########################################################################################################################

################################################# JOIN AND PJOIN #########################################################



##########################################################################################################################
@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hn))
async def _(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        dattext = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            chash = dattext[0]
            text = "Roger that...\nI'm on it."
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=chash))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Joined the chat successfully\nOver!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(accusage, parse_mode=None, link_preview=None )





@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hn))
async def _(e):
    if e.sender_id in SUDO_USERS or e.sender_id in DEV_USERS:
        dattext = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            chash = dattext[0]
            text = "Roger that...\nI'm on it."
            try:
                await e.client(ImportChatInviteRequest(chash))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Joined the chat successfully\nOver!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(accusage, parse_mode=None, link_preview=None )



##########################################################################################################################
################################################## RESTART ###############################################################


@Bot1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot51.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot52.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot53.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot54.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot55.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot56.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot57.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot58.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot59.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot60.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot61.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot62.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot63.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot64.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot65.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot66.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot67.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot68.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot69.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
@Bot70.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hn))
async def _(e):
    if e.sender_id in DEV_USERS:
        reboot_text = """
❣️❣️ SAMEER OP ❣️❣️

Rᴇʙᴏᴏᴛɪɴɢ ʙᴏᴛ...

Wᴀɪᴛ ғᴏʀ ᴀ ᴡʜɪʟᴇ ᴛᴏ ᴜsᴇ ɪᴛ ᴀɢᴀɪɴ.
        """
        await e.reply(reboot_text)
        try:
            Bot1.disconnect()
        except Exception as e:
            pass
        try:
            Bot2.disconnect()
        except Exception as e:
            pass
        try:
            Bot3.disconnect()
        except Exception as e:
            pass
        try:
            Bot4.disconnect()
        except Exception as e:
            pass
        try:
            Bot5.disconnect()
        except Exception as e:
            pass
        try:
            Bot6.disconnect()
        except Exception as e:
            pass
        try:
            Bot7.disconnect()
        except Exception as e:
            pass
        try:
            Bot8.disconnect()
        except Exception as e:
            pass
        try:
            Bot9.disconnect()
        except Exception as e:
            pass
        try:
            Bot10.disconnect()
        except Exception as e:
            pass
        try:
            Bot11.disconnect()
        except Exception as e:
            pass
        try:
            Bot12.disconnect()
        except Exception as e:
            pass
        try:
            Bot13.disconnect()
        except Exception as e:
            pass
        try:
            Bot14.disconnect()
        except Exception as e:
            pass
        try:
            Bot15.disconnect()
        except Exception as e:
            pass
        try:
            Bot16.disconnect()
        except Exception as e:
            pass
        try:
            Bot17.disconnect()
        except Exception as e:
            pass
        try:
            Bot18.disconnect()
        except Exception as e:
            pass
        try:
            Bot19.disconnect()
        except Exception as e:
            pass
        try:
            Bot20.disconnect()
        except Exception as e:
            pass
        try:
            Bot21.disconnect()
        except Exception as e:
            pass
        try:
            Bot22.disconnect()
        except Exception as e:
            pass
        try:
            Bot23.disconnect()
        except Exception as e:
            pass
        try:
            Bot24.disconnect()
        except Exception as e:
            pass
        try:
            Bot25.disconnect()
        except Exception as e:
            pass
        try:
            Bot26.disconnect()
        except Exception as e:
            pass
        try:
            Bot27.disconnect()
        except Exception as e:
            pass
        try:
            Bot28.disconnect()
        except Exception as e:
            pass
        try:
            Bot29.disconnect()
        except Exception as e:
            pass
        try:
            Bot30.disconnect()
        except Exception as e:
            pass
        try:
            Bot31.disconnect()
        except Exception as e:
            pass
        try:
            Bot32.disconnect()
        except Exception as e:
            pass
        try:
            Bot33.disconnect()
        except Exception as e:
            pass
        try:
            Bot34.disconnect()
        except Exception as e:
            pass
        try:
            Bot35.disconnect()
        except Exception as e:
            pass
        try:
            Bot36.disconnect()
        except Exception as e:
            pass
        try:
            Bot37.disconnect()
        except Exception as e:
            pass
        try:
            Bot38.disconnect()
        except Exception as e:
            pass
        try:
            Bot39.disconnect()
        except Exception as e:
            pass
        try:
            Bot40.disconnect()
        except Exception as e:
            pass
        try:
            Bot41.disconnect()
        except Exception as e:
            pass
        try:
            Bot42.disconnect()
        except Exception as e:
            pass
        try:
            Bot43.disconnect()
        except Exception as e:
            pass
        try:
            Bot44.disconnect()
        except Exception as e:
            pass
        try:
            Bot45.disconnect()
        except Exception as e:
            pass
        try:
            Bot46.disconnect()
        except Exception as e:
            pass
        try:
            Bot47.disconnect()
        except Exception as e:
            pass
        try:
            Bot48.disconnect()
        except Exception as e:
            pass
        try:
            Bot49.disconnect()
        except Exception as e:
            pass
        try:
            Bot50.disconnect()
        except Exception as e:
            pass
        try:
            Bot51.disconnect()
        except Exception as e:
            pass
        try:
            Bot52.disconnect()
        except Exception as e:
            pass
        try:
            Bot53.disconnect()
        except Exception as e:
            pass
        try:
            Bot54.disconnect()
        except Exception as e:
            pass
        try:
            Bot55.disconnect()
        except Exception as e:
            pass
        try:
            Bot56.disconnect()
        except Exception as e:
            pass
        try:
            Bot57.disconnect()
        except Exception as e:
            pass
        try:
            Bot58.disconnect()
        except Exception as e:
            pass
        try:
            Bot59.disconnect()
        except Exception as e:
            pass
        try:
            Bot60.disconnect()
        except Exception as e:
            pass
        try:
            Bot61.disconnect()
        except Exception as e:
            pass
        try:
            Bot62.disconnect()
        except Exception as e:
            pass
        try:
            Bot63.disconnect()
        except Exception as e:
            pass
        try:
            Bot64.disconnect()
        except Exception as e:
            pass
        try:
            Bot65.disconnect()
        except Exception as e:
            pass
        try:
            Bot66.disconnect()
        except Exception as e:
            pass
        try:
            Bot67.disconnect()
        except Exception as e:
            pass
        try:
            Bot68.disconnect()
        except Exception as e:
            pass
        try:
            Bot69.disconnect()
        except Exception as e:
            pass
        try:
            Bot70.disconnect()
        except Exception as e:
            pass
        args = [sys.executable, "-m", "sameer.py"]
        os.execl(sys.executable, *args)
        quit()

##########################################################################################################################

gladtext = """
  HAHA
"""
print(gladtext)
print("")
print("")
print("Rooted successfully...")
print("Starting Deadly Spammerbots...")
print("Started....")
if len(sys.argv) not in (1, 3, 4):
    try:
        Bot1.disconnect()
    except Exception as e:
        pass
    try:
        Bot2.disconnect()
    except Exception as e:
        pass
    try:
        Bot3.disconnect()
    except Exception as e:
        pass
    try:
        Bot4.disconnect()
    except Exception as e:
        pass
    try:
        Bot5.disconnect()
    except Exception as e:
        pass
    try:
        Bot6.disconnect()
    except Exception as e:
        pass
    try:
        Bot7.disconnect()
    except Exception as e:
        pass
    try:
        Bot8.disconnect()
    except Exception as e:
        pass
    try:
        Bot9.disconnect()
    except Exception as e:
        pass
    try:
        Bot10.disconnect()
    except Exception as e:
        pass
    try:
        Bot11.disconnect()
    except Exception as e:
        pass
    try:
        Bot12.disconnect()
    except Exception as e:
        pass
    try:
        Bot13.disconnect()
    except Exception as e:
        pass
    try:
        Bot14.disconnect()
    except Exception as e:
        pass
    try:
        Bot15.disconnect()
    except Exception as e:
        pass
    try:
        Bot16.disconnect()
    except Exception as e:
        pass
    try:
        Bot17.disconnect()
    except Exception as e:
        pass
    try:
        Bot18.disconnect()
    except Exception as e:
        pass
    try:
        Bot19.disconnect()
    except Exception as e:
        pass
    try:
        Bot20.disconnect()
    except Exception as e:
        pass
    try:
        Bot21.disconnect()
    except Exception as e:
        pass
    try:
        Bot22.disconnect()
    except Exception as e:
        pass
    try:
        Bot23.disconnect()
    except Exception as e:
        pass
    try:
        Bot24.disconnect()
    except Exception as e:
        pass
    try:
        Bot25.disconnect()
    except Exception as e:
        pass
    try:
        Bot26.disconnect()
    except Exception as e:
        pass
    try:
        Bot27.disconnect()
    except Exception as e:
        pass
    try:
        Bot28.disconnect()
    except Exception as e:
        pass
    try:
        Bot29.disconnect()
    except Exception as e:
        pass
    try:
        Bot30.disconnect()
    except Exception as e:
        pass
    try:
        Bot31.disconnect()
    except Exception as e:
        pass
    try:
        Bot32.disconnect()
    except Exception as e:
        pass
    try:
        Bot33.disconnect()
    except Exception as e:
        pass
    try:
        Bot34.disconnect()
    except Exception as e:
        pass
    try:
        Bot35.disconnect()
    except Exception as e:
        pass
    try:
        Bot36.disconnect()
    except Exception as e:
        pass
    try:
        Bot37.disconnect()
    except Exception as e:
        pass
    try:
        Bot38.disconnect()
    except Exception as e:
        pass
    try:
        Bot39.disconnect()
    except Exception as e:
        pass
    try:
        Bot40.disconnect()
    except Exception as e:
        pass
    try:
        Bot41.disconnect()
    except Exception as e:
        pass
    try:
        Bot42.disconnect()
    except Exception as e:
        pass
    try:
        Bot43.disconnect()
    except Exception as e:
        pass
    try:
        Bot44.disconnect()
    except Exception as e:
        pass
    try:
        Bot45.disconnect()
    except Exception as e:
        pass
    try:
        Bot46.disconnect()
    except Exception as e:
        pass
    try:
        Bot47.disconnect()
    except Exception as e:
        pass
    try:
        Bot48.disconnect()
    except Exception as e:
        pass
    try:
        Bot49.disconnect()
    except Exception as e:
        pass
    try:
        Bot50.disconnect()
    except Exception as e:
        pass
    try:
        Bot51.disconnect()
    except Exception as e:
        pass
    try:
        Bot52.disconnect()
    except Exception as e:
        pass
    try:
        Bot53.disconnect()
    except Exception as e:
        pass
    try:
        Bot54.disconnect()
    except Exception as e:
        pass
    try:
        Bot55.disconnect()
    except Exception as e:
        pass
    try:
        Bot56.disconnect()
    except Exception as e:
        pass
    try:
        Bot57.disconnect()
    except Exception as e:
        pass
    try:
        Bot58.disconnect()
    except Exception as e:
        pass
    try:
        Bot59.disconnect()
    except Exception as e:
        pass
    try:
        Bot60.disconnect()
    except Exception as e:
        pass
    try:
        Bot61.disconnect()
    except Exception as e:
        pass
    try:
        Bot62.disconnect()
    except Exception as e:
        pass
    try:
        Bot63.disconnect()
    except Exception as e:
        pass
    try:
        Bot64.disconnect()
    except Exception as e:
        pass
    try:
        Bot65.disconnect()
    except Exception as e:
        pass
    try:
        Bot66.disconnect()
    except Exception as e:
        pass
    try:
        Bot67.disconnect()
    except Exception as e:
        pass
    try:
        Bot68.disconnect()
    except Exception as e:
        pass
    try:
        Bot69.disconnect()
    except Exception as e:
        pass
    try:
        Bot70.disconnect()
    except Exception as e:
        pass
else:
    try:
        Bot1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot30.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot31.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot32.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot33.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot34.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot35.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot36.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot37.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot38.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot39.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot40.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot41.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot42.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot43.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot44.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot45.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot46.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot47.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot48.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot49.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot50.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot51.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot52.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot53.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot54.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot55.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot56.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot57.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot58.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot59.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot60.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot61.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot62.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot63.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot64.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot65.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot66.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot67.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot68.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot69.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Bot70.run_until_disconnected()
    except Exception as e:
        pass
