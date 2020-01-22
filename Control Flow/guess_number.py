"""write a game called "Guess the number", where the computer selects a random number.
Then it will recieve a number from the user. If it's the same number, the user wins and a suitable message will be printed to the screen.
Then write a function that generates a random number and call it when you call the 1st function"""
import random


def guess_number(random_number):
    user_number = int(input('Please enter a number from 1 to 10: '))
    print("The computer's number is: " + str(random_number))
    if random_number == user_number:
        print("You Won! Your number and the computer's number are equal! ")
    elif random_number > user_number:
        print("Oh no! You lost. Your number is lower than the computer's number. ")
    elif random_number < user_number:
        print("Oh no! You lost. Your number is greater than the computer's number.")

def random_from_computer():
    random_number = random.randint(1,10)
    return random_number

guess_number(random_from_computer())
    

