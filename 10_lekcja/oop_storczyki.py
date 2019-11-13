import random


class Storczyki:
    krolestwo = "Storczyki rulz"

    def __init__(self, color, gatunek):
        self.color = color
        self.gatunek = gatunek

    def bloom(self):
        time = ['wiosna', 'lato', 'jesień', 'zima']
        return random.choice(time)

storczyk_1 = Storczyki("czerwony", "storczykowaty")
storczyk_2 = Storczyki("niebieski", "kwieciste")
