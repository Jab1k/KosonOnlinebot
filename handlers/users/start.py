from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default.keyboards import *
import datetime


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Assalomu aleykum!\nSiz Koson tumani online savdo botiga tashrif buyurdingiz.\n"
                        "Bu yerdan extiyojingiz uchun kerak bo'ladigan mahsulotlarni xarid qilishingiz mumkin.\n"
                        "Quyidagilardan kerakli bo'limni tanlang.", reply_markup=keyboard1)
    await dp.bot.send_message(-1001674061189, text=f"""
   👤Ismi: {message.from_user.full_name}
ℹ️username: @{message.from_user.username}
🕛vaqt: {datetime.datetime.now()}
✍️Nima dep yozdi: {message.text}
       """)

