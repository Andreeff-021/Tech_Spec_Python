# Напишите программу банкомат.
# Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

from datetime import datetime


global balans
balans = 0
WEALTH = 5000000
SUM_ACTION = 50
COMMISSION = 1.5
MIN_COMMISSION = 30
MAX_COMMISSION = 600
PERCENT = 3
MULTI_OPERATIONS = 3
TAX = 10
global counter
counter = 0
global log
log = {}


def checking_multiplicity(cash):
    return cash % SUM_ACTION == 0


def commission(cash):
    result = cash / 100 * COMMISSION
    if result < MIN_COMMISSION:
        return MIN_COMMISSION
    elif result > MAX_COMMISSION:
        return 0
    else:
        return result



def withdraw():
    global balans
    global counter
    if balans > WEALTH:
        balans -= balans / 100 * TAX
    cash = int(input("Укажите сумму: "))
    if checking_multiplicity(cash):
        if (balans - cash - commission(cash)) < 0:
            print("Недостаточно денег")
        else:
            balans = balans - cash - commission(cash)
            counter += 1
    else:
        print("Введите сумму кратную 50")
    print(f'На балансе осталось {balans}')
    log_('снятие', cash)


def deposit():
    global balans
    global counter
    if balans > WEALTH:
        balans -= balans / 100 * TAX
    cash = int(input("Укажите сумму: "))
    if checking_multiplicity(cash):
        balans += cash
        counter += 1
    else:
        print("Введите сумму кратную 50")
    print(f'На балансе осталось {balans}')
    log_('пополнение', cash)


def log_(operation: str, cash: int):
    time_ = str(datetime.now().replace(microsecond=0))
    global log
    log[operation] = [cash, time_]


while True:
    action_money = int(input("\n1 - Снять, 2 - внести, 3 - выйти \nНомер операции: "))
    if action_money == 1:
        withdraw()
    elif action_money == 2:
        deposit()
    elif action_money == 3:
        break
    else:
        print("Неверный ввод!")
    if (counter > 0) and (counter % MULTI_OPERATIONS == 0):
        balans += round((balans / 100 * PERCENT), 2)
        print(f'Начислено {PERCENT} процента. Баланс {balans}')