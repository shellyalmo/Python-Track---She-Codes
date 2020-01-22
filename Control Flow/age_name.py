"""write a function that asks the user to enter his birth year, first name and surname.
keep each of these things in a variable.
the function will calculate what is the age of the user, the initials of his name, and print them.
example: John
         Doh
1989
should return: >> your initials are JD and you are 27 years old"""

def age_name():
    year = input('Please enter your birth year: ')
    first_name = input('Please enter your first name: ')
    first_capital = first_name[0]
    sur_name = input('Please enter your surname: ')
    last_capital = sur_name[0]
    age = 2019 - int(year)
    print ('your initials are ' + first_capital.upper() + last_capital.upper() + ' and you are ' + str(age) + ' years old.')

age_name()
