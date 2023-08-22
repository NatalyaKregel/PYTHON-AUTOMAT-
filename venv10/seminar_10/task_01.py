'''
Задание №1
Создайте класс окружность. Класс должен принимать радиус окружности при создании
экземпляра. У класса должно быть два метода, возвращающие длину
окружности и её площадь.
'''
import math 
#from math import pi

class Circle:
    radius = 0

    def __init__(self, radius):
        self.radius = radius
        self.__long = math.pi * self.radius * 2
        self.__area = math.pi * self.radius ** 2

    def get_long(self) -> float:
        return self.__long

    def get_area(self) -> float:
        return self.__area


if __name__ == '__main__':
    c1 = Circle(5)
    print(f'Площадь круга с радусом {c1.radius} равна {c1.get_area()}')
    print(f'Длина окружности с радусом {c1.radius} равна {c1.get_long()}')