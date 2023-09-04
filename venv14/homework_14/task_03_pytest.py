'''
Для цифры верните её квадрат, например 4 - 16
Для двузначного числа произведение цифр, например 25 - 10
Для трёхзначного числа его зеркальное отображение, например 183 - 381
'''

import pytest
from task_03_doctest import calculation

def test_square():
    assert calculation(4) == 16

def test_works():
    assert calculation(25) == 10

def test_mirror():
    assert calculation(183) == 381

if __name__ == '__main__':
    pytest.main(['-v'])