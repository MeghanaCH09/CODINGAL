def setOrNot(number, n): 
    mask = 1
    if (n & mask) == 1 or (n & mask) == 0:
        if number & (1 << (n-1)): 
            print("Wohoo! It is a set")
        else: 
            print("Sorry, it is not a set")
number = int(input("Enter your desired number: "))
n = int(input("Enter the bit position: "))
setOrNot(number, n)