# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
# print(num)
count = 10

while count > 0:
    answer = int(input("Введите число: "))
    if answer == num:
        print("Вы угадали!")
        break
    else:
        if answer > num:
            print("Меньше")
        else:
            print("Больше")
    count -= 1
    print(f"Осталось {count} попыток")

else:
    print("Попытки закончились!")
