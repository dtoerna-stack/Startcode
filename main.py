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

    while True:
        antwoord = input("\nRecept verwijderen of terug? (verwijderen/home): ").lower()
        if antwoord == "verwijderen":
            bevestig_verwijdering(recepten, gekozen_recept)
            break
        elif antwoord == "home":
            break
        else:
            print("Foutieve invoer.") 
    
def bevestig_verwijdering(recepten, recept):
    while True:
        antwoord = input("Weet je het zeker? (ja/nee): ").lower()
        if antwoord == "ja":
            recepten.remove(recept)
            print("Recept verwijderd.")
            break
        elif antwoord == "nee":
            break
        else:
            print("Foutieve invoer.")

def voeg_ingredienten_toe(recept):
    while True:
        naam = input("Naam ingrediënt: ")

        hoeveelheid = ""
        while hoeveelheid == "":
            try:
                hoeveelheid = input("Hoeveelheid (getal): ")
                float(hoeveelheid)
            except ValueError:
                print("Foutieve invoer.")
                hoeveelheid = ""

        eenheid = input("Eenheid (bijv. gram, ml, el): ")

        kcal = 0
        while True:
            try:
                kcal = int(input("Kcal: "))
                break
            except ValueError:
                print("Foutieve invoer.")

        ingredient = Ingredient(naam, hoeveelheid, eenheid, kcal)

        while True:
            antwoord = input("Plantaardig alternatief? (ja/nee): ").lower()
            if antwoord == "ja":
                alt_naam = input("Naam alternatief: ")
                alt_kcal = 0
                while True:
                    try:
                        alt_kcal = int(input("Kcal alternatief: "))
                        break
                    except ValueError:
                        print("Foutieve invoer.")
                alternatief = Ingredient(alt_naam, hoeveelheid, eenheid, alt_kcal)
                ingredient.set_plantaardig_alternatief(alternatief)
                break
            elif antwoord == "nee":
                break
            else:
                print("Foutieve invoer.")

        recept.voeg_ingredient_toe(ingredient)

        while True:
            antwoord = input("Nog een ingrediënt? (ja/nee): ").lower()
            if antwoord == "ja":
                break
            elif antwoord == "nee":
                return
            else:
                print("Foutieve invoer.")

def voeg_stappen_toe(recept):
    while True:
        beschrijving = input("Stap beschrijving: ")
        tip = None

        while True:
            antwoord = input("Tip toevoegen? (ja/nee): ").lower()
            if antwoord == "ja":
                tip = input("Tip: ")
                break
            elif antwoord == "nee":
                break
            else:
                print("Foutieve invoer.")

        recept.voeg_stap_toe(Stap(beschrijving, tip))

        while True:
            antwoord = input("Nog een stap? (ja/nee): ").lower()
            if antwoord == "ja":
                break
            elif antwoord == "nee":
                return
            else:
                print("Foutieve invoer.")

def main():
    recepten = maak_recepten()

    while True:
        toon_keuzemenu()
        keuze = input("Kies een optie: ")

        if keuze == "1":
            toon_overzicht(recepten)
        elif keuze == "2":
            naam = input("Naam recept: ")
            omschrijving = input("Omschrijving: ")
            nieuw_recept = Recept(naam, omschrijving)
            voeg_ingredienten_toe(nieuw_recept)
            voeg_stappen_toe(nieuw_recept)
            recepten.append(nieuw_recept)
            print("\nRecept toegevoegd!")
            nieuw_recept.get_plantaardig_recept(False)
        elif keuze == "0":
            print("Tot de volgende keer!")
            break
        else:
            print("Foutieve invoer. Kies toevoegen, tonen of exit.")


if __name__ == "__main__":
    main()