numer = "add"

try:
    numer == int(numer)
except TypeError as er1:
    result = str(er1)
    print(result)