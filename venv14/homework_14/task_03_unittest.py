'''
Для цифры верните её квадрат, например 4 - 16
Для двузначного числа произведение цифр, например 25 - 10
Для трёхзначного числа его зеркальное отображение, например 183 - 381
'''

from task_03_doctest import calculation
import unittest

class TestUnit(unittest.TestCase):
    def test_square(self):
        self.assertEqual(calculation(4), 16)

    def test_works(self):
        self.assertEqual(calculation(25), 10)

    def test_mirror(self):
        self.assertEqual(calculation(183), 381)

    def test_less_zero(self):
        self.assertEqual(calculation(0), 'num должно быть > 0')

    def test_less_thousand(self):
        self.assertEqual(calculation(1001), 'num должно быть < 999')

    def test_float(self):
        self.assertEqual(calculation(1.8), 'num должно быть целым числом')

    def test_int(self):
        self.assertEqual(calculation('45'), 'num должно быть числом')


if __name__ == '__main__':
    unittest.main(verbosity=2)

