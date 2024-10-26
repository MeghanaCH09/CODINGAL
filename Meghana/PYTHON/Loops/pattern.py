pattern=int(input("Enter the number of rows: "))

for i in range (1,pattern+1):
    for e in range(i):
        print("*", end="")
    print()