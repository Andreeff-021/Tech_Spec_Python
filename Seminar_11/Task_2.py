# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
    Creates one instance of the class and saves all the properties of the class in the list
    """
    _instance = None

    def __init__(self, text: str, num: int):
        """Initializes the class"""
        print('init')
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """Saves properties to a list"""
        print('new')
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums_archives = []
            cls._instance.text_archives = []
        else:
            cls._instance.nums_archives.append(cls._instance.num)
            cls._instance.text_archives.append(cls._instance.text)
        return cls._instance

    def __str__(self):
        return f'Текст: {self.text}, число: {self.num}\n' \
               f'Архив текста:\n' \
               f'{self.text_archives}.\n' \
               f'Архив чисел:\n' \
               f'{self.nums_archives}'


if __name__ == '__main__':
    element_1 = Archive('text_1', 1)
    element_2 = Archive('text_2', 2)
    element_3 = Archive('text_3', 3)
    print(element_3.text)
    print(element_3.text_archives)
    print(element_3)
