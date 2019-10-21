# zadanie 1
#napisz fkcje, która pyta o pary książka + ocena i zapisuje w programie
#zadanie 2
#fkcja pytająca o ocene książki i wyświetli ksiazke wraz z oceną jesli ksiazka o takiej ocenie istnieje
#zadanie 3
#w prosty sposob obsluz blad uz - uz zapyta o nr w bazie, ktory nie istnieje


def add_book(dict_books): #brak parametru dict_books sprawiłby, że musiałbym dodać pusty słownik w tej fkcji np dict_books = {}
    counter = int(input('Ile książek zostanie dodanych: '))
    for _ in range(counter):
        title = input('Podaj tytuł: ')
        grade = input('Podaj ocenę: ')
        dict_books[title] = grade

    return dict_books

def read_book_by_grade(books):  #zmienna w metodzie nie przechodzi poza ta metode
    g = input("Podaj szukaną ocenę: ")
    if g in books.values():
        for title, grade in books.items():
            if grade == g:
                print(title, " - ocena:", grade)
    else:
        print('Brak książki o takiej ocenie.')


books = {}
books = add_book(books)  #dajemy parametr, który wysyłany jest do funkcji add_book. uzupełniamy tak pusty słownik
print(books)

read_book_by_grade(books)
