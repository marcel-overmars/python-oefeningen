# ==========================================================
# UITLEG PROJECT - FANTASY ARENA
# ==========================================================
#
# In dit project beheer ik de Dragon Arena. Vechters kunnen
# worden aangemeld, hun klasse wordt gecontroleerd en het
# programma houdt het aantal geldige deelnemers bij.
#
# Gebruikte onderdelen:
# - functies maken met def
# - parameters en argumenten
# - functies met 1, 2 en 3 parameters
# - positional arguments
# - functies meerdere keren aanroepen
# - waarden uit een dictionary als argument gebruiken
# - dictionaries en lijsten
# - while-loop met een flag
# - if / else
# - in
# - input van de gebruiker
# - tellers met +=
# - for-loops
#
# Het belangrijkste nieuwe onderdeel was het werken met
# parameters en argumenten. De parameters worden bepaald bij
# het definiëren van een functie. Bij het aanroepen geef ik
# de daadwerkelijke waarden als argumenten mee.
#
# Hierdoor kan dezelfde functie meerdere keren met
# verschillende gegevens worden gebruikt.
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ================================
# Arenagegevens met dictionary
# ================================

arena = {
    'naam': 'Dragon Arena',
    'plaats': 'Ironforge',
    'status': 'open',
    'vechters': 0
}

for gegevens, waarde in arena.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# =======================================
# Vechter voorstellen met functie(def)
# =======================================

def welkom(naam):
    """VOORSTELLEN"""
    print(f"Welkom in de arena, {naam.title()}")

welkom('arthas')
welkom('jaina')
welkom('thrall')

# ===================================
# Vechtergegevens met 2 parameters
# ===================================

def vechtergegevens(naam, klasse):
    print(f"\nVechter: {naam.title()}")
    print(f"Klasse: {klasse.title()}")

vechtergegevens('arthas', 'paladin')
vechtergegevens('jaina', 'rogue')
vechtergegevens('thrall', 'shaman')

# ==================================
# Wapencontrole met 3 parameters
# ==================================

def wapencontrole(naam, wapen, schade):
    """WAPENCONTROLE"""
    print(f"\nVechter: {naam.title()}")
    print(f"Wapen: {wapen.title()}")
    print(f"Schade: {schade}")

wapencontrole('thrall', 'doomhammer', 85 )
wapencontrole('jaina', 'windfury', 110)
wapencontrole('arthas', 'stormbreaker', 70 )
print()

# =====================
# Gevechtscontrole
# =====================

toegestane_klasse = [
    'paladin',
    'mage',
    'warrior',
    'hunter',
    'shaman'
]

inschrijven_active = True
aantal_inschrijvingen = 0

while inschrijven_active:
    naam = input(f"\nWat is je naam? ")
    klasse = input("Wat is je klasse? ")

    if klasse in toegestane_klasse:
        print(f"{naam.title()} mag deelnemen aan de arena.")
        aantal_inschrijvingen += 1
    else:
        print("Deze klasse is niet toegestaan")

    herhaling = input("Wil je nog een speler inschrijven? (ja/nee) ")

    if herhaling == 'nee':
        inschrijven_active = False

arena['vechters'] += aantal_inschrijvingen
print()

for gegevens, waarde in arena.items():
    print(f"{gegevens.title()}: {waarde}")
print()

# ==================================================
# Arena-status met functie(def) met 2 parameters
# ==================================================

def arena_status(arena_naam, aantal_vechters):
    print("=== ARENA STATUS ===")
    print(arena_naam)
    print(f"Aantal vechters: {aantal_vechters}")

arena_status(arena['naam'], arena['vechters'])

# ==============
# Eindrapport
# ==============

print("====================")
print("=== DRAGON ARENA ===")
print("====================")
print()
print(f"Plaats: {arena['plaats']}")
print(f"Status: {arena['status']}")
print(f"Aantal geldige vechters: {arena['vechters']}")
print()
print("Toegestane klassen:")

for klasse in toegestane_klasse:
    print(klasse)