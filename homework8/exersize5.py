# Задание 5. json в pickle
# Напишите функцию, которая ищет json файлы в заданной директории и сохраняет их содержимое
# в виде одноименных pickle файлов
__all__ = ['json_to_pickle']

import json
import pickle
from pathlib import Path

def json_to_pickle(path: Path) -> None:
    for file in path.iterdir():
        if file.is_file() and file.suffix=='.json':
            with (open(file, 'r', encoding = 'utf-8') as f_read,
                  open(f'{file.stem}.pickle', 'wb') as f_write):
                data = json.load(f_read)
                pickle.dump(data, f_write)

if __name__ == '__main__':
    json_to_pickle(Path('.'))