from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print(
    """DEADLY SPAM BOT"""
)

print("\n • Telethon Session •")

print("\n\nEnter Your Valid Details To Continue!\n\n")

        
APP_ID = int(input("\nEnter APP ID here: "))
API_HASH = input("\nEnter API HASH here: ")


try:
   with TelegramClient(StringSession(), APP_ID, API_HASH) as Deadly:
       print("\nSTRING SESSION GENERATE SUCCESSFULLY CHECK SAVED MASSAGE")
       Deadly.send_message("me", f"**Deadly X Spam Session :**\n\n`{Deadly.session.save()}`\n\n__Do not share this anywhere!!__")
       
except Exception as e:
    print(f"{e}")
