from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from emoji.core import emojize

from another.callback_data_bot import callback_for_next_training, callback_for_complete_training
from another.request_to_api import get_info_about_user_program, get_detail_training_info
from keyboards.inline_keyboards import current_program_inline_keyboard_format, create_complete_training_inline_keyboard
from keyboards.reply_keyboards import MY_TRAININGS
from settings.config import DP, KEYBOARD, BOT


async def my_trainings(message: types.Message):
    '''Обработчик для кнопки Мои тренировки'''

    await message.answer(text=f'{emojize(":robot:")}Раздел "мои тренировки".\n'
                              'Здесь можно посмотреть текущую программу, '
                              'перейти к выбору программы тренировок и многое другое.',
                         reply_markup=MY_TRAININGS)


async def current_program(message: types.Message):
    '''Обработчик для раздела Текущая программа'''

    user_tlg_id = message.from_user.id
    resp = await get_info_about_user_program(user_tlg_id)
    if resp:
        if resp[0][0]:
            this_message = await message.answer(
                text=f'Название программы: {resp[0][0]}\n'
                     f'Цель программы: {resp[0][2]}\n'
                     f'Общее количество тренировок: {resp[0][3]}\n'
                     f'Средняя продолжительность тренировки: {resp[0][4]}\n'
                     f'Рекомендуемое количество тренировок в неделю: {resp[0][5]}\n\n'
                     f'Описание программы: \n{resp[0][1]}'
            )
            message_id = this_message.message_id
            inline_keyboard = current_program_inline_keyboard_format(
                user_training_numb=resp[0][6],
                program_training_numb=resp[0][3],
                next_training_id=resp[0][7],
                user_tlg_id=user_tlg_id,
                program_id=resp[0][8],
                message_id=message_id
            )
            await this_message.edit_text(
                text=f'Название программы: {resp[0][0]}\n'
                     f'{emojize(":bullseye:")}Цель программы: {resp[0][2]}\n'
                     f'Общее количество тренировок: {resp[0][3]}\n'
                     f'Средняя продолжительность тренировки: {resp[0][4]}\n'
                     f'Рекомендуемое количество тренировок в неделю: {resp[0][5]}\n\n'
                     f'Описание программы: \n{resp[0][1]}',
                reply_markup=inline_keyboard
            )
        else:
            await message.answer(text=f'{emojize(":robot:")} Спервы Вы должны выбрать программу.')
    else:
        await message.answer(text=f'{emojize(":robot:")} Ошибка сервера. Запрос не выполнен...')


async def training(call: CallbackQuery, callback_data: dict):
    '''Обработчик при нажатии на кнопку очередной тренировки'''

    await call.answer(text=f'{emojize(":robot:")} Выполняю запрос к серверу для получения Вашей тренировки...')
    resp = await get_detail_training_info(callback_data.get('user_tlg_id'))
    if resp:
        inline_keyboard = create_complete_training_inline_keyboard(
            training_id=resp[0][0],
            message_id=callback_data['message_id'],
            user_tlg_id=callback_data['user_tlg_id']
        )
        await call.message.edit_text(
            text=f'Название программы: {resp[0][1]}\n'
                 f'Номер тренировки: {resp[0][2]}\n\n'
                 f'Описание тренировки: {resp[0][3]}',
            reply_markup=inline_keyboard
        )
    else:
        await call.answer(text=f'{emojize(":robot:")} Ошибка сервера. Запрос не удался...')


async def send_training_result(call: CallbackQuery, callback_data: dict):
    '''Обработчик для отправки результата тренировки'''

    await call.answer(text='Введите результат тренировки в произвольной форме.\n'
                                      'Это обязательно, чтобы перейти к следующей тренировке.', show_alert=True)
    await call.message.edit_text(text='Введите результат тренировки в произвольной форме.\n'
                                      'Это обязательно, чтобы перейти к следующей тренировке.',)


def register_my_trainings_handlers():
    '''Функция для регистрации обработчиков тренировок'''

    DP.register_message_handler(my_trainings, Text(equals=KEYBOARD['MY_TRAININGS']))
    DP.register_message_handler(current_program, Text(equals=KEYBOARD['CURRENT_PROGRAM']))
    DP.register_callback_query_handler(training, callback_for_next_training.filter(flag='next'))
    DP.register_callback_query_handler(send_training_result, callback_for_complete_training.filter(flag='complete_training'))
