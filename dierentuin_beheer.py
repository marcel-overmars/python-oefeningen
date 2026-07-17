​# ============================================================
# PROJECT: DIERENTUIN BEHEER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor het
# beheren van een dierentuin. Tijdens het programma worden
# dieren toegevoegd, gewijzigd en verwijderd. Daarnaast wordt
# bijgehouden hoeveel dieren aanwezig zijn, worden de dieren
# gevoerd en gecontroleerd met behulp van een for-loop en wordt
# de verwachte omzet van de dierentuin berekend.
#
# In dit project oefen ik met:
# - Lists maken en gebruiken
# - Een lege list vullen met append()
# - Elementen wijzigen met een index
# - Nieuwe elementen invoegen met insert()
# - Elementen verwijderen met del
# - Elementen verwijderen en bewaren met pop()
# - Elementen verwijderen op naam met remove()
# - Het aantal elementen bepalen met len()
# - Gegevens ophalen met positieve en negatieve indexen
# - Tijdelijk sorteren met sorted()
# - Permanent sorteren met sort()
# - Permanent sorteren in omgekeerde volgorde met reverse=True
# - String-methodes zoals .upper() en .title()
# - Variabelen
# - Constanten
# - Integers en floats
# - Berekeningen uitvoeren
# - F-strings gebruiken
# - Getallen leesbaar maken met underscores
# - Geldbedragen weergeven met twee decimalen (:.2f)
# - Herhalende taken uitvoeren met een for-loop
# - print(), \n en \t gebruiken voor een overzichtelijke uitvoer
# - Mijn programma indelen met duidelijke commentaren en kopjes
#
# Doel:
# Leren hoe verschillende bewerkingen op lijsten gecombineerd
# kunnen worden binnen één groter programma. Daarnaast oefen ik
# voor het eerst met for-loops om automatisch dezelfde opdracht
# uit te voeren voor ieder item in een lijst. Ook oefen ik met
# het berekenen en overzichtelijk presenteren van gegevens.
# ============================================================


print("=========================")
print("=== DIERENTUIN BEHEER ===")
print("=========================")
print()

# ===================================
# Lijst van dieren in de dierentuin
# ===================================

dieren = []
dieren.append('leeuw')
dieren.append('olifant')
dieren.append('giraffe')
dieren.append('bruine beer')
dieren.append('wolf')
dieren.append('tijger')
dieren.append('neushoorn')
dieren.append('nijlpaard')
print(dieren)
print()

# =================================
# Wijzigingen beschikbare dieren
# =================================

dieren[-1] = 'zebra'
dieren.insert(3, 'krokodil')
del dieren[2]
afwezig = dieren.pop(0)
dieren.remove('wolf')
print(f"De {afwezig.title()} is tijdelijk afwezig in de dierentuin vanwege een fokprogramma!")
print()

# ===================================
# Aantal dieren en speciale dieren
# ===================================

aantal_dieren = len(dieren)
print(f"Het aantal dieren te bezichtigen is: {aantal_dieren}")
print()
print("Bijzondere dieren die bezichtigd kunnen worden:")
print()
print(dieren[1].upper())
print(dieren[3].upper())
print(dieren[-1].upper())
print()

# =================
# Gevoerde dieren
# =================

print("=== GEVOERDE DIEREN ===")
print()

for dier in dieren:
    print(f"Het volgende dier is gevoerd:\t{dier.title()}")
print()

# ===================================
# Controle uitvoering bij de dieren
# ===================================

print("=== GECONTROLEERDE DIEREN ===")
print()

for dier in dieren:
    print(f"De controle is uitgevoerd bij de {dier.title()}!")
print()

# ===============================
# Dierenverblijven op volgorde
# ===============================

print(sorted(dieren))
print()

dieren.sort()
print(f"permanente alfabetische volgorde:")
print(dieren)
print()

dieren.sort(reverse=True)
print("permanente omgekeerde alfabetische volgorde:")
print(dieren)
print()

# ==================
# Berekening omzet
# ==================

PRIJS_TOEGANGSKAART = 35
aantal_bezoekers = 267
opbrengst_souvenirwinkel = 3_250.35
opbrengst_restaurant = 3_596.95
totale_omzet = (PRIJS_TOEGANGSKAART * aantal_bezoekers) + opbrengst_souvenirwinkel + opbrengst_restaurant
print(f"De totale omzet van de dierentuin is €{totale_omzet:.2f}")
