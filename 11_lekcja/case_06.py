class Country:

    def __init__(self, name, population, language, capitol):
        self.name = name
        self.population = population
        self.language = language
        self.capitol = capitol

    def __repr__(self):
        return self.name + " has capitol: " + self.capitol


Poland = Country("Poland", 37.98, "Polish", "Warsaw")
Germany = Country("Germany", 82.79, "German", "Berlin")
Nibylandia = Country("Nibylandia", 0, "None", "Doesn't exist")

list = [Poland, Germany, Nibylandia]
# print(list)
print(Country.__repr__(Poland)) # wyświetlanie __repr__ dla pojedynczego \o/ zostawiam, bo tak!
print(list)
