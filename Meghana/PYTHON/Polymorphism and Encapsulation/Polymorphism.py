class kangaroo:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Hey, I'm a Kangaroo, my name is {self.name} and I am {self.age} years old.")
    def style(self):
        print("I can hop")

class koala:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Hey, I'm a Koala, my name is {self.name} and I am {self.age} years old.")
    def style(self):
        print("I can climb")

okangaroo=kangaroo("Kang", 12)
okoala=koala("Koa", 7)

for animal in(okangaroo, okoala):
    animal.style()
    animal.info()