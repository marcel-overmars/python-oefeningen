# ==========================================================
# UITLEG PROJECT - DIERENASIEL DAGBEHEER
# ==========================================================
#
# In dit project beheer ik een dierenasiel gedurende zeven
# dagen. De gegevens van het asiel worden opgeslagen in een
# dictionary en de verblijven worden automatisch aangemaakt
# en als dictionaries in een lijst opgeslagen.
#
# Met een while-loop worden de zeven dagen doorlopen.
# Tijdens iedere dag verandert de voedselvoorraad van het
# asiel en de verblijven. Met de modulo-operator (%) worden
# speciale dagen gecontroleerd waarop extra voedsel wordt
# gegeven of een controle plaatsvindt.
#
# Na de zeven dagen wordt de voedselvoorraad van ieder
# verblijf gecontroleerd en krijgt ieder verblijf een
# bijpassende status. De eerste drie verblijven krijgen
# daarnaast extra voedsel.
#
# Ook wordt een dictionary met verzorgers gebruikt. Met een
# geneste for-loop worden per verzorger de verschillende
# diersoorten weergegeven.
#
# Gebruikte onderdelen:
# - dictionaries
# - een lijst met dictionaries
# - dictionaries automatisch aanmaken
# - for-loops
# - een geneste for-loop
# - while-loop
# - range()
# - modulo-operator (%)
# - if, elif en else
# - dictionarywaarden ophalen en wijzigen
# - slices
# - len()
# - .items()
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ===================
# Asielgegevens
# ===================

asielgegevens = {
    'naam': 'dierenasiel zonnehof',
    'voedsel': 400,
    'medewerkers': 6,
    'status': 'open'
}

for asiel, gegevens in asielgegevens.items():
    print(f"{asiel.title()}: {gegevens}")
print()

# ======================
# Verblijvem aanmaken
# ======================

verblijven = []

for aantal_verblijven in range(1, 9):
    verblijf = {
        'dier': 'hond',
        'aantal': 3,
        'voedsel': 40,
        'status': 'rustig'
    }

    verblijven.append(verblijf)

print(f"Aantal verblijven: {len(verblijven)}")

# ====================
# 7 dagen verzorgen
# ====================

dag = 1

while dag < 8:
    for verblijf in verblijven:
        verblijf['voedsel'] -= 5
        print(f"Voedsel voor dag {dag} in het verblijf is: {verblijf['voedsel']}")
    print()

    asielgegevens['voedsel'] -= 20
    print(f"Voedsel voor dag {dag} in het asiel is: {asielgegevens['voedsel']}")
    print()

    if dag % 3 == 0:
        for verblijf in verblijven:
            verblijf['voedsel'] += 10
            print("Vandaag krijgt het verblijf er 10 voedsel bij!")
    print()

    if dag % 5 == 0:
        for verblijf in verblijven:
            verblijf['status'] = 'controle'
            print(f"Er is controle geweest in alle verblijven")
    print()

    dag += 1

# ==========================
# Eindcontrole verblijven
# ==========================

for verblijf in verblijven:
    if verblijf['voedsel'] < 20:
        verblijf['status'] = 'voedselvoorraad laag'
    elif verblijf['voedsel'] < 35:
        verblijf['status'] = 'voedselvoorraad voldoende'
    else:
        verblijf['status'] = 'voedselvoorraad goed'

for verblijf in verblijven:
    print(verblijf)
print()

# =========================================
# Extra voedsel voor eerste 3 verblijven
# =========================================

for verblijf in verblijven[:3]:
    verblijf['voedsel'] += 15

# ====================================
# Aangepaste status voedselvoorraad
# ====================================

for verblijf in verblijven:
    if verblijf['voedsel'] < 20:
        verblijf['status'] = 'voedselvoorraad laag'
    elif verblijf['voedsel'] < 35:
        verblijf['status'] = 'voedselvoorraad voldoende'
    else:
        verblijf['status'] = 'voedselvoorraad goed'

# =================
# Verzorgers
# =================

for verblijf in verblijven:
    print(verblijf)
print()


verzorgers = {
    'marcel': [
        'honden',
        'katten'
    ],

    'elena': [
        'konijnen',
        'vogels'
    ],

    'victor': [
        'honden',
        'reptielen',
        'katten'
    ]
}

for naam, dieren in verzorgers.items():
    print(f"\n{naam.title()} verzorgt de volgende dieren:")
    for dier in dieren:
        print(dier)



# ===============
# Eindrapport
# ===============

print("====================")
print("=== ASIELRAPPORT ===")
print("====================")
print()
print(f"Naam: {asielgegevens['naam'].title()}")
print(f"Resterend voedsel: {asielgegevens['voedsel']}")
print(f"Aantal medewerkers: {asielgegevens['medewerkers']}")
print()
print("VERBLIJVEN")
print()

for verblijf in verblijven:
    print(verblijf)