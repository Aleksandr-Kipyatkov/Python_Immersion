# Задание 3. json в csv
# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формат csv

__all__ = ['json_to_csv']

import csv
import json
from pathlib import Path


def json_to_csv(file: Path) -> None:
    with open(file, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)
    rows = []
    for lvl, value in data.items():
        for id, name in value.items():
            rows.append({'level': int(lvl), 'id': int(id), 'name': name})
    print(rows)
    with open(file.stem + '.csv', 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    json_to_csv(Path('users.json'))
