#DeadlyOp By @TheDEADLY

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from DeadlyOp.utils import load_plugins
import logging
from telethon import events
from . import DEADLY, DEADLY2, DEADLY3, DEADLY4, DEADLY5 , DEADLY6, DEADLY7, DEADLY8, DEADLY9, DEADLY10, DEADLY11, DEADLY12, DEADLY13, DEADLY14, DEADLY15, DEADLY16, DEADLY17, DEADLY18, DEADLY19, DEADLY20, DEADLY21, DEADLY22, DEADLY23, DEADLY24, DEADLY25, DEADLY26, DEADLY27, DEADLY28, DEADLY29, DEADLY30, DEADLY31, DEADLY32, DEADLY33, DEADLY34, DEADLY35, DEADLY36, DEADLY37, DEADLY38, DEADLY39, DEADLY40

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "DeadlyOp/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("🔥🔥 DEADLY Bot Spam Successfully deployed -! 🔥🔥")
print("Enjoy! Do visit @DEADLY_SPAM_BOT")

if len(argv) not in (1, 3, 4):
    try:
        DEADLY.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY2.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY3.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY4.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY5.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY6.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY7.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY8.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY9.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY10.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY11.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY12.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY13.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY14.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY15.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY16.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY17.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY18.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY19.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY20.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY21.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY22.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY23.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY24.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY25.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY26.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY27.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY28.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY29.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY30.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY31.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY32.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY33.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY34.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY35.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY36.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY37.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY38.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY39.disconnect()
    except Exception as e:
        pass
    try:
        DEADLY40.disconnect()
    except Exception as e:
        pass
else:
    try:
        DEADLY.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY30.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY31.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY32.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY33.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY34.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY35.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY36.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY37.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY38.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY39.run_until_disconnected()
    except Exception as e:
        pass
    try:
        DEADLY40.run_until_disconnected()
    except Exception as e:
        pass
