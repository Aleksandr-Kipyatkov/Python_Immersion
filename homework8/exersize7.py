# Задание 7. Считать csv
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader
# Распечатайте его как pickle строку
__all__ = ['csv_to_pickle']
import csv
import pickle
from pathlib import Path

def csv_to_pickle(csv_file: Path) -> None:
    with open(csv_file, 'r', encoding='utf-8', newline='') as f_read:
        pickle_list = []
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            if i==0:
                pickle_keys = line
            else:
                pickle_dict = {key: value for key, value in zip(pickle_keys, line)}
                pickle_list.append(pickle_dict)
        print(pickle.dumps(pickle_list))

if __name__ == '__main__':
    csv_to_pickle(Path('users_new.csv'))