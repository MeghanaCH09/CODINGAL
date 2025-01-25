def multiply_one_step(a, b):
    return a * b

def multiply_with_iterations(a, b):
    result = 0
    for _ in range(b):  # Add 'a' to the result 'b' times
        result += a
    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Result using one step:", multiply_one_step(num1, num2))
print("Result using iterations:", multiply_with_iterations(num1, num2))
