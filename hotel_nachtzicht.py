# ==========================================================
# UITLEG PROJECT - HOTEL NACHTZICHT
# ==========================================================
#
# In dit project beheer ik de gegevens van een hotel en een
# gast met behulp van dictionaries. Ik oefen met het ophalen
# van gegevens met get() en het geven van een standaardwaarde
# wanneer een key niet bestaat.
#
# Tijdens het programma worden gastgegevens toegevoegd en
# verwijderd, verblijfskosten berekend en de hotelbezetting
# aangepast. Ook worden aangevraagde voorzieningen
# gecontroleerd en wordt de actuele hotelstatus bepaald.
#
# Gebruikte onderdelen:
# - dictionaries en key-value paren
# - get() met en zonder standaardwaarde
# - waarden toevoegen en wijzigen
# - key-value paren verwijderen met del
# - lists en for-loops
# - if, elif en else
# - in
# - berekeningen
# - f-strings en title()
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =====================
# Hotelgegevens
# =====================

hotel = {}

hotel['naam'] = 'hotel nachtzicht'
hotel['kamers'] = 60
hotel['bezette kamers'] = 42
hotel['personeel'] = 18
hotel['kas'] = 2500
hotel['status'] = 'geopend'

print(hotel)
print()

# ===================
# Gast gegevens
# ===================

gast ={
    'naam': 'olivia',
    'leeftijd': 34,
    'kamernummer': 27,
    'nachten': 4,
    'kamertype': 'luxe'
}

naam = gast.get('naam')
print(naam)
print()

kamernummer = gast.get('kamernummer')
print(kamernummer)
print()

telefoonnummer = gast.get('telefoonnummer', 'geen telefoonnummer bekend')
print(f"Telefoonnummer: {telefoonnummer}")
print()

# ==========================
# Onbekende betaalmethode
# ==========================

betaalmethode = gast.get('betaalmethode', 'nog niet geregistreerd')
print(f"Betaalmethode: {betaalmethode}")
print()

# ==========================
# Aanvullende gegevens
# ==========================

gast['telefoonnummer'] = '0612345678'
gast['betaalmethode'] = 'pin'

telefoonnummer = gast.get('telefoonnummer')
print(telefoonnummer)
print()

betaalmethode = gast.get('betaalmethode')
print(betaalmethode)
print()

# =================
# Kamerprijzen
# =================

kamerprijzen ={
    'standaard': 75,
    'comfort': 110,
    'luxe': 160,
    'suite': 250
}

kamertype = gast.get('kamertype')

totale_prijs = gast['nachten'] * kamerprijzen[kamertype]
hotel['kas'] = hotel['kas'] + totale_prijs

# ==========================
# Hotelbezetting verandert
# ==========================

hotel['bezette kamers'] = hotel['bezette kamers'] + 8

if hotel['bezette kamers'] < 30:
    print("Het hotel is rustig")
elif hotel['bezette kamers'] < 45:
    print(f"Het hotel is redelijk druk")
elif hotel['bezette kamers'] < 60:
    print(f"Het hotel is bijna vol")
else:
    print(f"Het hotel is vol")
print()

if hotel['bezette kamers'] < 60:
    hotel['status'] = 'geopend'
elif hotel['bezette kamers'] >= 60:
    hotel['status'] = 'gesloten'

# =============================
# Beschikbare voorzieningen
# =============================

beschikbare_voorzieningen =[
    'restaurant',
    'zwembad',
    'sauna',
    'fitnessruimte',
    'roomservice',
    'parkeergarage'
]

gevraagde_voorzieningen =[
    'zwembad',
    'spa',
    'roomservice',
    'casino',
    'parkeergarage'
]

for voorziening in gevraagde_voorzieningen:
    if voorziening in beschikbare_voorzieningen:
        print(f"De volgende voorziening is beschikbaar: {voorziening}")
    else:
        print(f"De volgende voorziening is niet beschikbaar: {voorziening}")
print()

# ========================
# Verwijderde gegevens
# ========================

del gast['kamernummer']

kamernummer = gast.get('kamernummer', 'uitgecheckt')

print(gast)

# ================
# Eindrapport
# ================

print("====================================")
print("=== HOTEL NACHTZICHT EINDRAPPORT ===")
print("====================================")
print()
print(f"Hotel: {hotel['naam'].title()}")
print(f"Aantal kamers: {hotel['kamers']}")
print(f"Bezette kamers: {hotel['bezette kamers']}")
print(f"Personeel: {hotel['personeel']}")
print(f"Status: {hotel['status']}")
print(f"Resterend geld in de kas: {hotel['kas']}")
print()
print("==========================================")
print()
print(f"Gast: {gast['naam'].title()}")
print(f"Aantal nachten: {gast['nachten']}")
print(f"Kamertype: {gast['kamertype'].title()}")
print(f"Kamernummer: {kamernummer}")
print(f"Telefoonnummer: {gast['telefoonnummer']}")
print(f"Betaalmethode: {gast['betaalmethode']}")
print(f"Totale verblijfkosten: {totale_prijs}")