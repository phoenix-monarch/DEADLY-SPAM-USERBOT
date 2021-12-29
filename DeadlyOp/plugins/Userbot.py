# DEADLYOP X Spam - Spam Userbots
# © 2021 - 2022 - TheDEADLYOP

import os
import sys
from DeadlyOp import DEADLY, DEADLY2, DEADLY3, DEADLY4, DEADLY5 , DEADLY6, DEADLY7, DEADLY8, DEADLY9, DEADLY10, DEADLY11, DEADLY12, DEADLY13, DEADLY14, DEADLY15, DEADLY16, DEADLY17, DEADLY18, DEADLY19, DEADLY20, DEADLY21, DEADLY22, DEADLY23, DEADLY24, DEADLY25, DEADLY26, DEADLY27, DEADLY28, DEADLY29, DEADLY30, DEADLY31, DEADLY32, DEADLY33, DEADLY34, DEADLY35, DEADLY36, DEADLY37, DEADLY38, DEADLY39, DEADLY40, SUDO_USERS
from DeadlyOp import ALIVE_PIC, DEADLYversion
from .. import CMD_HNDLR as hl
from telethon import events, version
from time import time
from datetime import datetime

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY21.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY22.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY23.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY24.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY25.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY26.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY27.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY28.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY29.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY30.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY31.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY32.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY33.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY34.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY35.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY36.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY37.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY38.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY39.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@DEADLY40.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        if e.reply_to_msg_id:
            fuk = await e.respond("Pᴏɴɢ!!.....", reply_to=e.reply_to_msg_id)
        else:
            fuk = await e.reply("Pᴏɴɢ!!.....")
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        pingop = f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\nϟ Dᴇᴀᴅʟʏ sᴘᴀᴍ ϟ︎ `{ms}` ᴍs"                   
        await fuk.edit(pingop)


# ALIVE

DEADLY_PIC = ALIVE_PIC if ALIVE_PIC else ""


DEADLYOP = "✧ 𝗗𝗲𝗮𝗱𝗹𝘆 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲 ✧\n\n"

DEADLYOP += f"┏━━━━━━━━━━━━━━━━━━━\n"

DEADLYOP += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

DEADLYOP += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

DEADLYOP += f"┣➣ **Dᴇᴅᴀᴅʟʏ ᴠᴇʀsɪᴏɴ**  : `{DEADLYOPversion}`\n"
    
DEADLYOP += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/DEADLY_SPAM_BOT)\n"

DEADLYOP += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/DEADLY_SPAMMER)\n"

DEADLYOP += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

DEADLYOP += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/DEADLY-FIGHTERS/DEADLY_SPAM_BOT) 🖤"            
                                    
@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%salive" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await DEADLY.send_file(event.chat_id,
                                  DEADLY_PIC,
                                  caption=DEADLYOP)
   
   
# help

HELP_PIC = " "

DEADLYOPX = "🔥 𝗗𝗘𝗔𝗗𝗟𝗬 𝗦𝗣𝗔𝗠 🔥\n\n"
 
DEADLYOPX += f"__ᴄᴍᴅs Aᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅᴇᴀᴅʟʏ sᴘᴀᴍ Bᴏᴛ__\n\n"

DEADLYOPX += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

DEADLYOPX += f" `.ping` - `.alive` - `.setname` - `.setbio` - `.inviteall` - .`restart` - `.update` - `.stats` - `.addsudo` \n\n"
 
DEADLYOPX += fn\n"

DEADLYOPX += f" `.join` - `.pjoin` - `.leave`\n\n"
 
DEADLYOPX += f" ↧ 𝚂𝙿𝙰𝙼 / 𝚁𝙰𝙸𝙳 𝙲𝙼𝙳𝚂 ↧\n\n"

DEADLYOPX += f" `.raid` - `.replyraid` - `.dreplyraid` - `.delayraid` \n\n `.spam` - `.bigspam` - `.delayspam` - `.abuse` \n\n"

