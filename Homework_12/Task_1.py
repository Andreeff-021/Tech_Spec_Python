import csv


class Name:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError("Не все символы являются буквами!")
        elif not value.istitle():
            raise ValueError("Нет заглавной буквы!")
        else:
            setattr(instance, self.param_name, value)


class Subject:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        with open('subjects.csv', 'r', newline='') as file:
            csv_file = csv.reader(file)
            data = [''.join(line) for line in csv_file]
            if value not in data:
                raise ValueError(f'Предмет {value} отсутствует в списке ')


class Score:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Student:
    l_name = Name()
    f_name = Name()
    m_name = Name()
    subject = Subject()
    score = Score(2, 5)
    test_1 = Score(0, 100)
    test_2 = Score(0, 100)
    test_3 = Score(0, 100)

    def __init__(self, l_name, f_name, m_name, subject, score, test_1, test_2, test_3):
        self.l_name = l_name
        self.f_name = f_name
        self.m_name = m_name
        self.subject = subject
        self.score = score
        self.test_1 = test_1
        self.test_2 = test_2
        self.test_3 = test_3
        self.grade = {self.subject: {"score": self.score, "test_1": self.test_1,
                                     "test_2": self.test_2, "test_3": self.test_1}}

    def __str__(self):
        return f'{self.l_name}, {self.f_name}, {self.m_name}, {self.subject}, {self.score}, ' \
               f'test_1 = {self.test_1}, test_2 = {self.test_2}, test_3 = {self.test_3}'


if __name__ == '__main__':
    student = Student("Андреев", "Владимир", "Сергеевич", "history", 3, 38, 6, 90)
    print(student)