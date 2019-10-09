tet = str.isalpha('1234')
print(tet)
#mozna uzyc "tekst".isnumeric()
tet2 = str.isalpha('abcd')
print(tet2)
tet3 = str.isdecimal('123')
print(tet3)
tet4 = str.isdecimal('12E')
print(tet4)

zad2 = "tekst"
print(str.center(zad2,10,'*'))
#zad2.center(20, '****') lawtiej

zad3 = 'www.flynerd.pl'
zad3.rstrip('pl')
print(zad3.rstrip('pl'))

zad4 = 'mata'
print(zad4.isalpha() and (not zad4.islower()))

zad5 = 'banana'
print(zad5.count('na'))

