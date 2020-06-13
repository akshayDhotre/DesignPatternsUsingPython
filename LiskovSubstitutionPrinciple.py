# LSP
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Squre(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


# any method desughed to work with class should work with all inherited classes 
def use_it(rect):
    w = rect.width
    rect.height = 10
    expected_area = w * 10
    print(f'Expected an area of {expected_area}, but got {rect.area}')


rc = Rectangle(2,3)
use_it(rc)

sq = Squre(5)
use_it(sq)
