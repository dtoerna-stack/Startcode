from ingredient import Ingredient
from stap import Stap


class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten: list[Ingredient] = []
        self.__stappen: list[Stap] = []

    def get_naam(self) -> str:
        return self.__naam

    def get_omschrijving(self) -> str:
        return self.__omschrijving

    def voeg_ingredient_toe(self, ingredient: Ingredient):
        self.__ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap: Stap):
        self.__stappen.append(stap)

    def toon_details(self):
        print(f"\n{'=' * 50}")
        print(f"Recept: {self.__naam}")
        print(f"Omschrijving: {self.__omschrijving}")

        print("\nIngrediënten (per persoon):")
        for ingredient in self.__ingredienten:
            print(f"  • {ingredient}")

        print("\nBereidingsstappen:")
        for index, stap in enumerate(self.__stappen, start=1):
            print(f"  {index}. {stap}")

        print(f"{'=' * 50}")