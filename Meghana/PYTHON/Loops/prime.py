num=int(input("Enter a numebr to check: "))
if num > 1:
    for i in range (2, int(num**0.5)+1):
        if num%i==0:
            print("The number is not a prime number")
            break
    else:
        print("The number is a prime number")
else:
    print("The number is not a prime number")