# ==========================================================
# UITLEG PROJECT - RAVENWOOD TRADING POST
# ==========================================================
#
# In dit project beheer ik een middeleeuwse handelspost.
# Het programma berekent aankopen, voegt handelsbelasting
# toe, verwerkt verkopen en houdt de voorraad en het
# beschikbare goud bij.
#
# Gebruikte onderdelen:
# - Dictionaries en lijsten met dictionaries
# - For-loops en if/elif-statements
# - Functies maken met def
# - Positional en keyword arguments
# - Default values voor parameters
# - Return om berekende waarden terug te geven
# - Resultaten van functies opnieuw gebruiken
# - Dictionarywaarden aanpassen met += en -=
#
# Het belangrijkste oefenonderdeel was def en return.
# Hiermee bereken ik aankoopprijzen en geef ik de
# resultaten door aan andere functies.
#
# Daarnaast heb ik oudere Python-technieken herhaald,
# zoals het doorlopen en aanpassen van dictionaries.
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de opdracht en feedback.
# ==========================================================

# ==============================
# Gegevens van de handelspost
# ==============================

handelspost = {
    'naam': 'Ravenwood Trading Post',
    'locatie': 'Ravenwood',
    'eigenaar': 'Arthur',
    'goud': 500,
    'status': 'geopend'
}

for post, gegevens in handelspost.items():
    print(f"{post.title()}: {gegevens}")
print()

# ==================
# Handelsvoorraad
# ==================

product_1 = {
    'naam': 'Iron Sword',
    'prijs': 80,
    'voorraad': 5
}

product_2 = {
    'naam': 'Health Potion',
    'prijs': 25,
    'voorraad': 12
}

product_3 = {
    'naam': 'Leather armor',
    'prijs': 120,
    'voorraad': 3
}

product_4 = {
    'naam': 'Magic Scroll',
    'prijs': 60,
    'voorraad': 7
}

producten = [
    product_1,
    product_2,
    product_3,
    product_4
]

for product in producten:
    print(product)
print()

# ======================
# Productinformatie
# ======================

def toon_product(naam, prijs, voorraad):
    print(f"Naam: {naam}")
    print(f"Prijs: {prijs} goud")
    print(f"Voorraad: {voorraad}")

toon_product(product_2['naam'], product_2['prijs'], product_2['voorraad'])
print()

toon_product(prijs=product_4['prijs'], voorraad=product_4['voorraad'], naam=product_4['naam'])
print()

# ====================
# Aankoop berekenen
# ====================

def bereken_aankoop(prijs, aantal):
    bedrag = prijs * aantal
    return bedrag

totaal_bedrag = bereken_aankoop(product_1['prijs'], 2)

print(f"{product_1['naam']} is 2x verkocht voor een bedrag van: {totaal_bedrag} goud")
print()

# =====================
# Handelsbelasting
# =====================

def bereken_eindprijs(totaal_bedrag, belasting=10):
    eind_bedrag = totaal_bedrag + belasting
    return eind_bedrag

aankoop_eind_bedrag = bereken_eindprijs(totaal_bedrag)

print(f"Aankoop inclusief belasting brengt het eindbedrag op: {aankoop_eind_bedrag} goud")
print()

# ======================
# Voorraad aanpassen
# ======================

product_1['voorraad'] -= 2

handelspost['goud'] += aankoop_eind_bedrag

print(f"De nieuwe voorraad van {product_1['naam']} is: {product_1['voorraad']}")
print()
print(f"De nieuwe goudvoorraad van {handelspost['naam']} is: {handelspost['goud']}")
print()

# ====================
# Voorraadcontrole
# ====================

for product in producten:
    if product['voorraad'] < 4:
        product['status'] = 'bijna uitverkocht'
    elif product['voorraad'] >= 4:
        product['status'] = 'voldoende voorraad'

for product in producten:
    print(product)
print()

# ====================
# Tweede aankoop
# ====================

totaal_health_potion = bereken_aankoop(product_2['prijs'], 3)

eindbedrag_health_potion = bereken_eindprijs(totaal_health_potion)

print(f"Het totaal voor 3 {product_2['naam']} is: {eindbedrag_health_potion}")
print()

product_2['voorraad'] -= 3

handelspost['goud'] += eindbedrag_health_potion

# =============
# Eindrapport
# =============

print("==============================")
print("=== RAVENWOOD TRADING POST ===")
print("==============================")
print()
print(f"Eigenaar: {handelspost['eigenaar']}")
print(f"Locatie: {handelspost['locatie']}")
print(f"Status: {handelspost['status']}")
print()
print(f"TOTAAL GOUD: {handelspost['goud']}")
print()
print("VOORRAAD")
print()

for product in producten:
    print(product)