#Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
#Для цифры верните её квадрат, например 5 - 25
#Для двузначного числа произведение цифр, например 30 - 0
#Для трёхзначного числа его зеркальное отображение, например 520 - 25
#Если число не из диапазона, запросите новое число. Откажитесь от магических чисел. В коде должны быть один input и один print

import logging
logging.basicConfig(filename='my_func2.log', filemode='a', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger(__name__)

import math
def number(num):
    if num <= 0:
        logger.error(f'num должно быть > 0')
        return float('inf')
    if num > 999:
        logger.error(f'num должно быть < 999')
        return float('inf')
        #raise ValueError('num должно быть < 999')
    if math.floor(num) != num:
        logger.error(f'num должно быть целым числом')
        return float('inf')
        #raise ValueError('num должно быть целым числом')
    if (num > 0) and (num < 1000):
        if num < 10:
            print(f"Квадрат цифры {num} - {num ** 2}")
        elif 9 < num < 100:
            first_number = num // 10
            second_number = num % 10
            print(f"произведение цифр двухзначного числа {num} - {first_number * second_number}")
        else:
            first_number = num // 100
            second_number = num % 100 // 10
            third_number = num % 10
            print(f"для трехзначного числа {num} зеркальное число - {third_number * 100 + second_number * 10 + first_number}")
        quit()
    print('Вы ввели некорректное число, попробуйте еще раз')

num = 108

print(number(num))