from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from emoji.core import emojize

from another.request_to_api import get_user_info, create_new_user
from keyboards.reply_keyboards import MAIN_MENU
from settings.config import DP, KEYBOARD


async def start_page(message: types.Message):
    '''Обработчик реакции на команду start'''

    user_tlg_id = message.from_user.id
    user_tlg_name = message.from_user.username
    response = await create_new_user(user_tlg_id, user_tlg_name)
    if response == 200:
        await message.answer(text=f'{emojize(":robot:")}Привет! Я бот-тренер{emojize(":mechanical_arm:")}. Помогу тебе регулярно тренироваться и становится лучшей версией себя.\n'
                              'Мои разделы:\n'
                              'Мои тренировки - здесь ты можешь тренироваться.\n'
                              'Выбрать программу - посмотреть доступные программы тренировок и выбрать себе подходящую.\n'
                              'Случайное испытание - получить случайное задание и проверить свои силы.\n'
                              'Мне нужен тренер - найти человека, который поможет тебе достичь своих целей.\n',
                         reply_markup=MAIN_MENU)
    else:
        await message.answer(text=f'{emojize(":robot:")} Не удалось выполнить запрос...Введите повторно команду /start')


async def head_page(message: types.Message):
    '''Обработчик для главного меню'''

    user_tlg_id = message.from_user.id
    resp = await get_user_info(user_tlg_id=user_tlg_id)
    await message.answer(text=f'Привет, {resp[0][1] if resp[0][1] else "<имя не указано>"}\n'
                              f'Ты занимаешься по программе: {resp[0][3] if resp[0][3] else "...программа не выбрана"}\n'
                              f'Твоя очередная тренировка № {resp[0][5] if resp[0][5] else "...программа не выбрана"}\n'
                              f'Всего тренировок в программе: {resp[0][4] if resp[0][4] else "...программа не выбрана"}\n'
                              f'Дата крайней тренировки: {resp[0][2] if resp[0][2] else "...дата отсутствует"}',
                         reply_markup=MAIN_MENU)


def register_head_page_handlers():
    '''Функция для регистрации обработчиков'''
    DP.register_message_handler(start_page, Command(['start', 'help']))
    DP.register_message_handler(head_page, Text(equals=KEYBOARD['HEAD_PAGE']))
