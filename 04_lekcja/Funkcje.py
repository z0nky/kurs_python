def my_mood(answer):  #zliczamy wszystkie potrzebne parametry
    print('My mood today:')
    print(answer)

resp = input('How are you?')  #funkcja dostaje zmienną resp, która zastąpi answer
my_mood(resp)

#tworzymy funkcję przyjmującą parametr i zwraca odpowiedź dwukrotnie:
def my_mood(answer):
    return answer * 2

resp = input('How are you?')
my_mood(resp)
twiced = my_mood(resp)
print('My mood is like', twiced)
