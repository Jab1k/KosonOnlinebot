from aiogram import types
from loader import dp
from keyboards.default.keyboards import *
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.newstate import Auth
from backend.id import getid
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from keyboards.default.keyboards import kafes

from backend import backend as back

all_market_ids = [ ["🛒Gulmira Market" , -1001674061189], ["🍔Bursa HALLAL FOOD", -1001674061189] ]




@dp.message_handler(lambda m: m.text == "Uy qurulish mollari")
async def check_Uy_nullish(mess: types.Message):
    await mess.reply(text=f"Siz {mess.text}ni tanladingiz va bulardan birini tanlang!", reply_markup=keyboard_xostavar)

@dp.message_handler(lambda m: m.text == "Dorixonalar")
async def checking_dorixonlar(mess: types.Message):
    await mess.reply(text=f"Siz {mess.text} bo'limini tanladingiz va bulardan birini tanlang!", reply_markup=keyboard_dori)

@dp.message_handler(lambda m: m.text in dorixona)
async def checking_name_dori(mess: types.Message):
    await mess.reply(text=f"Xozirda ushbu savdo do'koni Online tizimda emas!", reply_markup=keyboard1)





@dp.message_handler(lambda m: m.text in xostavar)
async def checking_name_xostavar(mess: types.Message):
    await mess.reply(text=f"Xozirda ushbu savdo do'koni Online tizimda emas!", reply_markup=keyboard1)


@dp.message_handler(lambda m: m.text == "Savdo Do'konlari")
async def check_Uy_nullish(mess: types.Message):
    await mess.reply(text=f"Siz {mess.text}ni tanladingiz va bulardan birini tanlang!", reply_markup=keyboard_savdo)


@dp.message_handler(lambda m: m.text == "Restoran va Kafe")
async def kafe(mess: types.Message):
    await mess.reply(text=f"Siz {mess.text}ni tanladingiz va bulardan birini tanlang!", reply_markup=kafe1)


@dp.message_handler(lambda m: m.text == "Orqaga")
async def next(mess: types.Message):
    await mess.reply(text=mess.text, reply_markup=keyboard1)


keys = []
values = []
value = []
Data = {}
all_make = []
pagination_callback = CallbackData('pagination', 'action', 'page')
market_name = ""
old_message_id = 0
old_mahsulot = ""
old_page_name = ""


@dp.message_handler(lambda m: m.text in Savdo or m.text in kafes)
async def check_markets(message: types.Message):
    global Data
    global value
    global keys
    global all_make
    global market_name
    global all_market_ids
    global values
    global old_message_id
    global old_page_name
    all_make.clear()
    old_page_name = ""
    Data.clear()
    value.clear()
    values.clear()
    keys.clear()
    Data = back.getgroup(message.text)
    value = list(Data.keys())
    if value[0] == "kechirasiz":
        await message.reply(text=f"Xozirda ushbu savdo do'koni Online tizimda emas!", reply_markup=keyboard1)
    else:
        keys = list(Data.items())
        values = list(Data.values())
        market_name = message.text
        old_message_id = message.message_id
        current_page = 1
        all_make.clear()
        await show_pages(message, keys, current_page)



@dp.message_handler(lambda m: m.text.isdigit())
async def checking_howmuch(message: types.Message):
    await message.reply(text="Barakalla yana maxsulot tanlang!")
    for i in range(len(all_make)):
        if all_make[i][0] == old_mahsulot:
            all_make[i].append(int(message.text))
    await show_pages(message, keys, 1)

async def show_pages(message: types.Message, kalit, current_page):
    items_per_page = 20
    start_index = (current_page - 1) * items_per_page
    end_index = min(start_index + items_per_page, len(kalit))

    keyboard = InlineKeyboardMarkup(row_width=2)

    for a in range(start_index, end_index):
        keyboard.insert(InlineKeyboardButton(text=f'{kalit[a][0]}', callback_data=f'{kalit[a][0]}'))

    if current_page > 1:
        keyboard.insert(InlineKeyboardButton(text='⏪', callback_data=pagination_callback.new(action='prev',
                                                                                              page=current_page - 1)))

    if end_index < len(kalit):
        keyboard.insert(InlineKeyboardButton(text='⏩', callback_data=pagination_callback.new(action='next',
                                                                                              page=current_page + 1)))

    keyboard.add(InlineKeyboardButton(text='🚚Buyurtma qilish!✅', callback_data='end'))
    keyboard.add(InlineKeyboardButton(text='Qidirish🔎', callback_data='search'))
    keyboard.insert(InlineKeyboardButton(text="🏠 Bosh menyu", callback_data='fist'))

    await message.delete()
    await message.answer(
        text=f'Bulardan birini tanlang, {message.from_user.full_name}',
        reply_markup=keyboard,
    )
