# Задание 4. csv в json
# Прочитайте созданный в прошлом задании csv файл без csv.DictReader
# Дополните id до 10 цифр незначащими нулями
# В именах первую букыу сделайте прописной
# Добавьте поле хеш на основе имени и идентификатора
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь
# Имя исходного и конечного файла передавайте как аргументы функции
__all__ = ['csv_to_json']

import csv
import json
from pathlib import Path

def csv_to_json(csv_file: Path, json_file: Path) -> None:
    json_list = []
    with open(csv_file, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
            if i!=0:
                level, id, name = line
                json_dict['level'] = level
                json_dict['id'] = f'{int(id):010}'
                json_dict['name'] = name.lower()
                json_dict['hash'] = hash(f'{json_dict['name']}{json_dict['id']}')
                json_list.append(json_dict)
    with open(json_file, 'w', encoding='utf-8') as f_write:
        json.dump(json_list,f_write, indent=2)

if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('users_new.json'))
