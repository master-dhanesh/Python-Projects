import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x}: "))
        if guess < random_number:
            print("Opps! Too low...")
        elif guess > random_number:
            print("Ohh! Too high...")
    print(f"yeah boy! the number is {random_number}")


guess_number = int(input("Enter Upper Bound"))
guess(guess_number)