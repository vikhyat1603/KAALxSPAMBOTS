from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from .. import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, OWNER_ID
from KaalX.plugins.help import *


PythonIMG = "https://te.legra.ph/file/fd2cbade34ff0dc8b2f2a.jpg"

Python_Button = [
        [
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/YARRO_121")
        ],
        [
        Button.inline("⚡ ᴄᴏᴍᴍᴀɴᴅs ⚡", data="help_back")
        ]
        ]
               
PythonX_Button = [
        [
        Button.url("✨ ᴄʜᴀɴɴᴇʟ ✨", "https://t.me/YARRO_BOT_121"),
        Button.url("✨ sᴜᴘᴘᴏʀᴛ ✨", "https://t.me/YARRO_121")
        ],
        [
        Button.url("🔥 ʀᴇᴘᴏ 🔥", "https://github.com/Rajsinghrc/KAALxSPAMBOTS")
        ]
        ]
        
        
#USERS 


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       PythonBot = await event.client.get_me()
       bot_name = PythonBot.first_name
       bot_id = PythonBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       ThePython = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       ownermsg = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
       usermsg = f"**Hello !! [{firstname}](tg://user?id={userid})\nNice To Meet You, Well I Am [{bot_name}](tg://user?id={bot_id}), A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From The Button Given Below.** \n\n**Powered By : [𝗞𝗮𝗮𝗹𝙓](https://t.me/raj_singh_rc)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(ThePython,
                  PythonIMG,
                  caption=ownermsg, 
                  buttons=Python_Button)
       else:
            await event.client.send_file(ThePython,
                  PythonIMG,
                  caption=usermsg, 
                  buttons=PythonX_Button)
                

