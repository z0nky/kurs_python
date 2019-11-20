from abc import ABC, abstractmethod


class Vehicles(ABC):
    @abstractmethod
    def wheels(self):
        pass

    def doc(self):
        pass


class Car(Vehicles):

    def wheels(self):
        print("I have 4 wheels")

    def doc(self):
        print("Driving licence")


class Bicycle(Vehicles):

    def wheels(self):
        print("I have 2 wheels")

    def doc(self):
        print("Nothing at all!")

c = Car()
b = Bicycle()
c.doc()
b.doc()
