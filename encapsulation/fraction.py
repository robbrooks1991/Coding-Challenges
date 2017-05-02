from fractions import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.gcd = gcd(numerator, denominator)
        self.num = numerator // self.gcd
        self.den = denominator // self.gcd

    def __repr__(self):
        return '%s/%s' % (divmod(self.num, self.den), self.den)

        """return '%s, %s/%s' % (self.num // self.den, self.num % self.den, self.den)"""

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction( num, den )

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction( num, den )

    def __mul__(self, other):
        return Fraction( self.num * other.num, self.den * other.den )

    def __div__(self, other):
        return Fraction( self.num * other.den, self.den * other.num )

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ > other.__dict__
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ < other.__dict__
        else:
            return False

