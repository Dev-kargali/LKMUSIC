import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("help")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://j.top4top.io/p_273634wmy1.jpg",
        caption=f"""** 𝐿𝐾 ダ source ↜**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس المملكه \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n** 𝐿𝐾 ダ source ↜**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𓆩˹الـٰ‌ـہڪـہ‌ـࢪ غـٰ‌ـہلـٰ‌ـي ᬼ✆‌᭄˼𓆪♤ 🫥", url=f"https://t.me/L_ii_Q"),
                    InlineKeyboardButton(
                        "حسابي الثاني", url=f"https://t.me/AZ_UX"),
                ],[
                
                    InlineKeyboardButton(
                        "𝐿𝐾 ダ source ↜", url=f"https://t.me/L_B_K1"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""** 𝐿𝐾 ダ source ↜**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

** 𝐿𝐾 ダ source ↜**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="دليل")],
            [InlineKeyboardButton("|𓆩˹الـٰ‌ـہڪـہ‌ـࢪ غـٰ‌ـہلـٰ‌ـي ᬼ✆‌᭄˼𓆪♤ 🫥", url=f"https://t.me/L_ii_Q"),
             InlineKeyboardButton("حسابي الثاني", url=f"https://t.me/AZ_UX")],
            [InlineKeyboardButton("★ 𝐿𝐾 ダ source ↜", url=f"https://t.me/HL_BG")],
        ]
    ))