old_current_start = 0
async def show_page_callbackdata(message: types.CallbackQuery, kalit1, current_page):
    global old_current_start
    items_per_page = 20
    start_index = (current_page - 1) * items_per_page
    end_index = min(start_index + items_per_page, len(kalit1))
    keyboard = InlineKeyboardMarkup(row_width=2)
    # print(old_current_start, start_index, len(kalit1))
    if old_current_start > 0:
        for e in range(old_current_start, len(kalit1)):
            # print(e)
            old_current_start = e
            b = "".join(kalit1[e][0:18])
            # print(b, "hello")
            keyboard.insert(InlineKeyboardButton(text=f'{b}', callback_data=f'{b}'))
    elif old_current_start < 0 < start_index:
        for e in range(start_index, end_index):
            # print(e)

            old_current_start = e
            b = "".join(kalit1[e][0:18])
            # print(b, "hello")
            keyboard.insert(InlineKeyboardButton(text=f'{b}', callback_data=f'{b}'))
    elif start_index <= 0 < old_current_start:
        for e in range(old_current_start, start_index):
            # print(e)

            old_current_start = e
            b = "".join(kalit1[e][0:18])
            # print(b, "hello")
            keyboard.insert(InlineKeyboardButton(text=f'{b}', callback_data=f'{b}'))
    else:
        for e in range(start_index, end_index):
            old_current_start = e
            b = "".join(kalit1[e][0:18])
            # print(b, "hello")
            keyboard.insert(InlineKeyboardButton(text=f'{b}', callback_data=f'{b}'))

    if current_page > 1:
        keyboard.insert(InlineKeyboardButton(text='⏪', callback_data=pagination_callback.new(action='prev',
                                                                                              page=current_page - 1)))

    if end_index < len(kalit1):
        # print("salom1")
        keyboard.insert(InlineKeyboardButton(text='⏩', callback_data=pagination_callback.new(action='next',
                                                                                              page=current_page + 1)))
    keyboard.add(InlineKeyboardButton(text="🏠 Bosh menyu", callback_data='fist'))
    keyboard.add(InlineKeyboardButton(text='🚚Buyurtma qilish!✅', callback_data='end'))
    keyboard.add(InlineKeyboardButton(text='Qidirish🔎', callback_data='search'))
    keyboard.insert(InlineKeyboardButton(text="🏠 Bosh menyu", callback_data='fist'))
    # await message.message.delete()
    await message.message.answer(
        text=f'Bulardan birini tanlang, {message.from_user.full_name}',
        reply_markup=keyboard
    )
    await message.message.delete()
current_page = 1
@dp.callback_query_handler(pagination_callback.filter())
async def handle_pagination_callback(callback_query: types.CallbackQuery, callback_data: dict):
    global current_page
    global old_page_name
    global old_current_start
    if callback_data['action'] == "prev" or callback_data["action"] == "next":
        action = callback_data['action']
        current_page = int(callback_data['page'])

        if action == 'prev':
            current_page = 0
            old_current_start = 0
        elif action == 'next':
            current_page += 1
        if old_page_name is None or old_page_name == "":
            print("is none", keys, current_page)
            await show_pages(callback_query.message, keys, current_page)
        else:
            print("is not none", Data[old_page_name], current_page)

            await show_page_callbackdata(callback_query, Data[old_page_name], current_page)


from keyboards.default.keyboards import end


@dp.callback_query_handler(lambda x: x.data == "end")
async def isend(callback_query: types.CallbackQuery):
    message = "Siz olmoqchi bo'lgan maxsulotlar:\n"
    message += "---------------------------------\n"
    for item in all_make:
        message += f"{item[0]}\n" \
                   f"*{item[1]} x {item[2]} = {(item[2] * item[1])}\n\n*"
    message += "---------------------------------\n"
    message += f"\nSiz olmoqchi bo'lgan maxsulotlarni tastiqlaysizmi ?"
    await callback_query.message.reply(message,reply_markup=end, parse_mode='Markdown')

@dp.callback_query_handler(lambda x: x.data == "ha")
async def yes(callback_query: types.CallbackQuery):
    if callback_query.message.text.isdigit():
        await callback_query.message.reply(text="Iltimos son kiritmang!")
    else:
        await callback_query.message.reply("To'lov usulini tanlang", reply_markup=keyboard_request_qanday_turi)
        await Auth.qanday_turda_pul_utqazadi.set()

@dp.message_handler(lambda x: x.text == "Naqd pul💸",state=Auth.qanday_turda_pul_utqazadi)
async def naxt_tulash(message: types.Message, state: FSMContext):
    await message.reply("Dastafka turini tanlang!", reply_markup=keyboard_request_dastafka)
    await state.update_data(qandayturdatulaydi=message.text)
    await Auth.qanaqa_turda.set()

@dp.message_handler(lambda x: x.text == "Plastik karta💳",state=Auth.qanday_turda_pul_utqazadi)
async def kartadan_tulash(message: types.Message, state: FSMContext):
    await message.reply("Dastafka turini tanlang!", reply_markup=keyboard_request_dastafka)
    await state.update_data(qandayturdatulaydi=message.text)
    await Auth.qanaqa_turda.set()


