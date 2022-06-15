from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from settings.config import KEYBOARD


'''Клавиатура главного меню'''
MAIN_MENU = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=KEYBOARD['MY_TRAININGS'])
        ],
        [
            KeyboardButton(text=KEYBOARD['CHOOSE_PROGRAM']),
            KeyboardButton(text=KEYBOARD['RANDOM_WOD'])
        ],
        [
            KeyboardButton(text=KEYBOARD['I_NEED_COACH'])
        ],
        [
            KeyboardButton(text=KEYBOARD['HEAD_PAGE'])
        ],
    ],
    resize_keyboard=True
)

'''Клавиатура для раздела МОИ ТРЕНИРОВКИ'''

MY_TRAININGS = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=KEYBOARD['CURRENT_PROGRAM']),
            KeyboardButton(text=KEYBOARD['CHOOSE_PROGRAM']),
        ],
        [
            KeyboardButton(text=KEYBOARD['HEAD_PAGE'])
        ],
    ],
    resize_keyboard=True
)

'''Клавиатура для раздела описания тренировки'''

TRAINING_DESCRIPTION = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=KEYBOARD['HEAD_PAGE']),
            KeyboardButton(text=KEYBOARD['CURRENT_PROGRAM']),
        ]
    ],
    resize_keyboard=True
)
