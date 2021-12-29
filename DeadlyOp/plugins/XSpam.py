async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from DeadlyOp import DEADLY, DEADLY2, DEADLY3, DEADLY4, DEADLY5 , DEADLY6, DEADLY7, DEADLY8, DEADLY9, DEADLY10, DEADLY11, DEADLY12, DEADLY13, DEADLY14, DEADLY15, DEADLY16, DEADLY17, DEADLY18, DEADLY19, DEADLY20, DEADLY21, DEADLY22, DEADLY23, DEADLY24, DEADLY25, DEADLY26, DEADLY27, DEADLY28, DEADLY29, DEADLY30, DEADLY31, DEADLY32, DEADLY33, DEADLY34, DEADLY35, DEADLY36, DEADLY37, DEADLY38, DEADLY39, DEADLY40, SUDO_USERS
from .. import CMD_HNDLR as hl
from resources.data import DeadlyHeHeX


# spam

@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        DeadlyHeHe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(DeadlyHeHe) == 2:
            message = str(DeadlyHeHe[1])
            counter = int(DeadlyHeHe[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(DeadlyHeHe[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(DeadlyHeHe[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


#bigspam

@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        DeadlyHeHe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(DeadlyHeHe) == 2:
            message = str(DeadlyHeHe[1])
            counter = int(DeadlyHeHe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(DeadlyHeHe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(DeadlyHeHe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#delayspam

@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        DeadlyHeHe = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        DeadlySpamBot = DeadlyHeHe[1:]
        if len(DeadlySpamBot) == 2:
            message = str(DeadlySpamBot[1])
            counter = int(DeadlySpamBot[0])
            sleeptime = float(DeadlyHeHe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(DeadlySpamBot[0])
            sleeptime = float(DeadlyHeHe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(DeadlySpamBot[0])
            sleeptime = float(DeadlyHeHe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

#abuse

@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **DM Spam**\n\nCommand:\n\n.dmspam <count> <username> <message to spam>\n\n.dmspam <count> <username> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        DeadlyHeHe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 2)
        DeadlySpamBot = DeadlyHeHe[1:]
        smex = await e.get_reply_message()
        if len(DeadlySpamBot) == 2:
            user = str(DeadlySpamBot[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DeadlyHeHeX:
                text = f"I can't Dm To @OFFICIAL_SAMEER's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(DeadlySpamBot[1])
                counter = int(DeadlyHeHe[0])
                await e.reply("☢️ Dm Spam Started ☢️")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            user = str(DeadlySpamBot[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DeadlyHeHeX:
                text = f"I can't Dm To @OFFICIAL_SAMEER's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:           
                 counter = int(DeadlyHeHe[0])
                 await e.reply("☢️ Dm Spam Started ☢️")
                 for _ in range(counter):
                     async with e.client.action(g, "document"):
                        smex = await e.client.send_file(g, smex, caption=smex.text)
                        await gifspam(e, smex) 
                        await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            user = str(DeadlySpamBot[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DeadlyHeHeX:
                text = f"I can't Dm To @OFFICIAL_SAMEER's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(DeadlyHeHe[0])
                await e.reply("☢️ Dm Spam Started ☢️")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )       

