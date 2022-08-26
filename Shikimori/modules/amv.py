import os
import re
from platform import python_version as kontol
from telethon import events, Button
from Shikimori.events import register
from Shikimori import telethn as tbot


PHOTO = "https://telegra.ph/file/e465194098909856f9647.png"
PHOTO1 = "https://telegra.ph/file/456d5eefe72145a3e07f5.png"
PHOTO2 = "https://telegra.ph/file/f25bd10eb8f5596f5ac03.png"


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

@register(pattern=("/manime"))
async def awake(event):
    TEXT2 = "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ \n"
    TEXT2 += "┣ 🔸[𝗠𝘆𝘀𝘁𝗶𝗰 𝗔𝗻𝗶𝗺𝗲](https://t.me/Mystic_Anime) \n"
    TEXT2 += "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈"
    BUTTON2 = [
        [
            Button.url("[🔸ANIME🔸]", "https://t.me/Mystic_Anime"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO2, caption=TEXT2, buttons=BUTTON2)    

__help__ = """
 ──「MYSTICCHANNELS」──                         
 
❂ /pfp: Get information about PFP Channel
❂ /amv: Get information about AMV Channel
❂ /manime: Get information about ANIME Channel"""
   
__mod_name__ = "Mʏsᴛɪᴄ"
