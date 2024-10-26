def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    
num = int(input("Enter your chosen number: "))

if num < 0: 
    print("The factorial does not exist, type another value garter than 0")

elif num == 0: 
    print("The factorial of 1 is 0")
else: 
    print("The factorial of", num, "is", recur_factorial(num))