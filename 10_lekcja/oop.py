class Dog: # tworzenie klasy, zapisujemy klasy raczej z Dużej Litery
    tail = True # łączy wszystkie psy - ATRYBUT KLASY

    def __init__(self, name, breed, age, color): # nie usuwamy nigdy self
        self.name = name        # zapewniamy, że klasa zapamięta dla tego obiektu (poprzez self) wprowadzone imię np. "Pimpek" jako name
        self.breed = breed      # to są ATRYBUTY OBIEKTU
        self.age = age
        self.color = color

    def bark(self):
        return self.age * 'hau'


obj_pimpek = Dog("Pimpek", "Shiba", 5, "red")  # do tworzenia nowego obiektu używamy nawiasów, mimo że tworząc klasę ich nie wpisujemy
obj_dyzio = Dog("Dyzio", "German shepherd", 7, "black and white")

# obj_pimpek.name = "Pimpek"  # dodanie obiektu name. Da się od razu wyświetlić, bez dopisania niczego w "class Dog"
# obj_pimpek.breed = "Sznaucer"   # plot twist! To nie jest wygodne ;D
# obj_pimpek.age = 12
# obj_pimpek.color = "White"

print(obj_pimpek.name)  # wywołujemy parametr z self.<atrybut> w tym wypadku self.name
print(obj_pimpek.color)
print(obj_pimpek.bark())
print(obj_pimpek.tail)
print(obj_dyzio.tail)
print(Dog.tail) # ale już print(Dog.name) nie mogę zrobić
print('---')
print(Dog.__dict__) # wyświetla jakie pola są dostępne z punktu widzenia klasy Dog. Warto pamiętać, że nie widzi wartości pól.
print(obj_dyzio.__dict__) # wyświetla jakie pola są widoczne z punktu widzenia obiektu. Nie ma tu atrybutu tail!
print('***')
print(obj_dyzio.bark())
print(Dog.bark(obj_dyzio))  # tak też można to wyświetlić, trzeba pamiętać o odwołaniu do obiektu
print('\o/')

names = "Anna, Marta, Marek, Paweł"
print(names.split(","))
print(str.split(names)) # analogicznie jak nasze odwołanie do klasy Dog.bark
