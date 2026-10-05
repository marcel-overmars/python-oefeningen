# ==========================================================
# UITLEG PROJECT - PRETPARK CONTROLECENTRUM
# ==========================================================
#
# In dit project beheer ik het pretpark Adventure World.
# Het programma opent en sluit het park, controleert
# attractiekeuzes en houdt het aantal bezoekers bij.
#
# Gebruikte onderdelen:
# - functies maken met def
# - functies aanroepen
# - docstrings
# - dictionaries en lijsten
# - for-loops
# - while-loop met een stopvoorwaarde
# - if / elif / else
# - in
# - input van de gebruiker
# - teller met +=
# - dictionarywaarden aanpassen
#
# Het belangrijkste nieuwe onderdeel van dit project was het
# maken van eigen functies. Een functie wordt eerst met def
# gedefinieerd en wordt pas uitgevoerd wanneer de functie
# wordt aangeroepen.
#
# Daarnaast heb ik oudere Python-onderdelen gecombineerd,
# waaronder een while-loop met if/elif/else om alleen geldige
# attractiekeuzes als bezoeker mee te tellen.
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# =================
# Parkgegevens
# =================

parkgegevens = {
    'naam': 'Adventure World',
    'status': 'gesloten',
    'bezoekers': 0
}

for park, gegevens in parkgegevens.items():
    print(f"{park.title()}: {gegevens}")
print()

# ====================
# Openingsprocedure
# ====================

def openingsprocedure():
    """OPENINGSPROCEDURE"""
    print("De veiligheidscontrole is uitgevoerd;")
    print("De attracties zijn gestart;")
    print("De poorten worden geopend.")

openingsprocedure()
print()

parkgegevens['status'] = 'open'

# ==============
# Attracties
# ==============

attracties = [
    'achtbaan',
    'reuzenrad',
    'wildwaterbaan',
    'spookhuis',
    "botsauto's"
]

for attractie in attracties:
    print(attractie)
print()

attractie = ""
geldige_attractie = 0

while attractie != 'stop':
    attractie = input("Voer een attractie in of druk op 'stop': ")

    if attractie == 'stop':
        print("De invoerprocedure is afgelopen")
    elif attractie in attracties:
        print(f"Toegang toegestaan tot: {attractie}")
        geldige_attractie +=1
    else:
        print("Deze attractie bestaat niet.")
print()

# =======================
# Dagelijkse controle
# =======================

def dagelijkse_controle():
    """DAGELIJKSE CONTROLE"""
    print("Nooduitgangen: OK")
    print("Camera's: OK")
    print("EHBO-post: OK")

dagelijkse_controle()
print()
dagelijkse_controle()
print()

# ====================
# Bezoekersaantal
# ====================

parkgegevens['bezoekers'] = parkgegevens['bezoekers'] + geldige_attractie

for park, gegevens in parkgegevens.items():
    print(f"{park}: {gegevens}")
print()

# ======================
# Sluitingsprocedure
# ======================

def sluitingsprocedure():
    """SLUITINGSPROCEDURE"""
    print("Attracties worden uitgeschakeld.")
    print("Terrein wordt gecontroleerd.")
    print("Poorten worden gesloten.")

sluitingsprocedure()
print()

parkgegevens['status'] = 'gesloten'

# =================
# Eindrapport
# =================

print("=======================")
print("=== ADVENTURE WORLD ===")
print("=======================")
print()
print(f"Status: {parkgegevens['status']}")
print(f"Bezoekers vandaag: {parkgegevens['bezoekers']}")
print()

print("ATTRACTIES")

for attractie in attracties:
    print(attractie)