import sqlite3
from ingredient import Ingredient
from stap import Stap
from recept import Recept


def maak_verbinding():
    return sqlite3.connect("receptenboek.db")


def maak_tabellen():
    conn = maak_verbinding()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recept (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT,
            omschrijving TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredient (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recept_id INTEGER,
            naam TEXT,
            hoeveelheid TEXT,
            eenheid TEXT,
            kcal INTEGER,
            is_alternatief INTEGER DEFAULT 0,
            alternatief_voor INTEGER DEFAULT NULL,
            FOREIGN KEY (recept_id) REFERENCES recept(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stap (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recept_id INTEGER,
            beschrijving TEXT,
            tip TEXT,
            FOREIGN KEY (recept_id) REFERENCES recept(id)
        )
    """)

    conn.commit()
    conn.close()


def sla_recept_op(recept):
    conn = maak_verbinding()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO recept (naam, omschrijving) VALUES (?, ?)",
        (recept.naam, recept.omschrijving)
    )
    recept_id = cursor.lastrowid

    for ingredient in recept.ingredienten:
        cursor.execute(
            "INSERT INTO ingredient (recept_id, naam, hoeveelheid, eenheid, kcal, is_alternatief) VALUES (?, ?, ?, ?, ?, ?)",
            (recept_id, ingredient.naam, ingredient.hoeveelheid, ingredient.eenheid, ingredient.kcal, 0)
        )
        ingredient_id = cursor.lastrowid

        if ingredient.plantaardig_alternatief is not None:
            alt = ingredient.plantaardig_alternatief
            cursor.execute(
                "INSERT INTO ingredient (recept_id, naam, hoeveelheid, eenheid, kcal, is_alternatief, alternatief_voor) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (recept_id, alt.naam, alt.hoeveelheid, alt.eenheid, alt.kcal, 1, ingredient_id)
            )

    for stap in recept.stappen:
        cursor.execute(
            "INSERT INTO stap (recept_id, beschrijving, tip) VALUES (?, ?, ?)",
            (recept_id, stap.beschrijving, stap.tip)
        )

    conn.commit()
    conn.close()


def laad_recepten():
    conn = maak_verbinding()
    cursor = conn.cursor()

    cursor.execute("SELECT id, naam, omschrijving FROM recept")
    recept_rijen = cursor.fetchall()

    recepten = []

    for rij in recept_rijen:
        recept_id, naam, omschrijving = rij
        recept = Recept(naam, omschrijving)

        cursor.execute(
            "SELECT id, naam, hoeveelheid, eenheid, kcal FROM ingredient WHERE recept_id = ? AND is_alternatief = 0",
            (recept_id,)
        )
        ingredient_rijen = cursor.fetchall()

        for ing_rij in ingredient_rijen:
            ing_id, ing_naam, hoeveelheid, eenheid, kcal = ing_rij
            ingredient = Ingredient(ing_naam, hoeveelheid, eenheid, kcal)

            cursor.execute(
                "SELECT naam, hoeveelheid, eenheid, kcal FROM ingredient WHERE alternatief_voor = ?",
                (ing_id,)
            )
            alt_rij = cursor.fetchone()
            if alt_rij is not None:
                alt = Ingredient(alt_rij[0], alt_rij[1], alt_rij[2], alt_rij[3])
                ingredient.set_plantaardig_alternatief(alt)

            recept.voeg_ingredient_toe(ingredient)

        cursor.execute(
            "SELECT beschrijving, tip FROM stap WHERE recept_id = ?",
            (recept_id,)
        )
        for stap_rij in cursor.fetchall():
            recept.voeg_stap_toe(Stap(stap_rij[0], stap_rij[1]))

        recepten.append(recept)

    conn.close()
    return recepten


def verwijder_recept(recept_naam):
    conn = maak_verbinding()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM recept WHERE naam = ?", (recept_naam,))
    rij = cursor.fetchone()

    if rij is not None:
        recept_id = rij[0]
        cursor.execute("DELETE FROM ingredient WHERE recept_id = ?", (recept_id,))
        cursor.execute("DELETE FROM stap WHERE recept_id = ?", (recept_id,))
        cursor.execute("DELETE FROM recept WHERE id = ?", (recept_id,))
        conn.commit()

    conn.close()