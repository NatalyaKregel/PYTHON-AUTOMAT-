'''
Задание №3
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
'''

import logging
from functools import wraps
from typing import Callable


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def decor_saved_result_json(fun: Callable):
    @wraps(fun)
    def wrapper(*args):
        # res = fun(*args)
        if args[1] == 0:
            logger.error(f'АВТО3: деление числа {args[0]} на {args[1]} = {fun(*args)}, функция "{fun.__name__}()"')
        else:
            logger.info(f'АВТО3: деление числа {args[0]} на {args[1]} = {fun(*args)}, функция "{fun.__name__}()"')

    return wrapper


@decor_saved_result_json
def diving(a, b):
    try:
        res = a / b
        # logger.info(f'деление на ноль числа {a} на {b} = {res}')
        return res
    except ZeroDivisionError as exp:
        # logger.error(f'деление на ноль числа {a}')
        print('делить на ноль нельзя')
    return float('inf')


if __name__ == '__main__':
    FORMAT = '{levelname} - {asctime}. в {created} секунд записала сообщение: {msg}'

    logging.basicConfig(format=FORMAT, filename='project.log', style='{', filemode='a', encoding='utf-8', level=logging.NOTSET)
    logger = logging.getLogger(__name__)
    diving(2, 6)
    diving(2, 0)