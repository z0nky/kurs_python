class Vertebrate:
    backbone = True

    def __init__(self):
        print("I haz backbone bby!")

    # def __str__(self):
    #     return "I am Vertebrate"

    def desc(self):
        print("Kręgowce zamieszkują najróżniejsze środowiska.")


class Cat(Vertebrate):
    def __init__(self, name):
        print("Me cat! MEOW!")
        self.name = name

    def sound(self):
        return "purr"

    def desc(self):
        super().desc()  # super() pozwala dostać się do SUPERIOR class
        print("Koty są ok.")


ver = Vertebrate()
kitty = Cat("Ze Cat")
# print(ver)
print(kitty.desc())
