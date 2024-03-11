import math


class Fraction:
    __slots__ = ("_numerator", "_denominator")

    def __init__(self, numerator=0, denominator=1):
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError(
                "Fraction(%s, %s) - значения числителя и знаменателя должны быть целыми числами"
                % (numerator, denominator)
            )
        if denominator == 0:
            raise ZeroDivisionError("Fraction(%s, 0)" % numerator)
        g = math.gcd(numerator, denominator)
        if denominator < 0:
            g = -g
        numerator //= g
        denominator //= g
        self._numerator = numerator
        self._denominator = denominator

    # Сумма двух дробей
    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self._numerator * other._denominator
                + other._numerator * self._denominator,
                self._denominator * other._denominator,
            )
        return NotImplemented

    # Разность двух дробей
    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self._numerator * other._denominator
                - other._numerator * self._denominator,
                self._denominator * other._denominator,
            )
        return NotImplemented

    # Произведение двух дробей
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self._numerator * other._numerator,
                self._denominator * other._denominator,
            )
        return NotImplemented

    # Частное двух дробей
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self._numerator * other._denominator,
                self._denominator * other._numerator,
            )
        return NotImplemented

    # x < y
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return (
                self._numerator * other._denominator
                < other._numerator * self._denominator
            )
        return NotImplemented

    # x <= y
    def __le__(self, other):
        if isinstance(other, Fraction):
            return (
                self._numerator * other._denominator
                <= other._numerator * self._denominator
            )
        return NotImplemented

    # x == y
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (
                self._numerator * other._denominator
                == other._numerator * self._denominator
            )
        return NotImplemented

    # x != y
    def __ne__(self, other):
        if isinstance(other, Fraction):
            return (
                self._numerator * other._denominator
                != other._numerator * self._denominator
            )
        return NotImplemented

    # x > y
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return (
                self._numerator * other._denominator
                > other._numerator * self._denominator
            )
        return NotImplemented

    # x >= y
    def __ge__(self, other):
        if isinstance(other, Fraction):
            return (
                self._numerator * other._denominator
                >= other._numerator * self._denominator
            )
        return NotImplemented

    def __repr__(self):
        if self._denominator == 1:
            return "Fraction(%s)" % self._numerator
        else:
            return "Fraction(%s, %s)" % (self._numerator, self._denominator)

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        else:
            return "%s/%s" % (self._numerator, self._denominator)

    def getABS(self):
        return Fraction(abs(self._numerator), abs(self._denominator))
