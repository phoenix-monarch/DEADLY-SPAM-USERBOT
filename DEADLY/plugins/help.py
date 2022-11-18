from pyrogram import filters
from sys import version_info
from pyrogram import Client
from pyrogram.types import Message
from config import *

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

↧ ʀᴀɪᴅ 𝙲𝙼𝙳𝚂 ↧
 
 !raid - to raid
 !replyraid - to active reply raid
 !dreplyraid - to de-active reply raid

↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧

 !spam - this cmd use for Normal spam
 !sspam - this cmd use for sticker spam

 !pornspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧

© @TheDeadlyBots

"""

@Client.on_message(filters.user(SUDOERS) & filters.command(["help", "cmds"], [".", "!", "/", ",", "+", "?"]))
async def alive(client, m: Message):
   await client.reply_photo(photo=ALIVE_PIC, caption=HELP_TXT) 
