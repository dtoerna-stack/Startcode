from recept import Recept 
from ingredient import Ingredient
from stap import Stap

def main():

    # Recept 1
    r1 = Recept("Spaghetti met Kip", "Romige spaghetti met kipstukjes en tomatensaus.")
    r1.voeg_ingredient_toe(Ingredient("spaghetti", "100", "gram"))
    r1.voeg_ingredient_toe(Ingredient("kipfilet", "150", "gram"))
    r1.voeg_ingredient_toe(Ingredient("tomatensaus", "150", "ml"))
    r1.voeg_ingredient_toe(Ingredient("knoflook", "2", "teentjes"))
    r1.voeg_ingredient_toe(Ingredient("geraspte kaas", "2", "el"))
    r1.voeg_ingredient_toe(Ingredient("olijfolie", "1", "el"))
    r1.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes"))
    r1.voeg_stap_toe(Stap("Kook de spaghetti gaar in gezouten water."))
    r1.voeg_stap_toe(Stap("Snijd de kip in blokjes en kruid met zout en peper."))
    r1.voeg_stap_toe(Stap("Bak de kip in olijfolie gaar op middelhoog vuur."))
    r1.voeg_stap_toe(Stap("Voeg de knoflook toe en bak 1 minuut mee."))
    r1.voeg_stap_toe(Stap("Voeg de tomatensaus toe en laat 5 minuten sudderen."))
    r1.voeg_stap_toe(Stap("Schep de spaghetti door de saus en serveer met kaas."))


     # Recept 2
    r2 = Recept("Lasagna", "Klassieke ovenschotel met gehakt, tomatensaus en bechamelsaus.")
    r2.voeg_ingredient_toe(Ingredient("lasagnebladen", "4"))
    r2.voeg_ingredient_toe(Ingredient("gehakt", "150g"))
    r2.voeg_ingredient_toe(Ingredient("tomatensaus", "150ml"))
    r2.voeg_ingredient_toe(Ingredient("melk", "200ml"))
    r2.voeg_ingredient_toe(Ingredient("bloem", "1 el"))
    r2.voeg_ingredient_toe(Ingredient("boter", "1 el"))
    r2.voeg_ingredient_toe(Ingredient("geraspte kaas", "50g"))
    r2.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes"))
    r2.voeg_stap_toe(Stap("Verwarm de oven voor op 200 graden."))
    r2.voeg_stap_toe(Stap("Bak het gehakt rul en voeg de tomatensaus toe."))
    r2.voeg_stap_toe(Stap("Maak de bechamelsaus: smelt boter, voeg bloem toe en roer melk erdoor tot een gladde saus."))
    r2.voeg_stap_toe(Stap("Laag een ovenschaal in: lasagnebladen, gehaktsaus, bechamelsaus. Herhaal."))
    r2.voeg_stap_toe(Stap("Eindig met bechamelsaus en strooi de kaas erover."))
    r2.voeg_stap_toe(Stap("Bak 30 minuten in de oven tot de bovenkant goudbruin is."))

# Lijst tonen
    recepten = [r1, r2]

    print("Welkom in het receptenboek!")
    print("==========================")
    nummer = 1
    for recept in recepten:
        print(str(nummer) + ". " + recept.naam)
        nummer += 1

    keuze = int(input("\nKies een recept: "))
    recepten[keuze - 1].toon_details()

if __name__ == "__main__":
    main()



