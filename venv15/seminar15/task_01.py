'''
Задание №1
Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль
'''

import logging
logging.basicConfig(filename='project.log', filemode='a', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger(__name__)

def diving(a, b):
    try:
        res = a/b
        logger.info(f'деление на ноль числа {a} на {b} = {res}')
        return res
    except ZeroDivisionError as exp:
        logger.error(f'деление на ноль числа {a}')
        print('делить на ноль нельзя')
    return float('inf')

if __name__ == '__main__':
    print(diving(2, 6))