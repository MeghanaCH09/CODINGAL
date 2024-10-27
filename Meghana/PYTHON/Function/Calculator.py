def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("Enter two numbers to be added, substracted, mulitplies, and divided")
num1=int(input("Enter a value for the first number: "))
num2=int(input("Enter a value for the second number: "))

print("The sum of both the numebrs is,", add(num1,num2))
print("The difference between both the numebrs is,", sub(num1,num2))
print("The multiplication of both the numebrs is,", mul(num1,num2))
print("The division of both the numebrs is,", div(num1,num2))