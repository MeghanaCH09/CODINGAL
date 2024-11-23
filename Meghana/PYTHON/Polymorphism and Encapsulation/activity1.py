class cat: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    def info(self): 
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self): 
        print("Meow")

class dog: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}.")
    def make_sound(self): 
        print("Bark")

cat1 = cat("Milo", 12)
dog1 = dog("Logitech", 10)

for animal in (cat1, dog1): 
    animal.make_sound()
    animal.info()