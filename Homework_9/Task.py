# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.


import csv
from random import randint
from typing import Callable
import json
from os.path import exists


def log_to_json(func: Callable) -> Callable:
    def wrapper(*args):
        file_path = 'file_2.json'
        data = []
        if exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        result = func(*args)
        curr_data = {'args': args, 'result': result}
        data.append(curr_data)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)

    return wrapper


def quadratic_equation_from_data_csv(func: Callable) -> Callable:
    def wrapper():
        file_path = 'file_1.csv'
        gen_random_nums_to_csv(file_path)
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for item in csv_reader:
                item = list(map(float, item))
                func(*item)

    return wrapper


@quadratic_equation_from_data_csv
@log_to_json
def quadratic_equation(*args) -> str:
    a, b, c = args
    d = b ** 2 - 4 * a * c
    if d < 0:
        result = 'Корней нет'
    elif d == 0:
        result = str(f'x = {-b / (2 * a)}')
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        result = str(f'{x1 = }, {x2 = }')
    return result


def gen_random_nums_to_csv(path_file):
    count_str = (100, 1001)
    count_num = 3
    res = [[randint(*count_str) for _ in range(count_num)] for _ in range(randint(*count_str))]
    with open(path_file, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(res)


if __name__ == '__main__':
    quadratic_equation()
