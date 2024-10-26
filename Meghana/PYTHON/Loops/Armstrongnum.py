num=int(input("Enter a number to check whether it is an Armstrong number: "))

def armstrong(num):
    num_str = str(num)
    len_num = len(num_str)
    sum_of_powers = sum(int (digit) ** len_num for digit in num_str)

    return sum_of_powers == num

if armstrong(num):
     print(f"{num} is an Armstrong number.")
else:
     print(f"{num} is not an Armstrong number.") 

