# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнитть, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляютсч проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитается налог на богатство 10% перед каждой операцией, даже ошибочной
# любое действие выводиь сумму денег

import decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(1.5) / decimal.Decimal(100)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

account = decimal.Decimal(0)
count = 0

while True:
    command = input(f'Пополнить - {CMD_DEPOSIT}, Снять - {CMD_WITHDRAW}, Выйти - {CMD_EXIT}: ')
    if command == CMD_EXIT:
        print(f'Возьмите карту, на которой {account} у.е.')
        break
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержан налог на богатство {RICHNESS_TAX}% в размере {percent} у.е.\n',
              f'Итого на карте осталось {account} у.е.')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = int(input(f'Введите сумму в {MULTIPLICITY} у.е.: '))
        if command == CMD_DEPOSIT:
            account += amount
            count += 1
            print(f'Пополнение карты на {amount} у.е.\n',
                  f'Итого на карте {account} у.е.')
        elif command == CMD_WITHDRAW:
            withdraw_tax = amount * WITHDRAW_PERCENT
            withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
                            MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)            
            if account >= amount + withdraw_tax:
                account -= (amount + withdraw_tax)
                count += 1
                print(f'Снятие с карты {amount} у.е.\n',
                      f'Комиссия за снятие {withdraw_tax} у.е.\n',
                      f'На карте осталось {account} у.е.')
            else:
                print(f'Недостаточно денег для выполнения операции\n',
                      f'На карте {account} у.е.')
        if count % COUNT_OPER == 0:
            bonus_percent = account * ADD_PERCENT
            account += bonus_percent
            print(f'На счет начислено {ADD_PERCENT * 100}% в размере {bonus_percent} у.е.\n',
                  f'Итого на карте {account} у.е.')
    else:
        print('Неверная команда')
        
