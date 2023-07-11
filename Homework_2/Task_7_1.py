# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата

NUM_HEX = 16


def get_number_from_user():
    number = int(input("Введите число: "))
    return number


def converter_to_hex(number):
    result_str = ""
    while number > 0:
        result = number % NUM_HEX
        if result > 9:
            result_str = format(result, '#x') + result_str
        else:
            result_str = str(result) + result_str
        number //= NUM_HEX
    return print(result_str)


num = get_number_from_user()

converter_to_hex(num)
print(hex(num))




