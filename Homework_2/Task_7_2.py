# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction as fr

frac_num_1 = str(input("Введите первое дробное число в формате x/y: "))
frac_num_2 = str(input("Введите второе дробное число в формате x/y: "))


def sum_fractions(frac_num_1, frac_num_2):
    num_1 = int(frac_num_1.split("/")[0])
    denum_1 = int(frac_num_1.split("/")[1])
    num_2 = int(frac_num_2.split("/")[0])
    denum_2 = int(frac_num_2.split("/")[1])
    if denum_1 == denum_2:
        return print(f'Сумма {frac_num_1} и {frac_num_2} равна {num_1 + num_2}/{denum_1}')
    else:
        return print(f'Сумма {frac_num_1} и {frac_num_2} равна '
                     f'{num_1 * denum_2 + num_2 * denum_1}/{denum_1 * denum_2}')


def power_fractions(frac_num_1, frac_num_2):
    num_1 = int(frac_num_1.split("/")[0])
    denum_1 = int(frac_num_1.split("/")[1])
    num_2 = int(frac_num_2.split("/")[0])
    denum_2 = int(frac_num_2.split("/")[1])
    if num_1 % denum_2 == 0:
        num_1 /= denum_2
        denum_2 /= denum_2
    if denum_2 % num_1 == 0:
        denum_2 /= num_1
        num_1 /= num_1
    if num_2 % denum_1 == 0:
        num_2 /= denum_1
        denum_1 /= denum_1
    if denum_1 % num_2 == 0:
        denum_1 /= num_2
        num_2 /= num_2
    return print(f'Произведение {frac_num_1} и {frac_num_2} равно {int(num_1 * num_2)}/{int(denum_1 * denum_2)}')


sum_fractions(frac_num_1, frac_num_2)
power_fractions(frac_num_1, frac_num_2)
print(fr(1, 3) + fr(4, 5))
print(fr(1, 3) * fr(4, 5))
