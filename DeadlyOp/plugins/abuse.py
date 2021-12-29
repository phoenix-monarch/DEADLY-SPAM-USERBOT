import asyncio
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from DeadlyOp import DEADLY, DEADLY2, DEADLY3, DEADLY4, DEADLY5 , DEADLY6, DEADLY7, DEADLY8, DEADLY9, DEADLY10, DEADLY11, DEADLY12, DEADLY13, DEADLY14, DEADLY15, DEADLY16, DEADLY17, DEADLY18, DEADLY19, DEADLY20, DEADLY21, DEADLY22, DEADLY23, DEADLY24, DEADLY25, DEADLY26, DEADLY27, DEADLY28, DEADLY29, DEADLY30, DEADLY31, DEADLY32, DEADLY33, DEADLY34, DEADLY35, DEADLY36, DEADLY37, DEADLY38, DEADLY39, DEADLY40, SUDO_USERS
from resources.data import DEADLYoeLX
from .. import CMD_HNDLR as hl
  
    
@DEADLY.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY2.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY3.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY4.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY5.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY6.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY7.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY8.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY9.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY10.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY11.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY12.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY13.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY14.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY15.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY16.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY17.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY18.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY19.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY20.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY21.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY22.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY23.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY24.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY25.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY26.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY27.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY28.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY29.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY30.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY31.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY32.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY33.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY34.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY35.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY36.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY37.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY38.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY39.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@DEADLY40.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
async def _(e):
    usage = "**Module Name = Abuse**\n\nCommand:\n\n .gali <Username of User>\n\nit will continuously abuse until you restart!!."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        DEADLYoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(DEADLYoeL) == 1:
            user = str(DEADLYoeL[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DEADLYoeLX:
                text = f"I can't abuse @DEADLYoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                name = f"[{c}](tg://user?id={g})"
                caption1 =f"{name} GAND FATT GYII KYA HIJRE KI OLAAD"
                caption2 =f"{name} **RANDI KE PILLLE**"
                caption3 =f" {name} 𝑪𝑯𝑯𝑯𝑯𝑯𝑼𝑼𝑼𝑼𝑼𝑫𝑫𝑫𝑫 𝑮𝒀𝑨𝑨𝑨𝑨𝑨𝑨𝑨 𝑳𝑶𝑽𝑽𝑽𝑽𝑽𝑫𝑫𝑬𝑬 𝑻𝑼𝑼𝑼𝑼"
                caption4 =f" {name} 𝕋𝕖𝕣𝕚 𝕄𝕒𝕒 𝕂𝕚 𝕏𝕙𝕠𝕥 𝕓𝕒𝕕𝕙𝕧𝕖"
                caption5 =f"{name} **ISKE MAAKI CHUTT LELO FREE FULL NIGHT**"
                caption6 =f" {name} __TERE MAAKI CHUTT MASTT SOFT SOFT HE__ 🤤"
                caption7 =f"# {name} TERE MAAKI CHUT ME MERAA LUNDD"
                caption8 =f"{name} **RAANDD KAA PILLAAA**"
                caption9 =f"{name} 𝙄𝙎𝙆𝙄 𝘽𝙃𝙀𝙉 𝙈𝙀𝙍𝘼 𝙇𝙐𝙉𝘿 𝘾𝙃𝙊𝙊𝙎𝙏𝙄𝙄 𝙃E"
                caption10 =f"{name} __AGAYA SWADH__"
                caption11 =f"{name} **TERI MAAA**"
                caption12 =f"**MERE SE**"
                caption13 =f"**Rozz CHUDTII**"
                caption14 =f"__Haiii__"
                caption15 =f"{name} TERE BHEN KO CHODU"
                caption16 =f"🆃🅰🅿🅰"
                caption17 =f"🆃🅰🅿"
                caption18 =f"🆃🅰🅿🅰"
                caption18 =f"🆃🅰🅿"
                caption20 =f"__NON STOP__"
                caption21 =f"{name} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗘 𝗟𝗨𝗡𝗗 𝗟𝗘 𝗡𝗔𝗖𝗛𝗧𝗜 𝗛𝗘"
                caption22 =f"🤤"
                caption23 =f"{name} __TERI MAA MST ARAAM DETI HE__🤤🤤"
                caption24 =f"{name} __KE BHEN KI CHUT LELO FULL NIGHT FREEE__"
                caption25 =f"{name} __KI BHEN RANDIII__"
                caption26 =f"{name} __ISKE BHEN MST MARI RANDI__ 🤤🤤"
                caption27 =f"😂🖕🤣"
                caption28 =f"😂"
                caption29 =f"__EK RUPAY KI PEPSI {name} KI NAANI SEXYY__"
                caption30 =f"{name} **ISKI BHEN MERI PERSONAL HE MENE BOHOT CHODAA HE USKO__ \n\n __DM {name} FOR PERSONAL RANDI__"
                fuk = e.chat_id
                async with e.client.action(fuk, "typing"):
                        await e.client.send_message(fuk, caption1)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption2)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption3)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption4)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption5)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption6)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption7)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption8)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption9)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption10)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption11)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption12)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption13)
                        await asyncio.sleep(0.4)
                        await e.client.send_message(fuk, caption14)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption15)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption16)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption17)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption18)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption19)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption20)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption21)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption22)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption23)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption24)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption25)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption26)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption27)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption28)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption29)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption30)
                        await asyncio.sleep(0.3)

        else:
             await e.reply(usage)
