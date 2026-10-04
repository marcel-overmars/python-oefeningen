# ==========================================================
# UITLEG PROJECT - NOVA PRIME RUIMTEKOLONIE
# ==========================================================
#
# In dit project beheer ik de ruimtekolonie Nova Prime.
# Het programma registreert kolonisten, voert controles uit,
# verwerkt energie en voorraden en maakt een eindrapport.
#
# Gebruikte onderdelen:
# - dictionaries en lijsten
# - tuples
# - for-loops en geneste loops
# - meerdere vormen van while-loops
# - while met een flag
# - while met een voorwaarde
# - while zolang een lijst gevuld is
# - while True met break
# - input van de gebruiker
# - in en not in
# - remove(), pop() en append()
# - tellers met +=
# - min(), max() en sum()
# - lijsten kopiëren met [:]
# - sorteren met .sort()
# - slices
# - dictionarywaarden aanpassen
#
# Het belangrijkste doel van dit project was oefenen met het
# zelfstandig herkennen van welke while-constructie geschikt
# is voor verschillende problemen. Daarnaast heb ik oudere
# Python-onderdelen opnieuw toegepast als herhaling.
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ====================
# Koloniegegevens
# ====================

koloniegegevens = {
    'naam': 'Nova Prime',
    'planeet': 'Kepler-186f',
    'kolonisten': 0,
    'energie': 850,
    'status': 'opbouw'
}

for kolonie, gegevens in koloniegegevens.items():
    print(f"{kolonie.title()}: {gegevens}")
print()

vaste_sectoren = (
    'woonsector',
    'landbouw',
    'techniek',
    'onderzoek'
)

for sector in vaste_sectoren:
    print(sector)
print()

# =================================
# Nieuwe kolonisten registreren
# =================================

registratie = {}

registratie_active = True

while registratie_active:
    naam = input(f"\nWat is je naam? ")
    beroep = input("Wat is je beroep? ")

    registratie[naam] = beroep

    herhaling = input("Moet er nog iemand geregistreerd worden? (ja/nee) ")

    if herhaling == 'nee':
        registratie_active = False
print()

for naam, beroep in registratie.items():
    print(f"{naam.title()}: {beroep.title()}")
print()

koloniegegevens['kolonisten'] = koloniegegevens['kolonisten'] + len(registratie)

for kolonie, gegevens in koloniegegevens.items():
    print(f"{kolonie.title()}: {gegevens}")
print()

# =====================
# Toegangscontrole
# =====================

verwijderde_registratie = 0

verboden_personen = [
    'voss',
    'kane',
    'miller',
    'voss',
    'voss',
    'kane'
]

while 'voss' in verboden_personen:
    verboden_personen.remove('voss')
    verwijderde_registratie += 1

print(f"Aantal verwijderde registraties: {verwijderde_registratie}")
print()

if 'anderson' not in verboden_personen:
    print("Anderson heeft toegang tot het onderzoekscentrum")
print()

# ===================
# Energiecentrale
# ===================

cyclus = 0

while koloniegegevens['energie'] >= 75:
    koloniegegevens['energie'] -= 75

    cyclus += 1

    print(f"Cyclus: {cyclus}")
    print(f"Energie over: {koloniegegevens['energie']}")
print()

print(f"Aantal volledig uitgevoerde cycli: {cyclus}")
print()

    # =====================
    # Voorraadtransport
    # =====================

voorraden = [
    'water',
    'voedsel',
    'medicijnen',
    'gereedschap',
    'zuurstof',
    'onderdelen',
    'zaden',
    'batterijen'
]

hoofdmagazijn = []

while voorraden:
    voorraad = voorraden.pop()
    hoofdmagazijn.append(voorraad)

print(f"Aantal items in voorraden: {len(voorraden)}")
print(f"Aantal voorraden in magazijn: {len(hoofdmagazijn)}")
print()

# ===================
# Energieonderzoek
# ===================

metingen =[
    120,
    95,
    140,
    80,
    110,
    135
]

print(f"Laagste meting: {min(metingen)}")
print(f"Hoogste meting: {max(metingen)}")
print(f"Totaal van alle metingen: {sum(metingen)}")
print()

metingen_2 = metingen[:]

metingen_2.sort()

print(f"Metingen van de originele lijst: {metingen}")
print(f"Metingen kopie gesorteerd: {metingen_2}")
print()
print(f"De eerste 3 waarden van de gesorteerde lijst: {metingen_2[:3]}")
print(f"De laatste 2 waarden van de gesorteerde lijst: {metingen_2[-2:]}")
print()

# ==================
# Sectorbemanning
# ==================

sectorbemanning = {
    'techniek': [
        'monteur',
        'ingenieur',
        'elektricien'
    ],

    'onderzoek': [
        'bioloog',
        'natuurkundige'
    ],

    'landbouw': [
        'boer',
        'botanicus',
        'irrigatiespecialist'
    ]
}

for sector, bemanning in sectorbemanning.items():
    print(f"\n{sector}:")
    for werker in bemanning:
        print(f"- {werker}")
print()

# ==============
# Noodconsole
# ==============

while True:
    opdracht = input("Voer 'status', 'energie' in of 'afsluiten': ")

    if opdracht == 'status':
        print(f"De huidige status is: {koloniegegevens['status']}")

    if opdracht == 'energie':
        print(f"De huidige energie is: {koloniegegevens['energie']}")

    if opdracht == 'afsluiten':
        break
print()

# ==================
# Eindrapport
# ==================

koloniegegevens['status'] = 'operationeel'

print("=================================")
print("=== NOVA PRIME KOLONIERAPPORT ===")
print("=================================")
print()
print(f"Kolonie: {koloniegegevens['naam']}")
print(f"Planeet: {koloniegegevens['planeet']}")
print(f"Status: {koloniegegevens['status']}")
print(f"Kolonisten: {koloniegegevens['kolonisten']}")
print(f"Energie over: {koloniegegevens['energie']}")
print()
print("KOLONISTEN:")

for kolonist, beroep in registratie.items():
    print(f"{kolonist.title()}: {beroep.title()}")
print()

print("VOORRAAD:")

for magazijn in hoofdmagazijn:
    print(magazijn)
print()

print(f"Aantal verwijderde Voss-registraties: {verwijderde_registratie}")
print()

print("ENERGIEONDERZOEK:")
print(f"Laagste: {min(metingen)}")
print(f"Hoogste: {max(metingen)}")
print(f"Totaal: {sum(metingen)}")