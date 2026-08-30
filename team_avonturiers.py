# ==========================================================
# UITLEG PROJECT - AVONTURIERSTEAM
# ==========================================================
#
# In dit project oefen ik voor het eerst met nesting door
# meerdere dictionaries in één lijst op te slaan. Iedere
# dictionary bevat de gegevens van één avonturier.
#
# Met for-loops worden de dictionaries uit de lijst
# doorlopen. Gegevens van een avonturier worden aangepast
# en op basis van levenspunten en goud worden nieuwe
# statusgegevens aan iedere dictionary toegevoegd.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - meerdere dictionaries in een list
# - dictionaries doorlopen met een for-loop
# - waarden uit dictionaries ophalen en wijzigen
# - nieuwe keys en values toevoegen
# - if, elif en else
# - lists en slices
# - len()
# - berekeningen met dictionarywaarden
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =================================
# Dictionaries van 3 avonturiers
# =================================

avonturier_1 = {
    'naam': 'marcel',
    'beroep': 'mage',
    'level': 35,
    'levenspunten': 25,
    'goud': 125
}

avonturier_2 = {
    'naam': 'dennis',
    'beroep': 'rogue',
    'level': 33,
    'levenspunten': 56,
    'goud': 55
}

avonturier_3 = {
    'naam': 'jeroen',
    'beroep': 'warrior',
    'level': 38,
    'levenspunten': 93,
    'goud': 313
}

# ==============================
# De 3 avonturiers in 1 lijst
# ==============================

team = [
    avonturier_1,
    avonturier_2,
    avonturier_3
]

print(team)
print()

# =======================
# Door het team loopen
# =======================

for speler in team:
    print(speler)
print()

# ================================
# Aanpassingen van 1 avonturier
# ================================

avonturier_3['levenspunten'] = avonturier_3['levenspunten'] - 20

avonturier_3['goud'] = avonturier_3['goud'] + 75

avonturier_3['level'] = avonturier_3['level'] + 1

for speler in team:
    print(speler)
print()

# ======================
# Gezondheidscontrole
# ======================

for speler in team:
    if speler['levenspunten'] < 30:
        speler['levenspunten status'] = 'kritiek'
    elif speler['levenspunten'] < 60:
        speler['levenspunten status'] = 'gewond'
    else:
        speler['levenspunten status'] = 'gezond'

for speler in team:
    print(speler)
print()

# ===============
# Goudcontrole
# ===============

for speler in team:
    if speler['goud'] < 100:
        speler['goud status'] = 'weinig goud'
    elif speler['goud'] < 300:
        speler['goud status'] = 'voldoende goud'
    else:
        speler['goud status'] = 'rijke avonturier'

for speler in team:
    print(speler)
print()

# ====================================
# Eerste 2 leden van het team tonen
# ====================================

for speler in team[:2]:
    print(speler)
print()

# ===============
# Eindrapport
# ===============

totale_goud = avonturier_1['goud'] + avonturier_2['goud'] + avonturier_3['goud']

print("===============================")
print("=== AVONTURIERSTEAM RAPPORT ===")
print("===============================")
print()
print(f"Aantal avonturiers: {len(team)}")
print(f"Naam eerste avonturier: {avonturier_1['naam'].title()}")
print(f"Naam laatste avonturier: {avonturier_3['naam'].title()}")
print(f"Totaal goud van het team: {totale_goud}")