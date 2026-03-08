class Stap:
    def __init__(self, beschrijving, tip=None):
        self.beschrijving = beschrijving
        self.tip = tip

    def __str__(self):
        return self.beschrijving