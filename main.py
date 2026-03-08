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


def maak_recepten():
    recepten = []

    r1 = Recept("Spaghetti met Kip", "Romige spaghetti met kipstukjes en tomatensaus.")
    r1.voeg_ingredient_toe(Ingredient("spaghetti", "100", "gram", 350))
    r1.voeg_ingredient_toe(Ingredient("kipfilet", "150", "gram", 165))
    r1.voeg_ingredient_toe(Ingredient("tomatensaus", "150", "ml", 50))
    r1.voeg_ingredient_toe(Ingredient("knoflook", "2", "teentjes", 10))
    r1.voeg_ingredient_toe(Ingredient("geraspte kaas", "2", "el", 80))
    r1.voeg_ingredient_toe(Ingredient("olijfolie", "1", "el", 120))
    r1.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes", 0))
    r1.voeg_stap_toe(Stap("Kook de spaghetti gaar in gezouten water."))
    r1.voeg_stap_toe(Stap("Snijd de kip in blokjes en kruid met zout en peper."))
    r1.voeg_stap_toe(Stap("Bak de kip in olijfolie gaar op middelhoog vuur.", "Zorg dat de pan goed heet is voor een mooie kleur."))
    r1.voeg_stap_toe(Stap("Voeg de knoflook toe en bak 1 minuut mee."))
    r1.voeg_stap_toe(Stap("Voeg de tomatensaus toe en laat 5 minuten sudderen."))
    r1.voeg_stap_toe(Stap("Schep de spaghetti door de saus en serveer met kaas."))
    tofu = Ingredient("tofu", "150", "gram", 120)
    r1.get_ingredienten()[1].set_plantaardig_alternatief(tofu)
    recepten.append(r1)

    r2 = Recept("Lasagna", "Klassieke ovenschotel met gehakt, tomatensaus en bechamelsaus.")
    r2.voeg_ingredient_toe(Ingredient("lasagnebladen", "4", "stuks", 140))
    r2.voeg_ingredient_toe(Ingredient("gehakt", "150", "gram", 300))
    r2.voeg_ingredient_toe(Ingredient("tomatensaus", "150", "ml", 50))
    r2.voeg_ingredient_toe(Ingredient("melk", "200", "ml", 100))
    r2.voeg_ingredient_toe(Ingredient("bloem", "1", "el", 30))
    r2.voeg_ingredient_toe(Ingredient("boter", "1", "el", 90))
    r2.voeg_ingredient_toe(Ingredient("geraspte kaas", "50", "gram", 180))
    r2.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes", 0))
    r2.voeg_stap_toe(Stap("Verwarm de oven voor op 200 graden."))
    r2.voeg_stap_toe(Stap("Bak het gehakt rul en voeg de tomatensaus toe."))
    r2.voeg_stap_toe(Stap("Maak de bechamelsaus: smelt boter, voeg bloem toe en roer melk erdoor tot een gladde saus.", "Blijf constant roeren zodat er geen klontjes ontstaan."))
    r2.voeg_stap_toe(Stap("Laag een ovenschaal in: lasagnebladen, gehaktsaus, bechamelsaus. Herhaal."))
    r2.voeg_stap_toe(Stap("Eindig met bechamelsaus en strooi de kaas erover."))
    r2.voeg_stap_toe(Stap("Bak 30 minuten in de oven tot de bovenkant goudbruin is."))
    linzen = Ingredient("linzen", "150", "gram", 180)
    r2.get_ingredienten()[1].set_plantaardig_alternatief(linzen)
    recepten.append(r2)

    r3 = Recept("Stampot met Rookworst", "Hollandse klassieker met aardappel, boerenkool en rookworst.")
    r3.voeg_ingredient_toe(Ingredient("aardappelen", "300", "gram", 250))
    r3.voeg_ingredient_toe(Ingredient("boerenkool", "100", "gram", 35))
    r3.voeg_ingredient_toe(Ingredient("rookworst", "1", "stuks", 290))
    r3.voeg_ingredient_toe(Ingredient("melk", "3", "el", 20))
    r3.voeg_ingredient_toe(Ingredient("boter", "1", "el", 90))
    r3.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes", 0))
    r3.voeg_stap_toe(Stap("Schil de aardappelen en kook ze gaar in gezouten water."))
    r3.voeg_stap_toe(Stap("Voeg de boerenkool de laatste 5 minuten mee toe aan het kookwater."))
    r3.voeg_stap_toe(Stap("Verwarm de rookworst in warm water volgens de verpakking.", "Laat het water niet koken, anders barst de worst."))
    r3.voeg_stap_toe(Stap("Giet de aardappelen en boerenkool af en stamp ze fijn."))
    r3.voeg_stap_toe(Stap("Voeg melk en boter toe en stamp tot een smeuige stampot."))
    r3.voeg_stap_toe(Stap("Breng op smaak met zout en peper en serveer met de rookworst."))
    vegaworst = Ingredient("vegetarische rookworst", "1", "stuks", 180)
    r3.get_ingredienten()[2].set_plantaardig_alternatief(vegaworst)
    recepten.append(r3)

    return recepten


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