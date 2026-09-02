# ==========================================================
# UITLEG PROJECT - HERBERG DE ZILVEREN DRAAK
# ==========================================================
#
# In dit project oefen ik verder met nesting door lijsten
# als values in dictionaries op te slaan en deze gegevens
# vervolgens met for-loops te doorlopen.
#
# Met keys(), values() en items() worden verschillende delen
# van dictionaries bekeken. Met een tweede for-loop worden
# de afzonderlijke voorwerpen uit de inventarislijsten van
# de gasten doorlopen en gecontroleerd.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - een lijst als value in een dictionary
# - nesting en geneste for-loops
# - keys(), values() en items()
# - get() voor ontbrekende gegevens
# - sorted()
# - for-loops
# - if, elif en else
# - len()
# - lists en slices
# - append(), insert(), remove() en pop()
# - indexen en dictionarywaarden combineren
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ===============================
# Basisgegevens van de herberg
# ===============================

herberg = {
    'naam': 'de zilveren draak',
    'locatie': 'ravenburg',
    'kamers': 18,
    'bezette kamers': 11,
    'goudvoorraad': 750,
    'status': 'geopend'
}

for gegevens, waarde in herberg.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# =========================
# Aleen de gegevensnamen
# =========================

for gegevens in herberg.keys():
    print(gegevens)
print()

# ===================
# Alleen de waarden
# ===================

for waarden in herberg.values():
    print(waarden)
print()

# ===============
# Eerste gast
# ===============

gast = {
    'naam': 'elara',
    'beroep': 'magiër',
    'level': 27,
    'goud': 85,
    'voorwerpen': [
        'staf',
        'toverboek',
        'mana potion',
        'sleutel'
    ]
}

print(f"Naam van de gast: {gast['naam'].title()}")
print(f"Beroep van de gast: {gast['beroep'].title()}")
print()
print("Voorwerpen die gast bij zich heeft:")

for voorwerpen in gast['voorwerpen']:
    print(voorwerpen)
print()

# =========================
# Een ontbrekend gegeven
# =========================

paard = gast.get('paard', 'Geen paard geregistreerd.')

print(paard)
print()

# =================
# Gastenregister
# =================

gastenregister = {
    'elara': [
        'staf',
        'toverboek',
        'mana potion'
    ],
    'borin': [
        'zwaard',
        'schild'
    ],
    'luna': ['boog'],
    'darius': [
        'dolk',
        'kaart',
        'touw'
    ],
    'sofia': [
        'kruiden',
        'verband'
    ]
}

# ===========================================
# Alle gastnamen op alfabetische volgorde
# ===========================================

for gastnaam in sorted(gastenregister.keys()):
    print(gastnaam)
print()

# ==========================
# Alle inventarislijsten
# ==========================

for inventaris in gastenregister.values():
    print(inventaris)
print()

# ==========================
# Gast en zijn voorwerpen
# ==========================

for gast, inventaris in gastenregister.items():
    print(f"\n{gast.title()} heeft bij zich:")
    for voorwerpen in inventaris:
        print(f"{voorwerpen}")
print()

# ================================
# Controle op aantal voorwerpen
# ================================

for gast, inventaris in gastenregister.items():
    if len(inventaris) < 2:
        print(f"{gast.title()} reist licht.")
    elif len(inventaris) < 3:
        print(f"{gast.title()} heeft normale berpakking")
    else:
        print(f"{gast.title()} is zwaar bepakt")

# ====================
# Herbergvoorraad
# ====================

benodigdheden = [
    'brood',
    'kaas',
    'vlees',
    'kaarsen',
    'brandhout',
    'bier'
]

benodigdheden.append('verband')
benodigdheden.insert(1, 'water')
benodigdheden.remove('kaarsen')
verwijderd_item = benodigdheden.pop(-1)

print(f"De volledige lijst: {benodigdheden}")
print(f"De eerste 3 items: {benodigdheden[:3]}")
print(f"De laatste 3 items: {benodigdheden[-3:]}")
print(f"Het aantal overgebleven benodigdheden: {len(benodigdheden)}")
print(f"Het volgende item is uit de lijst gehaald: {verwijderd_item}")

# ==============
# Eindrapport
# ==============

print("=====================================")
print("=== DE ZILVEREN DRAAK EINDRAPPORT ===")
print("=====================================")
print()
print(f"Naam: {herberg['naam'].title()}")
print(f"Locatie: {herberg['locatie'].title()}")
print(f"Status: {herberg['status'].title()}")
print(f"Aantal kamers: {herberg['kamers']}")
print(f"Aantal bezette kamers: {herberg['bezette kamers']}")
print(f"Goudvoorraad: {herberg['goudvoorraad']}")
print(f"Aantal geregistreerde gasten: {len(gastenregister)}")
print(f"Aantal voorwerpen van Elara: {len(gastenregister['elara'])}")
print(f"Aantal benodigdheden: {len(benodigdheden)}")