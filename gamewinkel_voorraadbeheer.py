# ==========================================================
# UITLEG PROJECT - GAMEWINKEL VOORRAADBEHEER
# ==========================================================
#
# In dit project beheer ik de voorraad van een gamewinkel.
# De winkelgegevens worden opgeslagen in een dictionary en
# de verschillende games worden als dictionaries in één
# lijst opgeslagen.
#
# Met voorwaarden wordt de voorraad van iedere game
# gecontroleerd en krijgt iedere game een passende status.
# De eerste twee games krijgen korting en met een slice
# worden deze games opnieuw weergegeven.
#
# De games worden daarnaast verdeeld over categorieën.
# Met een geneste for-loop worden per categorie de
# verschillende games afzonderlijk weergegeven.
#
# Voor de klantenservice gebruik ik een while-loop met een
# flag. Zolang de flag True is blijft het systeem actief.
# Wanneer 'sluiten' wordt ingevoerd, verandert de flag naar
# False en stopt de while-loop.
#
# Gebruikte onderdelen:
# - dictionaries
# - een lijst met dictionaries
# - dictionarywaarden ophalen en wijzigen
# - for-loops
# - geneste for-loop
# - if, elif en else
# - while-loop
# - boolean flag met True en False
# - .items()
# - slices
# - len()
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ===================
# Winkelgegevens
# ===================

winkelgegevens = {
    'naam': 'Pixel Games',
    'stad': 'Apeldoorn',
    'medewerkers': 4,
    'status': 'Geopend'
}

for winkel, gegevens in winkelgegevens.items():
    print(f"{winkel.title()}: {gegevens}")
print()

# ==========
# Games
# ==========

game_1 = {
    'naam': 'world of warcraft',
    'prijs': 29.99,
    'voorraad': 4
}

game_2 = {
    'naam': 'minecraft',
    'prijs': 15.00,
    'voorraad': 7
}

game_3 = {
    'naam': 'skyrim',
    'prijs': 59.99,
    'voorraad': 3
}

game_4 = {
    'naam': 'cyberpunk 2077',
    'prijs': 9.99,
    'voorraad': 12
}

game_5 = {
    'naam': 'elden ring',
    'prijs': 49.99,
    'voorraad': 8
}

games = [
    game_1,
    game_2,
    game_3,
    game_4,
    game_5
]

print(f"Aantal verschillende games: {len(games)}")
print()

# ==================
# Voorraadcontrole
# ==================

for game in games:
    if game['voorraad'] < 5:
        game['status'] = 'bijna uitverkocht'
    elif game['voorraad'] < 10:
        game['status'] = 'beperkte voorraad'
    else:
        game['status'] = 'op voorraad'


game_1['prijs'] -= 5 # aanbieding

game_2['prijs'] -= 5 # aanbieding

for game in games[:2]:
    print(game)

# =================
# Categorieën
# =================

categorieen = {
    'rpg': [
        'skyrim',
        'cyberpunk 2077',
        'elden ring'
    ],

    'online': [
        'world of warcraft',
        'minecraft'
    ]
}

for categorie, spellen in categorieen.items():
    print(f"\n{categorie.title()} heeft de volgende spellen:")
    for spel in spellen:
        print(spel.title())
print()

# =====================
# Klantenservice
# =====================

actief = True

while actief:
    klantenservice = input("Welke vraag heeft de klant? ")

    if klantenservice == 'sluiten':
        actief = False
    else:
        print(f"Klantvraag: {klantenservice}")

print(f"\nKlantenservice afgesloten")

# ===============
# Eindrapport
# ===============

print("===================")
print("=== PIXEL GAMES ===")
print("===================")
print()
print(f"Naam: {winkelgegevens['naam']}")
print(f"Stad: {winkelgegevens['stad']}")
print(f"Medewerkers: {winkelgegevens['medewerkers']}")
print(f"Status: {winkelgegevens['status']}")
print(f"Aantal games: {len(games)}")
print()
print("================")
print("  Gamevoorraad")
print("================")
print()
for game in games:
    print(game)