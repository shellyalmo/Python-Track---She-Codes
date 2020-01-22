# write a function that accepts a string and produces a dictionary
# that connects between an alphabet letter to the number of times it appears
# in the string.
# for example calling char_freq("abzz") will return the dictionary:
# freq = {'a':1, 'b':1, 'z':2}


def frequency_of_letters(some_string):
    the_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    freq = {}
    for letter in the_alphabet:
        if letter in some_string:
            freq[letter] = some_string.count(letter)
    return freq


print(frequency_of_letters("abzz"))