DEADLYOPX += f" 𝙳𝙼 / 𝙴𝚌𝚑𝚘 𝙲𝚖𝚍𝚜 \n\n"

DEADLYOPX += f" `.dm` - `.dmraid` - `.dmspam` \n\n `.addecho` - `.rmecho` \n\n"

DEADLYOPX += f"All Cmds Uploaded : [•HERE•](https://t.me/Resourcez/4) \n\n"
 
DEADLYOPX += f"© @DEADLY_SPAMMER |@DEADLY_SPAM_BOT\n"


@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await DEADLY.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DEADLYOPX)                                                         


@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY21.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY22.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY23.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY24.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY25.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY26.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY27.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY28.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY29.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY30.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY31.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY32.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY33.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY34.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY35.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY36.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY37.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY38.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY39.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@DEADLY40.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "𝙍𝙀𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂\n\n ....Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await DEADLY.disconnect()
        except Exception:
            pass
        try:
            await DEADLY2.disconnect()
        except Exception:
            pass
        try:
            await DEADLY3.disconnect()
        except Exception:
            pass
        try:
            await DEADLY4.disconnect()
        except Exception:
            pass
        try:
            await DEADLY5.disconnect()
        except Exception:
            pass
        try:
            await DEADLY6.disconnect()
        except Exception:
            pass
        try:
            await DEADLY7.disconnect()
        except Exception:
            pass
        try:
            await DEADLY8.disconnect()
        except Exception:
            pass
        try:
            await DEADLY9.disconnect()
        except Exception:
            pass
        try:
            await DEADLY10.disconnect()
        except Exception:
            pass
        try:
            await DEADLY11.disconnect()
        except Exception:
            pass
        try:
            await DEADLY12.disconnect()
        except Exception:
            pass
        try:
            await DEADLY13.disconnect()
        except Exception:
            pass
        try:
            await DEADLY14.disconnect()
        except Exception:
            pass
        try:
            await DEADLY15.disconnect()
        except Exception:
            pass
        try:
            await DEADLY16.disconnect()
        except Exception:
            pass
        try:
            await DEADLY17.disconnect()
        except Exception:
            pass
        try:
            await DEADLY18.disconnect()
        except Exception:
            pass
        try:
            await DEADLY19.disconnect()
        except Exception:
            pass
        try:
            await DEADLY20.disconnect()
        except Exception:
            pass
        try:
            await DEADLY21.disconnect()
        except Exception:
            pass
        try:
            await DEADLY22.disconnect()
        except Exception:
            pass
        try:
            await DEADLY23.disconnect()
        except Exception:
            pass
        try:
            await DEADLY24.disconnect()
        except Exception:
            pass
        try:
            await DEADLY25.disconnect()
        except Exception:
            pass
        try:
            await DEADLY26.disconnect()
        except Exception:
            pass
        try:
            await DEADLY27.disconnect()
        except Exception:
            pass
        try:
            await DEADLY28.disconnect()
        except Exception:
            pass
        try:
            await DEADLY29.disconnect()
        except Exception:
            pass
        try:
            await DEADLY30.disconnect()
        except Exception:
            pass
        try:
            await DEADLY31.disconnect()
        except Exception:
            pass
        try:
            await DEADLY32.disconnect()
        except Exception:
            pass
        try:
            await DEADLY33.disconnect()
        except Exception:
            pass
        try:
            await DEADLY34.disconnect()
        except Exception:
            pass
        try:
            await DEADLY35.disconnect()
        except Exception:
            pass
        try:
            await DEADLY36.disconnect()
        except Exception:
            pass
        try:
            await DEADLY37.disconnect()
        except Exception:
            pass
        try:
            await DEADLY38.disconnect()
        except Exception:
            pass
        try:
            await DEADLY39.disconnect()
        except Exception:
            pass
        try:
            await DEADLY40.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
