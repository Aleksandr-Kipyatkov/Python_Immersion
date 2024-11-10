# Задание 3. Слияние файлов
# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами
# Перемножьте пары чисел, в новый файл сохраните имя и произведение
# Если результат умножения отрицательный, сохраните имя строчными буквами и произведение по модулю
# Если результат умножения положительный, сохраните имя прописными буквами и произведение, округленное до целого
# В результирующем файле должно быть столько строк, сколько в более длинном файле
# При достижении конца более короткого файла возвращайтесь в его начало

__all__ = ['read_line_or_begin', 'convert']

from pathlib import Path
from typing import TextIO


def read_line_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.rstrip()


def convert(names: str | Path, numbers: str | Path, results: str | Path):
    with (open(names,'r',encoding='utf-8') as f_names,
          open(numbers, 'r', encoding='utf-8') as f_numbers,
          open(results, 'w', encoding='utf-8') as f_results,
          ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        max_len = max(len_names, len_numbers)
        for i in range(max_len):
            name = read_line_or_begin(f_names)
            num = read_line_or_begin(f_numbers)
            num1, num2 = num.split('|')
            num1, num2 = int(num1), float(num2)
            mult = num1*num2
            if mult<0:
                f_results.write(f'{name.upper()}|{abs(mult)}\n')
            else:
                f_results.write(f'{name.lower()}|{int(mult)}\n')

if __name__ == '__main__':
    convert('names.txt', 'file.txt', 'result.txt')



