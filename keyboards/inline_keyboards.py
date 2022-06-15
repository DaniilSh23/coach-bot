from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from another.callback_data_bot import callback_training_results_list, callback_for_finish_program, \
    callback_for_next_training, callback_for_complete_training
from settings.config import KEYBOARD


def current_program_inline_keyboard_format(user_training_numb, program_training_numb,
                                           next_training_id, user_tlg_id, program_id, message_id):
    '''Функция для создания инлайн клавиатуры к разделу Текущая программа'''

    inline_keyboard = InlineKeyboardMarkup(row_width=2)

    # кнопка очередной тренировки
    if user_training_numb < program_training_numb:
        inline_button = InlineKeyboardButton(
            text=KEYBOARD['NEXT_TRAINING'],
            callback_data=callback_for_next_training.new(
                next_training_id=next_training_id,
                message_id=message_id,
                flag='next',
                user_tlg_id=user_tlg_id
            ),
        )
        inline_keyboard.insert(inline_button)

    # кнопка результатов тренировок
    inline_button = InlineKeyboardButton(
        text=KEYBOARD['TRAINING_RESULTS'],
        callback_data=callback_training_results_list.new(
            user_tlg_id=user_tlg_id,
            message_id=message_id,
            flag='results'
        ),
    )
    inline_keyboard.insert(inline_button)

    # кнопка завершения програмы
    inline_button = InlineKeyboardButton(
        text=KEYBOARD['FINISH_PROGRAM'],
        callback_data=callback_for_finish_program.new(
            program_id=program_id,
            message_id=message_id,
            flag='finish'
        ),
    )
    inline_keyboard.insert(inline_button)
    return inline_keyboard


def create_complete_training_inline_keyboard(training_id, message_id, user_tlg_id):
    '''Создание инлайн клавиатуры для выполненной тренировки'''

    inline_keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=KEYBOARD['COMPLETE'],
                    callback_data=callback_for_complete_training.new(
                        training_id=training_id,
                        message_id=message_id,
                        user_tlg_id=user_tlg_id,
                        flag='complete_training',
                    )
                )
            ],

        ]
    )
    return inline_keyboard
