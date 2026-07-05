# ============================================================
# PROJECT: BIBLIOTHEEKBEHEER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor het
# beheren van een bibliotheek. Ik begin met een lege lijst,
# voeg boeken toe aan de collectie en pas deze vervolgens aan
# door boeken te wijzigen, toe te voegen en te verwijderen.
#
# In dit project oefen ik met:
# - Lists maken en gebruiken
# - Een lege list vullen met append()
# - Elementen wijzigen met een index
# - Nieuwe elementen invoegen met insert()
# - Elementen verwijderen met del
# - Gegevens ophalen met positieve en negatieve indexen
# - String-methodes zoals .title(), .upper() en .lower()
# - Variabelen
# - Integers en floats
# - Een constante gebruiken
# - Multiple assignment
# - Rekenen met prijzen en boetes
# - F-strings gebruiken
# - print(), \n en \t gebruiken voor een overzichtelijke uitvoer
# - Mijn programma indelen met duidelijke commentaren en kopjes
#
# Doel:
# Leren hoe een lijst tijdens een programma kan veranderen en
# hoe verschillende onderdelen van Python samen gebruikt kunnen
# worden in een groter en realistischer oefenproject.
# ============================================================



# ===================
# BIBLIOTHEEKBEHEER
# ===================

print(f"\t\t\t=================")
print(f"\t\t\tBIBLIOTHEEKBEHEER")
print(f"\t\t\t=================")
print()

# ===========
# Boekenlijst
# ===========

boeken = []

boeken.append('lord of the rings: the two towers')
boeken.append('narnia: prins caspian')
boeken.append('harry potter: de steen der wijzen')
boeken.append('stille geheimen')
boeken.append('het droompad')
boeken.append('de laatste ochtend')
boeken.append('stemmen in het duister')
print(boeken)
print()

# ===========
# Wijzigingen
# ===========

boeken[2] = 'de terugkeer'
boeken.insert(4, 'zomernacht')
del boeken[-1]
print(boeken)
print()

# ================
# Populaire boeken
# ================

print(f"Populaire boeken:")
print(boeken[0].title())
print(boeken[2].title())
print(boeken[-1].title())
print()
print(f"{boeken[0].upper()} is het tweede deel van lord of the rings!")
print()
print(f"Het boek {boeken[2].lower()} wordt veel gelezen!")
print()
print(f"{boeken[-1].title()} wordt beschreven als erg spannend!")
print()

# ===========
# Huur boeken
# ===========

boek_1, boek_2, boek_3, boek_4, boek_5, boek_6, boek_7 = 3.50, 3.50, 1.35, 2.85, 3.35, 2.35, 1.55
aantal_beschadigde_boeken = 3
BOETE_PER_BESCHADIGING = 2.50
totaal_bedrag = (boek_1 + boek_2 + boek_3 + boek_4 + boek_5 + boek_6 + boek_7) + (aantal_beschadigde_boeken * BOETE_PER_BESCHADIGING)
print(f"Het totaal bedrag dat u moet betalen €{totaal_bedrag}!")