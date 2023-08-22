'''
Задача 5:
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
'''


class Rectangle:

    def __init__(self, side_a: float, side_b: float = None):
        self.side_a = side_a
        self.side_b = side_a if side_b is None else side_b
        self._area = self.side_a * self.side_b
        self._long = 2 * (self.side_a + self.side_b)

    def get_area(self) -> float:
        return self._area

    def get_long(self) -> float:
        return self._long

    def __add__(self, other):
        new_long = self._long + other._long
        new_a = self.side_a + other.side_a
        new_b = new_long / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        new_long = abs(self._long - other._long)
        new_a = abs(self.side_a - other.side_a)
        new_b = new_long / 2 - new_a
        return Rectangle(new_a, new_b)

    def __eq__(self, other):
        return self._area == other._area

    def __lt__(self, other):
        return self._area < other._area

    def __str__(self):
        return f'Класс создает прямоугольник с параметрами: длина = {self.side_a} ' + \
               f'ширина = {self.side_b}, периметр = {self._long}, площадь = {self._area}'

    def __repr__(self):
        return f'(Rectangle{self.side_a}, {self.side_b}, {self._long}, {self._area})'


if __name__ == '__main__':
    rectangle1 = Rectangle(5, 6)
    rectangle2 = Rectangle(3, 4)
    print(f'Периметр прямоугольника со сторонами ({rectangle1.side_a, rectangle1.side_b} = {rectangle1.get_long()}')
    print(f'Площадь прямоугольника со сторонами ({rectangle1.side_a, rectangle1.side_b} = {rectangle1.get_area()}')
    new_rec = rectangle1 + rectangle2
    print(f'{rectangle1.get_long() = }, {rectangle2.get_long() = }, {new_rec.get_long() = }')
    new_rec = rectangle1 - rectangle2
    print(f'{rectangle1.get_long() = }, {rectangle2.get_long() = }, {new_rec.get_long() = }')
    print(f'{new_rec = }')
    print(rectangle1 == rectangle2)
    print(rectangle1 > rectangle2)