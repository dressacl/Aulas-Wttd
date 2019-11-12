def positivo(num):
    if num >= 0:
        return True
    else:
        return False

assert positivo(100) == 1
assert positivo(0) == 1
assert positivo(-100) == 0