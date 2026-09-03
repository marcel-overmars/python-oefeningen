# ==========================================================
# UITLEG PROJECT - KONINKLIJKE HELDENACADEMIE
# ==========================================================
#
# In dit project oefen ik met verschillende vormen van
# nesting door dictionaries en lijsten met elkaar te
# combineren.
#
# Met een for-loop en range() worden automatisch meerdere
# rekruten als dictionaries aangemaakt en aan een lijst
# toegevoegd. Met slices worden bepaalde groepen rekruten
# geselecteerd en afhankelijk van hun rang aangepast.
#
# Daarnaast bevat een dictionary met trainers per trainer
# een lijst met vaardigheden. Met een for-loop binnen een
# for-loop worden eerst de trainers en daarna hun
# afzonderlijke vaardigheden doorlopen.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - een lijst met dictionaries
# - een dictionary met lijsten als values
# - nesting en geneste for-loops
# - dictionaries aanmaken in een for-loop
# - append() en range()
# - keys(), values() en items()
# - sorted()
# - for-loops
# - slices en indexen
# - if, elif en else
# - dictionarywaarden controleren en wijzigen
# - len()
# - gegevens uit geneste structuren ophalen
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ========================
# Basisgegevens academie
# ========================

academie = {
    'naam': 'koninklijke heldenacademie',
    'locatie': 'ravenburg',
    'goud': 1500,
    'trainers': 5,
    'status': 'actief'
}

for gegevens, waarde in academie.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# =======================================================
# Alleen de keys en alleen de values van de dictionary
# =======================================================

for gegevens in academie.keys():
    print(gegevens)
print()

for waarde in academie.values():
    print(waarde)
print()

# =============================
# Automatisch rekruten maken
# =============================

rekruten = []

for training in range(1, 16):
    rekruut = {
        'rang': 'rekruut',
        'level': 1,
        'kracht': 20,
        'levenspunten': 100,
        'status': 'in training'
    }
    rekruten.append(rekruut)

for rekruut in rekruten[:5]:
    print(rekruut)
print()

for rekruut in rekruten[:5]:
    if rekruut['rang'] == 'rekruut':
        rekruut['rang'] = 'soldaat'
        rekruut['level'] = 5
        rekruut['kracht'] = 35
        rekruut['status'] = 'getraind'

for rekruut in rekruten[:5]:
    print(rekruut)
print()

# ========================
# Tweede trainingsronde
# ========================

for rekruut in rekruten[:10]:
    if rekruut['rang'] == 'rekruut':
        rekruut['rang'] = 'soldaat'
        rekruut['level'] = 5
        rekruut['kracht'] = 35
        rekruut['status'] = 'getraind'
    elif rekruut['rang'] == 'soldaat':
        rekruut['rang'] = 'ridder'
        rekruut['level'] = 10
        rekruut['kracht'] = 60
        rekruut['levenspunten'] = 150
        rekruut['status'] = 'ervaren'

for rekruut in rekruten:
    print(rekruut)
print()

# ============================
# Trainers en vaardigheden
# ============================

trainers = {
    'hendrik': [
        'zwaardvechten',
        'verdediging',
        'paardrijden'
    ],
    'elena': [
        'magie',
        'alchemie'
    ],
    'borin': [
        'boogschieten',
        'overleven',
        'speuren'
    ],
    'sofia': ['genezing'],
    'victor': [
        'tactiek',
        'leiderschap'
    ]
}

for trainer in sorted(trainers.keys()):
    print(trainer)
print()

# =================================
# Alleen de vaardigheidslijsten
# =================================

for vaardigheden in trainers.values():
    print(vaardigheden)
print()

# =================================
# Vaardigheidslijst per trainer
# =================================

for trainer, vaardigheden in trainers.items():
    print(f"\n{trainer.title()} geeft training in de volgende vaardigheden:")
    for vaardigheid in vaardigheden:
        print(vaardigheid.title())
print()

# ========================
# Hoeveel vaardigheden?
# ========================

for trainer, vaardigheid in trainers.items():
    if len(vaardigheid) < 2:
        print(f"{trainer.title()} is een specialist.")
    elif len(vaardigheid) < 3:
        print(f"{trainer.title()} is een ervaren trainer.")
    elif len(vaardigheid) >= 3:
        print(f"{trainer.title()} is een meestertrainer.")
print()

# =================================
# Specifieke rekruut controleren
# =================================

print(f"Rang van de eerste rekruut: {rekruten[0]['rang']}")
print(f"Kracht van de zesde rekruut: {rekruten[5]['kracht']}")
print(f"Status van de laatste rekruut: {rekruten[-1]['status']}")
print()

# =============
# Eindrapport
# =============

print("====================================")
print("=== HELDENACADEMIE - EINDRAPPORT ===")
print("====================================")
print()
print(f"Naam academie: {academie['naam']}")
print(f"Locatie: {academie['locatie']}")
print(f"Status: {academie['status']}")
print(f"Goud: {academie['goud']}")
print(f"Aantal trainers: {len(trainers)}")
print(f"Aantal rekruten: {len(rekruten)}")
print(f"Rang eerste rekruut: {rekruten[0]['rang']}")
print(f"Rang zesde rekruut: {rekruten[5]['rang']}")
print(f"Rang laatste rekruut: {rekruten[-1]['rang']}")
print(f"Aantal vaardigheden van hendrik: {len(trainers['hendrik'])}")