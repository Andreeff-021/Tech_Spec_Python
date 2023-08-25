import numpy as np
import pytest


class Matrix:
    __range_value = (1, 10)

    def __init__(self, rows: int, columns: int, matrix: list[list[int]] = None):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix
        if self.matrix is None:
            self.matrix = [[rnd(*self.__range_value) for _ in range(columns)] for _ in range(rows)]

    def __add__(self, other):
        matrix = np.add(np.array(self.matrix), np.array(other.matrix)).tolist()
        rows, columns = len(matrix), len(matrix[0])
        return Matrix(rows, columns, matrix)

    def __matmul__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return None
        matrix = np.matmul(np.array(self.matrix), np.array(other.matrix)).tolist()
        rows, columns = len(matrix), len(matrix[0])
        return Matrix(rows, columns, matrix)

    def __eq__(self, other):
        return np.array_equal(np.array(self.matrix), np.array(other.matrix))

    def __gt__(self, other):
        return np.greater_equal(np.array(self.matrix), np.array(other.matrix))

    def __le__(self, other):
        return np.less_equal(np.array(self.matrix), np.array(other.matrix))

    def __str__(self):
        return f'Матрица: {self.matrix}'


@pytest.fixture
def matrices():
    matrix_1 = Matrix(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    matrix_2 = Matrix(3, 3, [[2, 2, 2], [2, 2, 2], [2, 2, 2]])
    return matrix_1, matrix_2


def test_matrix_sum(matrices):
    matrix_1, matrix_2 = matrices
    assert matrix_1 + matrix_2 == Matrix(3, 3, [[3, 3, 3], [3, 3, 3], [3, 3, 3]])


def test_matrix_matmul(matrices):
    matrix_1, matrix_2 = matrices
    assert matrix_1 @ matrix_2 == Matrix(3, 3, [[6, 6, 6], [6, 6, 6], [6, 6, 6]])


def test_matrix_eq(matrices):
    matrix_1, matrix_2 = matrices
    assert (matrix_1 == matrix_2) == False


if __name__ == '__main__':
    pytest.main(['-v'])
