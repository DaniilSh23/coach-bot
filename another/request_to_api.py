import aiohttp
from loguru import logger

from settings.config import USER_INFO_API_URL, USER_TRAINING_PROGRAM, USER_CURRENT_TRAINING


@logger.catch
async def create_new_user(user_tlg_id, user_tlg_name):
    '''Запрос для внесения в БД нового пользователя'''

    req_link = USER_INFO_API_URL
    async with aiohttp.ClientSession() as session:
        async with session.post(req_link, data={
            'user_tlg_id': user_tlg_id,
            'user_tlg_name': user_tlg_name
        }) as response:
            return response.status


@logger.catch
async def get_user_info(user_tlg_id):
    '''Запрос для получения информации о пользователе'''

    if user_tlg_id:
        req_link = ''.join([USER_INFO_API_URL, f"?user_tlg_id={str(user_tlg_id)}"])
        # создаём клиент сессии
        async with aiohttp.ClientSession() as session:
            # выполняем GET запрос по указанному в константе адресу
            async with session.get(req_link) as response:
                # ждём выполнения корутины ответа и формируем из ответа json
                return await response.json()


@logger.catch
async def get_info_about_user_program(user_tlg_id):
    '''Получение информации о программе пользователя'''

    if user_tlg_id:
        req_link = ''.join([USER_TRAINING_PROGRAM, f'?user_tlg_id={str(user_tlg_id)}'])
        async with aiohttp.ClientSession() as session:
            async with session.get(req_link) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return False


@logger.catch
async def get_detail_training_info(user_tlg_id):
    '''Получение детальной информации о тренировке пользователя'''

    req_link = ''.join([USER_CURRENT_TRAINING, f'?user_tlg_id={str(user_tlg_id)}'])
    async with aiohttp.ClientSession() as session:
        async with session.get(req_link) as response:
            if response.status == 200:
                return await response.json()
            else:
                return False
