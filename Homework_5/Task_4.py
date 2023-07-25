# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci(n):
    fib_1, fib_2 = 0, 1
    for _ in range(n):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2

print(list(fibonacci(10)))