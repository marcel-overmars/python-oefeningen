# ==========================================================
# UITLEG PROJECT - MAGISCHE GOLEMFABRIEK
# ==========================================================
#
# In dit project oefen ik verder met nesting door meerdere
# dictionaries automatisch aan te maken en deze in één
# lijst op te slaan.
#
# Met slices worden verschillende groepen golems uit de
# lijst geselecteerd. Afhankelijk van hun huidige materiaal
# worden deze golems aangepast en verder geüpgraded.
# Hierdoor ontstaan standaard, verbeterde en elite golems.
#
# Gebruikte onderdelen:
# - een lijst met dictionaries
# - dictionaries aanmaken in een for-loop
# - append() gebruiken
# - range()
# - for-loops
# - slices
# - if, elif en else
# - dictionarywaarden controleren en wijzigen
# - indexen gebruiken bij een lijst met dictionaries
# - gegevens uit geneste dictionaries ophalen
# - len()
# - f-strings
#
# Zelf geprogrammeerd als oefening tijdens het leren van
# Python. ChatGPT hielp met de projectopdracht en feedback.
# ==========================================================

# ==================
# Golems maken
# ==================

golems = []

for aantal in range (1, 13):
    golem = {
        'materiaal': 'steen',
        'kracht': 20,
        'snelheid': 'langzaam',
        'levenspunten': 100,
        'status': 'standaard'
    }
    golems.append(golem)

print(f"Aantal gemaakte golems: {len(golems)}")
print()

# ==================
# Eerste controle
# ==================

for golem in golems[:4]:
    print(golem)
print()

# ===================
# Eerste upgrade
# ===================

for golem in golems[:4]:
    if golem['materiaal'] == 'steen':
        golem['materiaal'] = 'ijzer'
        golem['kracht'] = 40
        golem['snelheid'] = 'normaal'
        golem['levenspunten'] = 150
        golem['status'] = 'verbeterd'

for golem in golems[:4]:
    print(golem)
print()

# ===================
# Tweede upgrade
# ===================

for golem in golems[:8]:
    if golem['materiaal'] == 'steen':
        golem['materiaal'] = 'ijzer'
        golem['kracht'] = 40
        golem['snelheid'] = 'normaal'
        golem['levenspunten'] = 150
        golem['status'] = 'verbeterd'
    elif golem['materiaal'] == 'ijzer':
        golem['materiaal'] = 'magisch staal'
        golem['kracht'] = 70
        golem['levenspunten'] = 200
        golem['status'] = 'elite'

for golem in golems:
    print(golem)
print()

# ================
# Eindrapport
# ================

print("================================")
print("=== GOLEMFABRIEK EINDRAPPORT ===")
print("================================")
print()
print(f"Aantal golems: {len(golems)}")
print(f"Materiaal eerste golem: {golems[0]['materiaal']}")
print(f"Status eerste golem: {golems[0]['status']}")
print(f"Kracht eerste golem: {golems[0]['kracht']}")
print(f"Materiaal laatste golem: {golems[-1]['materiaal']}")
print(f"Status laatste golem: {golems[-1]['status']}")
print(f"Kracht laatste golem: {golems[-1]['kracht']}")