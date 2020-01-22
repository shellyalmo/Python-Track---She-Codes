"""given 2 strings s and t, write a function to determine if t is an angram of s.
s = "anagram, t = "nagaram" return True
s - "rat", t = "car", return False

>>> anagram("rat", "car")
False
"""

def anagram(s,t):
    test1_is_true = None
    test1_is_false = None
    test2_is_true = None
    test2_is_false = None
    if len(s) ==0 and len(t) ==0:
        return True
    for letter in s:
        if letter in t:
            if t.count(letter) == 1:
                test1_is_true = True
        else:
            test1_is_false = False
    for letter in t:
        if letter in s:
            if s.count(letter) == 1:
                test2_is_true = True
        else:
            test2_is_false = False
    if test1_is_true == True and test2_is_true == True and test1_is_false == None and test2_is_false == None :
        return True
    else:
        return False

        
# print(anagram("aacc","ccac"))


"""
write a function that accepts a string representing a "Roman Numeral" and outputs its numerical value. The output is promised to be between 1 and 3999. the logic:
add all the values unless you have a lesser value preceding a greater value, and then its subtractuve.
basic cases of subtraction - IV (4), IX (9), XL (50-10=40), XC (100-10=90), CD (500-100=400), CM(1000-100=900). we are only subtracting in these certain pairs. OTHERWISE WE ARE JUST ADDING.
and we have to know what is the range, and never repeating a letter more than 3 times.
maximum letter is M = 1000, so you cant have MMMM (4000). only 3999 = MMMCMXCIX = 3000+900+90+9
we are finding the max value that we can remove from our number rach iteration and then appending all together.
"""
#49 - less than 50 so we dont have L, and more than 40 so we have XL. We subtract 40 fro 49 and then we have 9 - we know its IX. so in total - XLIX
#2017- MM + (less than 20 but greater than 10 so X, then after we subtract we have 7, so we subtract 5 and then 2 )XVII
def convert_roman_to_numerical(roman):
    roman_basic_symbols = { 
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    # total =0
    total = roman_basic_symbols[roman[-1]]
    for i in reversed(range(len(roman))):
        if i > 0:
            if roman_basic_symbols[roman[i-1]] >= roman_basic_symbols[roman[i]]:
                total += roman_basic_symbols[roman[i-1]]
            
            else:
                total -= roman_basic_symbols[roman[i-1]]
                #  roman_basic_symbols[roman[i]] < roman_basic_symbols[roman[i-1]] and roman_basic_symbols[roman[i-1]] < roman_basic_symbols[roman[i-2]]:
                # total += roman_basic_symbols[roman[i-1]]
            # else:
            #     total += roman_basic_symbols[roman[i-1]]
        # else:
            # total += roman_basic_symbols[roman[i]]
        
            
    return total
# print(convert_roman_to_numerical("XX"))
# print(convert_roman_to_numerical("XLIX"))
# print(convert_roman_to_numerical("IV"))
# print(convert_roman_to_numerical("MMXVII"))
# print(convert_roman_to_numerical("XLV"))

"""given a non negative number represented as a list of list_of_numbers[is, add 1 to the number. The list_of_numbers[is are stored in a way that the most significant list_of_numbers[i is at the head of the list, and each element in the array contains a single list_of_numbers[i.
[5,1] returns [5,2]
[9] returns [1,0]
[9,9,9] returns [1,0,0,0]
[1,2,3] returns [1,2,4]
"""
def add_1(list_of_numbers):
    new_list = list_of_numbers
    last  = 0
    # new_list.append(list_of_numbers)
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == 9:
            list_of_numbers[i] = 1
            new_list.insert(-1,0)
        else:
            last = new_list.pop(-1) + 1
            new_list.append(last)
            break
    return new_list
# print(add_1([9,9]))

def plus_one(list_of_numbers):
    for i in range(len(list_of_numbers)-1,-1,-1):
        num = list_of_numbers[i] + 1
        if num > 9:
            list_of_numbers[i] = 0
            if i == 0:
                list_of_numbers = [1] + list_of_numbers
        else:
            list_of_numbers[i] += 1
            break
    return list_of_numbers

print(plus_one([1,2,9]))

#  for i in range(length-1, -1, -1):
#             num = digits[i] + 1
#             if num > 9:
#                 digits[i] = 0
#                 if i == 0:
#                     digits = [1] + digits
#             else:
#                 digits[i] += 1
#                 break
                
#         return digits





