# ==========================================================
# UITLEG PROJECT - PIXEL VAULT VOORRAADCONTROLE
# ==========================================================
#
# In dit project beheer ik de voorraad van een gamewinkel.
# Games die meerdere keren in de voorraad voorkomen kunnen
# volledig uit de lijst worden verwijderd.
#
# Met een while-loop wordt gecontroleerd of een bepaalde game
# nog in de lijst voorkomt. Zolang dat zo is, wordt telkens
# één exemplaar verwijderd. Met een teller wordt bijgehouden
# hoeveel exemplaren zijn verwijderd.
#
# Daarnaast worden games van de ene lijst naar een andere
# lijst verplaatst en worden games per platform weergegeven.
#
# Gebruikte onderdelen:
# - dictionaries en lijsten
# - lijsten in dictionaries
# - .items()
# - while ... in ...
# - remove()
# - while op basis van een gevulde lijst
# - pop() en append()
# - for-loops en geneste for-loops
# - tellers met +=
# - modulo (%)
# - if-statements
# - len()
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ==================================
# Dictionary voor winkelgegevens
# ==================================

winkelgegevens = {
    'naam': 'Pixel Vault',
    'plaats': 'Apeldoorn',
    'medewerkers': 6,
    'status': 'geopend'
}

for winkel, gegevens in winkelgegevens.items():
    print(f"{winkel.title()}: {gegevens}")
print()

# ================================
# Lijst van binnengekomen games
# ================================

games = [
    'world of warcraft',
    'minecraft',
    'diablo IV',
    'fortnite',
    'minecraft',
    'elden ring',
    'fortnite',
    'cyberpunk 2077',
    'minecraft',
    "baldur's gate 3"
]

print(f"Totaal aantal geregistreerde games: {len(games)}")
print()

# ==========================================================
# Remove gebruiken om minecraft uit de voorraad te halen
# ==========================================================

while 'minecraft' in games:
    games.remove('minecraft')

print("De nog geregistreerde games:")
for game in games:
    print(game)
print()

print(f"Het aantal geregistreerde games: {len(games)}")
print()

# ============================================================
# Ook fortnite verwijderen met remove
# en met een teller bijhouden hoeveel er verwijderd worden
# ============================================================

fortnite_verwijderd = 0

while 'fortnite' in games:
    games.remove('fortnite')
    teller += 1

print(f"Aantal exemplaren van Fortnite uit de collectie gehaald: {fortnite_verwijderd}")

# ================
# Prijscontrole
# ================

game_prijs = [
    20,
    35,
    50,
    65,
    80
]

game_nummer = 0

for prijs in game_prijs:
    game_nummer += 1
    print(game_nummer, prijs)

    if game % 40 == 0:
        print("Speciale prijscontrole")
print()

# ===================================================
# Games controleren en overzetten naar nieuwe lijst
# ===================================================

gecontroleerde_games = []

while games:
    controleren = games.pop()
    gecontroleerde_games.append(controleren)

# ====================================================================
# Games per platform georderd met een for loop binnen een for loop
# ====================================================================

platforms = {
    'PC': [
        'world of warcraft',
        'diablo IV',
        'cyberpunk 2077'
    ],

    'Playstation': [
        'elden ring',
        "baldur's gate 3"
    ],

    'Xbox': [
        'diablo IV',
        'cyberpunk 2077'
    ]
}

for platform, spellen in platforms.items():
    print(f"\n{platform}")
    for spel in spellen:
        print(spel.title())
print()

# ==============
# Eindrapport
# ==============

print("===================================")
print("=== PIXEL VAULT VOORRAADRAPPORT ===")
print("===================================")
print()
print(f"Winkel: {winkelgegevens['naam'].title()}")
print(f"Plaats: {winkelgegevens['plaats'].title()}")
print(f"Status: {winkelgegevens['status'].title()}")
print()
print(f"Aantal Fortnite verwijdert: {fortnite_verwijderd}")
print(f"Aantal spellen in games: {len(games)}")
print(f"Aantal spellen in gecontroleerde_games: {len(gecontroleerde_games)}")
print()
print("Games nog op voorraad:")

for game in gecontroleerde_games:
    print(game.title())