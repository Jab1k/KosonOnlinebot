from aiogram import types

from loader import dp
import datetime
from aiogram.types import ContentTypes


# Echo bot
@dp.message_handler(state=None, content_types=ContentTypes.ANY)
async def bot_echo(message: types.Message):
    await message.answer("Sizga qanday yordam bera olamiz ?\nMurojaat uchun:\nBizga bog\'laning:\n☎️+998996658666\n☎️+998906088666\n👉@jajikservis👈\nIshlatishni bilmasangiz /help yoki /start commandasini yuboring!")
    await message.copy_to(chat_id=-1001674061189, caption=f"""
👤Ismi: {message.from_user.full_name}
ℹ️username: @{message.from_user.username}
🕛vaqt: {datetime.datetime.now()}
✍️Nima dep yozdi yoki nima tashadi: {message.text, message.content_type}
🆔Idsi: {message.from_user.id}
            """)
