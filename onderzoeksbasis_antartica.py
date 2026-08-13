# ==========================================================
# UITLEG PROJECT - ONDERZOEKSBASIS AURORA
# ==========================================================
#
# In dit project beheer ik de gegevens van een onderzoeksbasis
# met behulp van een dictionary. Tijdens een sneeuwstorm
# veranderen verschillende waarden, zoals energie, brandstof,
# temperatuur, voedselvoorraad en de status van de basis.
#
# Het programma voert controles uit, berekent het herstel van
# de generator en vergelijkt gevraagde voorraden met de
# beschikbare voorraad. Ook wordt de voedselvoorraad gedurende
# zeven dagen bijgehouden en verwerkt in een eindrapport.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - bestaande dictionarywaarden aanpassen
# - lists en for-loops
# - if, elif en else
# - meerdere losse if-statements
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
# Basisregistratie
# =======================

registratie = {}

registratie['naam'] = 'aurora'
registratie['locatie'] = 'antarctica'
registratie['temperatuur'] = -18
registratie['energievoorraad'] = 100
registratie['voedselvoorraad'] = 90
registratie['brandstofvoorraad'] = 75
registratie['aantal onderzoekers'] = 12
registratie['status'] = 'operationeel'

print(registratie)
print()

# ===================
# De sneeuwstorm
# ===================

registratie['energievoorraad'] = registratie['energievoorraad'] - 25
registratie['brandstofvoorraad'] = registratie['brandstofvoorraad'] - 15
registratie['temperatuur'] = -32
registratie['status'] = 'sneeuwstorm'

print(f"De nieuwe temperatuur is: {registratie['temperatuur']}")
print(f"De nieuwe energievoorraad is: {registratie['energievoorraad']}")
print(f"De nieuwe brandstofvoorraad is: {registratie['brandstofvoorraad']}")
print(f"De status van de onderzoeksbasis is nu: {registratie['status']}")
print()

# ====================
# Energiecontrole
# ====================

if registratie['energievoorraad'] < 25:
    print(f"{registratie['naam'].title()} heeft een kritiek energieniveau")
elif registratie['energievoorraad'] < 50:
    print(f"Energiebesparing in {registratie['naam'].title()} is noodzakelijk")
elif registratie['energievoorraad'] < 75:
    print(f"Energievoorraad in {registratie['naam'].title()} is beperkt")
elif registratie['energievoorraad'] >= 75:
    print(f"{registratie['naam'].title()} heeft voldoende energie")
print()

# ==============================
# Reparatie van de generator
# ==============================

if registratie['brandstofvoorraad'] < 30:
    herstel = 5
elif registratie['brandstofvoorraad'] < 60:
    herstel = 15
else:
    herstel = 25

registratie['energievoorraad'] = registratie['energievoorraad'] + herstel
registratie['brandstofvoorraad'] = registratie['brandstofvoorraad'] - 10

print(f"De nieuwe energievoorraad is: {registratie['energievoorraad']}")
print(f"De nieuwe brandstofvoorraad is: {registratie['brandstofvoorraad']}")
print()

# =======================
# Voorraadlevering
# =======================

beschikbare_voorraad =[
    'medicijnen',
    'voedsel',
    'gereedschap',
    'brandstof',
    'winterkleding',
    'radioapparatuur',
    'zuurstofflessen',
]

gevraagde_voorraad =[
    'voedsel',
    'medicijnen',
    'generatoronderdelen',
    'winterkleding',
    'satelliettelefoon',
    'brandstof',
]

for voorraad in gevraagde_voorraad:
    if voorraad in beschikbare_voorraad:
        print(f"Het volgende artikel is beschikbaar en word bij de basis gedropt: {voorraad} ")
    else:
        print(f"Het volgende artikel is niet beschikbaar: {voorraad}")
print()

# =================================
# Meerdere problemen op de basis
# =================================

problemen =[
    'bevroren waterleiding',
    'beschadigde antenne',
    'defecte verwarming',
    'geblokkeerde nooduitgang',
]

for probleem in problemen:
    if probleem == 'bevroren waterleiding':
        print("De waterleiding is bevroren, actie is noodzakelijk")
    if probleem == 'beschadigde antenne':
        print("De antenne moet zo spoedig mogelijk gerepareerd worden anders is er geen contact met de buitenwereld")
    if probleem == 'defecte verwarming':
        print("De verwarming moet gerepareerd worden anders bevriezen we")
    if probleem == 'geblokkeerde nooduitgang':
        print("We moeten de nooduitgang vrij maken en andere nooduitgangen controleren")
print()

# ============================
# Voedsel tijdens de storm
# ============================

voedselmetingen = []

for dag in range(1, 8):
    registratie['voedselvoorraad'] = registratie['voedselvoorraad'] - 7
    voedselmetingen.append(registratie['voedselvoorraad'])

gemiddelde = sum(voedselmetingen) / len(voedselmetingen)

print(f"Alle voedselmetingen: {voedselmetingen}")
print(f"Voedselmetingen de eerste 3 dagen: {voedselmetingen[:3]}")
print(f"Voedselmetingen de laatste 3 dagen: {voedselmetingen[-3:]}")
print(f"Laagste voedselvoorraad: {min(voedselmetingen)}")
print(f"Hoogste voedselvoorraad: {max(voedselmetingen)}")
print(f"Gemiddelde voedselvoorraad: {gemiddelde}")
print(f"Aantal gemeten dagen: {len(voedselmetingen)}")
print()

# =======================
# Einde van de storm
# =======================

registratie['temperatuur'] = -14

if registratie['energievoorraad'] < 30:
    registratie['status'] = 'noodtoestand'
elif registratie['voedselvoorraad'] < 30:
    registratie['status'] = 'voedseltekort'
else:
    registratie['status'] = 'operationeel'

# =================
# Eindrapport
# =================

print("==================================")
print("=== ONDERZOEKBASIS EINDRAPPORT ===")
print("==================================")
print()
print(f"Naam: {registratie['naam'].title()}")
print(f"Locatie: {registratie['locatie'].title()}")
print(f"Temperatuur: {registratie['temperatuur']}")
print(f"Status: {registratie['status']}")
print(f"Onderzoekers: {registratie['aantal onderzoekers']}")
print(f"Energievoorraad: {registratie['energievoorraad']}")
print(f"Brandstofvoorraad: {registratie['brandstofvoorraad']}")
print(f"Voedselvoorraad: {registratie['voedselvoorraad']}")
print(f"Aantal voedselmetingen: {len(voedselmetingen)}")
print(f"Laagste voedselmeting: {min(voedselmetingen)}")
print(f"Hoogste voedselmeting: {max(voedselmetingen)}")
print(f"Gemiddelde voedselmeting: {gemiddelde}")