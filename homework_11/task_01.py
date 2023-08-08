'''
Задача 6:
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения

'''

class Rectangle:
    def __init__(self, a, b=None) -> None:
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)
    
    def get_area(self):
        return self.a * self.b
    
    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Second object is not Rectangle")
        new_a = (self.get_length() + other.get_length()) / 4
        return Rectangle(new_a)
    
    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Second object is not Rectangle")
        
        if self.get_length() < other.get_length():
            raise ValueError("Second Rectangle is more larger than first, cannot subtract it")
        
        new_a = (self.get_length() - other.get_length()) / 4
        return Rectangle(new_a)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            raise ValueError("Second object is not Rectangle")
        return self.get_area() == other.get_area()

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            raise ValueError("Second object is not Rectangle")
        return self.get_area() != other.get_area()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            raise ValueError("Second object is not Rectangle")
        return self.get_area() < other.get_area()

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            raise ValueError("Second object is not Rectangle")
        return self.get_area() <= other.get_area()

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            raise ValueError("Second object is not Rectangle")
        return self.get_area() > other.get_area()

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            raise ValueError("Second object is not Rectangle")
        return self.get_area() >= other.get_area()
    
    def __str__(self) -> str:
        return f"Rectangle with a = {self.a}, b = {self.b}, len = {self.get_length()}, area = {self.get_area()}"
    
    def __repr__(self) -> str:
        return f"Rectangle(a={self.a}, b={self.b})"


if __name__ == "__main__":
    r1 = Rectangle(2, 3)
    r2 = Rectangle(4, 5)
    print(r1)
    print(r2)

    r3 = r1 + r2
    print(r3)

    r4 = r2 - r1
    print(r4)
    try:
        r5 = r1 - r2
    except ValueError as e:
        print(e)

    print(repr(r1))

    print(r1 == r1)
    print(r1 == r2)

    print(r1 != r1)
    print(r1 != r2)

    print(r1 < r2)
    print(r1 <= r2)

    print(r2 > r1)
    print(r2 >= r1)

    try:
        print(r2 > "Hello")
    except ValueError as e:
        print(e)
    