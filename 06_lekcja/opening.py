filename = 'tekst.txt'

with open(filename, 'r') as f:  #f to ofkors zmienna, która poza blokiem nie działa :>
    content = f.readlines()
    print(content)

print('Koniec')
