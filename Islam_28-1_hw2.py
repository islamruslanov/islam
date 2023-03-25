class Figure:
    unit = "cm"

    def __init__(self):
        pass

    @property
    def perimetr(self):
        return self.__perimetr

    @perimetr.setter
    def perimetr(self, value):
        self.__perimetr = value

    def calculate_area(self):
        pass

    def calculate_perimetr(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length
        self.perimetr = self.calculate_perimetr()

    @property
    def side_length(self):
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        self.__side_length = value

    def calculate_perimetr(self):
        return self.__side_length * 4

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        print( f'Square\n'
               f'side length: {self.__side_length}{self.unit}\n'
               f'perimeter: {self.calculate_perimetr()}{self.unit}\n'
               f'area: {self.calculate_area()}{self.unit}\n')
#
class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()
        self.__length = length
        self.__width = width
        self.perimetr = self.calculate_perimetr()

    def calculate_area(self):
        return self.__width * self.__length

    def calculate_perimetr(self):
        return (self.__width + self.__length) * 2

    def info(self):
        print(f"Rectangle\n"
              f"length: {self.__length}\n"
              f"width: {self.__width}\n"
              f"perimetr: {self.calculate_perimetr()}\n"
              f"area: {self.calculate_area()}\n")

square = Square(2)
square2 = Square(4)

firstR = Rectangle(4, 5)
secondR = Rectangle(5, 5)
thirdR = Rectangle(6, 6)

spisok = [square, square2, firstR, secondR, thirdR]

for i in spisok:
    i.info()






