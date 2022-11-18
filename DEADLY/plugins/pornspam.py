import asyncio
import random
import asyncio
import time
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from resources.data import PORN, PROGROUPS
from .sudo import SUDOERS

@Client.on_message(filters.user(SUDOERS) & filters.command(["pornspam", "pspam"], [".", "!", "/"]))
async def prd(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("`You Cannot Pornspam In Deadly Chats!`")
        return    
    for _ in range(quantity):
        try: 
            file = random.choice(PORN) 
            await client.send_video(chat_id=message.chat.id, video=file)       
        except FloodWait as e:
            await asyncio.sleep(e.x)
