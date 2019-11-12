# def LCM(a, b):
#     d = a * b
#     c = a % b
#     if c == 0:
#         d = d / a
#         return d
#     else:
#         return LCM(b, c)

def LCM(a, b):
    d = a * b
    return d / Euklid(a, b)

def Euklid(a, b):
    c = a % b
    if c == 0:
        return b
    else:
        return Euklid(b, c)


print(int(LCM(54, 76)))
