from ingredient import Ingredient
from stap import Stap


class Recept:
    def __init__(self, naam, omschrijving):
        self.naam = naam
        self.omschrijving = omschrijving
        self.ingredienten = []
        self.stappen = []
        self.aantal_personen = 1

    def get_naam(self):
        return self.naam

    def voeg_ingredient_toe(self, ingredient):
        self.ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.stappen.append(stap)

    def get_ingredienten(self):
        return self.ingredienten

    def set_aantal_personen(self, personen):
        for ingredient in self.ingredienten:
            nieuwe_hoeveelheid = float(ingredient.get_hoeveelheid()) * personen
            if nieuwe_hoeveelheid == int(nieuwe_hoeveelheid):
                ingredient.set_hoeveelheid(str(int(nieuwe_hoeveelheid)))
            else:
                ingredient.set_hoeveelheid(str(nieuwe_hoeveelheid))
        self.aantal_personen = personen

    def get_aantal_personen(self):
        return self.aantal_personen

    def get_plantaardig_recept(self, plantaardig):
        totaal_kcal = 0
        print("Naam: " + self.naam)
        print("Omschrijving: " + self.omschrijving)
        print("Aantal personen: " + str(self.aantal_personen))

        print("\nIngredienten:")
        for ingredient in self.ingredienten:
            gekozen = ingredient.get_ingredient(plantaardig)
            print("  - " + str(gekozen))
            totaal_kcal += gekozen.get_kcal() * self.aantal_personen

        print("\nStappen:")
        nummer = 1
        for stap in self.stappen:
            print("  " + str(nummer) + ". " + stap.beschrijving)
            if stap.tip is not None:
                print("     Tip: " + stap.tip)
            nummer += 1

        print("\nTotaal kcal: " + str(totaal_kcal) + " kcal")

    def toon_details(self):
        self.get_plantaardig_recept(False)