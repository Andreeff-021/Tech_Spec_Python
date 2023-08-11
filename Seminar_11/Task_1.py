# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import datetime


class MyString(str):
    """
    If you use string, this class will also show you creator's name and time of crating an object.
    """
    def __new__(cls, text, creator):
        """Gives extra information about your string"""
        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = datetime.datetime.now().replace(microsecond=0)
        return instance

    def __str__(self):
        """shows not only text? But also creator's name and time of creating"""
        return f'{super().__str__()}, автор {self.creator}, время {self.time}'


my_str_1 = MyString('Текст_1', 'Владимир')
my_str_2 = MyString('Тескт_2', 'Пётр')

print(my_str_1)
print(my_str_2)
