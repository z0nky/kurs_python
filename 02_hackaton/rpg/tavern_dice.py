# taver_dice
import random

filename = "eq.txt"

with open(filename, 'r') as f:
    content = f.readlines()
    print(content)

adventurer = content[0].split()[1]
purse = (content[3].split()[1])
def forester():
    print(" Its take you 8 hours to got to the forest man, so your supply are diminish to half")

    print(" Suddenly form the wood jump out the wolf, you must fight with him, and you got hurt, he lost -2 life points")
    print(" You need some medical attention, suddenly you meet the forester")
    print(" Do you need help , answer y/n")
    answer = input()
    if answer == "y":
        print("The forester gave you some food, and medical attention, you fill better, you got back +1 of your life points")
    elif answer == "n":
        print("You loose some blood, you fill bad, you loos another -1 of your life points")
    else:
        print(" Wrong answer, think one more time")
        forester()

def roll_the_dice():
    cubes_wall = ['1', '2', '3', '4', '5', '6']
    dice_number = random.choice(cubes_wall)
    #print("You rolled the dice dropped out: ", dice_number)
    return dice_number

def play():
    user_dice_number = roll_the_dice()
    print("Your dice number:", user_dice_number)
    tawern_man_dice_number = roll_the_dice()
    print("Tavern man dice number:", tawern_man_dice_number)
    if int(user_dice_number) > int(tawern_man_dice_number):
        winner = "user"
        return winner
    elif int(user_dice_number) < int(tawern_man_dice_number):
        winner = "tawernman"
        return winner
    else:
        winner = "0"
        return winner

def gold_purse(money):
    global purse
    purse = int(purse) + int(money)
    print("You have " + str(purse) + " zł on your count")
    return purse


def tawer_place():
    print("If you want to know what is your mission you need to go to the tavern, there will be a man in red hat")
    print("You went to a tavern and you meet a man who sad: Roll the dice, if you win , then I will tale you what to do next")
    choice = input(" Do you wont to play y/n:")
    if choice == 'y':
        print("Lest play then")
        winner = play()
        if winner == "user":
            print(" You win you should go to the forest, you got an extra money")
            money = 40
            print(gold_purse(money))
            print(" When you got to hte forest look after the forester, he will gave you some answers ")
            forester()

        elif winner == "tawernman":
            print(" You loose you need to pay me for information - 20 zł: ")
            money = -20
            print(gold_purse(money))
            print(" You should go back to your home")
        elif winner == "0":
            print(" You have lucky lets play again")
            play()

    elif choice == 'n':
        print("It was a bad choice, you have two doors to chose to go out from here")
        print("Chose one of the doors , select the number: 1 or 2 :")
        answer = input()
        if answer == "1":
            print("You chose door number 1 - you will go to the dungeons you have to kill a dragon")
            print("You need too chose your weapon")
        elif answer == "2":
            print("You chose door number 2 - you will go out on the desert you have to buy a water for 50 zł to stay alive")
            money = -50
            print(gold_purse(money))
            if  gold_purse(money) >= 0:
                print(" Here is your water good luck")
                print(" When you go through the desert, you should find the : Human City")
            else:
                print("You have not enough money to bay a watter, you will die")
                print("It, was pleasure to meet you , you loose you are a death man")
                print("END of GAME")
    else:
        print("Wrong choice try again")
        tawer_place()
