# zadanie 1
#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
txt = "Pionierzy"
#sprawdza dlugosc wyrazu

mid = len(txt)//2
print(txt[mid - 1 : mid + 2])

# zadanie 2
#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
s1 = "Monty"
s2 = "Python"
s1l = len(s1) // 2
s3 = print(s1[0:s1l] + s2 + s1[s1l:])

# zadanie 3
#Do zmiennej quote przypisz zdanie:
#„Honesty is the first chapter in the book of wisdom.”, a następnie:
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

# zadanie 4
#Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
booktit = input("Podaj tytuł: ")
bookaut = input("Podaj autora: ")
bookpag = input("Policz strony: ")

#Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print(booktit.isalpha() and bookaut.isalpha() and bookpag.isnumeric())

#Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print(booktit.title())
print(bookaut.title())

#Połącz dane w jeden ciąg book za pomocą spacji
book = booktit.title() + " " + bookaut.title() + " " + bookpag
print(book)

#Policz liczbę wszystkich znaków w napisie book
print(len(book))

# zadanie 5

pal = "kajak"
lap = pal.lower()[::-1]
print(bool(lap == pal))

#pal2 = input("Enter za word: ")
#lap2 = pal2.lower()[::-1]
#print(bool(lap2 == pal2))

sen = "Kobyła ma mały bok"
sen.replace(" ", "")
sen = sen.lower()
nes = sen[::-1]
print(bool(sen == nes))

#zadanie 6

zen = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

#liczymy 'better'
print(zen.count("better"))

#usuniecie gwiazdek

#Zamień jedno wystąpienie explain na understand

newzen = zen.replace ('explain', 'understand', 1)

#Usuń spacje i połącz wszystkie słowa myślnikiem

nospace = zen.replace (" ", "-")

#Podziel tekst na osobne zdania za pomocą kropki

zen.split(" .")



#zadanie 7

lett = "word1"
numb = "2word"

print("{0}".format(lett + numb))
