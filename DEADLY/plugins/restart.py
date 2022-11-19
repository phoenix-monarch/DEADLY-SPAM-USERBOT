import os
import shutil
import asyncio
from git import Repo
from config import SUDOERS
from pyrogram.types import Message
from pyrogram import filters, Client
from git.exc import GitCommandError, InvalidGitRepositoryError

@Client.on_message(filters.user(SUDOERS) & filters.command(["restart", "reboot"], ["."]))
async def restart(client, m: Message):
    reply = await m.reply_text("Restarting....")     
    await m.delete() 
    await reply.edit(
        "<b>Reboot has been initiated successfully! Wait for 1 - 2 minutes until the bot restarts.</b>"
    )
    os.system(f"kill -9 {os.getpid()} && bash start")
