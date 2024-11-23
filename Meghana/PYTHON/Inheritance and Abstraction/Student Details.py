class student:
    
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def display (self):
        print(f"First Name of student is {self.firstname}")    
        print(f"Last Name of student is {self.lastname}")   

class detail(student):

    def __init__(self,firstname,lastname,rollno):
        super().__init__(firstname,lastname)
        self.rollno=rollno 

stdinfo=detail("Meghana", "Cheruvu", 3)
stdinfo.display()
print(f"Roll number of student is {stdinfo.rollno}")