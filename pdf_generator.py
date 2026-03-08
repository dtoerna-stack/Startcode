from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas


def genereer_pdf(recept, plantaardig=False):
    bestandsnaam = recept.naam + ".pdf"
    c = canvas.Canvas(bestandsnaam, pagesize=A4)
    breedte, hoogte = A4
    y = hoogte - 50

    def schrijf_regel(tekst, x=50, grootte=12, vet=False, kleur=colors.black):
        c.setFont("Helvetica-Bold" if vet else "Helvetica", grootte)
        c.setFillColor(kleur)
        c.drawString(x, y, tekst)

    def nieuwe_regel(stap=18):
        nonlocal y
        y -= stap
        if y < 60:
            c.showPage()
            nonlocal y
            y = hoogte - 50

    # Titel
    schrijf_regel(recept.naam, grootte=22, vet=True, kleur=colors.HexColor("#2e86ab"))
    nieuwe_regel(30)

    # Omschrijving
    schrijf_regel(recept.omschrijving, grootte=11, kleur=colors.grey)
    nieuwe_regel(25)

    # Streep
    c.setStrokeColor(colors.HexColor("#2e86ab"))
    c.setLineWidth(1.5)
    c.line(50, y, breedte - 50, y)
    nieuwe_regel(20)

    # Personen en kcal
    totaal_kcal = sum(
        ingredient.get_ingredient(plantaardig).get_kcal() * recept.aantal_personen
        for ingredient in recept.ingredienten
    )
    schrijf_regel("Personen: " + str(recept.aantal_personen) + "   |   Totaal kcal: " + str(totaal_kcal), grootte=11)
    nieuwe_regel(25)

    # Ingredienten
    schrijf_regel("Ingrediënten", grootte=14, vet=True)
    nieuwe_regel()

    for ingredient in recept.ingredienten:
        gekozen = ingredient.get_ingredient(plantaardig)
        schrijf_regel("•  " + str(gekozen), x=60, grootte=11)
        nieuwe_regel()

    nieuwe_regel(10)

    # Stappen
    schrijf_regel("Bereidingsstappen", grootte=14, vet=True)
    nieuwe_regel()

    nummer = 1
    for stap in recept.stappen:
        schrijf_regel(str(nummer) + ".  " + stap.beschrijving, x=60, grootte=11)
        nieuwe_regel()
        if stap.tip is not None:
            schrijf_regel("Tip: " + stap.tip, x=75, grootte=10, kleur=colors.HexColor("#e07b39"))
            nieuwe_regel()
        nummer += 1

    c.save()
    print("PDF opgeslagen als: " + bestandsnaam)