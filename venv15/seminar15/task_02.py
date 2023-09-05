'''
Задание №2
На семинаре про декораторы был создан логирующий декоратор.
Он сохранял аргументы функции и результат её работы в файл.
Напишите аналогичный декоратор, но внутри используйте модуль logging.
'''

import logging
from typing import Callable


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def decor_saved_result_json(fun: Callable):
    def wrapper(*args):
        res = fun(*args)

        logger.info(f'АВТО: деление на ноль числа {args[0]} на {args[1]} = {res}')

    return wrapper


@decor_saved_result_json
def diving(a, b):
    try:
        res = a / b
        # logger.info(f'деление на ноль числа {a} на {b} = {res}')
        return res
    except ZeroDivisionError as exp:
        #   logger.error(f'деление на ноль числа {a}')
        print('делить на ноль нельзя')
    return float('inf')


if __name__ == '__main__':
    logging.basicConfig(filename='project.log', filemode='a', encoding='utf-8', level=logging.NOTSET)
    logger = logging.getLogger(__name__)
    diving(2, 6)
    diving(2, 0)
    diving(6, 5)

