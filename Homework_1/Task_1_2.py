# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

START_DIGIT = 2
END_DIGIT = 11
start_digit_2 = 2
end_digit_2 = 6
count = 0
str = ""

print(" " * 22 + "ТАБЛИЦА УМНОЖЕНИЯ")

for i in range(START_DIGIT, END_DIGIT):
    for j in range(start_digit_2, end_digit_2):
        if i > 9 and (i * j > 9):
            str += f'{j} x {i} = {i * j}       '
        elif i * j > 9:
            str += f'{j} x {i} = {i * j}        '
        else:
            str += f'{j} x {i} = {i * j}         '
        count += 1
        if count == 4:
            print(str)
            str = ""
            count = 0

print(" ")
start_digit_2 = 6
end_digit_2 = 10

for i in range(START_DIGIT, END_DIGIT):
    for j in range(start_digit_2, end_digit_2):
        if i > 9 and (i * j > 9):
            str += f'{j} x {i} = {i * j}       '
        elif i * j > 9:
            str += f'{j} x {i} = {i * j}        '
        else:
            str += f'{j} x {i} = {i * j}         '
        count += 1
        if count == 4:
            print(str)
            str = ""
            count = 0