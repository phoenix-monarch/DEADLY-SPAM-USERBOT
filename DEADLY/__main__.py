import config
import asyncio
from pyrogram import idle
from DEADLY import bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10

OWNER_ID = "ELRIC_XD"

async def main():
    await bot1.start() 
    await bot1.join_chat("Deadly_spam_bot") 
    await bot1.join_chat("deadly_spambot") 
    await bot1.send_message(
            OWNER_ID, 
            "<b> Congrats!! DeadlySpam [1] Started Successfully!</b>", 
        ) 
    if bot2:
       await bot2.start() 
       await bot2.join_chat("Deadly_spam_bot") 
       await bot2.join_chat("deadly_spambot") 
       await bot2.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [2] Started Successfully!</b>", 
           )
    if bot3:
       await bot3.start() 
       await bot3.join_chat("Deadly_spam_bot") 
       await bot3.join_chat("deadly_spambot") 
       await bot3.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [3] Started Successfully!</b>", 
           )
    if bot4:
       await bot4.start() 
       await bot4.join_chat("Deadly_spam_bot") 
       await bot4.join_chat("deadly_spambot") 
       await bot4.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [4] Started Successfully!</b>", 
               )
    if bot5:
       await bot5.start() 
       await bot5.join_chat("Deadly_spam_bot") 
       await bot5.join_chat("deadly_spambot") 
       await bot5.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [5] Started Successfully!</b>", 
           )
    if bot6:
       await bot6.start() 
       await bot6.join_chat("Deadly_spam_bot") 
       await bot6.join_chat("deadly_spambot") 
       await bot6.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [6] Started Successfully!</b>", 
           )
    if bot7:
       await bot7.start() 
       await bot7.join_chat("Deadly_spam_bot") 
       await bot7.join_chat("deadly_spambot") 
       await bot7.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [7] Started Successfully!</b>", 
           )
    if bot8:
       await bot8.start() 
       await bot8.join_chat("Deadly_spam_bot") 
       await bot8.join_chat("deadly_spambot") 
       await bot8.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [8] Started Successfully!</b>", 
           )
    if bot9:
       await bot9.start() 
       await bot9.join_chat("Deadly_spam_bot") 
       await bot9.join_chat("deadly_spambot") 
       await bot9.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [9] Started Successfully!</b>", 
           )
    if bot10:
       await bot10.start() 
       await bot10.join_chat("Deadly_spam_bot") 
       await bot10.join_chat("deadly_spambot") 
       await bot10.send_message(
               OWNER_ID, 
               "<b> Congrats!! DeadlySpam [10] Started Successfully!</b>", 
           )
    await idle()


print("Your DeadlySpam Userbot Deployed Successfully 🥳 Please visit @deadly_spam_bot for any help!") 


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
