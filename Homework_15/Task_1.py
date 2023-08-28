# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import json
from typing import Set
from user import User
from my_exception import LevelException, AccessException
import logging
import argparse

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename='log_1.log', encoding='utf-8', level=logging.NOTSET, format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def parse():
    project = Project('users.json')
    parser = argparse.ArgumentParser(prog='Администрирование пользователей',
                                     description='Администратор может добавлять новых пользователей',
                                     epilog='Вход администратора: entrance(name, user_id),'
                                            'Добавление нового пользователя add_user(name, user_id, user_level)')
    parser.add_argument('-a', '--admin', help='Имя пользователя')
    parser.add_argument('-i', '--admin_id', type=int, help='Идентификатор пользователя')
    parser.add_argument('-n', '--name', help='Имя пользователя')
    parser.add_argument('-u', '--user_id', type=int, help='Идентификатор пользователя')
    parser.add_argument('-l', '--level_user', type=int, help='Уровень доступа')
    args = parser.parse_args()
    project.entrance(args.admin, args.admin_id)
    project.add_user(args.name, args.user_id, args.level_user)
    print(*project.users)


class Project:
    def __init__(self, json_file_path: str):
        self.admin = None
        self.json_file_path = json_file_path
        self.users = self.user_from_json()

    def dump_users(self):
        data = [{"name": user.name, "user_id": user.user_id, "access_level": user.user_level} for user in self.users]
        with open('users.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

    def user_from_json(self) -> Set[User]:
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        users = set()
        for user in data:
            users.add(User(user['name'], int(user['user_id']), int(user['access_level'])))
        return users

    def entrance(self, name: str, user_id: int):
        test_user = User(name, user_id, user_level=0)
        if test_user in self.users:
            for user in self.users:
                if test_user == user:
                    self.admin = user
                    print('Вы вошли как администратор')
        else:
            raise AccessException(name, user_id)

    def add_user(self, name: str, user_id: int, user_level: int):
        if user_level > self.admin.user_level:
            raise LevelException(self.admin, user_level)
        new_user = User(name, user_id, user_level)
        self.users.add(new_user)
        self.dump_users()
        msg = f'{__name__} - Добавлен новый пользователь {new_user}'
        logger.info(msg)


if __name__ == '__main__':
    parse()