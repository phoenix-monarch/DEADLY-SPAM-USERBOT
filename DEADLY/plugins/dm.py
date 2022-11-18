from pyrogram import filters, Client
from pyrogram.types import *
from DEADLY import *
from resources.data import DEV, PROGROUPS

DM_TXT = """
𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗺


Command:

.dm <user name> <dm-text>

.dm <reply to a message> <dm-text>

Sender must be SUDOERS .
"""

@Client.on_message(filters.user(SUDOERS) & filters.command(["dm", "ib"], [".", "!", "/"]))
async def dmm(client: Client, message: Message):
    blaze = await message.reply_text(DM_TXT)
    quantity = 1
    inp = message.text.split(None, 2)[1]
    user = await client.get_chat(inp)
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if int(user.id) in DEV:
       await blaze.edit("<b>Bhsdk 😂 Creator hai wo is source ka usko pelega tu? </b>") 
       return
 
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await blaze.edit("**Inbox Sent Successfully 🌚**")
            await client.send_message(user.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(user.id, spam_text)
        await blaze.edit("Message Delivered Successfully ✅")
        await asyncio.sleep(0.15)

