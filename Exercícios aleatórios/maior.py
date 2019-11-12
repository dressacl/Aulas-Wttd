def maior(valor):
    if valor >= 10:
        return 1
    else:
        return 0

assert 1 == maior(17)
assert 0 == maior(9)
assert 1 == maior(100)