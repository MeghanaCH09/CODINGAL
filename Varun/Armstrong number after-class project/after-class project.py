def is_armstrong_number(number):
    digits = str(number)
    order = len(digits)
    sum_of_powers = sum(int(digit) ** order for digit in digits)
    return sum_of_powers == number

user_input = int(input("Enter a number: "))

if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")