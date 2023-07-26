# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки


from random import randint as rnd

FIELD_SIZE = 8


def arrangement_queens(data: list[tuple[int, int]]) -> bool:
    x = []
    y = []
    for item in data:
        x.append(item[0])
        y.append(item[1])

    result = True
    for i in range(FIELD_SIZE):
        for j in range(i + 1, FIELD_SIZE):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                result = False

    return result


def gen_arrangement():
    return [(rnd(1, 9), rnd(1, 9)) for _ in range(FIELD_SIZE)]


# print(gen_arrangement())

if __name__ == '__main__':
    print(arrangement_queens(gen_arrangement()))
