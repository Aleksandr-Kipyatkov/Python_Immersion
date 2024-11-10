# Задание 4. Генерация файлов
# Создайте функцию, которая создает файлы с заданным расширением
# Функция принимает параметры: расширение, минимальная длина имени файла по умолчанию 6,
# максимальная длина имени файла по умолчанию 30, минимальное число байт по умолчанию 256,
# максимальное число байт по умолчанию 4096, количество файлов по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона

__all__ = ['create_file']

from random import randint, choices
from string import ascii_lowercase, digits


def create_file(extention: str, min_len: int = 6,
                max_len: int = 30,min_size: int=256, max_size: int=4096, count: int=42)->None:
    for _ in range(count):
        file_name=''.join(choices(ascii_lowercase+digits, k = randint(min_len, max_len)))+extention
        data = bytes(randint(0,255) for i in range(randint(min_size, max_size)))
        print(file_name, data)
        with open(file_name, 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    create_file('.txt', count=3)
