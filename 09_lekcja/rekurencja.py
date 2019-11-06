def sum_for(n):
    s = 0
    for i in range (1, n+1):
        s = s + i
    return s


print('Suma_for to:', sum_for(10))


def sum_while(n):
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s


print('Suma_while to:', sum_while(10))


def sum_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursion(n-1)


print('Suma_rekurencyjnie:', sum_recursion(10))