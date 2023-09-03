'''
Сщздайте функцию, которая удаляет из текста все символы, кроме букв латинского
алфавита и пробелов. Возвращается строка в нижнем регистре.
'''
import doctest
'''
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

import re
import doctest

def delsymbol(text: str):
    '''
    deleter all ...
    >>> delsymbol('hello')
    'hello'
    >>> delsymbol('Hello')
    'hello'
    >>> delsymbol('hello, kitty!')
    'hello kitty'
    >>> delsymbol('hello китти')
    'hello '
    >>> delsymbol('Hello, китти!')
    'hello '

    '''
    regex = re.compile('[^a-zA-Z ]')
    return regex.sub('', text).lower()

if __name__ == '__main__':
    print(delsymbol('Give me! a cup of wa@ter!'))
    doctest.testmod(verbose=True)


