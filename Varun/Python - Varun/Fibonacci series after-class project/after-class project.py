n = int(input("Enter the number of terms: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series up to", n, "term:")
    print(a)
else:
    print("Fibonacci series up to", n, "terms:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
