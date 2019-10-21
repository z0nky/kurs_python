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

#4 zadania na środę do 6 w powtórkach :E