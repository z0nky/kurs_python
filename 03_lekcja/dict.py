#zadanie 1

lists_to_dict = [
    ['ala', 'ola'],
    ['cat', 'dog'],
    ['beer', 'wine']
]

dict_from_list = dict(lists_to_dict)

print(dict_from_list)
print(dict_from_list['ala'])

print(lists_to_dict[0][1])


#zadanie 5

text = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

# 1. tworzymy pusty słownik: words = {}
# 2. txt -> przechowuje tekst wierszyka
# 3. txt -> dzielimy na osobne wyrazy, np split -> dostajemy listę w efekcie
# 4. for -> lista elementów txt
    # sprawdza czy słowo jest w słowniku
    # TAK: słownik[słowo] =+ 1
    # NIE: słownik[słowo] = 1
# 5. ładne wyświetlanie jak w zadaniu

words = {}
text = text.replace(',', '').lower()
wordlist = text.split()
words['szybko'] = 0
words['zbudź'] = 0

for elem in wordlist:
    if elem == 'szybko':
        words['szybko'] += 1
    elif elem == 'zbudź':
        words['zbudź'] += 1

for ke, va in words.items():
    print(ke, ':', va)

# zadanie 2
# Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe. Przekształć ją w słownik dict_from_tuples.

tuples_to_dict = (('ziemniak', 'potato'), ('jablko', 'apple'))
dict_from_tuples = dict(tuples_to_dict)

for key, value in dict_from_tuples.items():
    print(key, value)

# zadanie 3
# Utwórz dowolną tablicę n x n zawierającą dowolny znak,
# a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

n = 3

tab = [['-', '-', '-'],
  ['-', '-', '-'],
  ['-', '-', '-']]

for rows in tab:
    for dig in rows:
        print(dig, end=' ')
    print()

# zadanie 4
# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.

multi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counting = 1

for elem in multi:
    for mini in range(1, 11):
        print((mini * counting), end=' ')
    print()
    counting += 1

