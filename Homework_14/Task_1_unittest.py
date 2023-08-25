import unittest


def get_value(dct: dict, key, value_def='Нет значения'):
    if key not in dct:
        raise KeyError(f'Ключа {key} не существует')
    else:
        return dct[key]


class TestGetValue(unittest.TestCase):
    def test_get_value(self):
        self.assertEqual(get_value({'a': 1, 'b': 2, 'c': 3}, 'a'), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)