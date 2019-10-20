numbers = [1, 2, 3, (10, 20), 4, 5]

counter = 0

for n in numbers:
    if isinstance(n, tuple):
        break
    counter += 1
print(counter)


#zadanie 1
#Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.

uno = (1, 2, 3, 5, 3)

set(uno)

#zadanie 2
#Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
#Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3 ,4)
S_test = {1, 2, 3, 4}

print('Dla tuple nie zadziała append(), extend(), insert(), remove(), pop(), clear(), del T_test[:], sort(), reverse(), copy()')
print('Dla set nie zadziała append(), extend(), insert(), del S_test[:], index(), count(), sort(), reverse(). pop() działa, ale nie wiem jak wstawić inny element niż pozycji 0.')

#zadanie 3
#Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
#a oraz nieparzystych elementów z drugiej.

tup1 = ('a', 'b', 'a', 'b', 'a', 'b')
tup2 = (1, 2, 1, 2, 1, 2)
counter = 0

my_list = []

while counter <= len(tup1) - 1:
    if counter % 2 != 0:  #modulo for not even number cos counting index from 0!
        my_list.append(tup1[counter])
    counter += 1

counter = 0

while counter <= len(tup2) - 1:
    if counter % 2 == 0:  #modulo for even number cos counting index from 0 gives uneven index in return kek.
        my_list.append(tup2[counter])
    counter += 1

print(my_list)

#zadanie 4
#Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#output:
#[4, 3, 2, 1]
#[14, 13, 12, 11]
#[24, 23, 22, 21]

my_input = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

new_in1 = my_input[0 : len(my_input) // 3]
new_in2 = my_input[len(my_input) // 3 : (len(my_input) // 3) * 2]
new_in3 = my_input[(len(my_input) // 3) * 2 : ]

final_input = [new_in1[4:  : -1], new_in2[4:  : -1], new_in3[4:  : -1]]
print(final_input)
print('----')

for row in final_input:
    for val in row:
        if val == row[3]:
            print(val, end=' ]')
        elif val == row[0]:
            print('[', val, end=', ')
        else:
            print(val, end=', ')
    print()

#zadanie 5
#Porównaj zachowanie discard() vs remove() dla typu set

s1 = {1, 2, 3}
s2 = {1, 2, 3, 1}
s3 = {1, 2, 3, 1}

s1.discard(4)
s1.remove(4) # nie zadziała

s2.remove(1)
print(s2, 'remove')  #Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
s3.discard(1)
print(s3, 'discard')
