import tavern_dice as td


def vendor():
    print("Fat man sells some items. What do you want to browse?")
    browse = input(f"{adventurer.capitalize()} choose what do you want to buy (weapon/armor): ")
    global purse
    global user_armor
    global user_weapon
    if browse.lower() == "weapon":
        print(weapon)
        buy = input("Do you want to buy something? (y/n)")
        if buy == "y":
            what = input("What item do you want to buy? Enter it's full name: ")
            print(what in weapon)
            if (what in weapon) == True:
                print("Price", weapon.get(what))
                if (int(purse) - int(weapon.get(what))) < 0:
                    print("You have not enough money!")
                    vendor()
                else:
                    purse = (int(purse) - int(weapon.get(what)))
                    user_weapon = (user_weapon + ", " + what)
                    print("Nowe sald", purse)
                    enter_tav()
            else:
                print("No such item")
                vendor()
        else:
            print(f"{adventurer} sees that items sold here are plain garbage. No need to waste precious {purse} gold coins.")
            enter_tav()
    elif browse.lower() == "armor":
        print(armor)
        buy = input("Do you want to buy something? (y/n)")
        if buy == "y":
            what = input("What item do you want to buy? Enter it's full name: ")
            print(what in armor)
            if (what in armor) == True:
                print("Price", armor.get(what))
                if (int(purse) - int(armor.get(what))) < 0:
                    print("You have not enough money!")
                    vendor()
                else:
                    purse = (int(purse) - int(armor.get(what)))
                    user_armor = (user_armor + ", " + what)
                    print("Nowe sald", purse)
                    enter_tav()
            else:
                print("No such item")
                vendor()
        else:
            print(f"{adventurer} sees that items sold here are plain garbage. No need to waste precious {purse} gold coins.")
            enter_tav()


def enter_tav():
    print("You arrived in small tavern. Here you can buy items, play dice for money or go adventuring. You can check your purse.")
    desti = input("What do you want to do? (dice/shop/purse): ")
    if desti == "shop":
        vendor()
    elif desti == "dice":
        td.tawer_place()
    elif desti == "purse":
        print(f"{adventurer} has", purse, f"gold coins.")
        enter_tav()
    else:
        print(f"{adventurer} you need to type 'dice', 'purse' or 'shop'")
        enter_tav()


def open_eqfile_tav():
    filename = "eq.txt"
    global content, adventurer, purse, user_armor, user_weapon
    with open(filename, 'r+') as f:
        content = f.readlines()

    adventurer = content[0].split()[1]
    purse = (content[3].split()[1])
    user_armor = (content[4].split(":")[1])
    user_armor = (content[5].split(":")[1])
    enter_tav()


armor = {
    "Dirty rug" : 40,
    "Leather armor" : 80,
    "Plate armor" : 300
}

weapon = {
    "Stick" : 10,
    "Club" : 30,
    "Rusty sword" : 50,
    "Sharp knife": 100,
    "Longsword" : 300
}
