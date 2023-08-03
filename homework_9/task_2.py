'''
Задание №5:
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.

Задание №6:
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов
'''

import json
import os
from functools import wraps
from random import randint
from typing import Callable

def check(func:callable) -> Callable[[int,int], None]:
    @wraps(func)
    def wrapper(*args):
        if not args[0] in range(1, 101) or not args[1] in range(1,11):
            return func(randint(1,100), randint(1,10))
        return func(*args)
    
    return wrapper


def repeat(count:int) -> Callable:
    def decorator(func:Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    
    return decorator
            

def log(func:Callable) -> Callable[..., None]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = {}
        name = f"{func.__name__}.json"
        if os.path.exists(name):
            with open(name,encoding="utf-8") as jon_f:
                result = json.load(json_f)

        with open(name, "w", encoding="utf-8") as json_f:
            result[str(args)] = args
            result.update(**kwargs)
            result["result"] = func(*args, **kwargs)
            json.dump(result, json_f, indent=2, ensure_ascii=False)

    return wrapper


@log
@check
@repeat(count=2)
def guess(num:int, count:int):
    secret = randint(1, num)
    print(f" Угадай число от 1 до {num}. У Вас {count} попыток")

    for attept in range(count):
        guess = int(input(f"Попытка №{attept + 1}: "))

        if guess < secret:
            print("Загаданное число больше")
        elif guess > secret:
            print("Загаданное число меньше")
        else:
            print("Поздравляю! Вы угадали число!")
            break

if __name__ == '__main__':
    guess(420, 60)
            



    