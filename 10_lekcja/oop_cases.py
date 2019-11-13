import random
class Dog:
    tail = True

    def __init__(self, name, breed, age, color): # nie usuwamy nigdy self
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def bark(self):
        return self.age * 'hau'

    def wiggle_tail(self):
        mood = ["happily", "disappointed", "sadly", "angrily"]
        return "Wiggles his tail " + random.choice(mood)

obj_pimpek = Dog("Pimpek", "Shiba", 5, "red")
obj_dyzio = Dog("Dyzio", "German shepherd", 7, "black and white")

print(obj_dyzio.name + Dog.wiggle_tail(obj_dyzio) + "and barks " + obj_dyzio.bark())
