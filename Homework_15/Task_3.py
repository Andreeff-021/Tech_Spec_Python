import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename='log_3.log', encoding='utf-8', level=logging.NOTSET, format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def get_value(dct: dict, key):
    if key not in dct:
        msg = f'{get_value.__name__} - В словаре {dct} отсутствует значение {key}'
        logger.error(msg)
        raise KeyError(f'Ключа {key} не существует')
    else:
        msg = f'{get_value.__name__} - "args": ({dct}, {key}), "result": {dct[key]}'
        logger.info(msg)
        return dct[key]


if __name__ == '__main__':
    dict_1 = {'a': 1, 'b': 2, 'c': 3}
    print(get_value(dict_1, 'd'))