class computer: 
    def __init__(self):
        self.__maxprice=900
    def display(self):
        print(f"The selling price is :{self.__maxprice}")
    def setmaxprice(self, price):
        self.__maxprice=price

obj1 = computer()
obj1.display()

obj1.setmaxprice(1000)
obj1.display()