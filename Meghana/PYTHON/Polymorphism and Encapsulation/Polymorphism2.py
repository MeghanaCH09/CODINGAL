class car:
    def __init__(self, brand, warranty):
        self.brand=brand
        self.warranty=warranty
    def info(self):
        print(f"I am a {self.brand} car and I have a warranty of {self.warranty} years")
    def movement(self):
        print("I move at a certain speed")

class airplane:
    def __init__(self, brand, warranty):
        self.brand=brand
        self.warranty=warranty
    def info(self):
        print(f"I am an {self.brand} airplane and I have a warranty of {self.warranty} years")
    def movement(self):
        print("I travel on air")

class train:
    def __init__(self, brand, warranty):
        self.brand=brand
        self.warranty=warranty
    def info(self):
        print(f"I am an {self.brand} airplane and I have a warranty of {self.warranty} years")
    def movement(self):
        print("I move the fastest")

ocar=car("Volkswagen", 2)
oairplane=airplane("Emirates", 20)
otrain=train("Siemrns", 32)

for vehical in (ocar, oairplane, otrain):
    vehical.movement()
    vehical.info()