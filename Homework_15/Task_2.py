import logging
import argparse

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(filename='log_2.log', encoding='utf-8', level=logging.NOTSET, format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def numbers():
    while True:
        try:
            num = int(input('Введите число: '))
            print(num)
            msg = f'{numbers.__name__} - Добавлено целое число {num}'
            logger.info(msg)
            break
        except ValueError as e:
            msg = f'{numbers.__name__} - Не целое цеисло {e}'
            logger.error(msg)
            print(f'Не целое цеисло {e}')
            try:
                num = float(input('Введите число: '))
                print(num)
                break
            except ValueError as e:
                msg = f'{numbers.__name__} - Не float {e}'
                logger.error(msg)
                print(f'Не float {e}')


if __name__ == '__main__':
    numbers()
