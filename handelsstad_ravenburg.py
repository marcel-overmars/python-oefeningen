# ==========================================================
# UITLEG PROJECT - HANDELSSTAD RAVENBURG
# ==========================================================
#
# In dit project beheer ik een handelsstad met behulp van
# dictionaries en lijsten. Ik oefen met verschillende
# manieren om gegevens uit dictionaries te gebruiken.
#
# Met keys(), values() en items() worden verschillende delen
# van dictionaries doorlopen. Daarnaast gebruik ik sorted()
# om gegevens te sorteren en set() om dubbele waarden te
# verwijderen.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - keys(), values() en items()
# - get() om gegevens veilig op te vragen
# - sorted() en set()
# - waarden toevoegen, wijzigen en verwijderen
# - gegevens uit dictionaries opslaan in variabelen
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

# =============================
# Basisgegevens van de stad
# =============================

handelsstad ={
    'naam': 'ravenburg',
    'inwoners': 1250,
    'goudvoorraad': 2400,
    'bewakers': 55,
    'voedselvoorraad': 180,
    'status': 'veilig'
}

for gegeven, waarde in handelsstad.items():
    print(f"{gegeven.title()}: {waarde}")
print()

# ===========================
# Register van handelaren
# ===========================

handelarenregister ={
    'hendrik': 'wapens',
    'sofia': 'voedsel',
    'marcus': 'wapens',
    'elena': 'medicijnen',
    'victor': 'gereedschap',
    'luna': 'voedsel',
    'borin': 'wapens'
}

for handelaar in handelarenregister.keys():
    print(handelaar)
print()

# ======================================
# handelaren op alfabetische volgorde
# ======================================

for handelaar in sorted(handelarenregister.keys()):
    print(handelaar)
print()

# ==========================
# alleen de handelsoorten
# ==========================

for handelsoort in handelarenregister.values():
    print(handelsoort)
print()

# =======================
# Unieke handelsoorten
# =======================

for handelsoort in set(handelarenregister.values()):
    print(handelsoort)
print()

# =============================================================
# - Variabelen voor de goudvoorraad en bewaking van de stad 
#   en de handel van Elena uit de dictionary gehaald.
# =============================================================

goud = handelsstad['goudvoorraad']

bewakers = handelsstad['bewakers']

print(f"Ravenburg heeft {goud} goudstukken.")
print(f"Er bewaken {bewakers} bewakers de stad.")
print()

handel_elena = handelarenregister['elena']

print(f"Elana handelt in {handel_elena}.")
print()

# =======================
# Onbekende handelaar
# =======================

darius = handelarenregister.get('darius', 'Handelaar niet geregistreerd')
print(darius)
print()

# =================
# Leveringslijst
# =================

gevraagde_goederen =[
    'wapens',
    'medicijnen',
    'zijde',
    'voedsel',
    'paarden',
    'gereedschap'
]

for goederen in gevraagde_goederen:
    if goederen in handelarenregister.values():
        print(f"{goederen.title()} kunnen in {handelsstad['naam'].title()} worden gekocht!")
    else:
        print(f"{goederen.title()} zijn niet verkrijgbaar in {handelsstad['naam'].title()}")
print()

# ==========================
# Belangrijke handelaren
# ==========================

belangrijke_handelaren = [
    'sofia',
    'elena',
    'borin'
]

for handelaren in handelarenregister.keys():
    if handelaren in belangrijke_handelaren:
        print(f"{handelaren.title()} heeft toestemming om in het marktcentrum te handelen.")
print()

# =============================
# Veranderingen op de markt
# =============================

del handelarenregister['marcus']

handelarenregister['darius'] = 'paarden'

handelarenregister['victor'] = 'bouwmaterialen'

for handelaar, handel in handelarenregister.items():
    print(f"{handelaar.title()}: {handel.title()}")
print()

# ====================================
# Voorraad tijdens een handelsweek
# ====================================

voedselmetingen = []

for dag in range(1, 8):
    handelsstad['voedselvoorraad'] = handelsstad['voedselvoorraad'] - 18
    voedselmetingen.append(handelsstad['voedselvoorraad'])

gemiddelde = sum(voedselmetingen) / len(voedselmetingen)

print(f"Alle metingen: {voedselmetingen}")
print(f"Metingen van de eerste 3 dagen: {voedselmetingen[:3]}")
print(f"Metingen van de laatste 3 dagen: {voedselmetingen[-3:]}")
print(f"Laagste voorraad: {min(voedselmetingen)}")
print(f"Hoogste voorraad: {max(voedselmetingen)}")
print(f"Gemiddelde voorraad: {gemiddelde}")
print(f"Aantal metingen: {len(voedselmetingen)}")
print()

# ========================
# Controle van de stad
# ========================

handelsstad['bewakers'] = handelsstad['bewakers'] - 20

if handelsstad['bewakers'] < 20:
    handelsstad['status'] = 'onvoldoende verdediging'
elif handelsstad['bewakers'] < 40:
    handelsstad['status'] = 'verdediging verzwakt'
else:
    handelsstad['status'] = 'veilig'

# =================
# Eindrapport
# =================

print("===============================")
print("=== EINDRAPPORT - RAVENBURG ===")
print("===============================")
print()
print(f"Naam: {handelsstad['naam']}")
print(f"Inwoners: {handelsstad['inwoners']}")
print(f"Status: {handelsstad['status']}")
print(f"Goudvoorraad: {handelsstad['goudvoorraad']}")
print(f"Bewakers: {handelsstad['bewakers']}")
print(f"voedselvoorraad: {handelsstad['voedselvoorraad']}")
print(f"Aantal handelaren: {len(handelarenregister)}")
print(f"Aantal verschillende handelssoorten: {len(set(handelarenregister.values()))}")
print(f"Gemiddelde voedselvoorraad: {gemiddelde}")
print()