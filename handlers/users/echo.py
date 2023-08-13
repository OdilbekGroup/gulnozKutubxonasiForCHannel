from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(commands="start")
async def start_reply(msg: types.Message):
    await msg.answer("Assalomu alaykum, ushbu bot Gulnoz kutubxonasiga kanalga yuboriluvchi xabarlarni imzolashda yordam beradi.")

@dp.channel_post_handler(content_types=["text", "photo", "video", "voice"])
async def channel_editor(msg: types.Message):
    print(msg.content_type)
    if msg.content_type in ["photo", "video", "voice"]:
            await msg.edit_caption(f"{msg.html_text}\n\n<b>Gulnoz kutubxonasi</b>\n<a href='https://t.me/gulnoz_kutubxonasi'>Telegram</a> | <a href='https://youtube.com/@gulnozkutubxonasi'>YouTube</a> | <a href='https://t.me/+dLwL8X-Aac1hZTcy'>Muhokama</a>", parse_mode="HTML")
    if msg.content_type == "text":
            await msg.edit_text(f"{msg.html_text}\n\n<b>Gulnoz kutubxonasi</b>\n<a href='https://t.me/gulnoz_kutubxonasi'>Telegram</a> | <a href='https://youtube.com/@gulnozkutubxonasi'>YouTube</a> | <a href='https://t.me/+dLwL8X-Aac1hZTcy'>Muhokama</a>", parse_mode="HTML")
