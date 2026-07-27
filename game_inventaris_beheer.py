# ============================================================
# PROJECT: GAME INVENTARIS BEHEER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig inventarissysteem
# voor twee spelers. Beide spelers beginnen met dezelfde
# inventaris, waarna iedere speler zijn eigen wijzigingen kan
# aanbrengen zonder dat de inventaris van de andere speler wordt
# aangepast.
#
# In dit project oefen ik met:
# - Lijsten maken en beheren
# - Een volledige lijst kopiëren met [:]
# - Gegevens toevoegen, wijzigen en verwijderen
# - Werken met indexen
# - For-loops gebruiken
# - Slices combineren met een for-loop
# - Gegevens overzichtelijk weergeven
# - len() gebruiken
# - F-strings gebruiken
# - Mijn programma overzichtelijk indelen met
#   commentaarblokken
#
# Doel:
# In dit project leer ik hoe ik een kopie van een bestaande
# lijst kan maken, zodat beide lijsten onafhankelijk van elkaar
# kunnen worden aangepast. Daarnaast herhaal ik eerder geleerde
# Python-onderwerpen zoals het beheren van lijsten, for-loops,
# slices en het overzichtelijk weergeven van informatie.
# ============================================================


# ===================================
# Lijst met items in de inventaris
# ===================================

speler_1 = []
speler_1.append('ijzeren zwaard')
speler_1.append('schild')
speler_1.append('health potion')
speler_1.append('gloves')
speler_1.append('armor')
speler_1.append('boots')
speler_1.append('mantel')
speler_1.append('food')
speler_1.append('water')
speler_1.append('mana potion')

speler_2 = speler_1[:]

# =================================
# Speler 1 inventaris wijzigingen
# =================================

speler_1[3] = 'leather gloves'
speler_1.insert(-1, 'strength potion')
del speler_1[4]

# =================================
# speler 2 inventaris wijzigingen
# =================================

speler_2[1] = 'staf'
speler_2.insert(2, 'wand')
speler_2.remove('armor')

# ===========================================
# Tonen inventaris van speler 1 en speler 2
# ===========================================

print("=========================")
print("== Inventaris speler 1 ==")
print("=========================")
for item in speler_1[0:]:
    print(f"== {item.title()}")
print("=========================")
print()

print("=========================")
print("== Inventaris speler 2 ==")
print("=========================")
for item in speler_2[0:]:
    print(f"== {item.title()}")
print("=========================")
print()

# ============================
# Vergelijking inventarissen
# ============================

print(f"Het aantal items van speler 1 is: {len(speler_1)}")
print()
print(f"Het aantal items van speler 2 is: {len(speler_2)}")
print()
print(f"Het eerste voorwerp van speler 1 is: {speler_1[0]}")
print(f"Het laatste voorwerp van speler 1 is: {speler_1[-1]}")
print()
print(f"Het eerste voorwerp van speler 2 is: {speler_2[0]}")
print(f"Het laatste voorwerp van speler 2 is: {speler_2[-1]}")
