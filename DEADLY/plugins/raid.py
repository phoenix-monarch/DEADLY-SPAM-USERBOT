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
from DEADLY import SUDOERS

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

