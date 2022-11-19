import os
import sys
import asyncio
import re
from random import choice

from config import SUDOERS
from pyrogram import Client, filters
from pyrogram.types import Message
from resources.data import RAID, DEV, PROGROUPS


@Client.on_message(filters.user(SUDOERS) & filters.command(["raid"], [",", ".", "!", "/", "+", "?"]))
async def raid(app: Client, m:Message):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid [username] [count] \n\n.raid [reply to user] [count]\n\nCount must be a integer."     
    Deadly = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Deadly) == 2:
        username = str(Deadly[1]) 
        counter = int(Deadly[0])       
        if not counter:
          await e.reply_text(f"raid ammount not defined!")
          return
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_users(username)
        except:
           await m.reply_text("**Error:** User not found or is Deleted account!")
           return
      elif m.reply_to_message:
        counter = counter
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text(usage)
        return
      if int(m.chat.id) in PROGROUPS:
         await m.reply_text("**I cannot spam in deadly chats.**")
         return
      if int(user.id) in DEV:
         await m.reply_text("**I can't raid on my developer.**")
         return
      if int(user.id) in SUDOERS:         
         await m.reply_text("**This guy is a sudo users so i cannot raid.**")
         return
      mention = user.mention
      for _ in range(counter): 
         blaze = random.choice(RAID)
         spam = f"{mention} {blaze}"
         await app.send_message(m.chat.id, spam)
         await asyncio.sleep(0.8)


@Client.on_message(filters.user(SUDOERS) & filters.command(["raid"], [",", ".", "!", "/", "+", "?"]))
async def draid(app: Client, m:Message):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗠𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dmraid [username] [count] \n\n.dmraid [reply to user] [count]\n\nCount must be a integer."     
    Deadly = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Deadly) == 2:
        username = str(Deadly[1]) 
        counter = int(Deadly[0])       
        if not counter:
          await e.reply_text(f"raid ammount not defined!")
          return
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_chats(username)
        except:
           await m.reply_text("**Error:** User not found or is Deleted account!")
           return
      elif m.reply_to_message:
        counter = counter
        try:
           user = await app.get_chats(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text(usage)
        return
      if int(user.id) in DEV:
         await m.reply_text("**I can't raid on my developer.**")
         return
      if int(user.id) in SUDOERS:         
         await m.reply_text("**This guy is a sudo users so i cannot raid.**")
         return     
      for _ in range(counter): 
         blaze = random.choice(RAID)   
         await app.send_message(user, blaze)
         await asyncio.sleep(0.8)
