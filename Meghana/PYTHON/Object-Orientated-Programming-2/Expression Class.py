class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_sum(self):
        total = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {total}")

expression1 = Expression(5, 10, 15)
expression2 = Expression(20, 30, 50)

expression1.calculate_sum()
expression2.calculate_sum()  