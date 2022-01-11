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
from OfficialSameer import SAM, SAM2, SAM3, SAM4, SAM5 , SAM6, SAM7, SAM8, SAM9, SAM10, SAM11, SAM12, SAM13, SAM14, SAM15, SAM16, SAM17, SAM18, SAM19, SAM20, SAM21, SAM22, SAM23, SAM24, SAM25, SAM26, SAM27, SAM28, SAM29, SAM30, SAM31, SAM32, SAM33, SAM34, SAM35, SAM36, SAM37, SAM38, SAM39, SAM40, SUDO_USERS
from .. import CMD_HNDLR as hl
from resources.data import DEADLYSPAM


# spam

@SAM.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@SAM20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Deadly) == 2:
            message = str(Deadly[1])
            counter = int(Deadly[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Deadly[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Deadly[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


#bigspam

@SAM.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@SAM20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Deadly) == 2:
            message = str(Deadly[1])
            counter = int(Deadly[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(Deadly[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Deadly[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#delayspam

@SAM.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@SAM20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Deadly = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
         = Deadly[1:]
        if len(Deadlysexy) == 2:
            message = str(Deadlysexy[1])
            counter = int(Deadlysexy[0])
            sleeptime = float(Deadly[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Deadlysexy[0])
            sleeptime = float(Deadly[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Deadlysexy[0])
            sleeptime = float(Deadly[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

#abuse

@SAM.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM11.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM12.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM13.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM14.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM15.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM16.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM17.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM18.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM19.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@SAM20.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **DM Spam**\n\nCommand:\n\n.dmspam <count> <username> <message to spam>\n\n.dmspam <count> <username> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 2)
        Deadlysexy = Deadly[1:]
        smex = await e.get_reply_message()
        if len(Deadlysexy) == 2:
            user = str(Deadlysexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DEADLYSPAM:
                text = f"I can't Dm To @DEADLY_SPAMMER's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(Deadlysexy[1])
                counter = int(Deadly[0])
                await e.reply("☢️ Dm Spam Started ☢️")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            user = str(Deadlysexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DEADLYSPAM:
                text = f"I can't Dm To @DEADLY_SPAMMER's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:           
                 counter = int(Deadly[0])
                 await e.reply("☢️ Dm Spam Started ☢️")
                 for _ in range(counter):
                     async with e.client.action(g, "document"):
                        smex = await e.client.send_file(g, smex, caption=smex.text)
                        await gifspam(e, smex) 
                        await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            user = str(Deadlysexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DEADLYSPAM:
                text = f"I can't Dm To @Deadly_SpamMER's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(Deadly[0])
                await e.reply("☢️ Dm Spam Started ☢️")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )       

