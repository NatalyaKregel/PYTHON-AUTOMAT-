'''Задание №3
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
возврат строки без изменений возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

from task_01_doctest import delsymbol
import unittest

class TestUnit(unittest.TestCase):
    def test_method(self):
        self.assertEqual(delsymbol('hello kitty'), 'hello kitty')

    def test_method_2(self):
        self.assertEqual(delsymbol('Hello kitty'), 'hello kitty')

    def test_method_3(self):
        self.assertEqual(delsymbol('Hello, Kitty!'), 'hello kitty')

    def test_method_4(self):
        self.assertEqual(delsymbol('Hello яitty'), 'hello kitty')

    def test_method_5(self):
        self.assertEqual(delsymbol('Hello%, яitt%y'), 'hello kitty')

if __name__ == '__main__':
    unittest.main(verbosity=2)

