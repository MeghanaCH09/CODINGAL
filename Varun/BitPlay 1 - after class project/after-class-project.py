def find_rightmost_set_bit(num):
    if num == 0:
        return "No set bit, the number is zero."
    
    position = 1  
    while (num & 1) == 0:
        num = num >> 1
        position += 1

    return position
try:
    number = int(input("Enter a number: "))
    result = find_rightmost_set_bit(number)
    print(f"The position of the rightmost set bit is: {result}")
except ValueError:
    print("Please enter a valid integer.")
