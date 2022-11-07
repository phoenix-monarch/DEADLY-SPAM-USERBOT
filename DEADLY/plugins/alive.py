from pyrogram import filters, Client
from pyrogram.types import *

@Client.on_message(filters.command(["alive", "start"],["!", "/", ",", ".") & filters.SUDOERS)
async def alive(client: Client, message: Message):
       alive = """
A
B
C
"""
       pics = random.choice(PICS) 
       await message.reply_photo(photo=pics, caption=alive) 
