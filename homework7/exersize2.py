# Задание 2. Список имен
# Напишите функцию, которая генерирует псевдоимена
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные
# Полученные имена сохраните в файл

__all__ = ['random_names']

from random  import randint, choice
from pathlib import Path

VOWELS = 'eyuioa'
CONSTANANS = 'qwertpsdfghjklzxcvbnm'

MIN_LENGTH = 4
MAX_LENGTH = 7

def random_names(filename: str|Path, count: int):
    with open(filename, 'w', encoding = 'utf-8') as f:
        cur = 1
        for _ in range(count):
            name = ''
            for i in range(randint(MIN_LENGTH, MAX_LENGTH)):
                if cur<0:
                    name += choice(VOWELS)
                else:
                    name += choice(CONSTANANS)
                cur *= -1
            f.write(f"{name.title()}\n")

if __name__ == '__main__':
    random_names('names.txt', 100)

