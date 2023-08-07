# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class AinmalFabric:
    def __init__(self, class_animal: str, *args, **kwargs):
        self.class_animal = class_animal.lower()
        self.args = args
        self.kwargs = kwargs

    def make_animal(self):
        animals = {"fish": Fish, "bird": Bird, "cat": Cat}
        return animals[self.class_animal](*self.args, **self.kwargs)


class Animal:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Cat(Animal):
    def __init__(self, name, color, size, speed_run):
        super().__init__(name, color, size)
        self.speed_run = speed_run

    def get_specific(self):
        print(self.speed_run)


class Bird(Animal):
    def __init__(self, name, color, size, speed_fly):
        super().__init__(name, color, size)
        self.speed_fly = speed_fly

    def get_specific(self):
        print(self.speed_fly)


class Fish(Animal):
    def __init__(self, name, color, size, speed_swim):
        super().__init__(name, color, size)
        self.speed_swim = speed_swim

    def get_specific(self):
        print(self.speed_swim)


if __name__ == '__main__':
    fish = AinmalFabric("Fish", "Золотая рыбка", "золотая", 10, 15).make_animal()