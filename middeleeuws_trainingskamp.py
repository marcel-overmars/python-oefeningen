# ==========================================================
# UITLEG PROJECT - RAVENBURG TRAININGSKAMP
# ==========================================================
#
# In dit project beheer ik een trainingskamp waarin twaalf
# rekruten gedurende tien dagen worden getraind.
#
# Met range() worden automatisch twaalf dictionaries
# aangemaakt en in één lijst opgeslagen. Tijdens de
# trainingsdagen worden hun ervaring, energie en kracht
# aangepast.
#
# Een while-loop doorloopt de trainingsdagen. Met % worden
# speciale gebeurtenissen op vaste dagen uitgevoerd.
# Na de training worden de rekruten in verschillende
# stappen gepromoveerd.
#
# Ook bevat het programma trainers met meerdere trainingen.
# Met een for-loop binnen een for-loop worden deze
# trainingen afzonderlijk weergegeven.
#
# Gebruikte onderdelen:
# - dictionaries en lijsten
# - range() en append()
# - lijst met dictionaries
# - while-loop
# - for-loops en geneste loops
# - for-loop binnen een if-statement
# - if, elif en else
# - modulo (%)
# - slices
# - .items()
# - len()
# - += en -=
# - dictionarywaarden wijzigen
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =============
# Het kamp
# =============

trainingskamp = {
    'naam': 'ravenburg trainingskamp',
    'goud': 2500,
    'voedsel': 500,
    'trainingsdagen': 10,
    'status': 'actief'
}

for gegevens, waarde in trainingskamp.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# ===============
# De rekruten\
# ===============

rekruten = []

for rekruut in range(1, 13):
    training = {
        'rang': 'rekruut',
        'kracht': 20,
        'ervaring': 0,
        'energie': 100,
        'status': 'training'
    }

    rekruten.append(training)

print(f"Aantal rekruten in training: {len(rekruten)}")

# ====================
# De trainingsdagen
#=====================

trainingsdag = 1

while trainingsdag < 11:
    print(f"\n=== Trainingsdag {trainingsdag} ===")

    for rekruut in rekruten:
        rekruut['ervaring'] += 5
        rekruut['energie'] -= 3
        print(f"De rekruut heeft nu {rekruut['ervaring']} ervaringspunten.")
        print(f"De rekruut heeft nu {rekruut['energie']} energie.")

    trainingskamp['voedsel'] -= 20
    print(f"Het trainingskamp heeft nu {trainingskamp['voedsel']} voedsel")

    if trainingsdag % 3 == 0:
        for rekruut in rekruten:
            rekruut['kracht'] += 5
            print(f"De rekruut heeft nu {rekruut['kracht']} kracht.")

    if trainingsdag % 5 == 0:
        trainingskamp['voedsel'] += 100
        print(f"Het trainingskamp heeft nu {trainingskamp['voedsel']} voedsel.")

    trainingsdag += 1
print()

# ============
# Promotie
# ============

for rekruut in rekruten[:5]:
    if rekruut['kracht'] >= 30:
        rekruut['rang'] = 'soldaat'
        rekruut['kracht'] = 50
        rekruut['status'] = 'geslaagd'

for rekruut in rekruten:
    print(rekruut)
print()

# ===============
# Promotie 2
# ===============

for rekruut in rekruten:
    if rekruut['kracht'] >= 45:
        rekruut['rang'] = 'ridder'
        rekruut['kracht'] = 65
        rekruut['status'] = 'elite'
    elif rekruut['kracht'] >= 30:
        rekruut['rang'] = 'soldaat'
        rekruut['kracht'] = 50
        rekruut['status'] = 'getraind'
    else:
        rekruut['status'] = 'extra training nodig'

for rekruut in rekruten:
    print(rekruut)

# ==============
# De trainers
# ==============

trainers = {
    'elena': [
        'zwaardvechten',
        'verdediging'
    ],

    'borin': [
        'boogschieten',
        'overleven',
        'paardrijden'
    ],

    'sofia': [
        'genezing',
        'kruidenkennis'
    ],

    'victor': [
        'tactiek',
        'leiderschap',
        'belegering'
    ]
}

for trainer, trainingen in trainers.items():
    print(f"\n{trainer.title()} geeft de volgende trainingen:")
    for training in trainingen:
        print(training)
print()

# ==============
# Eindrapport
# ==============

print("========================")
print("=== TRAININGSRAPPORT ===")
print("========================")
print()
print(f"Kamp: {trainingskamp['naam'].title()}")
print(f"Status: {trainingskamp['status'].title()}")
print(f"Resterend goud: {trainingskamp['goud']}")
print(f"Resterend voedsel: {trainingskamp['voedsel']}")
print(f"Aantal rekruten: {len(rekruten)}")
print()
print("=== REKRUTEN ===")
print()
for rekruut in rekruten:
    print(rekruut)