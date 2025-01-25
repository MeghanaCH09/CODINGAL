def checkIfDifferent(number1, number2):
    if ((number1 ^ number2) != 0): 
        print("Numbers are different")
    else: 
        print("Both numbers are not different")

number1 = int(input("Enter first numbers to compare: "))
number2 = int(input("Enter your second number to compare: "))
checkIfDifferent(number1, number2)