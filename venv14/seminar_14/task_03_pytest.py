'''
Задание №4
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''
import pytest
from task_02_unittest import delsymbol

def test_method_no_ch():
    assert delsymbol('hello kitty') == 'hello kitty'

def test_method_title():
    assert delsymbol('Hello Kitty') == 'hello kitty'

def test_method_delete_symbols():
    assert delsymbol('Hello, KITTY!') == 'hello kitty'

def test_method_delete_rus():
    assert delsymbol('Hello kяtty') == 'hello ktty'

def test_method_all():
    assert delsymbol('Hello% kяtt%y') == 'hello ktty'

if __name__ == '__main__':
    pytest.main(['-v'])