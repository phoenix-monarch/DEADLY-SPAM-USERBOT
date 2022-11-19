from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from pyrogram.types import *
from DEADLY import *
from resources.data import DEV, PROGROUPS, RAID
from .sudo import SUDOERS



@Client.on_message(filters.user(SUDOERS) & filters.command(["dm", "ib"], [".", "!", "/"]))
async def dmm(client: Client, message: Message):
    blaze = await message.reply_text("Processing...")
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



@Client.on_message(filters.user(SUDOERS) & filters.command(["draid", "inraid"], [".", "!", "/"]))
async def dmm(client: Client, message: Message):
    blaze = await message.reply_text("Processing...")
    inp = message.text.split(None, 2)[1]
    user = await client.get_chat(inp)
    quantity = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if int(user.id) in DEV:
       await blaze.edit("<b>Bhsdk 😂 Creator hai wo is source ka usko pelega tu? </b>") 
       return
 
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id        
        for _ in range(quantity):
            try:
                spam_text = random.choice(RAID) 
                await client.send_message(user.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            except FloodWait as e:
                await asyncio.sleep(e.x) 
        return

    for _ in range(quantity):
        try:
            spam_text = random.choice(RAID) 
            await client.send_message(user.id, spam_text)
        except FloodWait as e:
            await asyncio.sleep(e.x)
