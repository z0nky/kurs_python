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

"""Szybko, zbudź się, szybko, wstawaj
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
