import wood

class Player:
    def __init__(self, name):
        self.name = name
        self.life = 100
        self.weapon = 0

    def __str__(self):
        return f"{self.name} has {self.life} % life and {self.weapon} current weapon"

    def eat(self):
        self.life = 100

    # @property
    # def life(self):
    #     self.life = 100
    #
    # @life.setter
    # def life(self, value):
    #     self._life = value


def main():
    generated_name = 'Zygfryd'
    player = Player(generated_name)
    print(player)
    wood.adventure(player)
    print(player)



if __name__ == "__main__":
    main()