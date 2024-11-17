class dad: 
    def __init__(self,name): 
        self.name=name
    def display(self): 
         print(self.name)
class son(dad): 
        def __init__(self,name, grade):
             super().__init__(name)
             self.grade=grade
sonobj=son("Varun", 10)
sonobj.display()