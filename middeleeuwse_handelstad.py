# ==========================================================
# UITLEG PROJECT - MIDDELEEUWSE HANDELSSTAD
# ==========================================================
#
# In dit project beheer ik de middeleeuwse stad Valenstad.
# Gegevens over de stad worden opgeslagen in een dictionary
# en veranderen door gebeurtenissen zoals een aanval en beleg.
#
# Daarnaast gebruik ik dictionaries om handelaren en prijzen
# op te slaan. Ik oefen met het opvragen, toevoegen, wijzigen
# en verwijderen van key-value paren.
#
# Verder controleert het programma beschikbare versterkingen,
# houdt het de voedselvoorraad bij en bepaalt het uiteindelijk
# de nieuwe status van de stad.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - waarden toevoegen, wijzigen en verwijderen met del
# - lists, for-loops en range()
# - if, elif en else
# - in
# - berekeningen
# - len(), min(), max() en sum()
# - list slicing
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =============================
# Basisgegevens van de stad
# =============================

basisgegevens = {}

basisgegevens['naam'] = 'valenstad'
basisgegevens['inwoners'] = 850
basisgegevens['goudvoorraad'] = 1200
basisgegevens['bewakers'] = 45
basisgegevens['status'] = 'veilig'

print(basisgegevens)
print()

# ==============
# Handelaren
# ==============

handelaren ={
    'hendrik':  'wapens',
     'sofia': 'voedsel',
     'bram': 'kleding',
     'elena': 'medicijnen',
     'victor': 'gereedschap',
}

print(f"Sofia verkoopt: {handelaren['sofia']}")
print(f"Victor verkoopt: {handelaren['victor']}")
print()

# =========================
# Een handelaar vertrekt
# =========================

del handelaren['bram']

print(handelaren)
print()

# ==========================
# Prijzen op de markt
# ==========================

prijzen ={
    'brood': 4,
    'zwaard': 75,
    'medicijnen': 30,
    'touw': 12,
    'fakkel': 8
}

zwaard = prijzen['zwaard']

print(f"Een zwaard kost {zwaard} goudstukken")

# =====================================
# Verliezen door aanval op de stad
# =====================================

basisgegevens['goudvoorraad'] = basisgegevens['goudvoorraad'] - 200
basisgegevens['bewakers'] =basisgegevens['bewakers'] - 12
basisgegevens['status'] = 'aangevallen'

if basisgegevens['bewakers'] < 15:
    print("De verdediging staat op instorten!")
elif basisgegevens['bewakers'] < 30:
    print("De stad heeft dringend versterking nodig!")
elif basisgegevens['bewakers'] <40:
    print("De verdediging is verzwakt!")
else:
    print("De stad is goed verdedigd!")
print()

# ===========================
# Beschikbare verdediging
# ===========================

beschikbare_versterking =[
    'boogschutters',
    'ridders',
    'wachters',
    'katapulten',
    'ruiters',
]

gevraagde_versterking =[
    'ridders',
    'kanonnen',
    'boogschutters',
    'draken',
    'ruiters',
]

for eenheid in gevraagde_versterking:
    if eenheid in beschikbare_versterking:
        print(f"{eenheid.title()} is beschikbaar en wordt gestuurd!")
    else:
        print(f"{eenheid.title()} is niet beschikbaar!")
print()

# ==========================
# Verzonden verdediging
# ==========================

if basisgegevens['goudvoorraad'] < 200:
    versterking = 5
elif basisgegevens['goudvoorraad'] < 400:
    versterking = 15
else:
    versterking = 25

basisgegevens['bewakers'] = basisgegevens['bewakers'] + versterking

# ====================================
# Voedselvoorraad tijdens het beleg
# ====================================

basisgegevens['voedselvoorraad'] = 140

voedselvoorraden = []

for dag in range(1, 8):
    basisgegevens['voedselvoorraad'] = basisgegevens['voedselvoorraad'] - 15
    voedselvoorraden.append(basisgegevens['voedselvoorraad'])

gemiddelde = sum(voedselvoorraden) / len(voedselvoorraden)

print(f"Alle metingen: {voedselvoorraden}")
print(f"De metingen over de eerste 3 dagen: {voedselvoorraden[:3]}")
print(f"De metingen over de laatste 3 dagen: {voedselvoorraden[-3:]}")
print(f"Laagste voorraad: {min(voedselvoorraden)}")
print(f"Hoogste voorraad: {max(voedselvoorraden)}")
print(f"Gemiddelde voorraad: {gemiddelde}")
print(f"Aantal gemeten dagen: {len(voedselvoorraden)}")
print()

# ==================
# Nieuwe status
#===================

if basisgegevens['voedselvoorraad'] < 40:
    basisgegevens['status'] = 'voedseltekort'
elif basisgegevens['bewakers'] < 40:
    basisgegevens['status'] = 'verdediging kritisch'
else:
    basisgegevens['status'] = 'situatie onder controle'

# ===================
# Eindrapport
# ===================

print("===============================")
print("=== VALENSTAD - EINDRAPPORT ===")
print("===============================")
print()
print(f"Naam: {basisgegevens['naam']}")
print(f"Inwoners: {basisgegevens['inwoners']}")
print(f"Status: {basisgegevens['status']}")
print(f"Goudvoorraad: {basisgegevens['goudvoorraad']}")
print(f"Aantal bewakers: {basisgegevens['bewakers']}")
print(f"Aantal handelaren: {len(handelaren)}")
print(f"Prijs van een zwaard: {zwaard}")
print(f"Resterende voedselvoorraad: {basisgegevens['voedselvoorraad']}")
print(f"Laagste voedselvoorraad: {min(voedselvoorraden)}")
print(f"Gemiddelde voedselvoorraad: {gemiddelde}")