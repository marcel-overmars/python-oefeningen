# ==========================================================
# UITLEG PROJECT - KONINKLIJKE WAPENKAMER
# ==========================================================
#
# In dit project beheer ik een koninklijke wapenkamer met
# behulp van dictionaries. Ik oefen met het doorlopen van
# alle key-value paren met een for-loop en items().
#
# Daarnaast worden voorraden aangepast, wapens gecontroleerd
# en onderhoudsproblemen verwerkt. Ook worden gegevens
# toegevoegd, gewijzigd en verwijderd en worden dagelijkse
# bezoekersaantallen bijgehouden.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - items() gebruiken in een for-loop
# - waarden ophalen met [] en get()
# - waarden toevoegen, wijzigen en verwijderen
# - lists en for-loops
# - if, elif en else
# - in
# - range(), slices en berekeningen
# - min(), max(), sum() en len()
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ===================================
# Basisgegevens van de wapenkamer
# ===================================

wapenkamer ={
    'naam': 'koninklijke wapenkamer',
    'locatie': 'noordtoren',
    'goudvoorraad': 900,
    'bewakers': 24,
    'status': 'beveiligd'
}

for wapen, waarde in wapenkamer.items():
    print(f"{wapen.title()}: {waarde}")
print()

# ==================
# Wapenvoorraad
# ==================

wapenvoorraad ={
    'zwaard': 35,
    'boog': 28,
    'speer': 42,
    'kruisboog': 16,
    'schild': 31,
    'hellebaard': 12
}

for wapen, voorraad in wapenvoorraad.items():
    print(f"{wapen.title()}: {voorraad}")
print()

# ===========================
# één voorraad controleren
# ===========================

kruisboog = wapenvoorraad['kruisboog']

if kruisboog < 20:
    print(f"Kruisbogen moeten bij besteld worden")
else:
    print(f"Kruisbogen zijn voldoende op voorraad")
print()

# ======================
# Voorraad verandert
# ======================

wapenvoorraad['zwaard'] = wapenvoorraad['zwaard'] - 8
wapenvoorraad['boog'] = wapenvoorraad['boog'] - 5
wapenvoorraad['speer'] = wapenvoorraad['speer'] - 10

wapenvoorraad['strijdhamer'] = 7

del wapenvoorraad['hellebaard']

for wapen, voorraad in wapenvoorraad.items():
    print(f"{wapen.title()}: {voorraad}")
print()

# ===========================
# Aanvragen van soldaten
# ===========================

gevraagde_wapens =[
    'zwaard',
    'kruisboog',
    'strijdhamer',
    'knots',
    'boog'
]

for wapen in gevraagde_wapens:
    if wapen in wapenvoorraad:
        print(f'Het volgende wapen is op voorraad en wordt geleverd: {wapen.title()}')
    else:
        print(f"Het volgende wapen is niet meer op voorraad en moet besteld worden: {wapen.title()}")
print()

# ====================
# Onderhoudstatus
# ====================

onderhoudsstatus ={
    'noorddeur': 'goed',
    'zuiddeur': 'beschadigd',
    'wapenrek': 'goed',
    'dak': 'lekkage',
    'alarmsysteem': 'defect'
}

for onderhoud, status in onderhoudsstatus.items():
    print(f"{onderhoud.title()} heeft status: {status.title()}")

if onderhoudsstatus['zuiddeur'] == 'beschadigd':
    print(f"De zuiddeur moet gerepareerd worden!")

if onderhoudsstatus['dak'] == 'lekkage':
    print(f"Het dak moet gerepareerd worden!")

if onderhoudsstatus['alarmsysteem'] == 'defect':
    print(f"Het alarmsysteem moet gecontroleerd worden!")

# ==============================
# Goudkosten voor reparaties
# ==============================

wapenkamer['goudvoorraad'] = wapenkamer['goudvoorraad'] - 175

if wapenkamer['goudvoorraad'] < 300:
    print("Kritisch lage goudvoorraad")
elif wapenkamer['goudvoorraad'] < 600:
    print("Beperkte goudvoorraad")
else:
    print("Voldoende goud")

if wapenkamer['goudvoorraad'] < 600:
    wapenkamer['status'] = 'goudtekort'

print(wapenkamer)

# ================================
# Dagelijkse bezoekerscontrole
# ================================

bezoekersmetingen = []

for dag in range(1, 8):
    bezoekers = dag * 85
    bezoekersmetingen.append(bezoekers)

gemiddelde = sum(bezoekersmetingen) / len(bezoekersmetingen)

print(f"Alle aantallen: {bezoekersmetingen}")
print(f"Eerste 3 dagen: {bezoekersmetingen[:3]}")
print(f"Laatste 3 dagen: {bezoekersmetingen[-3:]}")
print(f"Laagste aantal: {min(bezoekersmetingen)}")
print(f"Hoogste aantal: {max(bezoekersmetingen)}")
print(f"Totale aantal: {sum(bezoekersmetingen)}")
print(f"Gemiddelde bezoekersaantal: {gemiddelde}")
print(f"Aantal gemeten dagen: {len(bezoekersmetingen)}")
print()

# ===============
# Eindrapport
# ===============

print("======================================")
print("=== KONINKLIJKE WAPENKAMER RAPPORT ===")
print("======================================")
print()
print(f"Naam: {wapenkamer['naam'].title()}")
print(f"Locatie: {wapenkamer['locatie'].title()}")
print(f"Status: {wapenkamer['status']}")
print(f"Goudvoorraad: {wapenkamer['goudvoorraad']}")
print(f"Aantal bewakers: {wapenkamer['bewakers']}")
print(f"Aantal verschillende wapensoorten: {len(wapenvoorraad)}")
print(f"Aantal onderhoudsonderdelen: {len(onderhoudsstatus)}")
print(f"Laagste bezoekersaantal: {min(bezoekersmetingen)}")
print(f"Hoogste bezoekersaantal: {max(bezoekersmetingen)}")
print(f"Gemiddeld bezoekersaantal: {gemiddelde}")