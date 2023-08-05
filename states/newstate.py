from aiogram.dispatcher.filters.state import StatesGroup, State

class Auth(StatesGroup):
    qanday_turda_pul_utqazadi = State()
    qanaqa_turda = State()
    number = State()
    location = State()