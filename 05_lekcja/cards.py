#visa 4935010223474025
#master 5168441223630339
#america 371642190784801

card_number = input('Please give me your card number, I need some money: ')

can_be_card_numbeer = False

if len(card_number) < 13 or len(card_number) > 16:
    print('Wrong number')
else:
    if card_number.isdecimal():
        print('Can be a card number')
        can_be_card_numbeer = True
    else:
        print("Ya cheater, you didn't put a number")


# Visa
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
if can_be_card_numbeer and (len(card_number) == 16 or len(card_number) == 13):
    if card_number[0] == '4':
        print('Ha! Ya got Visa!')

# Master Card
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
if can_be_card_numbeer and len(card_number) == 16:
    if int(card_number[0:2]) in range(51, 56) or int(card_number[0:4]) in range(2221, 2721):
        print('Ha! Ya got MasterCard!')

# American Express
# American Express card numbers start with 34 or 37 and have 15 digits.
if can_be_card_numbeer and len(card_number) == 15:
    if int(card_number[0:2]) in (34, 37):
        print('Ha! Ya got American Express!')
