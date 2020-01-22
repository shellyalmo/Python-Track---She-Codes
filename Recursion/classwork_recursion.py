# recursive algorithm, has a base case (terminak case) and recursive case.
def factorial(num):
    if num < 2: #could be  if num == 1
        return 1
    else:
        return num * factorial(num - 1)

# print(factorial(6))
 
#iterative algorithm
def getFactorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

# print(getFactorial(6))

"""Write a function sum that takes a single argument n and computes the sum of all integers between 0 and n inclusive. Assume n is non-negative."""

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
# print(sum(5))

"""
The following examples of recursive functions show some examples of common recursion mistakes. Fix them so that they work as intended.
"""
def sum_every_other_number(n):
    """Return the sum of every other natural number 
    up to n, inclusive.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n == 0:
        return 0
    if n==1:
        return 1
    else:
        return n + sum_every_other_number(n - 2)

# print(sum_every_other_number(8))
# print(sum_every_other_number(9))

def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

"""
For the hailstone function from homework 1, you pick a positive integer n as the start. If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1. Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.
"""
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    num_steps = 1
    if n == 1:
        print(n)
        # num_steps += 1
        return num_steps
    else:
        if n%2 == 0:
            print(n)
            # num_steps += 1
            num_steps += hailstone(n/2)
            
        if n%2 != 0:
            print(n)
            # num_steps += 1
            num_steps += hailstone((n*3)+1)
            
    return num_steps       
# a = hailstone(10)
# print(a)

"""
Consider an insect in an M by N grid. The insect starts at the bottom left corner, (0, 0), and wants to end up at the top right corner, (M-1, N-1). The insect is only capable of moving right or up. Write a function paths that takes a grid length and width and returns the number of different paths the insect can take from the start to the goal. (There is a closed-form solution to this problem, but try to answer it procedurally using recursion.)

For example, the 2 by 2 grid has a total of two ways for the insect to move from the start to the goal. For the 3 by 3 grid, the insect has 6 diferent paths (only 3 are shown above).
"""
def paths(n, m):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if n == 1 or m == 1:
        return 1
    return paths(n-1,m) + paths(n,m-1)
# print(paths(5,7))