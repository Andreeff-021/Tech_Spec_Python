# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

__all__ = ['write_data_json_csv_pickle', 'get_data_dir']

import csv
import json
import os
import pickle
from os.path import getsize, join


def write_data_json_csv_pickle(data: dict) -> None:
    with open('file.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    with open('file.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_dict = csv.DictWriter(csv_file, dialect='excel', fieldnames=['object', 'root', 'type', 'size'])
        rows = []
        for obj, data_obj in data.items():
            rows.append({"object": obj, "root": data_obj['root'], "type": data_obj['type'], "size": data_obj['size']})
        csv_dict.writeheader()
        csv_dict.writerows(rows)
    with open('file.pickle', 'wb') as pickle_file:
        pickle.dump(data, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)


def get_data_dir(path_dir: str) -> dict:
    data = {}
    for root, dirs, files in os.walk(path_dir):
        for obj in dirs:
            data[obj] = {"root": root, "type": get_type(join(root, obj)), "size": get_size(join(root, obj))}
        for obj in files:
            data[obj] = {"root": root, "type": get_type(join(root, obj)), "size": get_size(join(root, obj))}
    return data


def get_size_dir(path_dir: str):
    sum_dir = 0
    for root, dirs, files in os.walk(path_dir, topdown=False):
        sum_dir += sum(getsize(join(root, name)) for name in files)
    return sum_dir


def get_type(obj: str) -> str:
    if os.path.isdir(obj):
        return "dir"
    else:
        return "file"


def get_size(obj: str) -> str:
    if os.path.isdir(obj):
        return f'{get_size_dir(obj)} bytes'
    else:
        return f'{os.path.getsize(obj)} bytes'


if __name__ == '__main__':
    write_data_json_csv_pickle(get_data_dir('dir_1'))
