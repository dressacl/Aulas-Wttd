def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

assert par(8)
assert not par(7)
assert par(0)