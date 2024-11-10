# Задание 1. Добавление в файл
# Напишите функцию, которая заполняет файл (добавляет в конец), случайными парами чисел
# Первое число int, второе float, разделены вертикальной чертой
# Минимальное число -1000, максимальное 1000
# Количество строк и имена файла передаются как элементы

__all__ = ['fill_num']

from random  import randint, uniform
from pathlib import Path

MIN_NUMBER = -1000
MAX_NUMBER = 1000

def fill_num(filename: str|Path, count: int):
    with open(filename, 'a', encoding = 'utf-8') as f:
        for _ in range(count):
            f.write(f"{randint(MIN_NUMBER, MAX_NUMBER)}|{uniform(MIN_NUMBER, MAX_NUMBER)}\n")


if __name__ == '__main__':
    fill_num('file.txt', 100)