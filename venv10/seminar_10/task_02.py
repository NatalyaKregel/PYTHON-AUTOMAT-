'''
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''
class Rectangle:

    def __init__(self, side_a: float, side_b: float = None):
        self.side_a = side_a
        self.side_b = side_a if side_b is None else side_b

    def get_area(self) -> float:
        return self.side_a * self.side_b

    def get_long(self) -> float:
        return 2 * (self.side_a + self.side_b)


if __name__ == '__main__':
    rectangle1 = Rectangle(5, 6)
    print(f'Периметр прямоугольника со сторонами ({rectangle1.side_a, rectangle1.side_b} = {rectangle1.get_long()}')
    print(f'Площадь прямоугольника со сторонами ({rectangle1.side_a, rectangle1.side_b} = {rectangle1.get_area()}')