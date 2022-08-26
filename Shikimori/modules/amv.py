import os
import re
from platform import python_version as kontol
from telethon import events, Button
from Shikimori.events import register
from Shikimori import telethn as tbot


PHOTO = "https://telegra.ph/file/e465194098909856f9647.png"


@register(pattern=("/pfp"))
async def awake(event):
    TEXT += "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ \n\n"
    TEXT += "┣ 🔸[𝗔𝗻𝗶𝗺𝗲 𝗣FP'𝘀](https://t.me/MysticPfp/164) \n\n"
    TEXT += "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈"
    BUTTON = [
        [
            Button.url("[🔸Anime PFP🔸]", "https://t.me/MysticPfp"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
__help__ = """
 ──「PFP」──                         
 
❂ /pfp: Get information about PFP Channel"""
   
__mod_name__ = "pfp"
