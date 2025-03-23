from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, name):
        self._name = name  
    
    @abstractmethod
    def area(self):
        pass
    
    def get_name(self):
        return self._name


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__('Rectangle')
        self.__length = length  
        self.__width = width    
    
    def area(self):
        return self.__length * self.__width


class Square(Polygon):
    def __init__(self, side):
        super().__init__('Square')
        self.__side = side  
    
    def area(self):
        return self.__side ** 2

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__('Triangle')
        self.__base = base 
        self.__height = height 
    
    def area(self):
        return 0.5 * self.__base * self.__height

def calculate_area(polygon):
    print(f"The area of the {polygon.get_name()} is: {polygon.area()}")

rectangle = Rectangle(10, 5)
square = Square(4)
triangle = Triangle(6, 3)


calculate_area(rectangle)
calculate_area(square)
calculate_area(triangle)
