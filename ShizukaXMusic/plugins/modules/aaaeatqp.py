import asyncio
import os
from pyrogram.types import CallbackQuery
from ShizukaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ShizukaXMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(filters.command(["اكامي"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c990c7c6d1f3e7e42812f.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : »» [𐏓 𝘼𝙆𝘼𝙈𝙀𝆹𝅥𝅮⏤͟͟͞͞ ░⃟‌‎‌‌🇪🇦](https://t.me/FHK_M5)
◉ 𝚄𝚂𝙴𝚁 : »» @FHK_M5
◉ 𝙸𝙳   : »» 6230638204
◉ 𝙱𝙸𝙾  : »» **- لم يعد بالي يُبالي فـ ليحترق ڪًٰل شي**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𐏓 𝘼𝙆𝘼𝙈𝙀𝆹𝅥𝅮⏤͟͟͞͞ ░⃟‌‎‌‌🇪🇦", url=f"https://t.me/FHK_M5"),
            ]
         ]
     )
  )

