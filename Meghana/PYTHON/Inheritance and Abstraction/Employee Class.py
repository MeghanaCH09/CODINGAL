class person(object):

    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def display(self):
        print(self.name)
        print(self.id)

class employee(person):

    def __init__(self,name, id, salary, join_date):
        self.salary=salary
        self.join_date=join_date
        
        person.__init__(self,name,id)
    
    def display(self):
        super().display()
        print(self.salary)
        print(self.join_date)

e=employee("Megha", 2234432, 236000, "4/10/2010")
e.display()