'''
Задание №5
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
'''


class Rectangle:
    
    __slots__ = ('_height', '_width')


    def __init__(self, height: int, width=None):
        self._height = height
        if width:
            self._width = width
        else:
            self._width = height

    def get_perimetr(self):
        return 2 * (self._height + self._width)

    def ger_area(self):
        return self._width * self._height
    

    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._height

    @height.setter
    def height (self, value):
        if value <= 0:
            raise ValueError("Должно быть больше нуля")
        self._height = value

    @width.setter
    def width (self, value):
        if value <= 0:
            raise ValueError("Должно быть больше нуля")
        self._width = value   


    def __str__(self):
        return f'прямоугольник ({self._width}x{self._height}), S = {self.get_area()}'

    def __repr__(self):
        return f'размеры: ({self._width}x{self._height}), S = {self.get_area()}'        

if __name__ == "__main__":
    rect = Rectangle(2, 5)
    rect.width = 8

    print(rect)

