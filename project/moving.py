def where_to_go():
    print("City road leads towards river and mine. But you have spotted sign saying 'Mines closed.'. You can also stay in the city")
    destination = input("Where will you travel? (river/stay) ")
    if destination == "river":
        return "river"
    elif destination == "stay":
        return "stay"
    else:
        print("Please input 'river' or 'stay'!")
        where_to_go()
