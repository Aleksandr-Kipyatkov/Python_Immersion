# Задание 7. Сортировка файлов
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и тд
# Каждая группа включает файлы с несколькими расширениями
# В исходной папке должны остаться только файлы, которые не подошли для сортировки

__all__ = ['sort_files']

import os
from os import chdir
from pathlib import Path

def sort_files(path: str|Path, **kwargs):
    chdir(path)
    reverse_dict = {}
    for key, item in kwargs.items():
        file_dir = Path(key)
        if not file_dir.is_dir():
            os.mkdir(file_dir)
        for i in item:
            reverse_dict[f'.{i}']=key
    for file in Path.cwd().iterdir():
        if file.is_file() and file.suffix in reverse_dict:
            file.replace(reverse_dict[file.suffix]+'/'+file.name)


if __name__ == '__main__':
    sort_files('dir', text = ['txt'], video = ['mp4'], photo = ['jpg', 'png'])