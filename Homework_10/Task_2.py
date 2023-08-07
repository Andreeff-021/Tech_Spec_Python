# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

import json
import csv


class ProcessNumAndNames:
    def __init__(self, path_nums_names, path_json):
        self.path_nums_names = path_nums_names
        self.path_json = path_json

    def process_num_and_names(self):
        nums_names_dict = {}
        with open(self.path_nums_names, 'r', encoding='utf-8') as input_file:
            for line in input_file:
                name_str, num_str = line.split('|')
                nums_names_dict[name_str.capitalize()] = float(num_str)

        with open(self.path_json, 'w', encoding='utf-8') as json_file:
            json.dump(nums_names_dict, json_file, ensure_ascii=False, indent=2)


class JsonToCsv:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path

    def json_to_csv(self):
        with open(self.json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(data)
        rows = []
        for access_level, users in data.items():
            for user_id, name in users.items():
                rows.append({"access_level": int(access_level), "id": int(user_id), "name": name})
        print(rows)
        with open('csv_file.csv', 'w', encoding='utf-8', newline='') as csv_file:
            csv_dict = csv.DictWriter(csv_file, fieldnames=['access_level', 'id', 'name'], dialect='excel')
            csv_dict.writeheader()
            csv_dict.writerows(rows)


if __name__ == '__main__':
    pro_1 = ProcessNumAndNames(r'C:\Users\andre\PycharmProjects\Tech_Spec_Python\Seminar_7\result.txt', 'json_file.json')
    pro_1.process_num_and_names()

    js_2 = JsonToCsv(r'C:\Users\andre\PycharmProjects\Tech_Spec_Python\Seminar_8\file_2.json')
    js_2.json_to_csv()