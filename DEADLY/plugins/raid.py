import asyncio
import random
import asyncio
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from resources.data import RAID, PROGROUPS, DEV
from traceback import format_exc
from typing import Tuple
from .sudo import SUDOERS

@Client.on_message(filters.user(SUDOERS) & filters.command(["raid"], [".", "!", "/"]))
async def raid(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = message.command[2]
        if not user:
            await sex.edit("**REPLY TO USER OR PROVIDE USERNAME!**")
            return
    userz = await client.get_users(user)
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("**Sorry You Cannot Spam In Deadly Chats!**")
        return 
    if int(userz.id) in DEV:
        await sex.edit("**You Cannot Raid On My Developer lol🌚**")
        return
    for _ in range(quantity):
        try: 
            raid = random.choice(RAID) 
            blaze = f"[{userz.first_name}](tg://user?id={userz.id}) {raid}"
            await client.send_message(message.chat.id, blaze)         
        except FloodWait as e:
            await asyncio.sleep(e.x)



@Client.on_message(filters.user(SUDOERS) & filters.command(["spam", "spamming"], [".", "!", "/"]))
async def sspam(client: Client, message: Message):
    sex  = await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommands!\n\nspam <count> <message to spam>\n.spam <count> <reply to a message>\n\nCount must be a integer.")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await sex.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


#STICKERSPAM HANDLER
@Client.on_message(filters.user(SUDOERS) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return

    if int(message.chat.id) in PROGROUPS:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)


HELP_TXT = """
🔥 Dᴇᴀᴅʟʏ Sᴘᴀᴍ Usᴇʀʙᴏᴛ 🔥
ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅᴇᴀᴅʟʏ ʙᴏᴛ
 ↧ sᴘᴀᴍʙᴏᴛ 𝙲𝙼𝙳𝚂 ↧
 !ping - to check ping
 !alive - to check bot alive/version (only main userbot will reply)
 !restart - to restart all spam bots 
 !addecho - to addecho 
 !rmecho - To remove Echo 
 
 ↧ ᴊᴏɪɴ|𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳𝚂  ↧
 !join - to join public channel/groups
 !leave - to leave public channel/groups
↧ ᴅᴍ  ↧
 !dm - to inbox someone
 !draid - to raid in someone's inbox
↧ ʀᴀɪᴅ 𝙲𝙼𝙳𝚂 ↧↧
 
 !raid - to raid
 !replyraid - to active reply raid
 !dreplyraid - to de-active reply raid
↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧
 !spam - this cmd use for Normal spam
 !sspam - this cmd use for sticker spam
 !pornspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧
© @TheDeadlyBots
"""


@Client.on_message(filters.user(SUDOERS) & filters.command(["cmds"], [".", "!", "/"]))
async def hsk(client: Client, message: Message):
    quantity = 1
    sex = await message.reply_text("`Processing..`")
    quantity = int(quantity) 
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("**Sorry You Cannot Spam In Deadly Chats!**")
        return 
    for _ in range(quantity):
        try: 
            await sex.delete() 
            blaze = f"{HELP_TXT}"
            await client.send_message(message.chat.id, blaze)         
        except FloodWait as e:
            await asyncio.sleep(e.x)
