from abc import ABC
class animal(ABC): 
    def sound(self): 
        pass

class dog(ABC): 
    def sound(self): 
        print("bow") 
class cat(ABC): 
    def sound(self): 
        print("meow") 
class lion(ABC): 
    def sound(self): 
        print("roar") 
catobj=cat()
catobj.sound()
dogobj=dog()
dogobj.sound()
lionobj=lion()
lionobj.sound()