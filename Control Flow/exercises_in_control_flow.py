#Given two int values, return their sum.
#Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  if a==b:
    return 2*(a+b)
  else:
    return a+b

#tests

print (sum_double(1, 2)) #should return 3
print (sum_double(3, 2)) #should return 5
print (sum_double(2, 2)) #should return 8


#Given a string, return a new string where "not " has been added to the front.
#However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if len(str) >=3 and str[:3]== 'not':
    return str
  else:
    return 'not ' + str

#tests

print (not_string('candy')) #should return 'not candy'
print (not_string('x')) #should return 'not x'
print (not_string('not bad')) #should return 'not bad'

#Given a non-empty string and an int n,
#return a new string where the char at index n has been removed.
#The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
  if len(str) >0 and isinstance(n, int)==True:
    return str[:n] + str[n+1:]

#test

print (missing_char('kitten', 1)) #should return 'ktten'
print (missing_char('kitten', 0)) #should return 'itten'
print (missing_char('kitten', 4)) #should return 'kittn'


#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) >1:
    first_letter = str[0]
    last_letter = str[-1]
    new_str = last_letter + str[1:-1] + first_letter
    return new_str
  elif len(str)==1:
    return str[0]
  else:
    return str

#tests  
print(front_back('code')) #should return 'eodc'
print(front_back('a')) #should return 'a'
print(front_back('ab')) #should return 'ba'






