# ==========================================================
# UITLEG PROJECT - MIDDELEEUWSE HANDELSKARAVAAN
# ==========================================================
#
# In dit project beheer ik een handelskaravaan en controleer
# ik de goederen voordat de karavaan kan vertrekken.
#
# De goederen beginnen op een wachtlijst. Met een while-loop
# worden ze één voor één uit deze lijst gehaald en aan de
# lijst met goedgekeurde goederen toegevoegd. De while-loop
# stopt automatisch zodra de wachtlijst leeg is.
#
# Daarna worden goederen over wagens verdeeld en wordt met
# een teller gecontroleerd wanneer een extra
# veiligheidscontrole nodig is.
#
# Gebruikte onderdelen:
# - dictionaries en lijsten
# - lijsten in dictionaries
# - .items()
# - for-loops en geneste for-loops
# - while-loop op basis van een gevulde lijst
# - pop() en append()
# - slices
# - len()
# - teller met +=
# - modulo (%)
# - if-statements
# - dictionarywaarden wijzigen
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ==================
# De karavaan
# ==================

karavaan = {
    'naam': 'de gouden draak',
    'vertrekstad': 'Apeldoorn',
    'aantal wagens': 4,
    'aantal bewakers': 8,
    'status': 'voorbereiding'
}

for gegevens, waarde in karavaan.items():
    print(f"{gegevens.title()}: {waarde}")

# =============
# Routes
# =============

handelsroutes = {
    'noord': [
        'zwolle',
        'kampen'
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

for gebied, bestemmingen in handelsroutes.items():
    print(f"\nIn {gebied.title()} zijn de volgende bestemmingen:")
    for bestemming in bestemmingen:
        print(bestemming.title())
print()

# ===============================================
# Goederen controleren en van lijst veranderen
# ===============================================

wachtlijst_goederen = [
    'graan',
    'ijzer',
    'wol',
    'hout',
    'zout',
    'leer',
    'honing',
    'kruiden'
]

goedgekeurde_goederen = []

print(f"Aantal goederen wachtend op controle: {len(wachtlijst_goederen)}")
print()

while wachtlijst_goederen:
    goedgekeurd = wachtlijst_goederen.pop()

    print(f"\nHet volgende goed wordt gecontroleerd: {goedgekeurd}")

    goedgekeurde_goederen.append(goedgekeurd)

    print(f"Het aantal goederen dat nog op controle wacht: {len(wachtlijst_goederen)}")
print()

print("Alle goederen zijn gecontroleerd")
print(f"Goederen op wachtlijst: {len(wachtlijst_goederen)}")
print(f"goedgekeurde goederen: {len(goedgekeurde_goederen)}")
print()

print("Goedgekeurde goederen:")
for goederen in goedgekeurde_goederen:
    print(goederen)
print()

# ==================
# Extra controle
# ==================

wagen_1 = goedgekeurde_goederen[:3]
wagen_4 = goedgekeurde_goederen[-3:]

print("Wagen 1 heeft de volgende goederen bij zich:")
print(wagen_1)
print()
print("Wagen 4 heeft de volgende goederen bij zich:")
print(wagen_4)
print()

teller = 0

for goed in goedgekeurde_goederen:
    teller += 1
    print(teller, goed)

    if teller % 3 == 0:
        print("Extra veiligheidscontrole")
print()

# =============
# Handelaren
# =============

handelaren = {
    'hendrik': [
        'graan',
        'honing'
    ],

    'mara': [
        'wol',
        'leer',
        'kruiden'
    ],

    'otto': [
        'ijzer',
        'hout',
        'zout'
    ]
}

for handelaar, handelgoed in handelaren.items():
    print(f"\n{handelaar.title()} verkoopt de volgende goederen:")
    for handel in handelgoed:
        print(handel.title())
print()

# =============
# Eindrapport
# =============

print("=======================")
print("=== KARAVAANRAPPORT ===")
print("=======================")
print()
print(f"Karavaan: {karavaan['naam'].title()}")
print(f"Vertrekstad: {karavaan['vertrekstad'].title()}")
print(f"Aantal wagens: {karavaan['aantal wagens']}")
print(f"Aantal bewakers: {karavaan['aantal bewakers']}")
print()
print(f"Goederen nog op de wachtlijst: {len(wachtlijst_goederen)}")
print(f"Aantal goedgekeurde goederen: {len(goedgekeurde_goederen)}")
print()
print(f"Goederen wagen 1: {wagen_1}")
print(f"Goederen wagen 4: {wagen_4}")
print()

karavaan['status'] = 'klaar voor vertrek'

for gegevens, waarde in karavaan.items():
    print(f"{gegevens.title()}: {waarde}")