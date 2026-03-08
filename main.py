from recept import Recept
from ingredient import Ingredient
from stap import Stap


def toon_keuzemenu():
    print("\n==========================")
    print("Wat wil je doen?")
    print("1. Tonen overzicht recepten")
    print("2. Toevoegen recept")
    print("0. Exit")
    print("==========================")


def main():
    recepten = maak_recepten()

    while True:
        toon_keuzemenu()
        keuze = input("Kies een optie: ")

        if keuze == "1":
            pass  # komt later
        elif keuze == "2":
            pass  # komt later
        elif keuze == "0":
            print("Tot de volgende keer!")
            break
        else:
            print("Foutieve invoer. Kies toevoegen, tonen of exit.")


if __name__ == "__main__":
    main()