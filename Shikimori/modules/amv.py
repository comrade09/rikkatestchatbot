import os
import re
from platform import python_version as kontol
from telethon import events, Button
from Shikimori.events import register
from Shikimori import telethn as tbot


PHOTO = "https://telegra.ph/file/e465194098909856f9647.png"
PHOTO1 = "https://telegra.ph/file/456d5eefe72145a3e07f5.png"


@register(pattern=("/pfp"))
async def awake(event):
    TEXT = "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ \n"
    TEXT += "┣ 🔸[𝗔𝗻𝗶𝗺𝗲 𝗣𝗙𝗣'𝘀](https://t.me/MysticPfp/164) \n"
    TEXT += "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈"
    BUTTON = [
        [
            Button.url("[🔸Anime PFP🔸]", "https://t.me/MysticPfp/164"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
    
@register(pattern=("/amv"))
async def awake(event):
    TEXT1 = "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ \n"
    TEXT1 += "┣ 🔸[Anime AMV'𝘀](https://t.me/MysticAmvs/4) \n"
    TEXT1 += "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈"
    BUTTON1 = [
        [
            Button.url("[🔸AMV🔸]", "https://t.me/MysticAmvs"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO1, caption=TEXT1, buttons=BUTTON1)
    
__help__ = """
 ──「CHANNELS」──                         
 
❂ /pfp: Get information about PFP Channel
❂ /amv: Get information about AMV Channel"""
   
__mod_name__ = "pfp"
