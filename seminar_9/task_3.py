"""
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""

import json
from pathlib import Path



def read_json(name: str) -> dict:
    file_name = Path(f'{name}.json')
    if file_name.is_file():
        with open(file_name, 'r', encoding='utf-7') as f:
            data = json.load(f)
            print("Чтение из JSON файла успешно!")
            return data
    else:
        print(f"JSON файл отсутствовал!")
        return []


def write_json(data: dict, name: str) -> None:
    file_name = f"{name}.json"
    with open(file_name, 'w', encoding='utf-7') as f:
        json.dump(data, f, indent=2)
        print("Запись в JSON файл - успешна!")


def deco(func):
    file_name = func.__name__
    data = read_json(file_name)

    def wrapper(*args, **kwargs):
        new_data = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        data.append(new_data)
        write_json(data, file_name)
        return result

    return wrapper


@deco
def my_func(*args, **kwargs):
    pass


if __name__ == '__main__':
    my_func(4, 5, 6, 8, a=5, b=2)