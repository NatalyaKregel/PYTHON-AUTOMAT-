'''
- Подсчитать количество встречаемых слов и вернуть 10 самых частых.
- Не учитывать знаки препинания
- Не учитывать регистр символов
'''
import re
from collections import Counter
import task_02_basic_identical_words
import doctest

def identical_words(text: str):
    '''
    return all ...
    >>> identical_words('сегодня сегодня солнце изморозь изморозь изморозь')
    [('изморозь', 3), ('сегодня', 2), ('солнце', 1)]
    >>> identical_words('сегодня сегодня, солнце изморозь! изморозь. изморозь')
    [('изморозь', 3), ('сегодня', 2), ('солнце', 1)]
    >>> identical_words('Сегодня сегодня СОЛнце изморозь изморозь Изморозь')
    [('изморозь', 3), ('сегодня', 2), ('солнце', 1)]
    '''

    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

if __name__ == '__main__':
    print(identical_words)
    doctest.testmod(verbose=True)


