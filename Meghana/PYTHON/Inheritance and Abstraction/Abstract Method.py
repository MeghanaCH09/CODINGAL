from abc import ABC, abstractmethod

class animal(ABC):

    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can talk, walk, and run")

class snake(animal):
    def move(self):
        print("I can crawl around")

class dog(animal):
    def move(self):
        print("I can bark")

h=human()
h.move()

s=snake()
s.move()

d=dog()
d.move()