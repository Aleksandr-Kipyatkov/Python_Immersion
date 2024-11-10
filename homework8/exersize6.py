# Задание 6. pickle в csv
# Напишите функцию, которая преобразует pickle файл, хранящий список словарей, в табличный csv файл
# Для тестирования возьмите pickle версию файла из задачи 4
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла
__all__ = ['pickle_to_csv']
import csv
import pickle
from pathlib import Path

def pickle_to_csv(file: Path) -> None:
    with (open(file, 'rb') as f_read,
      open(f'{file.stem}.csv','w' ,encoding = 'utf-8', newline='') as f_write):
        data = pickle.load(f_read)
        header_list = list(data[0].keys())
        print(header_list)
        csv_writer = csv.DictWriter(f_write, fieldnames = header_list, dialect = 'excel-tab')
        csv_writer.writeheader()
        csv_writer.writerows(data)

if __name__ == '__main__':
    pickle_to_csv(Path('users_new.pickle'))