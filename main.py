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

def toon_overzicht(recepten):
    if len(recepten) == 0:
        print("Er zijn nog geen recepten.")
        return

    print("\nWelkom in het receptenboek!")
    print("==========================")
    nummer = 1
    for recept in recepten:
        print(str(nummer) + ". " + recept.get_naam())
        nummer += 1
    
    gekozen_recept = recepten[keuze - 1]

    personen = 0
    while personen == 0:
        try:
            personen = int(input("Voor hoeveel personen? "))
            if personen < 1:
                print("Foutieve invoer.")
                personen = 0
        except ValueError:
            print("Foutieve invoer.")

    gekozen_recept.set_aantal_personen(personen)

    plantaardig = False
    while True:
        antwoord = input("Plantaardig? (ja/nee): ").lower()
        if antwoord == "ja":
            plantaardig = True
            break
        elif antwoord == "nee":
            break
        else:
            print("Foutieve invoer.")

    gekozen_recept.get_plantaardig_recept(plantaardig)

    keuze = 0
    while keuze == 0:
        try:
            keuze = int(input("\nKies een recept (0 = terug): "))
            if keuze == 0:
                return
            if keuze < 1 or keuze > len(recepten):
                print("Recept niet gevonden.")
                keuze = 0
        except ValueError:
            print("Foutieve invoer.")

def main():
    recepten = maak_recepten()

    while True:
        toon_keuzemenu()
        keuze = input("Kies een optie: ")

        if keuze == "1":
            toon_overzicht(recepten)
        elif keuze == "2":
            pass  # komt later
        elif keuze == "0":
            print("Tot de volgende keer!")
            break
        else:
            print("Foutieve invoer. Kies toevoegen, tonen of exit.")


if __name__ == "__main__":
    main()