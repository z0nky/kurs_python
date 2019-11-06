import sys

list = [2, 0, 5,'Tuwim', 2.57, True, False, 4+3j, {"pl":"poland","en":"england"}, (3, 4, 5)]
print(list)
i = 0
for i in list:

    try:
        result = 10 / i

    except ZeroDivisionError as er1:
        result = "Wyjątek 1" + str(er1)
    except TypeError as er2:
        result = "Wyjątek 2" + str(er2)
        x = " bład dzielenia"
    print(result)
