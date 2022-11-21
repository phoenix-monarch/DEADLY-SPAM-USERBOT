import os

import re
import sys
from os import getenv
from resources.data import DEV
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()




API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
ALIVE_PIC = getenv("ALIVE_PIC", None)

#CLIENT SESSION

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
STRING8 = getenv("STRING_SESSION8", None)
STRING9 = getenv("STRING_SESSION9", None)
STRING10 = getenv("STRING_SESSION10", None)
OWNER_ID = int(getenv("OWNER_ID", "")) 
SUDO_USERS = getenv("SUDO_USER") 


"""
------------------------------DON'T EDIT AFTER THIS LINE---------------------------------------
"""

# CONVERTING STR TO INT

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list




# SUDO SETUP

SUDOERS = []

if SUDO_USERS:
    SUDOERS = make_int(SUDO_USERS)

DEVS = DEV
for i in DEVS:
    SUDOERS.append(i)
    SUDOERS.append(OWNER_ID)
