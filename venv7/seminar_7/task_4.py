'''
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random
from random import sample, randint

MIN_LEN_NAME = 6
MAX_LEN_NAME = 30
MIN_SIZE = 256
MAX_SIZE = 4096
COUNT_FILE = 42
STR_CHAR = 'qwrtpsdfghjklzxcvbnmeyuioa'

def create_file(exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE, 
                max_size=MAX_SIZE, count_file=COUNT_FILE):
    for _ in range(0,count_file):
        name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp
        print(name_file)

        with open(name_file, 'wb') as f:
            f.write(bytes(randint(0,255) for _ in range (randint(min_size, max_size))))
    

if __name__ == '__main__':
    create_file('txt', count_file=3)
'''


from random import choices, randint
from string import ascii_lowercase, digits


def create_file(extension: str, min_name: int = 6, max_name: int = 30,
                min_size: int = 256, max_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    create_file('bin', count=1)            

