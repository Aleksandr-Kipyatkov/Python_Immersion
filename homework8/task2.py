# 2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

__all__ = ['path_to_list', 'save_to_json', 'save_to_csv', 'save_to_pickle']

import os
from pathlib import Path
import json
import csv
import pickle


def path_to_list(path):
    path = Path(path)
    print(str(path))
    if not path.exists():
        raise FileNotFoundError(f'Директория {path} не найдена')
    if not path.is_dir():
        raise NotADirectoryError(f'{path} - не директория')
    
    path_list = []
    for file in path.iterdir():
        if file.is_file():
            path_list.append({'name': file.name, 
                              'path': os.path.abspath(file), 
                              'type': 'File', 
                              'size': os.path.getsize(os.path.abspath(file)), 
                              'parent_dir': str(path)})
        if file.is_dir():
            path_list.append({'name': file.name, 
                              'path': os.path.abspath(file), 
                              'type': 'Dir', 
                              'size': sum(os.path.getsize(elem) for elem in os.scandir(file)) , 
                              'parent_dir': str(path)})

    return path_list


def save_to_json(path_list, file_name='save_to_json.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(path_list, f, indent=4)


def save_to_csv(dict_list, file_name='save_to_csv.csv'):
    with open('path_to_csv.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        header = list(dict_list[0].keys())
        writer.writerow(header)
        for i in dict_list:
            writer.writerow(list(i[head] for head in header))


def save_to_pickle(data, file_name='save_to_pickle.pkl'):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def main():
    path = input('Введите путь к директории: ')
    path_list = path_to_list(path)    
    save_to_json(path_list, 'path_to_json.json')
    save_to_csv(path_list, 'path_to_csv.csv')
    save_to_pickle(path_list, 'path_to_pickle.pkl')
    


if __name__ == '__main__':
    main()
    