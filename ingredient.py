class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid="", kcal=0):
        self.naam = naam
        self.hoeveelheid = hoeveelheid
        self.eenheid = eenheid
        self.kcal = kcal
        self.plantaardig_alternatief = None

    def set_hoeveelheid(self, hoeveelheid):
        self.hoeveelheid = hoeveelheid

    def get_hoeveelheid(self):
        return self.hoeveelheid

    def get_kcal(self):
        return self.kcal

    def set_plantaardig_alternatief(self, alternatief):
        self.plantaardig_alternatief = alternatief

    def get_ingredient(self, plantaardig):
        if plantaardig and self.plantaardig_alternatief is not None:
            return self.plantaardig_alternatief
        return self

    def __str__(self):
        return f"{self.hoeveelheid} {self.eenheid} {self.naam}"