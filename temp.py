podaj = int(input("Podaj liczbę do 8: "))
silnia = 1

for s in range(1, podaj + 1):
    silnia = silnia * s
    if s == podaj:
        print(s, '=', silnia)
    else:
        print(s, end=' * ')
print('Silnia z', podaj, 'wynosi', silnia)
