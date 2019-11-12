def celsius(f):
    return 5 * (f - 32) / 9

def fahrenheit(celsius):
    return celsius / 5 * 9 + 32

celsius = 100
f = 212

assert celsius == celsius(f)
assert fahrenheit == f(celsius)