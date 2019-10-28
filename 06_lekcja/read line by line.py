#with open('tekst.txt', 'r') as fopen:
#    while True:
#        current_line = fopen.readline()

# aktualna linia jest pusta
#        if current_line == '':
#            # dotarlismy do konca
#            break
#        print(current_line)
#ale to też takie sobie było więc:

with open('tekst.txt', 'r') as fopen:
    lines = fopen.readlines()       # tu wrzuca linie w listę i daje możliwość operowania na liście

for l in range(len(lines)):
    print("Line " + str(l), lines[l])


#                   ALBO :
#with open('plik.txt', 'r') as fopen:
#    lines = fopen.readlines()

#for l in lines:
#    print("Line : " + l )
