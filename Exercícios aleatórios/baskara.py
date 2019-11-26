import math

def delta(a, b, c):
    delta = b * 2 - (4 * a * c)
    return delta

def raiz1(a,b):
    x1 = ((-b + 64 ** (0.5)) / 2 * a)
    return x1

def raiz2(a,b):
    x2 = ((-b - 64 ** (0.5)) / 2 * a)
    return x2

a = 1
b = 0
c = -16

assert 64 == delta(a,b,c)
assert 4 == raiz1(a,b)
assert -4 == raiz2(a,b)
