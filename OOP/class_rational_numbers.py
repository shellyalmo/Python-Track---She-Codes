"""
write a class that can represent rational numbers, like fractions. p = numerator, q = denominator

>>> rational_num = Rational(10,20)
>>> rational_num.simplify()
The rational number is: 1 / 2

>>> Rational(10,20)
The rational number is: 10 / 20

>>> Rational(2,7)
The rational number is: 2 / 7

>>> Rational(2,7).simplify()
The rational number is: 2 / 7

>>> Rational(2,7) + Rational(3,7)
The rational number is: 5 / 7

>>> Rational(2,7) + Rational(3,14)
The rational number is: 1 / 2

>>> Rational(12,34) + Rational(2,34)
The rational number is: 7 / 17

>>> Rational(3,34) - Rational(2,34)
The rational number is: 1 / 34

>>> Rational(3,4) - Rational(2,6)
The rational number is: 5 / 12

>>> Rational(3,4) * Rational(2,6)
The rational number is: 1 / 4

>>> Rational(3,4) / Rational(2,6)
The rational number is: 9 / 4

>>> first = Rational(2,3)
>>> second = Rational(2,3)
>>> first.are_equal(second)
'equal'

>>> float(Rational(1,2))
0.5
>>> float(1.0/2.0)
0.5

>>> float(Rational(1,2)+Rational(1,4))
0.75
"""
class Rational:
    def __init__(self,p,q):
        self.p = p
        self.q = q

    def __repr__(self):
        return "The rational number is: {} / {}".format(self.p, self.q)

    def simplify(self):
        for i in range(1,self.p+1):
            if self.p%i == 0 and self.q%i == 0:
                greatest_common_divisor = i
        return Rational(self.p/greatest_common_divisor, self.q/greatest_common_divisor)
    
    def __float__(self):
        return float(self.p)/float(self.q)

    def __add__(self,other):
        if self.q == other.q:
            new_p = self.p + other.p
            return Rational(new_p, self.q).simplify()
        else:
            new_q = self.q * other.q 
            new_p = (self.p * other.q) + (other.p * self.q)
            return Rational(new_p, new_q).simplify()

    def __sub__(self,other):
        if self.q == other.q:
            new_p = self.p - other.p
            return Rational(new_p, self.q).simplify()
        else:
            new_q = self.q * other.q 
            new_p = (self.p * other.q) - (other.p * self.q)
            return Rational(new_p, new_q).simplify()

    def __mul__(self,other):
        new_q = self.q * other.q 
        new_p = self.p * other.p
        return Rational(new_p, new_q).simplify()

    def __div__(self,other):
        new_q = self.q * other.p 
        new_p = self.p * other.q
        return Rational(new_p, new_q).simplify()

    def are_equal(self,other):
        if self.p == other.p and self.q == other.q:
            return "equal"

if __name__ == "__main__":
    import doctest
    doctest.testmod()