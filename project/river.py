import dice

def river_direction(player):
    decision = input("You are near the river bank. You can go north or east. (north/east) ")
    if decision == "north":
        print("You found cave entrance. You can't see too far inside.")
        if player.quest == 1:
            pass #wczyta fkcje jaskini trolla
        elif player.quest == 0:
            print("You hear roar coming from dark cave. You don't feel like going inside!")
            river_direction(player)
        else:
            print("Please input 'north' or 'east'.")
            river_direction(player)
    elif decision == "east":
        print("On the small green grassland. You see small birds called Scavengers running around.")
        encounter_choice = input(f"{player.name} do you want to attack scavenger? Remember you have {player.life} hit points,"
                                 f"{player.weapon} attack points. (attack/back) ")
        if encounter_choice == "attack":
            print("You jump on the one of the scavengers.")
            player_roll = dice.roll_dice()
            scav_roll = dice.roll_dice()
            #ify na encounter
        elif encounter_choice == "back":
            print("You quiletly move back.")
            river_direction(player)
        else:
            print("Please input text according to the bracketed words.")
            river_direction(player)


def river_arrival(player):
    print(f"{player.name} arrived at the river bank.")
    river_direction(player)
