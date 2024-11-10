# Задание 6. Генерация с директорией
# Доработайте функции из предыдущих задач
# Генерируйте файлы в указанную директорию - отдельный параметр функции
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# Существующие файлы не должны заменяться в случае совпадения имен

__all__ = ['create_file', 'generate_file']

from random import randint, choices
from string import ascii_lowercase, digits
from os import chdir
from pathlib import Path

def create_file(extention: str, min_len: int = 6,
                max_len: int = 30,min_size: int=256, max_size: int=4096, count: int=42)->None:
    for _ in range(count):
        while True:
            file_name=''.join(choices(ascii_lowercase+digits, k = randint(min_len, max_len)))+extention
            print(Path(file_name))
            if not Path(file_name).is_file():
                break

        data = bytes(randint(0,255) for i in range(randint(min_size, max_size)))
        with open(file_name, 'wb') as f:
            f.write(data)

def generate_file(file_path: str='',**kwargs):
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if not file_path.is_dir():
        file_path.mkdir(parents=True)
    chdir(file_path)
    for key, item in kwargs.items():
            create_file(f'.{key}',count = item)

if __name__ == '__main__':
    generate_file('dir',txt=1, jpg=2, mp4=2, png=2, bin=4)