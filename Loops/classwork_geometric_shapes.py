"""1) write a program that prints the following shape onto the screen:
*
**
***
****
*****
"""
#write a funcion that receives a number of stars and prints one line of stars
def number_of_stars(num):
    for i in range(num):
        print("*"),
# number_of_stars(1)
#write the main function. create a loop, each time calling the function you wrote earlier
def print_stars_pyramid():
    for i in range(1,6):
        number_of_stars(i)
        print("")
# print_stars_pyramid()

"""2) write a similar program that will print a trapeze:
*****
******
*******
********
"""

def number_of_stars(num):
    for i in range(num):
        print("*"),

#write the main function. create a loop, each time calling the function you wrote earlier
def print_stars_trapeze():
    for i in range(5,9):
        number_of_stars(i)
        print("")
# print_stars_trapeze()

"""#write a funcion that creates a diamond shape"""
def number_of_stars(num):
    for i in range(0,num,1):
        print("*"),

# number_of_stars(3)

def create_spaces(num):
    for i in range(0,num,1):
        print(""),

# print("h"),

# create_spaces(2)
# print("i")
# print("hoooi")
# create_spaces(2),number_of_stars(1)

def print_stars_diamond(height):
     
    for i in range(height,0,-1):
        create_spaces(i),number_of_stars(height-i)
        print("")
    for i in range(0,height,1):
        create_spaces(i),number_of_stars(height-i)
        print("")
print_stars_diamond(3)