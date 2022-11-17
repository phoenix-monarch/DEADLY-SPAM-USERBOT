from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("join", ".") & filters.me)
async def join(client: Client, message: Message):
    blaze = message.text[6:]
    count = 0
    if not blaze:
        return await message.reply_text("Need a chat username or invite link to join.")
    if blaze.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(blaze)
        await message.reply_text(f"**Spammers Successfully Joined The Chat 🥱**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")

@Client.on_message(filters.command("leave", ".") & filters.me)
async def leave(client: Client, message: Message):
    blaze = message.text[6:]
    count = 0
    if not blaze:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if blaze.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:        
        await message.reply_text(f"**Spammers Successfully Left The Chat**")
        await client.leave_chat(blaze)
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")

