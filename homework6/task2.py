# 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# Создайте модуль и напишите в нем фенкцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или иложь, если такая дата невозможна
# Для простоты договоримся, что год может быть в диапазоне [1,9999]
# Весь период 1 января 1 года - 31 декабря 9999 года действует Григорианский календарь
# Проверку года на високосность вынести в отдельную защищенную функцию

__all__ = ['check_date']

from sys import argv


def _is_leap(year: int) -> bool:
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


def check_date(full_date: str) -> bool:
    day, month, year = (int(i) for i in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False
    elif month == 2 and (day > 29 or (day == 29 and not _is_leap(year))):
        return False
    return True


if __name__ == '__main__':
    if len(argv) > 1:
        print(f'Проверка даты {argv[1]} = {check_date(argv[1])}')

