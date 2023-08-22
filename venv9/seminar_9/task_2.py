'''
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
'''

from typing import Callable
from random import randint


def check_param(func) -> Callable[[], None]:
    def wrapper(num: int, count: int, *args, **kwargs):
        if not 0 < num < 100:
            num = randint(1, 100)
        if not 0 < count < 10:
            count = randint(1, 10)
        result = func(num, count)
        return result

    return wrapper


@check_param
def binary_search_game_wrap(number: int, count: int) -> None:
    for i in range(1, count + 1):
        print(f"Попытка номер {i} из {count}.")
        user_num = int(input("Введите число от 1 до 100: \n >>> "))
        if user_num == number:
            print("Угадал!!!")
            break
        elif user_num < number:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")


if __name__ == '__main__':
    binary_search_game_wrap(randint(-10, 100), randint(-3, 10))