import asyncio
import random
import asyncio
import time

from typing import Tuple
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters, Client
from resources.data import REPLYRAID as RAID, DEV, PROGROUPS
from DEADLY import SUDOERS
from traceback import format_exc
from typing import Tuple


#LOCAL DB STORAGE

ACTIVATE_LIST = []

# CREATE LMK

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


#REPLYRAID
@Client.on_message(filters.user(SUDOERS) & filters.command(["replyraid", "rraid"], [".", "!"]))
async def gban(app: Client, message):
    elric= await message.reply_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await elric.edit("**Provide Me A USER_ID or reply to someone**")
            return
    get_user = await app.get_users(user)
    if int(message.chat.id) in PROGROUPS:
        await elric.edit("`You Cannnot Spam In DeadlyChats`")
        return
    if int(get_user.id) in DEV:
        await elric.edit("You Cannot Spam On Developers")
        return
    elif int(get_user.id) in SUDOERS:
        await elric.edit("That Guy Is part of sudo user.")
        return
    elif int(get_user.id) in ACTIVATE_LIST:
        await elric.edit("User Already in Raidlist.")
        return
    ACTIVATE_LIST.append(get_user.id)
    await elric.edit(f"**Replyraid Activated On {get_user.first_name} Successfully ✅**")



#DREPLYRAID

@Client.on_message(filters.user(SUDOERS) & filters.command(["dreplyraid", "drraid"], [".", "!"]))
async def gbam(app: Client, message):
    elric= await message.reply_text("**Processing**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await elric.edit("Provide me username/userid or reply to user for deactivating replyraid")
            return
    get_user = await app.get_users(user)
    if int(get_user.id) not in ACTIVATE_LIST:
        await elric.edit("User Not in Replyraid db.")
        return
    ACTIVATE_LIST.remove(get_user.id)
    await elric.edit(f"**Reply Raid has Been Removed {get_user.first_name}, enjoy!**")






#WATCHER

@Client.on_message(filters.all)
async def check_and_del(app: Client, message):
    if not message:
        return
    if int(message.chat.id) in PROGROUPS:
        return
    try:
        if not message.from_user.id in ACTIVATE_LIST:
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await message.reply_text(f"{random.choice(RAID)}")
    except:
        pass
