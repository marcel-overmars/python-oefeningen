# =========================================
# Uitleg - Dierenkliniek De Trouwe Poot
# =========================================

# In dit project wordt een dierenkliniek beheerd met behulp van dictionaries.
# De gegevens van de kliniek, dieren en medicijnvoorraad worden opgeslagen
# en tijdens het programma aangepast.

# Gebruikte onderdelen:
# - Dictionaries maken en gegevens toevoegen, wijzigen en verwijderen
# - .items() gebruiken om keys en values samen te doorlopen
# - .keys() gebruiken om alleen de keys van een dictionary te doorlopen
# - .get() gebruiken om gegevens veilig op te vragen
# - For-loops en if-statements gebruiken voor controles
# - Lijsten gebruiken om dagelijkse voermetingen op te slaan
# - Berekeningen uitvoeren met sum(), min(), max() en len()
# - Een eindrapport maken met de actuele gegevens
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ========================================
# Gegevens dierenkliniek De Trouwe Poot
# ========================================

dierenkliniek ={
    'naam': 'Dierenkliniek De Trouwe Poot',
    'dieren aanwezig': 6,
    'medewerkers': 6,
    'kas': 1800,
    'status': 'geopend'
}

for kliniek, gegevens in dierenkliniek.items():
    print(f"{kliniek.title()}: {gegevens}")
print()

# =================
# Dierenregister
# =================

dieren = {}

dieren['max'] = 'hond'
dieren['luna'] = 'kat'
dieren['charlie'] = 'konijn'
dieren['bella'] = 'hond'
dieren['simba'] = 'kat'
dieren['coco'] = 'papegaai'

for dier, soort in dieren.items():
    print(f"{dier}: {soort}")
print()

# ================================
# Alleen de namen van de dieren
# ================================

for dier in dieren.keys():
    print(dier)
print()

# =====================
# Nieuwe registratie
# =====================

rocky = dieren.get('rocky', 'Rocky staat nog niet geregistreerd')

print(rocky)
print()

# ==================
# Bekende dieren
# ==================

bekende_dieren =[
    'max',
    'bella',
    'coco'
]

for naam in dieren.keys():
    if naam in bekende_dieren:
        print(f"{naam.title()} is een bekende patiënt")
print()

# ===========================================
# Nieuwe patiënt en uitschrijving patiënt
# ===========================================

dieren['rocky'] = 'hond'

del dieren['charlie']

for dier, soort in dieren.items():
    print(f"{dier.title()}: {soort}")
print()

# ===================
# Medicijnvoorraad
# ===================

medicijnvoorraad ={
    'pijnstiller': 35,
    'antibiotica': 18,
    'oogdruppels': 24,
    'ontworming': 12,
    'verband': 40
}

for artikel, voorraad in medicijnvoorraad.items():
    print(f"{artikel.title()}: {voorraad}")
print()

medicijnvoorraad['pijnstiller'] = medicijnvoorraad['pijnstiller'] - 7

medicijnvoorraad['antibiotica'] = medicijnvoorraad['antibiotica'] - 5

if medicijnvoorraad['antibiotica'] < 15:
    print("Antibiotica moet bijbesteld worden")
else:
    print("Er is voldoende antibiotica op voorraad")
print()

# ==========================
# Ontbrekende informatie
# ==========================

telefoonnummer = dierenkliniek.get('telefoonnummer', 'Telefoonnummer niet geregistreerd')

print(telefoonnummer)

# ==============================
# Zeven dagen voer verbruiken
# ==============================

dierenkliniek['dierenvoer'] = 140

voer = []

for dag in range(1, 8):
    dierenkliniek['dierenvoer'] = dierenkliniek['dierenvoer'] - 12
    voer.append(dierenkliniek['dierenvoer'])

gemiddelde = sum(voer) / len(voer)

print(f"Alle metingen: {voer}")
print(f"Eerste 3 metingen: {voer[:3]}")
print(f"Laatste 3 metingen: {voer[-3:]}")
print(f"Laagste voorraad: {min(voer)}")
print(f"Hoogste voorraad: {max(voer)}")
print(f"Gemiddelde voorraad: {gemiddelde}")
print(f"aantal metingen: {len(voer)}")
print()

# ===============
# Eindrapport
# ===============

print("====================================")
print("=== DE TROUWE POOT - EINDRAPPORT ===")
print("====================================")
print()
print(f"Naam: {dierenkliniek['naam']}")
print(f"Status: {dierenkliniek['status']}")
print(f"Dieren aanwezig: {dierenkliniek['dieren aanwezig']}")
print(f"Medewerkers: {dierenkliniek['medewerkers']}")
print(f"Kas: {dierenkliniek['kas']}")
print(f"Aantal geregistreerde dieren: {len(dieren)}")
print(f"Aantal medicijnen: {len(medicijnvoorraad)}")
print(f"Resterende voervoorraad: {dierenkliniek['dierenvoer']}")
print(f"Gemiddelde voervoorraad: {gemiddelde}")
print()