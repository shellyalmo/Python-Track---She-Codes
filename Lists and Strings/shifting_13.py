# This program is implying encryption method in which each letter is replaced with another letter in a permanent shift.
# In this program the shift is 13.
# 
# Implement a function that creates the dictionary: key = {'a':'n','b':'o'.....}
# the key starts at 'a', reaches 'z'. and then starts at 'A' and finishes at 'Z'
# the values are lower or upper case according to the key
# implement encryption and decryption functions using 13 shift.
# the function accepts a readable string and replaces letters according to the method.
# also write a function that decrypts the string and returns it to normal.
# try to decipher this: V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!

#function that creates the dictionary that shifts each letter 13 spots
def shifting_13():
    #creating 2 strings of the alphabet that go on after "z" till "z" also gets shifted
    abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmn"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMN"
    dictionary_shifting_13 = {}
    #looping through all the alphabet
    for i in range(0,26):
        dictionary_shifting_13.update({abc[i]:ABC[i+13]})
        dictionary_shifting_13.update({ABC[i]:abc[i+13]})
    return dictionary_shifting_13


#function that uses that dictionary and gets the desired letter for each letter in the string, and 
# brings the value of that letter (key)

def encryption(some_string):
    encrypted_list = []
    dictionary_shifting_13 = shifting_13()
    for letter in some_string:
        if dictionary_shifting_13.get(letter,'none') == 'none':
            encrypted_list.append(letter)
        else:
            encrypted_list.append(dictionary_shifting_13.get(letter))
    encrypted_string = " ".join(encrypted_list)
    return encrypted_list

print(encryption("V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!"))