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

'''
    def test_nagative_value(self):
        with self.assertRaises(ValueError) as e:
            calculation('jjj')
        self.assertEqual('Строка должна содержать только буквы', 'Строка должна содержать только буквы')
'''

if __name__ == '__main__':
    unittest.main(verbosity=2)

