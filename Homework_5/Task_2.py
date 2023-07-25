# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def tuple_path_name_extension(data: str) -> tuple[str, str, str]:
    return data.rsplit('/', 1)[0], \
           data.rsplit('/', 1)[1].split('.')[0], \
           data.rsplit('/', 1)[1].split('.')[1]


data_path = 'C:/Users/andre/PycharmProjects/Tech_Spec_Python/Homework_5/Task_2.py'
print(tuple_path_name_extension(data_path))