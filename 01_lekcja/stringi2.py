# zadanie 1
txt = "Pionierzy"
#sprawdza dlugosc wyrazu

mid = len(txt)//2
print(txt[mid - 1 : mid + 2])


# zadanie 3
quote = "Honesty is the first chapter in the book of wisdom."
ile = len(quote) #wszystkie znaki
print(ile)

# pokaz slowo wisdom
print(quote[-7:-1])

#Wyświetl tylko pierwszą połowę tekstu
mid = ile // 2
print(quote[0:mid])

#Wyświetl tylko kropkę
kropka = quote.find('.')
print(quote[kropka:kropka + 1])  #alternatywnie quote[-1: ]

#Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[mid:ile:3])

#Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])

#Wyświetl cały cytat odwrotnie
print(quote[::-1])

#Zamień wisdom na słowo friendship
print(quote[:-7] + 'friendship')  #raczej niezbyt dobry wybor

quote = quote.replace('wisdom', 'friendship')
print(quote)


# zadanie 5

pal = "kajak"
lap = pal.lower()[::-1]
print(bool(lap == pal))

pal2 = input("Enter za word: ")
lap2 = pal2.lower()[::-1]
print(bool(lap2 == pal2))

sen = "Kobyła ma mały bok"
sen.replace(" ", "")
sen = sen.lower()
nes = sen[::-1]
print(bool(sen == nes))

#zadanie 6


#zadanie 7
