# Напишите функцию для транспонирования матрицы


def matrix_transposition(array: list[[int], [int]]) -> list[[int], [int]]:
    return [list(i) for i in zip(*array)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_transposition(matrix))