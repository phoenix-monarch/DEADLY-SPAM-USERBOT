from pyrogram import filters
from sys import version_info
from pyrogram import Client
from pyrogram.types import Message
from config import *
from .sudo import SUDOERS



@Client.on_message(filters.user(SUDOERS) & filters.command(["help", "cmds"], [".", "!", "/", ",", "+", "?"]))
async def help(client, m: Message):
   await client.reply_text("**go to @deadly_spam_bot for command list**") 
