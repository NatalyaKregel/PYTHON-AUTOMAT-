'''
Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
'''

from collections import deque
import json

class Factorial:

    def __init__(self, count):
        self.count = count                  #запомнили
        self.archiv = deque(maxlen=count)   #создали список

    def __call__(self, number):
        res = 1
        for item in range(1, number+1):
            res *= item
        self.archiv.append((number, res))    
        return res    

    def __str__(self):
        return str(self.archiv)
    
    def __enter__ (self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('archiv.json', 'w', encoding='utf-8') as fj:
            spam = {item[0]: item[1]for item in self.archiv}
            json.dump(spam, fj, indent=2)
        
    
    
if __name__== "__main__":

    with Factorial(3) as factor:

        print(factor(5))
        print(factor(2))
        print(factor(3))
        factor(6)
        factor(2)

        print(factor)



