class computer:
    def __init__(self):
        self.__price=900
    def sell(self):
        print("Selling price is", self.__price)
    def maxprice(self, finalprice):
        self.__price=finalprice

c=computer()
c.sell()

c.maxprice(1100)
c.sell()
