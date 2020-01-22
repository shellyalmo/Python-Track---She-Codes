"""
write a program that counts from 1 to 50.
for each number, if its exactly divisible by seven, the cpmputer
prints out "boom". otherwise, the computer will print the number.
"""
def game_7_boom():
    for number in range(1,51):
        if number%7 == 0:
            print("boom")
        else:
            print(number)

# game_7_boom()

"""
write a function that counts from 1 to 20 without printing the numbers.
each time: the program asks the user to enter the next number.
the user registers the answer and presses the enter key.
the program checks whether the user's response was valid:
if the loop variable is divisible by seven. the program verifies that
the user has recorded "boom".
otherwise it makes sure that the user registered the correct number.
if the user made a mistake, the program informs him that he was wrong,
and ends the game.
"""

def next_number():
    for i in range(1,21):
        next = input("Next number?: ")
        if (i%7 == 0 and next != "boom") or (i!= next):
            print("You made a mistake. Start over!")
            break
       
# next_number()

"""
this time, every round of the loop checks whose turn it is to play.
if its the computer's turn, it prints the next number(or boom if the number
is divisible by 7).
if tis the player's turn, the program asks what the next number is, and checks it,
as in section 2. its reccommended to reuse the two previous functions and change them as needed.
"""
def human_vs_computer_7_boom():
    computer_turn = False
    for i in range(1,10):
        if computer_turn == True:
            print(i)
        if computer_turn == False:
            next = input ("Next number?: ")
            if (i%7 == 0 and next != "boom"): 
                #or (i!= next):
                print("You made a mistake. Start over!")
                break
            if i != next and next != "boom":
                print("You made a mistake. Start over!")
                break
        computer_turn = not computer_turn
        
# human_vs_computer_7_boom()


"""
bonus: expansion called "14 Splat".
if the number is divisible by 7, say "boom"
if the number is divisible by 14, say "splat"
"""
def human_vs_computer_14_splat_7_boom():
    computer_turn = False
    for i in range(1,21):
        if computer_turn == True:
            if i == 14:
                print("splat")
            else:
                print(i)
        if computer_turn == False:
            next = input ("Next number?: ")
            if (i%7 == 0 and next != "boom"): 
                print("You made a mistake. It was 7 boom. Start over!")
                break
            elif (i%14 == 0 and next != "splat"):
                print("You made a mistake. It was 14 splat. Start over!")
                break
            elif i != next and next != "boom":
                print("You made a mistake. Start over!")
                break
        computer_turn = not computer_turn
        
human_vs_computer_14_splat_7_boom()
