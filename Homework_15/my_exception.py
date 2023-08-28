import logging

from user import User


FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename='log_1.log', encoding='utf-8', level=logging.NOTSET, format=FORMAT, style='{')
logger = logging.getLogger(__name__)


class MyException(Exception):
    pass


class LevelException(MyException):
    def __init__(self, user: User, level: int):
        self.user = user
        self.level = level
        msg = f'{LevelException.__name__} - {self.user} пытался добавить пользователя с уровнем {self.level}'
        logger.error(msg)

    def __str__(self):
        return f'Нельзя добавить пользователя с уровнем {self.level}. ' \
               f'Вы вошли как {self.user.name} с уровнем {self.user.user_level}'


class AccessException(MyException):
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id
        msg = f'{AccessException.__name__} - Пользователь с именем "{self.name}" и ID {self.user_id} не найден'
        logger.error(msg)

    def __str__(self):
        return f'Отказано в доступе!' \
               f'Пользователь с именем {self.name} и ID {self.user_id} не найден'