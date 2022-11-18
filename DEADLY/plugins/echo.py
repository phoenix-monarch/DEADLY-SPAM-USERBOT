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
from .sudo import SUDOERS

ECHO_LIST = []

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])





@Client.on_message(filters.user(SUDOERS) & filters.command(["addecho"], [".", "!", "/", ",", "+", "?"]))
async def gban(app: Client, message):
    blaze = await message.reply_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await blaze.edit("**reply to user for activating echo!**")
            return
    get_user = await app.get_users(user)
    elif int(get_user.id) in ECHO_LIST:
        await blaze.edit("echo already activated on this user.")
        return
    ECHO_LIST.append(get_user.id)
    await blaze.edit(f"**Successfully  Started echo on {get_user.first_name}!**")

@Client.on_message(filters.user(SUDOERS) & filters.command(["rmecho"], [".", "!", "/", ",", "+", "?"]))
async def recho(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.reply_text("**Reply to user for removing echo! **")
            return
    get_user = await app.get_users(user)
    ECHO_LIST.remove(get_user.id)
    await message.reply_text(f"**Echo has Been Removed from {get_user.first_name} !**")


@Client.on_message(filters.text)
async def check_and_del(app: Client, message):
    if not message:
        return
    try:
        if not message.from_user.id in ECHO_LIST:
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await message.reply_text(f"{message.text}")
    except:
        pass