@dp.message_handler(lambda x: x.text == "O'zi olib ketish🚶‍♂️",state=Auth.qanaqa_turda)
async def oziolibketish(message: types.Message,state: FSMContext):
    await message.reply(text="Barakalla endi raqamingizni yuboring\npastdagi tugmani bosish orqali!",
                                       reply_markup=keybord_request_contact)
    await state.update_data(qanday=message.text)
    await Auth.number.set()


@dp.message_handler(lambda x: x.text == "Yetkazib berish🚚",state=Auth.qanaqa_turda)
async def dostafka(message: types.Message,state: FSMContext):
    await message.reply(text="Barakalla endi raqamingizni yuboring\npastdagi tugmani bosish orqali!",
                                       reply_markup=keybord_request_contact)
    await state.update_data(qanday=message.text)
    await Auth.number.set()


@dp.message_handler(state=Auth.number,content_types=["contact"])
async def chacking_number(message: types.Message, state: FSMContext):
    await message.reply(text="Barakalla endi lokatsiyangizni yuboring\npastdagi tugmani bosish orqali!",reply_markup=keybord_request_location)
    await state.update_data(number=message.contact.phone_number)
    await Auth.location.set()
abcs = 0

@dp.message_handler(state=Auth.location,content_types=["location"])
async def chacking_location(message: types.Message, state: FSMContext):
    print("sakom")
    global abcs
    await state.update_data(location=message.location)
    data = await state.get_data()
    late = data.get("location")
    which_turda_tulaydi = data.get("qandayturdatulaydi")
    qanday = data.get('qanday')
    id = getid()
    m = ""
    jami = 0
    for abc in all_make:
        print("sakom")
        jami += (abc[1] * abc[2])
    if qanday == "O'zi olib ketish🚶‍":
        print("sakom")
        abcs = 0
        jami += 0
    elif qanday == "Yetkazib berish🚚":
        abcs = 15000
        print(abcs)
        jami += 15000
    for item in all_make:
        m += f"*{item[0]} - {item[1]} x {item[2]} = {(item[2] * item[1])}*\n"
    await state.reset_state(with_data=True)
    print("sakom1")
    for ab in range(len(all_market_ids)):
        print("sakom", all_market_ids[ab][0], market_name)
        if all_market_ids[ab][0] == market_name:
            print("krdi")
            await message.reply(text=f"Tez orada siz bilan bog'lanamiz.\n\n"
                                f"*Sizning IDyingiz!: {id}*\n\n"
                                f"Siz buyurtma qilgan tovarlar: \n{m}\n"
                                f"*Dostafka turi: {qanday} - {abcs} *\n\n"
                                f"To'lov usuli: {which_turda_tulaydi}\n\n"
                                f"*Jami summa: {jami}*\n",
                                reply_markup=keyboard1,
                                parse_mode='Markdown'
                                )
            await dp.bot.send_message(all_market_ids[ab][1],text=
            f"Sizning IDyingiz!: {id}\n"
            f"Ismi: {message.from_user.full_name}\n"
            f"Raqami: {data.get('number')}\n"
            f"Buyurtma qilingan maxsulotlar: \n{m}\n"
            f"Qanday turda: {qanday} - {abcs}\n"
            f"To'lov usuli: {which_turda_tulaydi}\n"
            f"Jami summa: {jami}\n", parse_mode="Markdown"
                                      )
            await dp.bot.send_location(all_market_ids[ab][1], latitude=late.latitude, longitude=late.longitude)
            started_index = old_message_id
            ended_index = message.message_id - 1
            for abs in range(started_index, ended_index):
                await dp.bot.delete_message(chat_id=message.chat.id, message_id=str(abs))
            all_make.clear()
            break




@dp.callback_query_handler(lambda x: x.data == "yoq")
async def yes(callback_query: types.CallbackQuery):
    all_make.clear()
    await callback_query.message.reply("Unda maxsulotlarni qayta tanlang",reply_markup=keyboard1)


@dp.callback_query_handler(lambda x: x.data == 'search')
async def search_page(callback_queary: types.CallbackQuery):
    await callback_queary.message.reply("Kerakli maxsulotni nomini yozing", reply_markup=keyboard1)

@dp.callback_query_handler(lambda x: x.data == "fist")
async def handle_callback_queary_bosh(callbackdata: types.CallbackQuery):
    await callbackdata.message.reply("Bosh menuga o'tildi", reply_markup=keyboard1)



@dp.callback_query_handler()
async def handle_callback_query(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    global old_mahsulot
    global old_page_name
    global old_current_start
    print("salom", value, callback_data)
    if callback_data in value:
        print("salom", Data[callback_data])
        # print(callback_data)
        old_page_name = callback_data
        await show_page_callbackdata(callback_query, Data[callback_data], 1)
    else:
        print("hhi")
        old_page_name = ""
        old_current_start = 0
        name = back.checkmahs(callback_data)
        print(name)
        if name != 'Topilmadi!':
            old_mahsulot = callback_data
            all_make.append([callback_data, name])
            from keyboards.default.keyboards import menuStart
            await callback_query.message.answer(
                text=f'Maxsulot nomi:\n{callback_query.data}\n<b>{name}</b> ',
                parse_mode="HTML",
                reply_markup=menuStart
            )
