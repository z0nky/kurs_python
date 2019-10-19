# zadanie 1
# Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty
# i wyświetl komunikat “liczba parzysta”.
numba = int(input('Input a number: '))
rest = numba % 3
if rest == 0:
    print('This a triple digit!')
else:
    print('This is not a triple digit!')

# zadanie 2
# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

numb1 = int(input('Podaj liczbę całk.: '))
numb2 = int(input('Podaj jeszcze jedną liczbę całk.: '))
addin = numb1 + numb2
if addin > 100:
    print(addin)
else:
    print('KONIEC')

# zadanie 3
# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.
a = int(input('1st score 1-10: '))
b = int(input('2nd score 1-10: '))
c = int(input('3rd score 1-10: '))

score = (a + b + c) / 3

if score > 7:
    print('bardzo dobry')
elif score > 5:
    print('przeciętna')
else:
    print('nie warta uwagi')

# zadanie 4
# Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.
randomstr = 'abcde1'
afinder = randomstr.find('a')

if len(randomstr) > 5 and afinder == 0:
    randomstr = randomstr.replace('a', 'z')
    print(randomstr)

# zadanie 5
# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków. Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.
#elify wyrzucą 1 komunikat, ify wszystkie
password = input('Set ur password: ')
alphanum = password.isalnum()
condition_1_up = alphanum and not password.islower()

if len(password) < 8:
    print('Too short!')
if not alphanum:
    print('It should be alphanumeric!')
#rozw grupy ^
if password.isalpha() == True or password.isnumeric() == True:
    print('Needs at least one number and letters combined!')
if condition_1_up:
    print('Needs at least one capital letter')

# zadanie 6
# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

bingo = int(input('Try to guess number 1-100: '))

if bingo == 1:
    print('Bingo! One is the loneliest number!')
else:
    print('Pudło')

#zadanie 7
#Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

weight = float(input('Podaj swoją wagę: '))
height = float(input('Podaj swój wzrost: '))

BMI = weight / pow(height, 2)

if BMI < 18.50:
    print('Twoje BMI to:', BMI, '- niedowaga.')
elif BMI < 25:
    print('Twoje BMI to:', BMI, '- normalna waga.')
elif BMI < 30:
    print('Twoje BMI to:', BMI, '- nadwaga.')
elif BMI >= 30:
    print('Twoje BMI to:', BMI, '- otyłość!')

#zadanie 8
#Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

