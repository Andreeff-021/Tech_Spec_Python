# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

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
        return f'We have text: {self.text} and number: {self.num}.\n' \
               f'Archive of text: {self.text_archives}.\n' \
               f'Archive of nums: {self.nums_archives}'

    def __repr__(self):
        return f'Archive have text: {self.text} and number: {self.num}.\n'


if __name__ == '__main__':
    element_1 = Archive('text_1', 1)
    element_2 = Archive('text_2', 2)
    element_3 = Archive('text_3', 3)

    print(element_3.__repr__())