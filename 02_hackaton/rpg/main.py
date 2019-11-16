import character_creator as cc
import area_01 as a01
import area_tav as atv

def main_menu():
    return ('New Game - 1'
            '\nContinue Last Game - 2'
            '\nExit - 3')


def go_to_selection():
    print(('MAIN MENU').center(20, "*"))
    print(main_menu())
    go_to = input('Insert menu number positon (1-3): ')
    if go_to == '1':
        start_game()
    elif go_to == '2':
        pass
    elif go_to == '3':
        exit_the_program()
    else:
        print('Please enter number from range 1-3.')
        go_to_selection()


def exit_the_program():
    print('*' * 5, '\nThanks for playing, come again soon!')


def start_game():
    cc.start_creator()
    print("Game started")
    a01.area_01_wake()
    atv.open_eqfile_tav()

go_to_selection()