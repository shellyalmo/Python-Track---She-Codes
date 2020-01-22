"""Write a function that takes in two numbers and recursively multiplies them together
"""
def recursive_multiplication(n,m):
    # base case
    if n == 1 and m == 1:
        return 1
    elif n == 1:
        return m
    elif m == 1:
        return n
    elif n == 0 or m == 0:
        return 0
    # recursive case
    else:
        return recursive_multiplication(n-1,m) + m

# print(recursive_multiplication(12,3))

"""Write a function that takes in a base and an exp and recursively computes base**exp. You are not allowed to
use the ** operator!
"""
def exponent(base,exp):
    # base cases
    if exp == 0:
        return 1
       # recursive cases:
    else:
        return base * exponent(base,exp-1)
    
# print(exponent(2,4))

"""3. Write a function using recursion to print numbers from n to 0.

"""
def print_nums(n):
    # base case
    if n == 0:
        print(n)
        return 0
    elif n > 0 :
        print(n)
        return print_nums(n-1)
    elif n < 0:
        print(n)
        return print_nums(n+1)
# print_nums(-9)

"""4. Write a function using recursion to print numbers from 0 to n (you just need to change one line in the program
of problem 1).
"""
def countup(n,m):
    if m == n:
        print(m)
        return m
    else:
        print(m)
        return countup(n,m+1)
# countup(5,0)

"""5. Write a function using recursion that takes in a string and returns a reversed copy of the string. The only
string operation you are allowed to use is string concatenation.
"""
"""As others have pointed out, this is not the way you would usually do this in Python. An iterative solution is going to be faster, and using slicing to do it is going to be faster still.

Additionally, Python imposes a limit on stack size, and there's no tail call optimization, so a recursive solution would be limited to reversing strings of only about a thousand characters. You can increase Python's stack size, but there would still be a fixed limit, while other solutions can always handle a string of any length.
"""
# def reversed_string(str):
#     reversed = ""
#     for char in str:
#         reversed = char + reversed
#     return reversed
    
# str= "shalom"
# print(reversed_string(str))

def reversed_string(str):
    if len(str) == 0:
        return ""
    else:
        # return str[-1] + reversed_string(str[:-1])
        return reversed_string(str[1:]) + str[0]

# print(reversed_string("shalom"))

"""6. Write a function using recursion to check if a number n is prime (you have to check whether n is divisible by
any number below n).
"""
def is_prime(n,m=2):
    if n <=2 :
        print("{} is prime number".format(n))
        return True
    if m * m >= n:
        print("{} is prime number".format(n))
        return True
    if n%m == 0:
        print("{} is not prime number".format(n))
        return False

    return is_prime(n,m+1)
        
         
# print(is_prime(15))

"""7. Write a recursive function that takes in one argument n and computes Fn, the nth value of the Fibonacci
sequence. Recall that the Fibonacci sequence is defined by the relation

"""
def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(6))
