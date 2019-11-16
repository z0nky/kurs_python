list = "Gold: 100, 30"
newlist = list.split(":")
print(newlist[1])
newlist[1] = (newlist[1] + ", " + "added")
print(newlist)
