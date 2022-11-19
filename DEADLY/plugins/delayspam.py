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

@Client.on_message(filters.user(SUDOERS) & filters.command(["delayspam"], [",", ".", "!", "/", "+", "?"]))
async def delayspam(app: Client, m:Message):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam [sleep time] [count] [message to spam] \n\n.delayspam [sleep time] [count] [reply to a message]\n\nCount and Sleeptime must be a integer."     
    Deadly = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
    Deadlysexy = Deadly[1:]
    if len(Deadlysexy) == 2:
        message = str(Deadlysexy[1])
        counter = int(Deadlysexy[0])
        sleeptime = float(Deadly[0]) 
        if int(m.chat.id) in PROGROUPS:
           await app.reply_text("**Sorry !! cannot spam in deadly chats**")
           return
        if int(m.chat.id) in DEV:
           await app.reply_text("**sorry !! I cannot spam on my developer**")
           return
        if int(m.chat.id) in SUDOERS:
           await app.reply_text("**this guy is bot owner or sudouser so i cannot act against him**")           
           return
        if m.reply_to_message:
           reply_to_id = m.reply_to_message.message_id
           for _ in range(counter):
               await app.send_message(m.chat.id, message)
               await asyncio.sleep(sleeptime)
           return
        for _ in range(counter):
            await app.send_message(m.chat.id, message)
            await asyncio.sleep(sleeptime)
    else:
        await m.reply_text(usage)



@Client.on_message(filters.user(SUDOERS) & filters.command(["spam"], [",", ".", "!", "/", "+", "?"]))
async def delayspam(app: Client, m:Message):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam [count] [message to spam] \n\n.spam [count] [reply to a message]\n\nCount must be a integer."     
    Deadly = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
    Deadlysexy = Deadly[1:]
    if len(Deadlysexy) == 2:
        message = str(Deadlysexy[1])
        counter = int(Deadlysexy[0])
        sleeptime = 2
        if int(m.chat.id) in PROGROUPS:
           await app.reply_text("**Sorry !! cannot spam in deadly chats**")
           return
        if int(m.chat.id) in DEV:
           await app.reply_text("**sorry !! I cannot spam on my developer**")
           return
        if int(m.chat.id) in SUDOERS:
           await app.reply_text("**this guy is bot owner or sudouser**")           
           return
        if m.reply_to_message:
           reply_to_id = m.reply_to_message.message_id
           for _ in range(counter):
               await app.send_message(m.chat.id, message)
               await asyncio.sleep(sleeptime)
           return
        for _ in range(counter):
            await app.send_message(m.chat.id, message)
            await asyncio.sleep(sleeptime)
    else:
        await m.reply_text(usage)
