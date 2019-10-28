# zadanie 1
import random

user_file = input('Do you want to read your own quote file? y/n ')
if user_file == 'y':
    user_choosen_file = input('Input your text file with filename extension (for example "text.txt"): ')
    with open(user_choosen_file, 'r') as fopen:
        line = fopen.readlines()

    qoad = random.choice(line).split('-')
    print("The quote of the day is:\n")
    print('*'.rjust(110, '*'))
    print()
    print(qoad[0].center(110))
    print(qoad[1].rjust(110))
    print()
    print('*'.rjust(110, '*'))

elif user_file == 'n':
    with open('quotes.txt', 'r') as fopen:
        line = fopen.readlines()

    qoad = random.choice(line).split('-')
    print("The quote of the day is:\n")
    print('*'.rjust(110, '*'))
    print()
    print(qoad[0].center(110))
    print(qoad[1].rjust(110))
    print('*'.rjust(110, '*'))
else:
    print('We asked you to put "y" or "n"')

# zadanie 2


# zadanie 3
with open('tekst.txt', 'r') as fopen:
    lines = fopen.readlines()

for l in range(5):
    print("Line " + str(l), lines[l])

# zadanie 4
import random

def random_quote():
    print("The quotes of the day are:\n")
    i = 1
    while i <= 3:
        qoad = random.choice(line)
        print(qoad.center(150))
        print('*'.rjust(150, '*'))
        line.remove(qoad)
        i += 1
    print()

with open('quotes.txt', 'r') as fopen:
    line = fopen.readlines()

random_quote()

#### rozw Rity ####

def random_quote(words):
    quote_for_today = random.choice(words).strip()
    return quote_for_today


def show(quote):
    print('Quote of the day is:')
    print('*' * 50)
    print(quote[0].center(50))
    print(('~ ') + quote[1].center(50))
    print('*' * 50)

filename = 'quotes.txt'
with open(filename) as f:
    quotes = f.readlines()

for i in range(3):
    sentence = random_quote(quotes)
    print('----')
    show(sentence)

# zadanie 5
with open('tekst.txt', 'r') as fopen:
    content = fopen.read().replace(', ', ' ').split()
    # content = content.replace(', ', ' ').split()

longest_one = ''
for word in content:
    if len(word) > len(longest_one):
        longest_one = word
print(longest_one)
print(max(content, key = len))      # alternatywa od wujka google =)
