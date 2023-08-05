from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = 'Hamkorlik uchun bizga bog\'laning:\n☎️+998996658666\n☎️+998906088666\n👉@jajikservis👈'
    await message.answer(text=text)
