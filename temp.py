# visa 4935010223474025
# master 5168441223630339
# america 371642190784801


def is_visa(is_card, number):
    # All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
    if not is_card:
        return False

    if len(number) == 16 or len(number) == 13:
        if number[0] == '4':
            return True


def is_mastercard(is_card, number):
    # MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
    #  All have 16 digits.
    if not is_card:
        return False

    if len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True


def is_american_express(is_card, number):
    # American Express card numbers start with 34 or 37 and have 15 digits.
    if not is_card:
        return False

    if len(number) == 15:
        if int(number[0:2]) in (34, 37):
            return True


card_number = input('Please give me your card number, I need some money: ')

can_be_card_number = False

if len(card_number) < 13 or len(card_number) > 16:
    print('Wrong number')
else:
    if card_number.isdecimal():
        print('Can be a card number')
        can_be_card_number = True
    else:
        print("Ya cheater, you didn't put a number")

if is_visa(can_be_card_number, card_number):
    print('Ha! Ya got Visa!')
elif is_mastercard(can_be_card_number, card_number):
    print('Ha! Ya got MasterCard!')
elif is_american_express(can_be_card_number, card_number):
    print('Ha! Ya got American Express!')
else:
    print('Not known card type')
