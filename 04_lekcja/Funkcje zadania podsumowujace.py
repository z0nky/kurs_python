# zadanie 1
# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def calc_bmi(weight, height):
    return weight / pow(height, 2)

def bmi_status(BMI):
    if BMI < 18.50:
        print('Twoje BMI to:', BMI, '- niedowaga.')
    elif BMI < 25:
        print('Twoje BMI to:', BMI, '- normalna waga.')
    elif BMI < 30:
        print('Twoje BMI to:', BMI, '- nadwaga.')
    else:
        print('Twoje BMI to:', BMI, '- otyłość!')

h = float(input('Podaj swój wzrost (format m.cm): '))
w = float(input('Podaj swoją wagę: '))

bmi = calc_bmi(w, h)
print(bmi)
bmi_status(bmi)

# zadanie 2
# Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def minimum_of():

    number_list = []
    for _ in range(3):
        number = int(input('Podaj liczbę: '))
        number_list.append(number)

    number_list.sort()
    return number_list[0]

print(minimum_of())

# zadanie 3
# Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c)

def maximum_of():

    number_list = []
    for _ in range(3):
        number = int(input('Podaj liczbę: '))
        number_list.append(number)

    number_list.sort()
    return number_list[-1]

print(maximum_of())

# zadanie 4
# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def number_range(a, b):
    num_range = range(a, b)
    return num_range

def number_checker():
    x = int(input('Podaj szukaną liczbę: '))
    if a < x < b:
        return 'Tak, liczba', x, 'znajduje się w zakresie.'
    else:
        return 'Nie, liczba', x, 'nie znajduje się w zakresie'

a = int(input('Podaj liczbę zaczynającą zakres: '))
b = int(input('Podaj liczbę zamykającą zakres: '))
num_range = number_range(a, b)
print(number_checker())
