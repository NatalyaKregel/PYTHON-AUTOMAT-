'''
Для цифры верните её квадрат, например 4 - 16
Для двузначного числа произведение цифр, например 25 - 10
Для трёхзначного числа его зеркальное отображение, например 183 - 381
'''
from exeptions import NegativeError, LargeNumberError, FloatNumberError
import doctest

def calculation(num: int):
    '''
    calculation all...
    >>> calculation (4)
    16
    >>> calculation(25)
    10
   >>> calculation(183)
    381
    >>> calculation(5.5)
    NegativeError

    '''
    import math

    if num <= 0:
        raise NegativeError('Число должно быть > 0')
    if num > 999:
        raise LargeNumberError('Число должно быть < 1000')
    if math.floor(num) != num:
        raise FloatNumberError('Число должно быть целым')

    if (num > 1) and (num < 999):
        if num < 10:
            num = num ** 2
        elif 9 < num < 100:
            first_number = num // 10
            second_number = num % 10
            num = first_number * second_number
        else:
            first_number = num // 100
            second_number = num % 100 // 10
            third_number = num % 10
            num = third_number * 100 + second_number * 10 + first_number


        return (num)
    print('Вы ввели некорректное число, попробуйте еще раз')

def test_exception():
    try:
        calculation(0)
    except Exception as e:
        assert e

if __name__ == '__main__':
    try:
        error_negative = NegativeError('Число должно быть > 0')
        error_large_number = LargeNumberError('Число должно быть < 1000')
        error_float_number = FloatNumberError('Число должно быть целым')
    except (NegativeError, LargeNumberError, FloatNumberError) as e:
        print(f"\n\033[31mОшибка: {e}\033[0m")
    finally:
        print(calculation)

    doctest.testmod(verbose=True)


