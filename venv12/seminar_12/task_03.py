'''
Задание №3 (дополнение к прошлым задачам)
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
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
        
    
class GeneratorFactor:

    def __init__(self, *args):

        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start, self.stop = args
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args

    def __iter__(self):
        return self
    
    def __next__(self):

        while self.start < self.stop:
            res = 1
            for item in range(1, self.start + 1):
               res *= item 
            self.start += self.step   
            return res
        raise StopIteration



if __name__== "__main__":

    factor = GeneratorFactor(2, 8, 3)
    for item in factor:
        print(item)



