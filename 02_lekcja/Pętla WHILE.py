alls = 3

while alls > 0:
    subject = input("Przedmiot szkolny: ")
    grade = input("Ocena w skali 1-6: ")
    print(subject + ": " + grade)
    alls = alls - 1

print("Job's done")

# kod alternatywny
przedmioty = input("Podaj przemdioty podzielone myślnikiem: ")
oceny = input("Podaj oceny podzielone myślnikiem: ")

przedmioty = przedmioty.split("-")
oceny = oceny.split("-")

print(przedmioty[0])

while licznik < 3:
    print(przedmioty[licznik], " - ", oceny[licnzik])
    licznik = licznik + 1

# zadanie 1
# Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

F = 0

while F <= 200:
    C = 5 / 9 * (F - 32)
    C = round(c, 2)  # zaokrąglenie
    print(F, ' stopni Fahrenheita to ', C, ' stopni Celsjusza.')
    F = F + 20

# pętla FOR
for F in range(0, 200, 20):
    C = 5 / 9 * (F - 32)
    print(F, ' stopni Fahrenheita to ', C, ' stopni Celsjusza.')

# zadanie 2
# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

target = 7
guess = int(input("Try to guess ze numba from range 0-20: "))

while guess != 7:
    print("Nope ", guess, " isn't ze numba you are looking for! Try again.")
    guess = int(input("Try to guess ze numba from range 0-20: "))
print("Good job!", target, " is the correct numba!")
