from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Cliet.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("Hi Man 😁")
