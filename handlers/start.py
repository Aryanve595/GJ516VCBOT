import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):

     await message.reply_photo(
        photo=f"https://telegra.ph/file/e4ccacd74d5545c16ac85.jpg",
        caption=f""" ** Hey {message.from_user.mention()} , 🥀\n\n
๏ This is [{bn}](t.me/{bu}) ,  !
➻  most advance and superfast telegram music  bot with some awesome features.

──────────────────
๏  All of my command can be used with My command handle : ( / . • $ ^ ~ + * ? )
➻ Made 🖤 by : [🕊️★ Aryan ★🇮🇳⃝🕊️](https://t.me/Heartlessaryan_op) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                
                   
                       
                      
,[
                  
                       
                    
                    InlineKeyboardButton(
                        "📨 Support ", url=f"https://t.me/+p2A5gHTe9_YzNDk1"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 Bot Owner ", url=f"(https://t.me/Toxic_aadi28)"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"(https://t.me/Heartlessaryan_op)"
                    ),
                 
                    
                       
                    
                    
                       
                    ]
            ]
       ),
    )

