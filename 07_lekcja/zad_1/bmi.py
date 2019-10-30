def calc_bmi(weight, height):
    return weight / pow(height, 2)


def bmi_status(BMI):
    if BMI < 18.50:
        print('Twoje BMI to:', BMI, '- niedowaga.')
        return (filename == 'niedowaga')
    elif BMI < 25:
        print('Twoje BMI to:', BMI, '- normalna waga.')
        return (filename == 'niedowaga')
    elif BMI < 30:
        print('Twoje BMI to:', BMI, '- nadwaga.')
        return (filename == 'niedowaga')
    else:
        print('Twoje BMI to:', BMI, '- otyłość!')
        return (filename == 'niedowaga')


def main():
    h = float(input('Podaj swój wzrost (format m.cm): '))
    w = float(input('Podaj swoją wagę: '))
    bmi = calc_bmi(w, h)
    print(bmi)
    bmi_status(bmi)


if __name__ == '__main__':
    main()
