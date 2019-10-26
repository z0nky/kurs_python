def main_menu():
    return ('Show all records - 1'
            '\nAdd new record - 2'
            '\nDelete record - 3'
            '\nExit - 4')


def go_to_selection():
    print()
    print(main_menu())
    go_to = input('Insert menu number positon (1-4): ')
    if go_to == '1':
        show_all()
    elif go_to == '2':
        add_record()
    elif go_to == '3':
        remove_rec()
    elif go_to == '4':
        exit_the_program()
    else:
        print('meh')


def show_all():
    counter = 1
    for rec in address_book:
        print(counter, rec)
        counter += 1
    go_to_selection()


def add_record():
    counter = input('How many records do you want to add?')
    if not counter.isdigit():
        print('Ya have to gimme a number.')
        againer = input('Do you want to try again? y/n')
        if againer == 'y':
            add_record()
        else:
            go_to_selection()
    else:
        adding = 1
        while adding <= int(counter):
            address_book.append({'Surname' : input('Surname: '), 'Name' : input('Name: '), 'Phone' : input('Phone number: '), 'City' : input('City: ')})
            adding += 1
        show_all()


def remove_rec():
    to_remove = int(input('Which record do you want to remove? '))
    if to_remove > len(address_book):
        print('Record not found!')
        go_back = input('Do you want to try again? y/n: ')
        if go_back == 'y':
            remove_rec()
        else:
            go_to_selection()
    else:
        del address_book[to_remove-1]
        show_all()


def exit_the_program():
    print('See you next time!')


address_book = [{'Surname' : 'Kowalski', 'Name' : 'Jan', 'Phone' : '123456789', 'City' : 'Poznań'},
                {'Surname' : 'Mickiewicz', 'Name' : 'Adam', 'Phone' : 'unknown', 'City' : 'Cemetery'}]

go_to_selection()
