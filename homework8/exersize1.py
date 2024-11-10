# Задание 1. Перевод в JSON
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел
# Напишите функцию, которая создает из созданного ранее файла новый с данными в формате JSON
# Имена пишите с большой буквы, каждую пару сохраняйте с новой строки
__all__ = ['convert']

import json
from pathlib import Path

def convert(file: str|Path):
    file = Path(file)
    my_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, summa = line.rstrip().split('|')
            my_dict[name.title()]=summa
    with open(file.stem+'.json', 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    convert('result.txt')