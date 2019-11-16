import dice_roll


def area_01_wake():
    plot = (
        "\n\nThe terrain is flat. Next to you stands wooden elevator, which is at the top of the cliff. There is nothing to call it down."
        "\nThere is no way you can climb back, and even if you could, the barrier at the top would kill you."
        "\nAt the north of the small valley you can see road, probably often used one.")
    print(plot, "\n* * *")
    area_01_1choice()


def area_01_1choice():
    choice01 = input("You can look around or go north. What do you do? \n(look/north): ")
    if choice01 == "north":
        encounter_01_lotto()
    elif choice01 == "look":
        area_01_look()
    else:
        print("Please enter 'look' or 'north'")
        area_01_1choice()


def area_01_look():
    print("There is nothing else to see. Broken tools like pickaxes and shovels, torn clothes."
          "\nYou decided to proceed north")
    encounter_01_lotto()


def encounter_01_lotto():
    print("To proceed you need to roll a dice")
    dice = dice_roll.roll_dice()
    if dice <= 3:
        print(f"You rolled {dice}. Brace yourself!")
        print(".\n" * 10)
        print("Just kidding, proceed")
        return "enter_tav()"
    else:
        print(f"You rolled {dice}. The passage is safe")
        return "enter_tav()"

