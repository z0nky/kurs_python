### Historyjka a'la RPG:
#- Konieczność użycia modułu `random`.
#- Program wypisuje kolejne "przygody" bohatera.
#- Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami,
# np: "(bohater) poszedł do (miejsce) aby (czasownik)." może stać się "Jouxdrien II Niemrawy poszedł do tawerny aby zasnąć."
#- Historyjka ma mieć zadaną długość i ma być możliwie losowa.

import random




def start():
    "Let's start"
    beginning_1()


#def choose():
    #wut = input("What do you do?")
    #return wut


def no_way():
    print("\n\nYou can't in this direction.", "\n" + 3 * "*", "\n")


def wrong_com():
    print("\n\nUnknown command", "\n" + 3 * "*", "\n")



def beginning_1():
    sentence = ("\nYou woke up in the drop point. Wooden elevator is at the top of the cliff."
    "\nYou remember vividly some guy who punched you in the face saying 'Welcome to the colony.'"
    "\nYou slowly get up.")
    print(sentence)
    choose = input("What do you do?")
    if choose == l:
        area_beg_1()
        beginning_1()
    elif choose == go_n:
        print("\nYou travel north.\n")
        beginning_2()
    elif choose == go_e or choose == go_s or choose == go_w:
        no_way()
        beginning_1()
    else:
        wrong_com()
        beginning_1()


def area_beg_1():
    plot = ("\n\nThe terrain is flat. Next to you stands wooden elevator, which is at the top of the cliff. There is nothing to call it down."
            "\nThere is no way you can climb back, and even if you could, the barrier at the top would kill you."
            "\nAt the north of the small valley you can see road, probably often used one.")
    print(plot)
    print(3 * "*")


def beginning_2():
    sentence = ("\n\nThe road here leeds further north. On the left you can see closed mine."
                "\nNorth of you is small passage under the bridge."
                "\nOn the west you can see high stone wall.")
    print(sentence)
    choose = input("What do you do?")
    if choose == l:
        area_beg_2()
        beginning_2()
    elif choose == go_w or choose == go_e:
        no_way()
        beginning_2()
    elif choose == go_s:
        print("No point in going back!")
        beginning_2()
    elif choose == go_n:
        print("\nYou travel north.\n")
        wood_entrance()
    else:
        wrong_com()


def area_beg_2():
    plot = ("\n\nThe mine on the left is impossible to access."
            "\nThere is no way to climb to the ruined bridge."
            "\nThe only way is to go forward.\n")
    print(plot)
    print(3 * "*")


def wood_entrance():
    sentence = ("\nFar to the north you can see small settlement with wooden palisade."
                "\nBut to get there you have to pass through dark woods.\n")
    print(sentence)
    choose = input("What do you do?")
    if choose == l:
        wood_en_ar()
        wood_entrance()
    elif choose == go_w or choose == go_e:
        no_way()
        beginning_2()
    elif choose == go_s:
        print("No point in going back!")
        beginning_2()
    elif choose == go_n:
        maze()
    else:
        wrong_com()


def wood_en_ar():
    plot = ("\nThe woods do not seem too big, but are dense."
            "\nYou can't say what's inside them."
            "\nRock walls surround you, so the only way to proceed is to enter this forest.\n")
    print(plot)
    print(3 * "*")


def maze():
    import random
    woods = ['w1', 'w2', 'w3']
    where = random.choice(woods)
    stamina = 5
    while stamina >= 1:
        if where == 'w1':
            w1()
        elif where == 'w2':
            w2()
        elif where == 'w3':
            w3()
        stamina = stamina - 1
        print("You are getting exhausted. Your stamina:", stamina, "!")
        print("\n", "* * *", "\n")
    print("Your stamina has reached critical level. You fall asleep and die of malnutrition! HAHAHA!")





def w1():
    sentence = ("\nThe woods are dense, very dark. There are three routes:"
                "\nNorth, West, East.")
    print(sentence)
    choose = input("What do you do?")
    if choose == go_e or choose == go_n or choose == go_w:
        print("\nYou travel", choose, end=".")
        print(3 * "*")
    elif choose == go_s:
        no_way()
        w1()
    elif choose == l:
        wood_look()
        w1()
    else:
        wrong_com()


def w2():
    sentence = ("\nThe woods are dense, very dark. There are three routes:"
                "\nNorth, West, East.")
    print(sentence)
    choose = input("What do you do?")
    if choose == go_e or choose == go_n or choose == go_w:
        print("You travel", choose, end=".")
        print(3 * "*")
    elif choose == go_s:
        no_way()
        w2()
    elif choose == l:
        wood_look()
        w2()
    else:
        wrong_com()


def w3():
    sentence = ("\nThe woods are dense, very dark. There are three routes:"
                "\nNorth, West, East.")
    print(sentence)
    choose = input("What do you do?")
    if choose == go_e or choose == go_n or choose == go_w:
        print("You travel", choose, end=".")
        print(3 * "*")
    elif choose == go_s:
        no_way()
        w3()
    elif choose == l:
        wood_look()
        w3()
    else:
        wrong_com()

def wood_look():
    print("\nWoods are dark, you can see sh.. well almost nothing."
          "\nYou can't hear any animals, there are no plants."
          "\n***")



l = 'look'
go_n = 'north'
go_s = 'south'
go_w = 'west'
go_e = 'east'
start()
