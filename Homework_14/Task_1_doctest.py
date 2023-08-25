def get_value(dct: dict, key, value_def='Нет значения'):
    """
    >>> get_value({'a': 1, 'b': 2, 'c': 3}, 'a')
    1
    """
    if key not in dct:
        raise KeyError(f'Ключа {key} не существует')
    else:
        return dct[key]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
