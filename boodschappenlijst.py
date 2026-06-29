# ============================================================
# PROJECT: Boodschappenlijst
#
# In dit oefenproject maak ik een eenvoudige boodschappenlijst.
# Ik begin met een lege lijst en voeg vervolgens producten toe
# met de append()-methode. Daarna pas ik één product aan,
# haal ik verschillende producten uit de lijst op en bereken ik
# de totale kosten van alle boodschappen.
#
# In dit project oefen ik met:
# - Lists maken
# - Een lege list gebruiken
# - Elementen toevoegen met append()
# - Elementen wijzigen met een index
# - Elementen ophalen met positieve en negatieve indexen
# - String-methodes zoals .title()
# - Variabelen
# - Rekenen met floats
# - F-strings gebruiken
# - print() gebruiken voor een overzichtelijke uitvoer
# - Mijn code indelen met commentaar en duidelijke kopjes
#
# Doel:
# Leren hoe je een lijst kunt opbouwen, aanpassen en gebruiken
# binnen een klein Python-programma.
# ============================================================


# ==================
# boodschappenlijst
# ==================

print("------------------")
print("Boodschappenlijst")
print("------------------")
print()

boodschappenlijst = []

boodschappenlijst.append('melk')
boodschappenlijst.append('eieren')
boodschappenlijst.append('brood')
boodschappenlijst.append('schouderham')
boodschappenlijst.append('shampoo')
boodschappenlijst.append('badschuim')
print(boodschappenlijst)
print()
print()

# =============================
# Aangepaste boodschappenlijst
# =============================

print("----------------------------")
print(f"Boodschappenlijst aangepast")
print("----------------------------")
print()

boodschappenlijst[-1] = ('wasmiddel')
print(boodschappenlijst)
print()
print()

print("------------")
print("BELANGRIJK")
print("------------")
print()

print(f"{boodschappenlijst[0].title()}")
print(f"{boodschappenlijst[2].title()}")
print(f"{boodschappenlijst[-1].title()}")
print()
print()
print(f"{boodschappenlijst[0].title()} heb ik helemaal niet meer!")
print()
print()

# ======================================
# Wat ik moet betalen voor de producten.
# ======================================

print("-------")
print("Kosten")
print("-------")
print()

melk, eieren, brood, schouderham, shampoo, wasmiddel = 2.99, 3.50, 0.99, 1.85, 5.99, 7.55
totaal_prijs = melk + eieren + brood + schouderham + shampoo + wasmiddel
print(f"De totale kosten bedragen €{totaal_prijs}!")