import os
import sys
import asyncio
import re
from random import choice

from DEADLY import *
from config import *
from pyrogram import Client, filters
from pyrogram.types import Message
from resources.data import *


#DELAYSPAM

@bot1.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot2.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot3.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot4.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot5.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot6.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot7.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot8.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot9.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
@bot10.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
async def delayspam(_, m:Message):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    Deadly = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Deadlysexy = Deadly[1:]
        if len(Deadlysexy) == 2:
            message = str(Deadlysexy[1])
            counter = int(Deadlysexy[0])
            sleeptime = float(Deadly[0]) 
            if int(m.chat.id) in PROGROUP:
            return await _.reply_text("**Sorry !! Cannot Spam in here.**")
            if m.reply_to_message:
               reply_to_id = m.reply_to_message.message_id
               for _ in range(counter):
                   await _.send_message(m.chat_id, message)
                   await asyncio.sleep(sleeptime)
               return
            for _ in range(counter):
                await _.send_message(m.chat_id, message)
                await asyncio.sleep(sleeptime)
        else:
            await m.reply_text(usage)
