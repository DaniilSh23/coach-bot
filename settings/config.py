import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import re
from aiogram.utils.emoji import emojize
from dotenv import load_dotenv

load_dotenv()

# токен выдается при регистрации приложения
TOKEN = os.getenv('TOKEN')
PAY_TOKEN = os.getenv('PAY_TOKEN')

# Телеграм ID админов
ADMINS_ID_LST = [1978587604]
STAFF_ID = 1978587604

# абсолютный путь до текущей директории этого файла
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# кнопки управления
KEYBOARD = {
    'MY_TRAININGS': emojize(':man_lifting_weights: Мои тренировки'),
    'CHOOSE_PROGRAM': emojize('✅ Выбрать программу'),
    'RANDOM_WOD': emojize(':flexed_biceps: Случайное испытание'),
    'I_NEED_COACH': emojize(':man: Мне нужен тренер'),
    'HEAD_PAGE': emojize(":house_with_garden: Главная"),
    'CURRENT_PROGRAM': emojize(':trophy: Текущая программа'),
    'NEXT_TRAINING': emojize(':flexed_biceps: Очередная тренировка'),
    'TRAINING_RESULTS': emojize(':chart_increasing: Результаты тренировок'),
    'FINISH_PROGRAM': emojize(':chequered_flag: Завершить програму'),
    'COMPLETE': emojize('✅ ВЫПОЛНЕНО'),

    'X_ORDER': emojize('❌ ОТМЕНИТЬ ЗАКАЗ'),
    'X_BASKET': emojize('❌:wastebasket: ОЧИСТИТЬ'),
    'BACK_STEP_ITEM': emojize('◀️Назад'),
    'NEXT_STEP_ITEM': emojize('▶️ Вперёд'),
    'BACK_STEP_CATEG': emojize('⏪Назад'),
    'NEXT_STEP_CATEG': emojize('⏩Вперёд'),
    'PLUS_ITEM': emojize(':plus:'),
    'MINUS_ITEM': emojize(':minus:'),
    'STANDARD_BUTTON': emojize(':fuel_pump:'),
    'PAY': emojize(':yen_banknote:ОПЛАТИТЬ'),
    'ORDER_GIVEN': emojize(':package:ЗАКАЗ ПЕРЕДАН'),
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}

# URL адреса для запросов к АPI бота
DOMAIN_NAME = 'http://127.0.0.1:8000/api/'
USER_INFO_API_URL = f'{DOMAIN_NAME}user_info/'
USER_TRAINING_PROGRAM = f'{DOMAIN_NAME}training_program/'
USER_CURRENT_TRAINING = f'{DOMAIN_NAME}current_training/'


# объекты: бот, диспатчер, сторэдж для машины состояний
BOT = Bot(token=TOKEN, parse_mode='HTML')
STORAGE = MemoryStorage()
DP = Dispatcher(BOT, storage=STORAGE)

# регулярные выражения для бота
# RE_CATEGORY_LINK_PATTERN = re.compile(r'\?\w*\S\w*')
RE_CATEGORY_LINK_PATTERN = re.compile(r'\?.*')

# опции доставки
DELIVERY_FROM_CAFE = types.ShippingOption(
    id='delivery-form-cafe',
    title='Доставка из кафе',
    prices=[
        types.LabeledPrice(
            'Стандартная доставка', 15000
        )
    ]
)

PICKUP_FROM_CAFE = types.ShippingOption(
    id='pickup-form-cafe',
    title='Забрать самостоятельно',
    prices=[
        types.LabeledPrice(
            'Самовывоз', 0
        )
    ]
)
