'''
- Подсчитать количество встречаемых слов и вернуть 10 самых частых.
- Не учитывать знаки препинания
- Не учитывать регистр символов
'''

from task_02_doctest import identical_words
import unittest

class TestUnit(unittest.TestCase):
    def test_identical_words(self):
        self.assertEqual(identical_words('сегодня сегодня солнце изморозь изморозь изморозь'), [('изморозь', 3), ('сегодня', 2), ('солнце', 1)])

    def test_punctuation_words(self):
        self.assertEqual(identical_words('сегодня сегодня! солнце, изморозь изморозь. изморозь'), [('изморозь', 3), ('сегодня', 2), ('солнце', 1)])

    def test_register_words(self):
        self.assertEqual(identical_words('СЕГодня сегодня солнЦЕ изморозь изморозь изморозЬ'), [('изморозь', 3), ('сегодня', 2), ('солнце', 1)])

if __name__ == '__main__':
    unittest.main(verbosity=2)

