from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.config import Savdo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
xostavar = ["Billur", "Marvarit"]
dorixona = ["Istiqlol FARM", "TABLETKA"]
kafes = ["🍔Bursa HALLAL FOOD", "🥙Jazira Fast Food", "🍽Bahor Restorant🍲", "👨‍👩‍👧‍👦Orif Oilaviy Choyxona🍱"]
keyboard_xostavar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in xostavar:
    keyboard_xostavar.insert(i)
keyboard_dori = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for a in dorixona:
    keyboard_dori.insert(a)

kafe1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

for ass in range(len(kafes)):
    kafe1.row(str(kafes[ass]))

kafe1.add("Bosh menyu 🏠")


keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
keyboard1.row("Restoran va Kafe", "Savdo Do'konlari", "Dorixona", "Uy qurulish mollari")
keyboard_savdo = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

for i in range(len(Savdo)):
    keyboard_savdo.row(str(Savdo[i]))

keyboard_savdo.add("Bosh menyu 🏠")

end = InlineKeyboardMarkup(row_width=2)
end.insert(InlineKeyboardButton(text="Ha✅",callback_data="ha"))
end.insert(InlineKeyboardButton(text="yoq❌",callback_data="yoq"))
end.insert(InlineKeyboardButton(text="Bosh menyu 🏠", callback_data="fist"))

menuStart = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text='1'),
                        KeyboardButton(text="2"),
                        KeyboardButton(text="3"),
                        KeyboardButton(text="4"),
                        KeyboardButton(text="5"),
                        KeyboardButton(text="6"),
                        KeyboardButton(text="2"),
                        KeyboardButton(text="7"),
                        KeyboardButton(text="8"),
                        KeyboardButton(text="9"),
                        KeyboardButton(text="10"),
                    ],
                ],
                resize_keyboard=True
            )
keybord_request_contact = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keybord_request_contact.insert(KeyboardButton(request_contact=True,text="Raqam yuborish!📲"))

keyboard_request_qanday_turi = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_request_qanday_turi.add(KeyboardButton(text="Naqd pul💸"), KeyboardButton(text="Plastik karta💳"))

keybord_request_location = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keybord_request_location.insert(KeyboardButton(request_location=True,text="Locatsiyani yuborish!📍"))


keyboard_request_dastafka = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_request_dastafka.add(KeyboardButton(text="O'zi olib ketish 🚶‍♂️"),KeyboardButton(text="Yetkazib berish🚚"))

