import json


def add_new_one(lista):
    imie = input("Podaj dodawane imie: ")
    numer = input("Podaj numer nowego kontaktu: ")
    try:
        int(numer) == numer
    except ValueError:
        print("Wprowadz liczbe.")
    else:
        wpis = {"imie": imie, "numer": numer}
        lista.append(wpis)


def wczytaj_liste_wpisow():
    filename = "ksiazka_numerow.json"
    try:
        with open (filename, "r") as f:
            data = json.load(f)
            how_much = len(data)
            print("Wczytano", how_much, "wpisów.")
            return data
    except FileNotFoundError:
        return []


wpis = {"imie": "Alan", "numer": 666}
lista_numerow = [wpis]
# add_new_one(lista_numerow)

if __name__ == "__main__":
    lista_numerow = wczytaj_liste_wpisow()
    add_new_one(lista_numerow)
    with open("ksiazka_numerow.json", mode="w") as plik:
        json.dump(lista_numerow, plik, indent=2)
