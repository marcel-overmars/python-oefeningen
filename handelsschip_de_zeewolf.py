# ==========================================================
# UITLEG PROJECT - HANDELSSCHIP DE ZEEWOLF
# ==========================================================
#
# In dit project oefen ik verder met dictionaries en het
# aanpassen van bestaande waarden tijdens een programma.
# De gegevens van een handelsschip worden bijgehouden en
# veranderen tijdens verschillende gebeurtenissen.
#
# Tijdens de reis veranderen onder andere het goud, de
# rompsterkte, status en voedselvoorraad. De voedselvoorraad
# wordt meerdere keren aangepast binnen een for-loop.
#
# Daarnaast worden beschikbare en benodigde voorraden met
# elkaar vergeleken en worden verschillende berekeningen
# en controles uitgevoerd.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - bestaande dictionarywaarden aanpassen
# - nieuwe key-value paren toevoegen
# - lists en for-loops
# - if, elif en else
# - in
# - range() en append()
# - slices, min(), max(), sum() en len()
# - berekeningen en gemiddelden
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =======================
# Het schip registreren
# =======================

schip = {}

schip['naam'] = 'de zeewolf'
schip['kapitein'] = 'hendrik'
schip['rompsterkte'] = 100
schip['voedsel'] = 80
schip['goud'] = 250
schip['bemanning'] = 35
schip['status'] = 'zeewaardig'

print(schip)
print()

# ======================
# Eerste handelsstop
# ======================

schip['huidige haven'] = 'valoria'
schip['handelswaar'] = 'specerijen'

schip['goud'] = schip['goud'] - 75
schip['handelswaar'] = 'zijde'

print(f"Goud dat nog over is: {schip['goud']}")
print(f"Handelswaar dat momenteel aan boord is: {schip['handelswaar']}")
print()

# =================
# Storm op zee
# =================

schip['rompsterkte'] = schip['rompsterkte'] - 35

if schip['rompsterkte'] < 25:
    schip['status'] = 'kritiek beschadigd'
elif schip['rompsterkte'] < 50:
    schip['status'] = 'zwaar beschadigd'
elif schip['rompsterkte'] < 75:
    schip['status'] = 'beschadigd'
else:
    schip['status'] = 'zeewaardig'

print(f"De status van het schip is: {schip['status']}")
print()

# ========================
# reparaties uitvoeren
# ========================

if schip['goud'] < 50:
    reparatie = 5
elif schip['goud'] < 150:
    reparatie = 15
else:
    reparatie = 30

schip['goud'] = schip['goud'] - 50
schip['rompsterkte'] = schip['rompsterkte'] + reparatie

print(f"Goud dat nog over is: {schip['goud']}")
print(f"De huidige rompsterkte is: {schip['rompsterkte']}")
print()

# ============================
# Benodigdheden controleren
# ============================

beschikbare_voorraden =[
    'water',
    'brood',
    'fruit',
    'hout',
    'touw',
    'medicijnen',
    'kanonskogels',
]

benodigde_voorraden =[
    'water',
    'hout',
    'buskruit',
    'medicijnen',
    'zeilen',
]

for voorraad in benodigde_voorraden:
    if voorraad in beschikbare_voorraden:
        print(f"{voorraad.title()} is beschikbaar en wordt ingeladen")
    else:
        print(f"{voorraad.title()} is niet beschikbaar")
print()

# ======================
# Voedselverbruik
# ======================

voedselmetingen = []

for dag in range(1, 8):
    schip['voedsel'] = schip['voedsel'] - 8
    voedselmetingen.append(schip['voedsel'])

gemiddelde = sum(voedselmetingen) / len(voedselmetingen)

print(f"Alle voedselmetingen: {voedselmetingen}")
print(f"Voedselmetingen voor de eerste 3 dagen: {voedselmetingen[:3]}")
print(f"Voedselmetingen voor de laatste 3 dagen: {voedselmetingen[-3:]}")
print(f"Laagste voedselvoorraad: {min(voedselmetingen)}")
print(f"Hoogste voedselvoorraad: {max(voedselmetingen)}")
print(f"Gemiddelde voedselvoorraad: {gemiddelde}")
print(f"Aantal metingen: {len(voedselmetingen)}")
print()

# ===============
# Eindrapport
# ===============

print("==============================")
print("=== DE ZEEWOLF EINDRAPPORT ===")
print("==============================")
print()
print(f"Naam: {schip['naam'].title()}")
print(f"Kapitein: {schip['kapitein'].title()}")
print(f"Huidige haven: {schip['huidige haven'].title()}")
print(f"Handelswaar: {schip['handelswaar']}")
print(f"Rompsterkte: {schip['rompsterkte']}")
print(f"Status: {schip['status']}")
print(f"Goud: {schip['goud']}")
print(f"Bemanning: {schip['bemanning']}")
print(f"Resterend voedsel: {schip['voedsel']}")
print(f"Aantal voedselmetingen: {len(voedselmetingen)}")
print(f"Gemiddelde voedselvoorraad: {gemiddelde}")