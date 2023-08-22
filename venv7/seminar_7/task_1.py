'''
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции. 
'''

from random import randint, uniform 

MIN_NUM = -1000
MAX_NUM = 1000

def add_number(count: int, name_file: str):

    with open('name_file.txt', 'a', encoding='utf-8') as f:
        for i in range(0, count):
            f.write(f'{randint(MIN_NUM, MAX_NUM+1)} | {uniform(MIN_NUM, MAX_NUM)}\n')

if __name__=='__main__':
    add_number(5, 'name_file.txt')            
