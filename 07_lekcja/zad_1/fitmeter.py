import bmi

def main():
    height = float(input('Podaj swój wzrost (format m.cm): '))
    weight = float(input('Podaj swoją wagę: '))
    bmi.bmi_status(bmi.calc_bmi(weight, height))
    print(get_advice())


def get_advice():
    with open(bmi.filename + '.txt') as f:
        content = f.read()
    print(content)


# def get_advice():
#     if bmi.bmi_status(bmi.calc_bmi()) < 18.50:
#         with open('niedowaga.txt', 'r') as fopen:
#             return fopen.read()
#     elif bmi.bmi_status(bmi.calc_bmi()) < 25:
#         with open('normalna_waga.txt', 'r') as fopen:
#             return fopen.read()
#     elif bmi.bmi_status(bmi.calc_bmi()) < 30:
#         with open('nadwaga.txt', 'r') as fopen:
#             return fopen.read()
#     else:
#         with open('otyłość', 'r') as fopen:
#             return fopen.read()

if __name__ == '__main__':
    main()
