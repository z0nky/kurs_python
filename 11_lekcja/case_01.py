class Mammal:
    milk_drinker = True

    def __init__(self):
        print("I'm mammal!")

    def desc(self):
        print("are vertebrate animals constituting the class Mammalia")


class Human(Mammal):
    def __init__(self):
        super().__init__()
        print("I'm human!")


class Cat(Mammal):
    def __init__(self):
        super().__init__()
        print("I'm kitty meow!")


class Dog(Mammal):
    def __init__(self):
        super().__init__()
        print("I'm doggo!")


h = Human()
c = Cat()
d = Dog()

h.desc()