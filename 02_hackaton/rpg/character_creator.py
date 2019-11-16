import random


def finalize(final_name, final_gender, final_race):
    if final_gender == "1":
        final_gender = "female"
    else:
        final_gender = "male"
    print("Let's see what you got here!")
    print(f"You are {final_name}, of the mighty race {final_race}. Oh and you are a {final_gender}")
    filename = 'eq.txt'
    newfilename = final_name.lower() + ".txt"

    with open(filename, 'r') as f:
        content = f.readlines()

    del content[0:3]
    content.insert(0, (f"Name: {final_name}\n"))
    content.insert(1, (f"Gender: {final_gender}\n"))
    content.insert(2, (f"Race: {final_race}\n"))

    with open(filename, 'w') as f:
        for item in content:
            f.write(item)

    return newfilename


def name_choice(user_choice_gender, race):
    usa_choi = input("Do you want to auto generate name (lazy option!)? (y/n): ")
    if usa_choi == "y":
        if user_choice_gender == "1":
            if race == "Human":
                choosen_name = random.choice(name_pool[3])
                finalize(choosen_name, user_choice_gender, race)
                return choosen_name
            elif race == "Orc":
                choosen_name = random.choice(name_pool[4])
                finalize(choosen_name, user_choice_gender, race)
                return choosen_name
            else:
                choosen_name = random.choice(name_pool[5])
                finalize(choosen_name, user_choice_gender, race)
                return choosen_name
        if user_choice_gender == "0":
            if race == "Human":
                choosen_name = random.choice(name_pool[0])
                finalize(choosen_name, user_choice_gender, race)
                return choosen_name
            elif race == "Orc":
                choosen_name = random.choice(name_pool[1])
                finalize(choosen_name, user_choice_gender, race)
                return choosen_name
            else:
                choosen_name = random.choice(name_pool[2])
                finalize(choosen_name, user_choice_gender, race)
                return choosen_name
    elif usa_choi == "n":
        choosen_name = input("So please enter your name: ")
        finalize(choosen_name, user_choice_gender, race)
        return choosen_name
    else:
        print("Please writh 'y' or 'n'!")
        name_choice(user_choice_gender, race)


def race_choice():
    print("What is your race please select from option")
    print(" 1 - If you are an Orc")
    print(" 2 - If you are an Human")
    print(" 3 - If you are an Elf")
    select = input('')
    if select == "1":
        race = "Orc"
        return race
    elif select == "2":
        race = "Human"
        return race
    elif select == "3":
        race = "Elf"
        return race
    else:
        print('dupa')
        race_choice()


# def women_story():
#     print("You are ze woman")
#     gender = "1"
#     select = race_choice()
#     name_choice(gender, select)


def select_character(select):
    if select == '1':
        gender = "1"
        select = race_choice()
        name_choice(gender, select)
    elif select == '2':
        gender = "0"
        select = race_choice()
        name_choice(gender, select)
    else:
        print(" Their is no such character i will chose it random")
        #lottery()


def character_creator():
    print(" Who you want to be ?")
    print(" Select an option:")
    print(" 1 - Women")
    print(" 2 - Man")
    user_choice_gender = input("Choose the character put number from 1 to 2:")
    select_character(user_choice_gender)
    return user_choice_gender


def start_creator():
    print( "This is the Game ")
    character_creator()



# hu_m, or_m, el_m, hu_f, or_f, el_f
name_pool = [["Zygfryd", "Gerwazy", "Zawisza"],
["Wrukag", "Zargulg", "Sunuguk"],
["Methild", "Almon", "Elre"],
["Anna", "Rita", "Yennefer"],
["Grat", "Yazgash", "Burzob"],
["Caeda", "Shenarah", "Ayda"]]
