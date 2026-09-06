# ==========================================================
# UITLEG PROJECT - KONINKLIJKE EXPEDITIEGILDE
# ==========================================================
#
# In dit project oefen ik met de verschillende vormen van
# nesting door dictionaries en lijsten met elkaar te
# combineren.
#
# In het ledenregister bevat iedere key een nieuwe dictionary
# met gegevens van een lid. Daarnaast worden automatisch
# teamleden als dictionaries aangemaakt en in een lijst
# opgeslagen. Trainers en uitrusting bevatten juist lijsten
# als values binnen een dictionary.
#
# Met for-loops worden de geneste gegevens doorlopen,
# gecontroleerd en aangepast. Ook worden for-loops binnen
# andere for-loops gebruikt om de items uit geneste lijsten
# afzonderlijk te verwerken.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - een dictionary met dictionaries
# - een dictionary met lijsten
# - een lijst met dictionaries
# - nesting en geneste for-loops
# - items(), keys(), values() en get()
# - dictionaries automatisch aanmaken in een for-loop
# - append() en range()
# - dictionarywaarden ophalen en wijzigen
# - if, elif en else
# - slices en indexen
# - sorted() en set()
# - len()
# - gegevens uit geneste structuren ophalen
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ==============================
# Basisgegevens van de gilde
# ==============================

gilde = {
    'naam': 'koninklijke expeditiegilde',
    'locatie': 'ravenburg',
    'goud': 3200,
    'leden': 24,
    'status': 'actief'
}

for gegevens, waarde in gilde.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# =====================================
# Alleen de keys en alleen de values
# =====================================

for gegevens in gilde.keys():
    print(gegevens)
print()

for waarde in gilde.values():
    print(waarde)
print()

# =================
# Ledenregister
# =================

ledenregister = {
    'marcel': {
        'beroep': 'mage',
        'level': 35,
        'levenspunten': 85,
        'goud': 220,
        'status': 'beschikbaar'
    },

    'dennis': {
        'beroep': 'rogue',
        'level': 31,
        'levenspunten': 58,
        'goud': 95,
        'status': 'beschikbaar'
    },

    'jeroen': {
        'beroep': 'warrior',
        'level': 39,
        'levenspunten': 100,
        'goud': 340,
        'status': 'beschikbaar'
    }
}

for lid, gegevens in ledenregister.items():
    print(f"{lid.title()}: {gegevens}")
print()

# ===========================================
# Eén specifiek lid rechtstreeks opvragen
# ===========================================

print(f"Beroep van Marcel: {ledenregister['marcel']['beroep'].title()}")
print(f"Level van Dennis: {ledenregister['dennis']['level']}")
print(f"Goud van Jeroen: {ledenregister['jeroen']['goud']}")
print()

# ======================
# Ontbrekende gegeven
# ======================

paard = ledenregister['marcel'].get('paard', 'Geen paard geregistreerd.')

print(paard)
print()

# ======================================
# Gezondheidscontrole van alle leden
# ======================================

for lid, levens in ledenregister.items():
    if levens['levenspunten'] < 30:
        levens['status'] = 'kritiek'
    elif levens['levenspunten'] < 60:
        levens['status'] = 'gewond'
    else:
        levens['status'] = 'gezond'

for lid, waarde in ledenregister.items():
    print(f"{lid.title()}: {waarde}")
print()

# ==================================
# Automatisch expeditieteam maken
# ==================================

expeditieteam = []

for team in range(1, 9):
    teamgenoot = {
        'rang': 'rekruut',
        'ervaring': 0,
        'kracht': 20,
        'status': 'training'
    }
    expeditieteam.append(teamgenoot)

for team in expeditieteam:
    print(team)
print()

print("De eerste 4 teamleden:")

for team in expeditieteam[:4]:
    print(team)
print()

# =====================
# Teamleden trainen
# =====================

for team in expeditieteam[:4]:
    if team['rang'] == 'rekruut':
        team['rang'] = 'soldaat'
        team['ervaring'] = 25
        team['kracht'] = 35
        team['status'] = 'getraind'

for team in expeditieteam[:6]:
    if team['rang'] == 'rekruut':
        team['rang'] = 'soldaat'
        team['ervaring'] = 25
        team['kracht'] = 35
        team['status'] = 'getraind'
    elif team['rang'] == 'soldaat':
        team['rang'] = 'veteraan'
        team['ervaring'] = 60
        team['kracht'] = 55
        team['status'] = 'ervaren'

for team in expeditieteam:
    print(team)
print()

# ============================
# trainers en vaardigheden
# ============================

trainers = {
    'elena': [
        'magie',
        'alchemie'
    ],

    'borin': [
        'zwaardvechten',
        'verdediging',
        'paardrijden'
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

for vaardigheden in trainers.values():
    print(vaardigheden)
print()

# =================================
# Trainer en vaardigheden tonen
# =================================

for trainer, vaardigheden in trainers.items():
    print(f"\n{trainer.title()} geeft training in:")
    for vaardigheid in vaardigheden:
        print(vaardigheid)
print()

# ==================================
# Aantal vaardigheden controleren
# ==================================

for trainer, vaardigheden in trainers.items():
    if len(vaardigheden) < 2:
        print(f"{trainer.title()} is specialist.")
    elif len(vaardigheden) < 3:
        print(f"{trainer.title()} is een ervaren trainer.")
    elif len(vaardigheden) >= 3:
        print(f"{trainer.title()} is meestertrainer.")
print()

# =======================
# Uitrustingscontrole
# =======================

uitrusting = {
    'marcel': [
        'staf',
        'toverboek',
        'mana potion'
    ],

    'dennis': [
        'dolken',
        'gif',
        'touw'
    ],

    'jeroen': [
        'zwaard',
        'schild',
        'harnas'
    ]
}

for lid, inventaris in uitrusting.items():
    print(f"\n{lid.title()} heeft de volgende items bij zich:")
    for items in inventaris:
        print(items)
print()

# =============================
# Unieke uitrustingssoorten
# =============================

for lid, inventaris in uitrusting.items():
    items = set(inventaris)
    print(items)
print()

# =================
# Eindrapport
# =================

print("====================================")
print("=== EXPEDITIEGILDE - EINDRAPPORT ===")
print("====================================")
print()
print(f"Naam: {gilde['naam'].title()}")
print(f"Locatie: {gilde['locatie'].title()}")
print(f"Status: {gilde['status'].title()}")
print(f"Goud: {gilde['goud']}")
print(f"Aantal leden in ledenregister: {len(ledenregister)}")
print(f"Aantal expeditieteamleden: {len(expeditieteam)}")
print(f"Rang eerste expeditieteamlid: {expeditieteam[0]['rang'].title()}")
print(f"Rang laatste expeditieteamlid: {expeditieteam[-1]['rang']}")
print(f"Aantal trainers: {len(trainers)}")
print(f"Aantal vaardigheden van Borin: {len(trainers['borin'])}")