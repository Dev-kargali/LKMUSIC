import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين lk","المطورين","مطورين","مطورين حياه"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""*𝐿𝐾 ダ ᴍᴜsɪᴄ source ↜**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين المملكه ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**𝐿𝐾 ダ ᴍᴜsɪᴄ source ↜**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩˹الـٰ‌ـہڪـہ‌ـࢪ غـٰ‌ـہلـٰ‌ـي ᬼ✆‌᭄˼𓆪♤ 🫥 ", url=f"https://t.me/L_ii_Q"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "𝖉𝖊𝖛 𝖟𝖆𝖇𝖆𝖉𝖞 ", url=f"https://t.me/L_ii_Q"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "𝐿𝐾 ダ source ↜", url=f"https://t.me/L_B_K1"),
                
        ],[
                    
                
                    InlineKeyboardButton(
                        "『أّلَعٌأّبًثًـ أّلَأّخِـيِّر فُـيِّ هّـذأّ أّلَقُرنِ 』", url=f"https://t.me/L_ii_Q"),
                ],

            ]

        ),

    )









@app.on_message(
    command(["كرغلي","زبادي"])
 
)
async def yas(client, message):
    
    usr = await client.get_chat("L_ii_Q")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**𝐿𝐾 ダ ᴍᴜsɪᴄ source ↜\nمعلومات مطور السورس2 \n↜︙Dev 𝗡𝗔𝗠𝗘 ↬:{name}\n↜︙Dev 𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙Dev 𝐈𝐃 ↬ :`{usr.id}`\n↜︙Dev 𝐁𝐈𝐎 ↬: {usr.bio} \n\n **𝐿𝐾 ダ ᴍᴜsɪᴄ source ↜**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
   command(["مبرمج السورس","مطور السورس"])
   
)
async def yas(client, message):
    usr = await client.get_chat("L_ii_Q")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**𝐿𝐾 ダ ᴍᴜsɪᴄ source ↜\nمعلومات مبرمج السورس \n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],  [
                    InlineKeyboardButton(
                        "استدعاء المبرمج", url=f"https://t.me/{usr.username}"),                        
                 ],
            ]
        ),
    )


@app.on_message(
  command(["المطور"])
  
)
async def yas(client, message):
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**𝐿𝐾 ダ ᴍᴜsɪᴄ source ↜ \nمعلومات المطور الاساسي\n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "استدعاء المطور", url=f"https://t.me/{usr.username}"),                        
                 ],
            ]
        ),
    )
    



@app.on_message(
   command(["ذكاء المملكه"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""**𝐿𝐾 ダ source ↜**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس المملكه\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**𝐿𝐾 ダ source ↜**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩˹الـٰ‌ـہڪـہ‌ـࢪ غـٰ‌ـہلـٰ‌ـي ᬼ✆‌᭄˼𓆪♤ 🫥", url=f"https://t.me/L_ii_Q"), 
                 ],[
                
                    InlineKeyboardButton(
                        "𝐿𝐾 ダ source ↜", url=f"https://t.me/L_B_K1"),
                ],

            ]

        ),

    )



@app.on_message(
   command(["قرأن"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""**𝐿𝐾 ダ source ↜**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس المملكه\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**𝐿𝐾 ダ source ↜**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩˹الـٰ‌ـہڪـہ‌ـࢪ غـٰ‌ـہلـٰ‌ـي ᬼ✆‌᭄˼𓆪♤ 🫥", url=f"https://t.me/L_ii_Q"), 
                 ],[
                
                    InlineKeyboardButton(
                        "𝐿𝐾 ダ source ↜", url=f"https://t.me/L_B_K1"),
                ],

            ]

        ),

    )

@app.on_message(command(["غنيلي", "غني", "غ", "حياه غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.getrandbits(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="`🔥 ¦ تـم اختيـار الاغـنـية لـك`",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.getrandbits(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="`💕 ¦ تـم اختيـار الصوره لـك`",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


    
