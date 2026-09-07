# ==========================================================
# UITLEG PROJECT - PRETPARK DAGACTIE
# ==========================================================
#
# In dit project oefen ik met de modulo-operator (%) om te
# controleren of een bezoekersnummer precies deelbaar is
# door een bepaald getal.
#
# De bezoeker voert zelf gegevens in. Op basis van het
# bezoekersnummer bepaalt het programma of de bezoeker een
# gratis drankje krijgt. De uitkomst wordt opgeslagen zodat
# deze later opnieuw in het eindrapport gebruikt kan worden.
#
# Daarnaast bepaalt het programma aan de hand van de leeftijd
# welk type kaartje nodig is en wordt gecontroleerd of een
# gekozen attractie beschikbaar is.
#
# Gebruikte onderdelen:
# - input()
# - int()
# - modulo-operator (%)
# - if, elif en else
# - variabelen gebruiken om beslissingen op te slaan
# - lijsten
# - dictionaries
# - in
# - lower() en title()
# - len()
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ========================
# Gebruikersinformatie
# ========================

naam = input("Wat is je naam? ")
leeftijd = int(input("Wat is je leeftijd? "))
bezoekersnummer = int(input("Wat is je bezoekersnummer? "))
print()

# ============================================
# Gratis drankje voor elke vijfde bezoeker
# ============================================

if bezoekersnummer % 5 == 0:
    drankje = "een drankje"
else:
    drankje = "geen drankje"

print(f"{naam.title()} krijgt {drankje}")
print()

# ======================
# Leeftijdscontrole
# ======================

if leeftijd < 12:
    type_kaartje = 'kinderkaartje'
elif leeftijd < 18:
    type_kaartje = 'jongerenkaartje'
else:
    type_kaartje = 'normaal kaartje'
    print(f"{naam.title()} krijgt een {type_kaartje}")
print()



# ======================
# Favoriete attractie
# ======================

attracties = [
    'achtbaan',
    'wildwaterbaan',
    'spookhuis',
    'reuzenrad',
    "botsauto's",
]

attractie = input("Welke attractie zou je graag willen bezoeken? ")

if attractie.lower() in attracties:
    print(f"\n{attractie.title()} is aanwezig in het park!")
else:
    print(f"\n{attractie.title()} is helaas niet aanwezig in het park!")
print()

pretpark = {
    'naam': 'avonturenland',
    'aantal attractie': 5,
    'entreeprijs': 32,
    'status': 'open'
}

# ==============
# Eindrapport
# ==============

print("==========================")
print("=== BEZOEKERSOVERZICHT ===")
print("==========================")
print()
print(f"Naam: {naam.title()}")
print(f"Leeftijd: {leeftijd}")
print(f"Bezoekersnummer: {bezoekersnummer}")
print(f"Type kaartje: {type_kaartje.title()}")
print(f"Gekozen attractie: {attractie.title()}")
print(f"Gratis drankje: {drankje.title()}")