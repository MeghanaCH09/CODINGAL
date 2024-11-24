class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
result=input("Type your name: ")
obj1=student(result)
obj1.display()

class student: 
    grade = 11 
    print("Hi! I am a student of grade", grade)
ob = student()

class student1: 
    grade = 11
    name = "Varun"
    print("Hi! My name is", name, "and I am in grade", grade)
ob1 = student1()

class Parrot:
    def __init__(self,name): 
        self.name=name
    def display(self):
        print(self.name)
    
    def __init__(self,age):
        self.age=age
    def display(self): 
        print(self.age)
result=input("What is your name? ")
result=input("What is your age? ")
obj2=Parrot(result)
obj2.display()

class Parrot1: 
    name="Sing"
    name1= "Dance"
    age= 16
    print("Hi! I like to", name, "an I also like to", name1, "and I am ", age)
ob3 = Parrot1()

