from dossier import HNDLR as hn
from dossier import OWNER_NAME, OWNER_ID, ALIVE_MESSAGE, ALIVE_MEDIA



spamusage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
devusage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help devcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴅᴇᴠ ᴄᴏᴍᴍᴀɴᴅs."
sudousage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help devcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs."
accusage = f"**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nUsᴇ: ```{hn}help devcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛ ᴄᴏᴍᴍᴀɴᴅs."

spam_menu = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**


**{hn}spam**: Spams a message for given counter(<= 100).
Syntax:
i) {hn}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hn}spam <count> <replying any message>

**{hn}bigspam**: Spams a message for given counter.
Syntax:
i) {hn}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hn}bigspam <count> <replying any message>

**{hn}uspam**: Spams a message for infinite counter.
Syntax:
i) {hn}uspam <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hn}uspam <replying any message>

**{hn}dspam**: Delay spam a text for given counter after given time.
Syntax:
i) {hn}dspam <delay time(seconds)> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hn}dspam <delay time(seconds)> <count> <replying any message>

**{hn}packspam**: Spams all stickers from sticker pack.
Syntax: 
i) {hn}packspam (replying to any sticker)

**{hn}hang**: Spams hanging message for given counter.
Syntax:
i) {hn}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

**©️ @DEADLY_FIGHTERS**
"""
curse_menu = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**


**{hn}curse:** Activates curse on any individual user for given range.
Syntax:
i) {hn}curse @Telegram <counter>
ii) {hn}curse 10 <replying to anyone>

**{hn}ucurse:** Activates curse on the user for infinite range.
Syntax:
i) {hn}ucurse @telegram
ii) {hn}ucurse <replying to anyone>

**{hn}multicurse:** Activates curse on many users for given range.
Syntax:
i) {hn}multicurse <counter> <username> <username> <username>...

**{hn}umulticurse:** Activates curse on many users for infinite range.
Syntax:
i) {hn}umulticurse <username> <username> <username>...

**{hn}replycurse:** Activates reply and curse on the user!!
Syntax:
i) {hn}replycurse <replying to anyone>
ii) {hn}dreplycurse <username>

**{hn}dreplycurse:** Deactivates reply and curse on the user!!
Syntax:
i) {hn}dreplycurse <replying to anyone>
ii) {hn}dreplycurse <username>


**©️ @DEADLY_FIGHTERS**
"""
sudo_menu = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**


**{hn}ping**: Check ping of the server.

**{hn}alive**: Check if bot is alive.


**©️ @DEADLY_FIGHTERS**
"""

dev_menu = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

**{hn}usage**: Check usage of the heroku server.

**{hn}logs**: Get last 100 lines of your heroku app logs

**{hn}leave**: Bot will leave that chat.
Syntax:
i) {hn}leave <chat id>
ii) {hn}leave

**{hn}reboot**: Restarts the bot!(Too fast! **Supersonic**)

**©️ @DEADLY_FIGHTERS**
"""


acc_menu = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**

**Note: bio/name/profilepic cmds can only accessed by dev users**

**{hn}bio**: Changes bio text of spam accounts.
Syntax:
i) {hn}bio <new bio>

**{hn}name**: Changes name of spam accounts.
Syntax:
i) {hn}name <new name>

**{hn}profilepic**: Changes display picture of spam accounts.
Syntax:
i) {hn}profilepic <replying to any pic>

**{hn}join**: Joins any public chat (channel/group).
Syntax:
i) {hn}join <Public chat's Link/Username>

**{hn}pjoin**: Joins any private chat (channel/group).
Syntax:
i) {hn}join <Private chat's hash>
Note: If all you have is a link like this one: https://t.me/joinchat/AAAAAFFszQPyPEZ7wgxLtd, The part after the https://t.me/joinchat/, this is, AAAAAFFszQPyPEZ7wgxLtd on this example, is the hash of the chat or channel.


**©️ @DEADLY_FIGHTERS**
"""


help_menu = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**


**There are following categories:**

**spamcmds**: Get all spam commands and its usage.

**cursecmds**: Get all curse commands and its usage

**sudocmds**: Get all sudo commands and its usage.

**devcmds**: Get all developer commands and its usage.

**acccmds**: Get all commands which can be used with accounts(not bots).

**Type {hn}help <category> to get all commands in that category and its usage.**
**Example**: ```{hn}help spamcmds```


**©️ @DEADLY_FIGHTERS**
"""

