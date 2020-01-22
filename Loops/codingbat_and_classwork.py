"""
Given 2 strings, a and b, return the number of the positions where they contain
the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
since the "xx", "aa", and "az" substrings appear in the same place
in both strings.

"""

def string_match(a, b):
#   splitted_a = a.split()
#   splitted_b = b.split()
  number_of_substrings = 0
  shorter = min(len(a),len(b))
  for i in range(shorter-1):
        # if i==j:
            if a[i] == b[i] and a[i+1] == b[i+1]:
                number_of_substrings += 1
  return number_of_substrings


# print(string_match('xxcaazz', 'xxbaaz'))
#should 3
# print(string_match('abc', 'abc'))
# 2
# print(string_match('abc', 'axc'))
#  0

"""write a function that gets a list of strings and returns a list of strings whose first and last
characters match"""

def first_last_match(list_of_strings):
    list_of_strings_with_first_last_match = []
    for string in list_of_strings:
        # string = string.lower()
        if string[0] == string[-1]:
            list_of_strings_with_first_last_match.append(string)
    return list_of_strings_with_first_last_match

test1 = ["hi","abba","mama","SOS","Mayim","?why?"]
print(first_last_match(test1))

