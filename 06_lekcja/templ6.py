# zadanie 8
import random
filename = 'sentence_generator.csv'
with open(filename) as fopen:
    # content = fopen.read()
    content = fopen.readlines()
    #content = [w.replace(', ', ' ') for w in content]
    content = [w.replace('\n', '') for w in content]
    for row in content:
        dada = random.choice(row)
    print(dada)
    #content = fopen.read().replace(', ', ' ').split()
print(content)
