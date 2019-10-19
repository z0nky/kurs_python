text ='Python'

for stp in text:
    print("-", stp)

#zadanie 1
#Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
#Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

adventure = ['lina', 'siekiera', 'wifi']
for a in adventure:
    print(a)
print('Great, we are ready!')

#zadanie 2
#Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

ingridients = ['pyszne', 'uber', 'pizzeria']
for b in ingridients:
    print(b, 'czekaj na dostawę')

#zadanie 3
#Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

suma = 0

for i in range(1, 11):
    suma = suma + i
    print(suma)

#alternatywa

suma = 0
for i in range(1, 11):
    suma += i
    if i == 10:
        print(suma)
    else:
        print(suma, end=",  ")

#zadanie 4
#Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).
podaj = int(input("Podaj liczbę do 8: "))
silnia = 1

for s in range(1, podaj + 1):
    silnia = silnia * s
    if s == podaj:
        print(s, '=', silnia)
    else:
        print(s, end=' * ')
print('Silnia z', podaj, 'wynosi', silnia)
