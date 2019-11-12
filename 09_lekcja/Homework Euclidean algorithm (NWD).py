def Euklid(a, b):
    c = a % b
    if c == 0:
        return b
    else:
        return Euklid(b, c)


print('NWD to', Euklid(77, 3))
