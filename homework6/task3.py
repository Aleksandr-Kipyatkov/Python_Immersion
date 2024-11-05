# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


__all__ = ['are_queens_safe']


def are_queens_safe(queens_positions):
    rows = set()
    cols = set()
    diag1 = set()
    diag2 = set()

    for row, col in queens_positions:
        if row in rows or col in cols or (row - col) in diag1 or (row + col) in diag2:
            return False
        rows.add(row)
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

    return True


if __name__ == '__main__':

    positions = ((5, 6), (1, 4), (2, 2), (7, 3), (8, 7), (4, 8), (6, 1), (3, 5))

    if are_queens_safe(positions):
        print(f'В комбинации {positions} ферзи не бьют друг друга')
    else:
        print(f'В комбинации {positions} есть бьющие друг друга ферзи')

    positions = ((1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8))

    if are_queens_safe(positions):
        print(f'В комбинации {positions} ферзи не бьют друг друга')
    else:
        print(f'В комбинации {positions} есть бьющие друг друга ферзи')

