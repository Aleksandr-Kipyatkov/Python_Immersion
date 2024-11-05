# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


__all__ = ['generate_board']

from random import randint
from task3 import are_queens_safe


def generate_board():
    board = []
    for i in range(1,9):
        board.append((i,randint(1, 8)))
    return board


if __name__ == '__main__':

    for _ in range(4):
        while True:
            positions=generate_board()
            if are_queens_safe(positions):
                break

        print(f'В комбинации {positions} ферзи не бьют друг друга')

