import random
import asyncio
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from resources.data import Deadly_Spam_Bot, RAID
from DeadlyOp import DEADLY, DEADLY2, DEADLY3, DEADLY4, DEADLY5 , DEADLY6, DEADLY7, DEADLY8, DEADLY9, DEADLY10, DEADLY11, DEADLY12, DEADLY13, DEADLY14, DEADLY15, DEADLY16, DEADLY17, DEADLY18, DEADLY19, DEADLY20, DEADLY21, DEADLY22, DEADLY23, DEADLY24, DEADLY25, DEADLY26, DEADLY27, DEADLY28, DEADLY29, DEADLY30, DEADLY31, DEADLY32, DEADLY33, DEADLY34, DEADLY35, DEADLY36, DEADLY37, DEADLY38, DEADLY39, DEADLY40, SUDO_USERS
from .. import CMD_HNDLR as hl


@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY21.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY22.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY23.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY24.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY25.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY26.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY27.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY28.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY29.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY30.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY31.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY32.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY33.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY34.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY35.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY36.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY37.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY38.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY39.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@DEADLY40.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
async def _(e):   
    usage = "**MODULE NAME** : **DM**\n\n command: \n\n .dm <username> <massage> \n .dm <reply to the use> <massage>"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        DEADLYoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(DEADLYoeL) == 2:
            user = str(DEADLYoeL[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in Deadly_Spam_Bot:
                text = f"I can't Dm to @Deadly_Spam_Bot's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:            
                 message = str(DEADLYoeL[1])
                 await e.reply("🔸Message Delivered🔸")
                 await e.client.send_message(g, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in Deadly_Spam_Bot:
                text = f"I can't Dm to @Deadly_Spam_Bot's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(DEADLYoeL[0])
                await e.reply("🔸 Message Delivered 🔸")
                await e.client.send_message(g, message)
                await asyncio.sleep(0.3)

        else:
             await e.reply(usage)


@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY21.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY22.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY23.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY24.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY25.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY26.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY27.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY28.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY29.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY30.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY31.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY32.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY33.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY34.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY35.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY36.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY37.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY38.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY39.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@DEADLY40.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
async def dmraid(e):
    usage = "**MODULE NAME** : **DM RAID**\n\n command: \n\n .dmraid <count> <username> \n .dmraid <reply to the use> <massage>"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        DEADLYoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(DEADLYoeL) == 2:
            user = str(DEADLYoeL[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in Deadly_Spam_Bot:
                text = f"I can't raid on @Deadly_Spam_Bot's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(DEADLYoeL[0])
                await e.reply("⚜️ Dm Raid Strated Successfully ⚜️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, caption)
                        await asyncio.sleep(0.4)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in Deadly_Spam_Bot:
                text = f"I can't raid on @Deadly_Spam_Bot's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(DEADLYoeL[0])
                await e.reply("⚜️ Dm Raid Strated Successfully!! ⚜️")
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{reply}"
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)
