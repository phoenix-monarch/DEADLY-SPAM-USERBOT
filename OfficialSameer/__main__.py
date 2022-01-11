
import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from OfficialSameer.utils import load_plugins
import logging
from telethon import events
from . import SAM, SAM2, SAM3, SAM4, SAM5 , SAM6, SAM7, SAM8, SAM9, SAM10, SAM11, SAM12, SAM13, SAM14, SAM15, SAM16, SAM17, SAM18, SAM19, SAM20, SAM21, SAM22, SAM23, SAM24, SAM25, SAM26, SAM27, SAM28, SAM29, SAM30, SAM31, SAM32, SAM33, SAM34, SAM35, SAM36, SAM37, SAM38, SAM39, SAM40

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "OfficialSameer/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("🎉🎊🥳 Deadly Spam Bot  Successfully deployed 🥳🎊🎉")
print("Enjoy! Do visit @Deadly_Spam_Bot")

if len(argv) not in (1, 3, 4):
    try:
        SAM.disconnect()
    except Exception as e:
        pass
    try:
        SAM2.disconnect()
    except Exception as e:
        pass
    try:
        SAM3.disconnect()
    except Exception as e:
        pass
    try:
        SAM4.disconnect()
    except Exception as e:
        pass
    try:
        SAM5.disconnect()
    except Exception as e:
        pass
    try:
        SAM6.disconnect()
    except Exception as e:
        pass
    try:
        SAM7.disconnect()
    except Exception as e:
        pass
    try:
        SAM8.disconnect()
    except Exception as e:
        pass
    try:
        SAM9.disconnect()
    except Exception as e:
        pass
    try:
        SAM10.disconnect()
    except Exception as e:
        pass
    try:
        SAM11.disconnect()
    except Exception as e:
        pass
    try:
        SAM12.disconnect()
    except Exception as e:
        pass
    try:
        SAM13.disconnect()
    except Exception as e:
        pass
    try:
        SAM14.disconnect()
    except Exception as e:
        pass
    try:
        SAM15.disconnect()
    except Exception as e:
        pass
    try:
        SAM16.disconnect()
    except Exception as e:
        pass
    try:
        SAM17.disconnect()
    except Exception as e:
        pass
    try:
        SAM18.disconnect()
    except Exception as e:
        pass
    try:
        SAM19.disconnect()
    except Exception as e:
        pass
    try:
        SAM20.disconnect()
    except Exception as e:
        pass
    try:
        SAM21.disconnect()
    except Exception as e:
        pass
    try:
        SAM22.disconnect()
    except Exception as e:
        pass
    try:
        SAM23.disconnect()
    except Exception as e:
        pass
    try:
        SAM24.disconnect()
    except Exception as e:
        pass
    try:
        SAM25.disconnect()
    except Exception as e:
        pass
    try:
        SAM26.disconnect()
    except Exception as e:
        pass
    try:
        SAM27.disconnect()
    except Exception as e:
        pass
    try:
        SAM28.disconnect()
    except Exception as e:
        pass
    try:
        SAM29.disconnect()
    except Exception as e:
        pass
    try:
        SAM30.disconnect()
    except Exception as e:
        pass
    try:
        SAM31.disconnect()
    except Exception as e:
        pass
    try:
        SAM32.disconnect()
    except Exception as e:
        pass
    try:
        SAM33.disconnect()
    except Exception as e:
        pass
    try:
        SAM34.disconnect()
    except Exception as e:
        pass
    try:
        SAM35.disconnect()
    except Exception as e:
        pass
    try:
        SAM36.disconnect()
    except Exception as e:
        pass
    try:
        SAM37.disconnect()
    except Exception as e:
        pass
    try:
        SAM38.disconnect()
    except Exception as e:
        pass
    try:
        SAM39.disconnect()
    except Exception as e:
        pass
    try:
        SAM40.disconnect()
    except Exception as e:
        pass
else:
    try:
        SAM.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM30.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM31.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM32.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM33.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM34.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM35.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM36.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM37.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM38.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM39.run_until_disconnected()
    except Exception as e:
        pass
    try:
        SAM40.run_until_disconnected()
    except Exception as e:
        pass
