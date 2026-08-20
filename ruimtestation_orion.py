# ==========================================================
# UITLEG PROJECT - RUIMTESTATION ORION
# ==========================================================
#
# In dit project beheer ik een ruimtestation met behulp van
# verschillende dictionaries. Ik oefen vooral met items()
# om alle key-value paren te doorlopen en met get() om
# specifieke gegevens veilig op te vragen.
#
# Daarnaast worden technische systemen aangepast, problemen
# gecontroleerd en energie- en zuurstofvoorraden bijgehouden.
# De actuele gegevens worden uiteindelijk samengevat in
# een eindrapport.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - items() gebruiken in for-loops
# - waarden veilig ophalen met get()
# - waarden toevoegen, wijzigen en verwijderen
# - lists en for-loops
# - if, elif en else
# - range(), slices en berekeningen
# - min(), max(), sum() en len()
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ==================================
# Gegevens van het ruimtestation
# ==================================

ruimtestation ={
    'naam': 'orion',
    'bemanning': 32,
    'energie': 850,
    'zuurstof': 92,
    'locatie': 'mars-orbit',
    'status': 'operationeel'
}

for gegevens, waarde in ruimtestation.items():
    print(f"{gegevens}: {waarde}")
print()

# ========================
# Technische systemen
# ========================

technische_systemen = {
    'hoofdmotor': 'operationeel',
    'zuurstofsysteem': 'operationeel',
    'communicatiesysteem': 'storing',
    'navigatie': 'operationeel',
    'koelsysteem': 'beschadigd',
    'zwaartekrachtsysteem': 'operationeel'
}

for systeem, waarde in technische_systemen.items():
    print(f"{systeem.title()} heeft de volgende status: {waarde}")
print()

if technische_systemen['communicatiesysteem'] == 'storing':
    print(f"Het communicatiesysteem heeft een {technische_systemen['communicatiesysteem']} en moet nagekeken worden!")

if technische_systemen['koelsysteem'] == 'beschadigd':
    print(f"Controleer de schade aan het koelsysteem!")
print()

wapensysteem = technische_systemen.get('wapensysteem', 'wapensysteem niet geregistreerd')

print(wapensysteem)
print()

# =============
# Reparaties
# =============

technische_systemen['communicatiesysteem'] = 'operationeel'

del technische_systemen['koelsysteem']

technische_systemen['reservekoeling'] = 'operationeel'

for systeem, status in technische_systemen.items():
    print(f"{systeem.title()}: {status}")
print()

# =======================
# Bemanningsfuncties
# =======================

bemanning = {}

bemanning['elena'] = 'kapitein'
bemanning['victor'] = 'piloot'
bemanning['marcus'] = 'technicus'
bemanning['sofia'] = 'arts'
bemanning['david'] = 'onderzoeker'
bemanning['lucas'] = 'beveiliger'

for naam, functie in bemanning.items():
    print(f"{naam.title()}: {functie.title()}")
print()

sofia = bemanning.get('sofia')

emma = bemanning.get('emma', 'Geen bemanningslid gevonden')

print(sofia)
print(emma)
print()

# ==================
# Energieverlies
# ==================

ruimtestation['energie'] = ruimtestation['energie'] - 300

if ruimtestation['energie'] < 200:
    ruimtestation['status'] = 'kritiek energieniveau'
elif ruimtestation['energie'] < 400:
    ruimtestation['status'] = 'energiebesparing noodzakelijk'
elif ruimtestation['energie'] < 700:
    ruimtestation['status'] = 'energievoorraad beperkt'
else:
    ruimtestation['status'] = 'operationeel'

# ======================
# Beschadigde ruimtes
# ======================

ruimtes_controle = {
    'commandocentrum': 'veilig',
    'laboratorium': 'veilig',
    'machinekamer': 'beschadigd',
    'ziekenboeg': 'veilig',
    'vrachtruim': 'beschadigd',
    'luchtsluis': 'defect'
}

for ruimte, status in ruimtes_controle.items():
    print(f"De ruimte {ruimte} heeft de volgende status: {status}")
print()

if ruimtes_controle['machinekamer'] == 'beschadigd':
    print("Er is schade in de machinekamer dat gerepareerd moet worden!")

if ruimtes_controle['vrachtruim'] == 'beschadigd':
    print("Er is schade in het vrachtruim, er moeten mogelijk onderdelen vervangen worden!")

if ruimtes_controle['luchtsluis'] == 'defect':
    print("Er is een defect in de luchtsluis geconstateerd!")
print()

# =====================
# Zuurstofverbruik
# =====================

zuurstofmetingen = []

for dag in range(1, 8):
    ruimtestation['zuurstof'] = ruimtestation['zuurstof'] - 7
    zuurstofmetingen.append(ruimtestation['zuurstof'])

gemiddelde = sum(zuurstofmetingen) / len(zuurstofmetingen)

print(f"Alle zuurstofmetingen: {zuurstofmetingen}")
print(f"Metingen van de eerste 3 dagen: {zuurstofmetingen[:3]}")
print(f"Metingen van de laatste 3 dagen: {zuurstofmetingen[-3:]}")
print(f"Laagste zuurstofniveau: {min(zuurstofmetingen)}")
print(f"Hoogste zuurstofniveau: {max(zuurstofmetingen)}")
print(f"Gemiddeld zuurstofniveau: {gemiddelde}")
print(f"Aantal gemeten dagen: {len(zuurstofmetingen)}")
print()

# =========================
# Een ontbrekend gegeven
# =========================

registratienummer = ruimtestation.get('registratienummer', 'Registratienummer: Niet geregistreerd')

print(registratienummer)

# ================
# Eindrapport
# ================

print("===================================")
print("=== RUIMTESTATION ORION RAPPORT ===")
print("===================================")
print()
print(f"Naam: {ruimtestation['naam'].title()}")
print(f"Locatie: {ruimtestation['locatie'].title()}")
print(f"Status: {ruimtestation['status']}")
print(f"Bemanning: {ruimtestation['bemanning']}")
print(f"Energie: {ruimtestation['energie']}")
print(f"zuurstof: {ruimtestation['zuurstof']}")
print(registratienummer)
print(f"Aantal technische systemen: {len(technische_systemen)}")
print(f"Aantal bemanningsleden: {len(bemanning)}")
print(f"Aantal geregistreerde ruimtes: {len(ruimtes_controle)}")
print(f"Gemiddeld zuurstofniveau: {gemiddelde}")