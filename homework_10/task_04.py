'''
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. 
Задачи должны решаться через вызов методов экземпляра.
'''
'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
-   Для дочерних объектов указывайте родительскую директорию.
-   Для каждого объекта укажите файл это или директория.
-   Для файлов сохраните его размер в байтах,
    а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''


import os
from pathlib import Path
import csv
import json
import pickle

__all__ = [
    'recursive_directories'
]


def write_json(data: dict) -> None:
    with open('info.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Запись в JSON файл - успешна!")


def write_csv(fieldnames_for_csv: list, rows_for_csv: list) -> None:
    with open('info.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_for_csv)
        writer.writeheader()
        writer.writerows(rows_for_csv)
    print("Запись в csv файл - успешна!")


def write_pickle(data: dict) -> None:
    with open('info.pickle', 'wb') as f:
        pickle.dump(f'{pickle.dumps(data)}', f)
    print("Запись в pickle файл - успешна!")


def get_size_for_dir(path: Path = '.') -> int:
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_size_for_dir(entry.path)
    return result


def get_size(path: Path = '.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_size_for_dir(path)


def recursive_directories(path: Path) -> None:
    data_for_json = {}
    fieldnames_for_csv = ['name', 'path', 'size', 'type']
    rows_for_csv = []

    for dir_path, dir_names, file_names in os.walk(path):
        data_for_json.setdefault(dir_path, {})
        for dir_name in dir_names:
            size = get_size(dir_path + '/' + dir_name)
            data_for_json[dir_path].update({dir_name: {'size': size, 'type': 'directory'}})
            rows_for_csv.append({'name': dir_name, 'path': dir_path, 'size': size, 'type': 'directory'})
        for file_name in file_names:
            size = get_size(dir_path + '/' + file_name)
            data_for_json[dir_path].update({file_name: {'size': size, 'type': 'file'}})
            rows_for_csv.append({'name': file_name, 'path': dir_path, 'size': size, 'type': 'file'})
    write_json(data_for_json)
    write_csv(fieldnames_for_csv, rows_for_csv)
    write_pickle(data_for_json)


if __name__ == '__main__':
    recursive_directories(Path("C:\\Users\\Admin\\MyProjectsPython\\GB_python\\venv"))

    