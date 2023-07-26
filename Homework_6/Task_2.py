# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам
# дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# __all__ = ['arrangement_queens']
#
FIELD_SIZE = 8

def arrangement_queens(*args) -> bool:
    x = []
    y = []
    for item in args:
        x.append(item[0])
        y.append(item[1])

    correct = True
    for i in range(FIELD_SIZE):
        for j in range(i + 1, FIELD_SIZE):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False

    return correct


if __name__ == '__main__':
    print(arrangement_queens((1, 3), (2, 6), (3, 8), (4, 1), (5, 4), (6, 7), (7, 5), (8, 2)))