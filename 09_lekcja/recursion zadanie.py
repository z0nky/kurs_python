def wypisz(n):
    if n < 0:
        print('-')
        n = -n
    if n % 10 != 0:
        wypisz(n / 10)
    print(n % 10)

wypisz(123)

