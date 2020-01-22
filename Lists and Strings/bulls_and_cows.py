"""player 1 has to guess a 5 letter string, within the least number of rounds. in each round player 1 guesses a string and gets :
how many "bulls" = correct guesses of letters and in correct location,
how many "cows" = correct guess but wrong location
"""
import string
import random

def bulls_and_cows(real,guess):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == real[i]:
            bulls += 1
        elif guess[i] in real:
            cows += 1
    return "bulls: {}\ncows: {}".format(bulls,cows)
# print(bulls_and_cows("abcde","acdzr"))
# print(bulls_and_cows("abcde","abdzr"))
 
def game():
    # real = ""
    # guess = ""
    letters = string.ascii_lowercase
    # real = "qwert"
    real = ''.join(random.choice(letters) for i in range(5))
    guess = input("Enter the 5 letter word you are guessing: ")
    while len(guess) != 5:
        guess = input("Enter the 5 letter word you are guessing: ")
    print("The guessed word: " + guess)
    print(bulls_and_cows(real,guess))
    want_to_play = ""
    while guess != real:
        print("The real word:    " + real)
        want_to_play = input('You lost. Do you want to guess again? enter "Y" for yes or "N" for no ')
        if want_to_play == "Y":
            guess = input("Enter the 5 letter word you are guessing: ")
            while len(guess) != 5:
                guess = input("Enter the 5 letter word you are guessing: ")
            print("The guessed word: " + guess)
            print(bulls_and_cows(real,guess))
        else:
            break
    if guess == real:
        print("The real word:    " + real)
        print("You won!")
    return bulls_and_cows(real,guess)


game()

