import random

numbers = [10, 20, 30, 40, 50]

chosen_number = random.choice(numbers)

def guess_number():
    print("Welcome to the Quiz Competition!")
    print("Here are the numbers you can choose from:")
    print(numbers)
    
    while True:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if guess < chosen_number:
            print("Your guess is too low. Try again!")
        elif guess > chosen_number:
            print("Your guess is too high. Try again!")
        else:
            print(f"Congratulations! You guessed the correct number: {chosen_number}")
            break

guess_number()