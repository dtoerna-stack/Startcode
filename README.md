📖 Receptenboek

Een simpele console-applicatie gebouwd in Python met OOP. Je kunt recepten bekijken, ingrediënten en bereidingsstappen inzien, het aantal personen aanpassen en kiezen voor een plantaardig alternatief.

---

🚀 Opstarten

Run application in main.py file

Zorg dat je Python 3.10 of hoger hebt geïnstalleerd.

---

📐 Code Conventies

- **Klassenamen** beginnen met een hoofdletter: `Recept`, `Ingredient`, `Stap`
- **Methoden en variabelen** zijn in het Nederlands en gebruiken snake_case: `voeg_ingredient_toe`, `aantal_personen`
- **Elke klasse** staat in een eigen bestand
- **Eén klasse per bestand**, geen extra logica buiten de klasse
- Methoden die iets instellen beginnen met `set_`, methoden die iets ophalen met `get_`

---

## 🔀 Git Commit Conventies

Elke commit heeft een prefix die aangeeft wat voor werk er verzet is.

| Prefix | Betekenis | Voorbeeld |
|--------|-----------|-----------|
| `feat:` | Nieuwe functionaliteit toegevoegd | `feat: voeg Stap klasse toe` |
| `upd:` | Bestaande code aangepast of uitgebreid | `upd: hoeveelheid setter toegevoegd aan Ingredient` |
| `fix:` | Bug opgelost | `fix: foutieve index bij recept selectie` |
| `refactor:` | Code opgeschoond zonder gedragswijziging | `refactor: hernoem variabele naar snake_case` |
| `docs:` | Documentatie toegevoegd of aangepast | `docs: README aangemaakt` |
| `test:` | Testcode toegevoegd | `test: controleer kcal berekening voor 2 personen` |
| `chore:` | Kleine klusjes zoals bestandsnamen of opruimen | `chore: verwijder ongebruikte imports` |

### Goede commit voorbeelden

```bash
git commit -m "feat: voeg plantaardig alternatief toe aan Ingredient"
git commit -m "upd: kcal parameter toegevoegd aan Ingredient constructor"
git commit -m "fix: foutafhandeling bij ongeldige invoer in main"
git commit -m "refactor: toon_details verplaatst naar aparte methode"
git commit -m "docs: README aangemaakt met conventies"
```

### Slechte commit voorbeelden

```bash
git commit -m "fix"           # te vaag
git commit -m "dingen gedaan" # zegt niks
git commit -m "WIP"           # commit geen half werk
```

---

## 💡 Tips

- Commit **regelmatig** — na elke afgeronde stap, niet pas aan het einde
- Eén commit = één logische wijziging
- Schrijf je commit message alsof je aan een collega uitlegt wat je gedaan hebt
