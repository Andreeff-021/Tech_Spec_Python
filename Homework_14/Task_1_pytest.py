import pytest


def get_value(dct: dict, key, value_def='Нет значения'):
    if key not in dct:
        raise KeyError(f'Ключа {key} не существует')
    else:
        return dct[key]


def test_get_value():
    assert get_value({'a': 1, 'b': 2, 'c': 3}, 'a') == 1


if __name__ == '__main__':
    pytest.main(['-v'])
