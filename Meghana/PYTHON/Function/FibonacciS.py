def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_sequence(terms):
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()  

num_terms = 10
print_fibonacci_sequence(num_terms)
