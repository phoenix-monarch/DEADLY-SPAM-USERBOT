import os
import shutil
import asyncio
from git import Repo
from DEADLY import SUDOERS
from pyrogram.types import Message
from pyrogram import filters, Client

@Client.on_message(filters.user(OWNER_ID) & filters.command(["shutdown"], ["."]))
async def restart(client, m: Message):
    reply = await m.reply_text("Restarting....")     
    await m.delete() 
    await reply.edit(
        "<b>Shutting Down You DeadlyUserbot.</b>"
    )
    await sys.exit() 
