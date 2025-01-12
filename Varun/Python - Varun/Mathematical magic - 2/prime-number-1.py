user_input = int(input("Enter your desired number between 0 and 100: "))
if(user_input==1): 
    print("1 is a prime number")
elif(user_input>1): 
    for i in range(2, 101): 
        if (user_input%i==0):
            print("It is not a prime number")
            break 
        else: 
            print("It is a prime number")
else: 
    print("Please enter another value ")