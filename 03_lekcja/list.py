# zadanie 1
#Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Elementy na liście posortuj alfabetycznie, a następnie wyświetl.

mount = ['sandals', 'no jacket', 'wifi']
mount.sort()
print(mount)

# zadanie 2
#Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

numbers = input('Podaj 10 liczb oddzielonych spacją: ')
numbers = numbers.split()
output = []

for dig in numbers:
    if int(dig) % 2 == 0:
        output.append(dig)
        continue
print(output)



# zadanie 3
#Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

numberz = input("Podaj liczbę całkowitą, jeśli chcesz zakończyć dodawanie wpisz NIE: ")
numlist = []

while numberz != 'NIE':
    numlist.append(numberz)
    numberz = input("Podaj liczbę całkowitą, jeśli chcesz zakończyć dodawanie wpisz NIE: ")
print(numlist)

el1 = numlist[0]
el2 = numlist[-1]

checking = bool(el1 == el2)
print(checking)

# zadanie 3 by Rita

counter = int(input("Ile liczb chcesz dodać? "))

elements = []
for _ in range(counter): # podkreślinik zastępuje zmienną, która nie jest nam potrzebna
    tmp = input("Podaj dowolny ciąg znaków: ")
    elements.append(tmp)

print(elements)

print("Czy pierwszy i ostatni element są takie same:", elements[0] == elements[-1])

if elements[0] == elements[-1]
    print("Pierwszy i ostatni są takie same")
else:
    print("Nie są takie same")

# zadanie 3 wariant z poprawnym przerwaniem

num_arr = []
while True:
    e = input("Podaj nowy element. Naciśnij Q aby zakończyć: ")
    if e == "Q":
        break
    num_arr.append(e)

print(num_arr)

# zadanie 4
#Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

evens = input('Wprowadź parzystą liczbę elementów, oddziel je przecinkiem: ')
evens = evens.split(', ')

ev1 = evens[len(evens) // 2 - 1]
ev2 = evens[len(evens) // 2]

if ev1 == ev2:
    print('Środkowe wartości', ev1, ev2, 'są takie same!')
else:
    print('Środkowe wartości są różne!')


# zadanie 5
#Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób,
#natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np

ppl = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]

for row in ppl:
    for elem in row:
        print(elem, end=' ')
    print()

#inaczej
#liczba ludzi to (len(ppl)
print("-----------)")
for row in range(len(ppl)):
    for col in range(len(ppl[row])): #liczba elementó w wierszach range(len(ppl[row]
        if col == 1:
            print(ppl[row][col], end=' - ')
        else:
            print(ppl[row][col], end=' ')
    print()

#alternatywa
print("-------------------")
for row in ppl:
    print(row[0], row[1], "-", row[2])
