import os
import sys
import asyncio
import re
from random import choice

from DEADLY import *
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
    semx = Deadly[1:]
    if len(semx) == 2:
       quantity = int(semx[0])
       if int(m.chat.id) PROGROUPS:
            return await e.reply_text("You Cannot Spam in Deadly Chats! **")
       Spam_txt = str(semx[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply_text("**You Cannot Spam on Developer**")
       limit = float(Deadly[0])
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          blaze = await client.send_message(LOG_GRP, f"DelaySpam Is Being Used in {m.chat.id}") 
          for _ in range(quantity):
              await client.send_message(m.chat.id, Spam_txt, reply_to_message_id=reply_to_id)
              await asyncio.sleep(limit)
          return
       for _ in range(quantity):
           await client.send_message(m.chat.id, Spam_txt)
           await asyncio.sleep(limit)
       except Exception as a:
           error = f"𝙳𝙴𝙰𝙳𝙻𝚈 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙴𝚁𝚁𝙾𝚁 𝙵𝙾𝚄𝙽𝙳\n\n {a} \n\n 𝙿𝙻𝙴𝙰𝚂𝙴 𝚁𝙴𝙿𝙾𝚁𝚃 𝚃𝙾 @DEADLY_SPAM_BOT"
           await client.send_message(LOG_GRP, error)             
             pass

