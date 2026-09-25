# ==========================================================
# UITLEG PROJECT - SPEEDBOX PAKKET-SORTEERCENTRUM
# ==========================================================
#
# In dit project maak ik een sorteersysteem voor een
# pakketbezorgingsbedrijf.
#
# Pakketten worden opgeslagen in dictionaries en samen in
# een lijst geplaatst. Op basis van het gewicht krijgt ieder
# pakket een categorie. Daarnaast kunnen pakketten een aparte
# status krijgen, zoals 'spoed' of 'extra controle'.
#
# Het sorteercentrum gebruikt een while-loop waarin pakketten
# verwerkt, overgeslagen of gestopt kunnen worden. Met break
# wordt de loop beëindigd en met continue wordt een
# sorteerronde overgeslagen.
#
# Gebruikte onderdelen:
# - dictionaries en lijsten
# - lijst met dictionaries
# - lijst in een dictionary
# - .items(), .keys() en .values()
# - for-loops en geneste for-loops
# - while True
# - break en continue
# - if, elif en else
# - modulo (%)
# - slices
# - len()
# - dictionarywaarden toevoegen en wijzigen
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ===================
# Bedrijfgegevens
# ===================

bedrijfgegevens = {
    'naam': 'speedbox',
    'stad': 'apeldoorn',
    'bezorgers': 8,
    'busjes': 5,
    'status': 'actief'
}

for bedrijf, gegevens in bedrijfgegevens.items():
    print(f"{bedrijf.title()}: {gegevens}")
print()

for bedrijf in bedrijfgegevens.keys(): # Alleen de keys
    print(bedrijf)
print()

for gegevens in bedrijfgegevens.values(): # Alleen de waarden
    print(gegevens)
print()

# ==============
# Paketten
# ==============

pakket_1 = {
    'nummer': 101,
    'gewicht': 20,
    'bestemming': 'zwolle',
    'status': 'wacht op sortering'
}

pakket_2 = {
    'nummer': 102,
    'gewicht': 9,
    'bestemming': 'amersfoort',
    'status': 'wacht op sortering'
}

pakket_3 = {
    'nummer': 103,
    'gewicht': 4,
    'bestemming': 'utrecht',
    'status': 'wacht op sortering'
}

pakket_4 = {
    'nummer': 104,
    'gewicht': 6,
    'bestemming': 'hilversum',
    'status': 'wacht op sortering'
}

pakket_5 = {
    'nummer': 105,
    'gewicht': 3,
    'bestemming': 'apeldoorn',
    'status': 'wacht op sortering'
}

pakket_6 = {
    'nummer': 106,
    'gewicht': 17,
    'bestemming': 'arnhem',
    'status': 'wacht op sortering'
}

pakketten = [
    pakket_1,
    pakket_2,
    pakket_3,
    pakket_4,
    pakket_5,
    pakket_6
]

print(f"Totale paketten om te bezorgen: {len(pakketten)}")

# ====================
# Gewichtscontrole
# ====================

for pakket in pakketten:
    if pakket['gewicht'] < 5:
        pakket['categorie'] = 'licht'
    elif pakket['gewicht'] < 15:
        pakket['categorie'] = 'normaal'
    elif pakket['gewicht'] >= 15:
        pakket['categorie'] = 'zwaar'

for pakket in pakketten[-2:]:
    pakket['status'] = 'spoed'

# ====================
# Bezorggebieden
# ====================

gebieden = {
    'noord': [
        'apeldoorn',
        'zwolle'
    ],

    'west': [
        'amersfoort',
        'utrecht',
        'hilversum'
    ],

    'zuid': [
        'arnhem',
        'nijmegen'
    ]
}

for gebied, bestemmingen in gebieden.items():
    print(f"\n{gebied.title()} heeft de volgende bestemmingen:")
    for bestemming in bestemmingen:
        print(bestemming.title())
print()

# ===================
# Sorteercentrum
# ===================

sorteren = 0

while True:
    sorteer = input("Voer in 'pakket', 'overslaan' of 'stop': ")

    if sorteer == 'pakket':
        sorteren += 1
        print("Er is 1 pakket gesorteerd")
        print(f"Aantal gesorteerde pakketten in deze sessie: {sorteren}")

    if sorteer == 'overslaan':
        print(f"\nSorteerronde overgeslagen")
        continue
    print()

    if sorteer == 'stop':
        break

# =================
# Extra controle
# =================

    if sorteren % 4 == 0:
        print("Tijd voor controle van de sorteerband!")
    print()

# =====================
# Voorraad aanpassen
# =====================

for pakket in pakketten[:-2]:
    if pakket['categorie'] == 'zwaar':
        pakket['status'] = 'extra controle'

for pakket in pakketten:
    print(pakket)

# ===============
# Eindrapport
# ===============

print("============================")
print("=== SPEEDBOX EINDRAPPORT ===")
print("============================")
print()
print(f"Bedrijf: {bedrijfgegevens['naam'].title()}")
print(f"Stad: {bedrijfgegevens['stad'].title()}")
print(f"Bezorgers: {bedrijfgegevens['bezorgers']}")
print(f"Busjes: {bedrijfgegevens['busjes']}")
print()
print(f"gesorteerd tijdens sessie: {sorteren}")
print()
print("PAKKETTEN")
print()

for pakket in pakketten:
    print(pakket)