from aiogram import types
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import handlers.users.check_market_names as check
from keyboards.default.keyboards import keyboard1
from aiogram.types import ContentTypes

@dp.message_handler(content_types=ContentTypes.TEXT)
async def search_page_two(mes: types.Message):
    m = '',
    founds = []
    m = mes.text.lower()
    founds = universal_search(m, check.values)
    keyboard = InlineKeyboardMarkup(row_width=2)
    if founds is None:
        print("salom")
    for a in founds:
        keyboard.insert(InlineKeyboardButton(text=str(a),callback_data=str(a)))
    keyboard.add(InlineKeyboardButton("Bosh menyu 🏠", callback_data="fist"))
    await mes.reply(text="Sizning yuborgan xabaringini tekshirdik va mana shunaqa maxsulotlar kelib chiqdi!",reply_markup=keyboard,)
    founds.clear()




@dp.callback_query_handler(lambda x: x.data == "fist")
async def handle_callback_queary_bosh(callbackdata: types.CallbackQuery):
    await callbackdata.message.reply("Bosh menuga o'tildi", reply_markup=keyboard1)

def universal_search(query, nested_list):
    query = query.lower()  # Convert the query to lowercase for case-insensitive search
    found_items = []
    for sublist in nested_list:
        for item in sublist:
            if query in item.lower():
                found_items.append(item)

    return found_items
