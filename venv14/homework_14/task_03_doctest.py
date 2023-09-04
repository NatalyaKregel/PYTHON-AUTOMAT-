'''
Для цифры верните её квадрат, например 4 - 16
Для двузначного числа произведение цифр, например 25 - 10
Для трёхзначного числа его зеркальное отображение, например 183 - 381
'''

import doctest

def calculation(num):
    '''
    calculation all...
    >>> calculation(4)
    16
    >>> calculation(25)
    10
    >>> calculation(183)
    381
    >>> calculation(0)
    'num должно быть > 0'
    >>> calculation(1000)
    'num должно быть < 999'
    >>> calculation(8.9)
    'num должно быть целым числом'
    >>> calculation('42')
    'num должно быть числом'
    '''

    if not isinstance(num, (int, float)):
        return 'num должно быть числом'
    if num <= 0:
        return 'num должно быть > 0'
    if num > 999:
        return 'num должно быть < 999'
    if num != int(num):
        return 'num должно быть целым числом'

    if num < 10:
        return num ** 2
    elif 10 <= num <= 99:
        first_number = num // 10
        second_number = num % 10
        result = first_number * second_number
    else:
        first_number = num // 100
        second_number = (num // 10) % 10
        third_number = num % 10
        result = third_number * 100 + second_number * 10 + first_number

    return result

if __name__ == '__main__':
    doctest.testmod(verbose=True)