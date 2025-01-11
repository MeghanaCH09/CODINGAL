user_input=input("Enter a number: ")
reversed_input = user_input[::-1]
print(reversed_input)
if user_input == reversed_input: 
    print("Yes, it is a palindrome!")
else: 
    print("Invalid, choose another value")