'''
- Подсчитать количество встречаемых слов и вернуть 10 самых частых.
- Не учитывать знаки препинания
- Не учитывать регистр символов
'''

import pytest
from task_02_doctest import identical_words

def test_identical_words():
    assert identical_words('сегодня сегодня солнце изморозь изморозь изморозь') == [('изморозь', 3), ('сегодня', 2), ('солнце', 1)]

def test_punctuation_words():
    assert identical_words('сегодня сегодня! солнце, изморозь изморозь. изморозь') == [('изморозь', 3), ('сегодня', 2), ('солнце', 1)]

def test_register_words():
    assert identical_words('СЕГодня сегодня Солнце изморОЗЬ изморозь измоРозь') == [('изморозь', 3), ('сегодня', 2), ('солнце', 1)]


if __name__ == '__main__':
    pytest.main(['-v'])