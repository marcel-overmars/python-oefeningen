
# ============================================================
# PROJECT: GAME WINKEL BEHEER
# ============================================================
#
# In dit project maak ik een eenvoudig beheersysteem voor een
# gamewinkel. Het programma laat zien hoe vaste gegevens
# opgeslagen kunnen worden in een tuple en hoe producten
# beheerd kunnen worden met een lijst. Daarnaast oefen ik voor
# het eerst met if-statements om beslissingen te laten nemen
# op basis van de gegevens.
#
# In dit project oefen ik met:
# - Tuples gebruiken voor vaste gegevens
# - Lijsten maken en aanpassen
# - append(), insert(), del() en indexen
# - For-loops gebruiken
# - If- en else-statements
# - Gegevens vergelijken met ==
# - len() gebruiken
# - title() gebruiken voor een nette weergave
# - Gegevens overzichtelijk tonen met f-strings
# - Werken met duidelijke commentaarblokken
#
# Doel:
# Met dit project leer ik hoe een programma beslissingen kan
# nemen. In plaats van altijd dezelfde uitvoer te geven,
# controleert het programma eerst of een bepaalde voorwaarde
# waar is. Op basis daarvan wordt een andere boodschap
# weergegeven.
#
# Tijdens het bouwen heb ik geleerd:
# - Dat '=' wordt gebruikt om een waarde aan een variabele toe
#   te kennen.
# - Dat '==' wordt gebruikt om twee waarden met elkaar te
#   vergelijken.
# - Dat een if-statement een vraag stelt en alleen wordt
#   uitgevoerd als de voorwaarde waar (True) is.
# - Dat de else-code wordt uitgevoerd wanneer de voorwaarde
#   niet waar (False) is.
# - Dat for-loops en if-statements vaak samen worden gebruikt
#   om ieder item uit een lijst afzonderlijk te controleren.
# ============================================================

# ============================================
# Vaste catogorieën van de winkel met tuple
# ============================================

categorieën =(
    'Wapens',
    'Pantsers',
    'Drankjes',
    'Magie',
    'Materialen',
)

# =======================
# Lijst van producten
# =======================

producten = []

producten.append('dragon sword')
producten.append('schild')
producten.append('leren handschoenen')
producten.append('ijzeren laarzen')
producten.append('wand')
producten.append('health potion')
producten.append('mana potion')
producten.append('strength potion')
producten.append('leren armor')
producten.append('gun')

# ===========================
# Wijzigingen in producten
# ===========================

producten.insert(2, 'ijzeren handschoenen')
del producten[3]
producten[-1] = 'bow'

# =======================
# Controle met if
# =======================

for product in producten:
    if product == 'schild':
        print(f"{product.title()} is uitverkocht!\n")
    else:
        print(f"{product.title()} is nog beschikbaar!\n")
print()

# ===============================
# Zeldzaamheid producten met if
# ===============================

for product in producten:
    if product == 'dragon sword':
        print(f"{product.title()} is zeldzaam!\n")
    else:
        print(f"{product.title()} is normaal!\n")
print()

# ==============================
# Samenvatting game winkel
# ==============================

print("=======================")
print("Game winkel")
print("=======================")
print()

print("Categorieën:\n")
for categorie in categorieën:
    print(categorie.title())
print()

print("Producten:\n")
for product in producten:
    print(product.title())
print()

print(f"Aantal categorieën: {len(categorieën)}")
print(f"Aantal producten: {len(producten)}")
print(f"Eerste product: {producten[0].title()}")
print(f"Laatste product: {producten[-1].title()}")
print()
print("=======================")