alive_temxt = f"""
🔥 {ALIVE_MESSAGE} 🔥

                  ↼𝙼𝙰𝚂𝚃𝙴𝚁⇀
          『 {OWNER_NAME} 』

╔═══════════════╗
╠•➳➠ Bᴏᴛ Vᴇʀsɪᴏɴ: 0.01
╠•➳➠ sᴜᴘᴘᴏʀᴛ:  [𝙹𝙾𝙸𝙽](t.me/deadly_spam_bot)
╠•➳➠ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: [𝙹𝙾𝙸𝙽](t.me/deadly_spammer)
╠•➳➠ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: [Sᴀᴍᴇᴇʀ](t.me/official_sameer)
╚═══════════════╝

[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙱𝙾𝚃 ✨](https://github.com/DEADLY-FIGHTERS/DEADLY-SPAM-BOT)
"""

deadly_logo = "https://telegra.ph/file/c05ad657651d56c5b80fc.jpg"


start_caption = f"""
**Nᴏᴡ ᴍᴇ ᴛᴏ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ.
I ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ-ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ!
I'ᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴇsᴛʀᴏʏ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ 🔥🔥🔥
I ᴄᴀɴ sᴘᴀᴍ ᴄᴏɴᴛɪɴᴜᴏsʟʏ ᴡɪᴛʜ ʟᴇss ғʟᴏᴏᴅ-ᴡᴀɪᴛ ᴇʀʀᴏʀ ᴀɴᴅ ᴡɪᴛʜ ᴍᴏʀᴇ ᴀᴄᴄᴜʀᴀᴄʏ!**

**█▓▒­░⡷⠂𝗠𝗔𝗦𝗧𝗘𝗥⠂⢾░▒▓█**
🔥 {ALIVE_MESSAGE} 🔥

                  ↼𝙼𝙰𝚂𝚃𝙴𝚁⇀
          『 {OWNER_NAME} 』

╔═══════════════╗
╠•➳➠ Bᴏᴛ Vᴇʀsɪᴏɴ: 0.01
╠•➳➠ sᴜᴘᴘᴏʀᴛ:  [𝙹𝙾𝙸𝙽](t.me/deadly_spam_bot)
╠•➳➠ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: [𝙹𝙾𝙸𝙽](t.me/deadly_spammer)
╠•➳➠ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: [Sᴀᴍᴇᴇʀ](t.me/official_sameer)
╚═══════════════╝

[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙱𝙾𝚃 ✨](https://github.com/DEADLY-FIGHTERS/DEADLY-SPAM-BOT)
"""



start_caption1 = f"""
**Nᴏᴡ ᴍᴇ ᴛᴏ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ.
I ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ-ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ!
I'ᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴇsᴛʀᴏʏ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ 🔥🔥🔥
I ᴄᴀɴ sᴘᴀᴍ ᴄᴏɴᴛɪɴᴜᴏsʟʏ ᴡɪᴛʜ ʟᴇss ғʟᴏᴏᴅ-ᴡᴀɪᴛ ᴇʀʀᴏʀ ᴀɴᴅ ᴡɪᴛʜ ᴍᴏʀᴇ ᴀᴄᴄᴜʀᴀᴄʏ!**

**█▓▒­░⡷⠂𝗠𝗔𝗦𝗧𝗘𝗥⠂⢾░▒▓█**
🔥 {ALIVE_MESSAGE} 🔥

                  ↼𝙼𝙰𝚂𝚃𝙴𝚁⇀
          『 OWNER_NAME 』

╔═══════════════╗
╠•➳➠ Bᴏᴛ Vᴇʀsɪᴏɴ: 0.01
╠•➳➠ sᴜᴘᴘᴏʀᴛ:  [𝙹𝙾𝙸𝙽](t.me/deadly_spam_bot)
╠•➳➠ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: [𝙹𝙾𝙸𝙽](t.me/deadly_spammer)
╠•➳➠ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: [Sᴀᴍᴇᴇʀ](t.me/official_sameer)
╚═══════════════╝

[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙱𝙾𝚃 ✨](https://github.com/DEADLY-FIGHTERS/DEADLY-SPAM-BOT)


**[©️](https://telegra.ph/file/c05ad657651d56c5b80fc.jpg) @DEADLY_SPAM_BOT"""
