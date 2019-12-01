import dice
import moving
import river


def enter_the_city(player):
    print(f"{player.name} has arrived at  the City. \nYou can see small town. Most noticable buildings are tavern and order.")


def enter_the_tavern(player): # enter_tav():
    print("The tavern is small. Here you can buy weapons, eat food or play a dice.")
    answer = input(f"What do you want to do {player.name}? (buy/play/leave): ")
    if answer == "buy":
        vendor(player)
    elif answer == "play":
        tavern_play(player)
    elif answer == "leave":
        city_direction(player)
    else:
        print("Input either 'buy/play/leave'!")
        enter_the_tavern(player)


def tavern_play(player):
    print("Shady looking guy sits at the table.")
    if player.money >= 10:
        choice = input("Do you want to play traveler? (yes/no): ")
        if choice == 'y' or choice == 'yes':
            print("Lest play then")
            npc_roll = dice.roll_dice()
            player_roll = dice.roll_dice()
            if player_roll > npc_roll:
                print("Shady guy: Not bad. Lucky bastard.")
                player.money += 10
                print(player)
            elif player_roll < npc_roll:
                print("Too bad!")
                player.money -= 10
                print(player)
            else:
                print("Shady guy: Draw? What a pity.")
                print(player)
        elif choice == 'n' or choice == "no":
            print("Shady guy makes angry face and screams 'don't bother me then' and hits you in the face")
            player.life -= 10
            print(player)
        else:
            print("Choose 'yes' or 'no'!")
            tavern_play(player)
    else:
        print(f"Shady guy: You need at least 10 gold coins to play with me and you have only {player.money}. Go away!")
        enter_the_tavern(player)
    enter_the_tavern(player)


def vendor(player):
    weapons = [40, 70, 100]
    foods = [20, 60, 100]
    healing = [10, 30, 50]
    print("You can see vendor.")
    print(f"He sells weapons which improve your attack stat. Right now you have {player.weapon} attack.")
    print(f"He also seels food. It will instantly replenish your life. Right now you have {player.life}/100 hit points.")
    vendor_choice = input("What do you want to do? (weapon/food/leave)? ")
    if vendor_choice == "weapon":
        print("You can get swords adding +1, +2 and +3 attack stat. The price? 40, 70, 100")
        weapon_choice = int(input(f"{player.name} how much attack do you want to add? Input 1, 2, or 3. "))
        if 3 >= weapon_choice > 0:
            if weapons[weapon_choice - 1] > player.money:
                print("You have not enough money.")
                vendor(player)
            else:
                player.money -= weapons[weapon_choice - 1]
                player.weapon += weapon_choice
                print(player)
                vendor(player)
        else:
            print("You need  to input number in range 1-3")
            vendor(player)
    elif vendor_choice == "food":
        print(f"You can eat food regenerating 10, 30 or 50 hit points. You have currently {player.life} hit points.")
        print(f"The price? 20, 60, 100. You have {player.money} gold coins.")
        food_choice = int(input(f"{player.name} how much health points do you want to heal?  Input 1, 2, or 3. "))
        if 3 >= food_choice > 0:
            if foods[food_choice - 1] > player.money:
                print("You have not enough money.")
                vendor(player)
            else:
                player.money -= foods[food_choice - 1]
                player.life += healing[food_choice - 1]
                print(player)
                vendor(player)
        else:
            print("You need  to input number in range 1-3")
            vendor(player)
    elif vendor_choice == "leave":
        enter_the_tavern(player)
    else:
        print("You need to type 'buy' or 'weapon' or 'food'.")
        vendor(player)


def enter_the_order(player):
    print("At the small hall old scribe sits at the desk. As he is the only person there you approach him.")
    print("Scribe: what do you want traveler?")
    if player.quest == 0:
        dialogue_1 = input("Scribe: what do you want traveler? You have entered the Holy Order headquarters."
                           "We have some easy tasks to do for the city. Do you want to help us? (yes/no): ")
        if dialogue_1 == "yes" or dialogue_1 == "y":
            player.quest = 1
            print("Great! You have to travel to river. North from the river bank you will find small cave, where lives"
                  "small troll. He isn't too dangerous but I suggest to get at least basic weapon."
                  "I have to write your name so you will be remembered if any accident occurs.")
            print(f"Mighty {player.name} if you need to prepare please visit tavern. If you are ready... might the force be with you!")
            city_direction(player)
        elif dialogue_1 == "no" or dialogue_1 == "n":
            print("Then we have nothing to talk about. I'm too busy to talk about non important stuff.")
            city_direction(player)
        else:
            print("Please input 'yes' or 'no'")
            enter_the_order(player)
    elif player.quest == 1:
        print("Scribe: Did you deal with troll already?")
        print(f"{player.name}: no.")
        print("Scribe: Then we have nothing to talk about for now. You can leave now")
        print("You do as he said.")
        city_direction(player)
    elif player.quest == 2:
        print("Scribe: Did you deal with troll already?")
        print(f"{player.name}: Yes.")
        print("Scribe: Do you have any proof?")
        print(f"{player.name}: No, you didn't tell me I need to bring something. You can go there and check...")
        print("Scribe: Ah I see. You are a scammer. Well then I'm sorry to say but you will have to get punished.")
        print("You turn around and see knight in black armor entering the room. He has sword in hand and he instantly charges at you.")
        ending_game(player)


def ending_game(player):
    opponent_life = 666
    while player.life > 0 and opponent_life > 0:
        if moving.end_game(player) == "Player win":
            opponent_life -= player.weapon
            print(
                f"{player.name} hits Black Knight for {player.weapon} points! Black Knight has {opponent_life} hit points left.")
        elif moving.end_game(player) == "Black Knight win":
            player.life -= 10
            print(f"{player.name} takes hit for 10 points. You have {player.life} hit points left.")
        else:
            print(moving.end_game(player))
    if player.life == 0:
        print("Oh no, you are dead! X_X")
    elif opponent_life <= 0:
        prize = dice.roll_dice() * 666
        player.money += prize
        print(f"{player.name} has killed Black Knight and found {prize} gold coins. "
              f"Now {player.name} has {player.money} gold coins and {player.life}/100 hit points left.")
        print(f"{player.name} feeling strong walks away from dead Black Knight.")
        player.quest = 3
        print(
            f"Exhausted {player.name} goes to tavern to drink to death.")
        print("You win? I made mistake then it shouldn't be possible!")


def city_direction(player):
    decision = input("Do you want to go the tavern to get some resources or to the order? "
                     "\nYou can also go to the adventure. (tavern/order/adventure): ")
    if decision == "tavern":
        enter_the_tavern(player)
    elif decision == "order":
        enter_the_order(player)
    elif decision == "adventure":
        to_adventure = moving.where_to_go()
        if to_adventure == "stay":
            city_direction(player)
        elif to_adventure == "river":
            river.river_arrival(player)
    else:
        print("Please write 'tavern', 'order' or 'adventure'.")
        city_direction(player)
