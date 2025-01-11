number1 = int(input("Enter your first value: "))
number2 = int(input("Enter your second value: "))

for i in range (max(number1, number2), (number1 * number2)): 
    if i % number1 == i % number2 == 0: 
        lcm = i
print(f"The LCM of {number1} and {number2} is {lcm}")

