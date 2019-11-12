from math import *


def rozklad(x):
    if x <= 0:
        return 0
    i = 2
    e = floor(sqrt(x))
    r = []
    while i <= e:
        if x % i == 0:
            r.append(i)
            x /= i
            e = floor(sqrt(x))
        else:
            i += 1
    if x > 1:
        r.append(x)
    return r

# l=1
# while l>0:
#     print("Podaj liczbę: ")
#     l=int(input())
#     r=rozklad(l)
#     print(r)

print(rozklad(54))
