# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

from decimal import Decimal as dm


def gen_prize(names: list[str], salaries: list[int], awards: list[str]) -> dict[str: dm]:
    return {name: salary * dm(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)}


names = ['Петя', 'Вася', 'Ваня', 'Ирина']
salaries = [10_000, 25_000, 14_000, 17_000]
awards = ['9.5%', '7.85%', '12.33%', '16.66%']

print(gen_prize(names, salaries, awards))