from abc import ABC, abstractmethod

class polygon(ABC):

    def shape(self):
        pass

class Triangle(polygon):
    def shape(self):
        print("TRIANGLE")
        print("The formula to calcualte the area of a triangle is")
        print("A = 1/2*B*H, where b=base and h=height")

class Quadrilateral(polygon):
    def shape(self):
        print("QUADRILATERAL")
        print("The formula to calcualte the area of a quarilateral is")
        print("A = base*height")

class Pentagon(polygon):
    def shape(self):
        print("PENTAGON")
        print("The formula to calcualte the area of a pentagon is")
        print("A = 1/2*p*a, where p=perimeter and a=apothem")

class Hexagon(polygon):
    def shape(self):
        
        print("HEXAGON")
        print("The formula to calcualte the area of a hexagon is")
        print("A = (3√3 s^2)/2, where s=side length")
        
class Heptagon(polygon):
    def shape(self):
        print("HEPTAGON")
        print("The formula to calcualte the area of a heptagon is")
        print("A = (7a²/4) cot (π/7), where a=side length")

t=Triangle()
t.shape()

q=Quadrilateral()
q.shape()

p=Pentagon()
p.shape()

hex=Hexagon()
hex.shape()

hep=Heptagon()
hep.shape()