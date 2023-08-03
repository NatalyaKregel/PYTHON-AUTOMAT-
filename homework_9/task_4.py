'''
Напишите следующие функции:
    Нахождение корней квадратного уравнения
    Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
'''

from cmath import sqrt
from random import randint
import csv
from typing import Callable
from functools import wraps
from pathlib import Path
import json




def write_csv(fieldnames_for_csv: list, rows_for_csv: list) -> None:
    with open('random_numbers.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_for_csv)
        writer.writeheader()
        writer.writerows(rows_for_csv)
    print("Запись в csv файл - успешна!")


def solving_quadratic_equation_from_csv(file_name: str = 'random_numbers.csv'):
    def deco(func: Callable):
        @wraps(func)
        def reader_csv(*args, **kwargs):
            with open(file_name, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    args = [complex(item) for item in row]
                    result = func(*args, **kwargs)
                    yield result

        return reader_csv
    return deco


def generate_csv_random_nums(count_rows: int = randint(100, 1000)) -> None:
    fieldnames_for_csv = ["number_1", "number_2", "number_3"]
    rows = []
    for _ in range(count_rows):
        rows.append(
            {'number_1': randint(-100, 100), 'number_2': randint(-100, 100), 'number_3': randint(-100, 100)})
    write_csv(fieldnames_for_csv, rows)


def save_to_json(func):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []

    def write_json(*args, **kwargs):
        for result in func(*args, **kwargs):
            if result:
                data = {'args': args, **kwargs, 'result': str(result)}
                json_file.append(data)
                with open(file, 'w') as f:
                    json.dump(json_file, f, indent=2)
                # print("Запись в JSON файл - успешна!")
            else:
                break

    return write_json


@save_to_json
@solving_quadratic_equation_from_csv('random_numbers.csv')
def solving_quadratic_equation(coef_a: complex, coef_b: complex, coef_c: complex):
    discriminant = coef_b ** 2 - 4 * coef_a * coef_c
    # print(f"Дискриминант D = {round(discriminant, 2)}")
    if discriminant != 0 and coef_a != 0:
        x1 = (-coef_b + sqrt(discriminant)) / (2 * coef_a)
        x2 = (-coef_b - sqrt(discriminant)) / (2 * coef_a)
        # print(f"x1 = {x1}; x2 = {x2}")
        return discriminant, x1, x2
    elif coef_a != 0:
        x = -coef_b / (2 * coef_a)
        # print(f"x = {x1}")
        return discriminant, x, 0


if __name__ == '__main__':
    # print(solving_quadratic_equation(-4, 10, 10))
    generate_csv_random_nums()
    solving_quadratic_equation()
    


