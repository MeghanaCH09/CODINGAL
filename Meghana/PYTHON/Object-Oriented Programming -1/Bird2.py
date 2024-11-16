class animal:
    

    def __init__(self,type,place):
         self.type=type
         self.place=place
    def intro(slef):
        print("The roar of a tiger is fearful")
    def details(self):
        print("I am part of the ", self.type)
        print("I live in ", self.place)  
ob=animal("Wild Animal", "SouthEast Asia")
print(ob.intro())
print(ob.details())