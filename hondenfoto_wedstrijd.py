# ============================================================
# PROJECT: WEDSTRIJD HONDENFOTO'S
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor het
# beheren van een hondenfotowedstrijd. De ingezonden foto's
# worden opgeslagen in een lijst, waarna foto's worden
# toegevoegd, gewijzigd en verwijderd. Vervolgens worden de
# bestandsnamen opgeschoond zodat ze netjes weergegeven kunnen
# worden. Tot slot worden de foto's alfabetisch gesorteerd en
# wordt de totale prijzenpot berekend.
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
# - Strings opschonen met strip()
# - Tekst aan het begin verwijderen met removeprefix()
# - Tekst aan het einde verwijderen met removesuffix()
# - Tekst netjes weergeven met title()
# - Tekst aanpassen met replace()
# - Tijdelijk sorteren met sorted()
# - Permanent sorteren met sort()
# - Permanent sorteren in omgekeerde volgorde met reverse=True
# - Herhalende taken uitvoeren met for-loops
# - Variabelen
# - Constanten
# - Integers en floats
# - Berekeningen uitvoeren
# - F-strings gebruiken
# - Geldbedragen weergeven met twee decimalen (:.2f)
# - Mijn programma overzichtelijk indelen met commentaarblokken
#
# Doel:
# Leren hoe verschillende list-bewerkingen en stringmethodes
# gecombineerd kunnen worden binnen één groter programma.
# Daarnaast oefen ik met for-loops om meerdere foto's automatisch
# te verwerken en netjes weer te geven.
# ============================================================


print("==============================")
print("=== Wedstrijd hondenfoto's ===")
print('==============================')
print()

# =======================
# Lijst inzendfoto's
# =======================

hondenfoto = []
hondenfoto.append(' IMG_mechelse_herder.jpg')
hondenfoto.append(' IMG_franse_bulldog.jpg ')
hondenfoto.append(' IMG_poedel.jpg')
hondenfoto.append('IMG_zwitserse_herder.jpg ')
hondenfoto.append('IMG_duitse_herder.jpg ')
hondenfoto.append(' IMG_labrador.jpg')
hondenfoto.append(' IMG_goldenretriever.jpg ')
hondenfoto.append('IMG_amerikaanse_bulldog.jpg ')
print(hondenfoto)
print()

# ================================
# Wijzigingen in foto's
# ================================\

hondenfoto[1] = ' IMG_corso_cane.jpg '
hondenfoto.insert(2, ' IMG_duitse_dog.jpg')
del hondenfoto[-1]
gediskwalificeerd = hondenfoto.pop(4)
hondenfoto.remove(' IMG_labrador.jpg')
print(f"{gediskwalificeerd.title()} heeft de regels overtreden!")
print()

# ==========================
# Overgebleven kandidaten
# ==========================

overgebleven = len(hondenfoto)
print(f"Het aantal deelnemers is nog:\t{overgebleven}")
print()

# ========================
# Alle foto's tonen
# ========================

for hond in hondenfoto:
    nette_naam = hond.strip().removeprefix("IMG_").removesuffix(".jpg").title()
    print(nette_naam)
print()

# ====================
# Controle foto's
# ====================

for hond in hondenfoto:
    controle = hond.strip().removeprefix("IMG_").removesuffix(".jpg").title().replace("_", " ")
    print(f"De volgende foto is gecontroleerd:\t{controle}")
print()

# ====================================================================================
# Het tijdelijk en permanent en permanent omgekeerd alfabetisch sorteren van foto's
# ====================================================================================

print("Dit is de tijdelijke alfabetische volgorde:")
print(sorted(hondenfoto))
print()
hondenfoto.sort()
print("Dit is de permanente alfabetische volgorde:")
print(hondenfoto)
print()
hondenfoto.sort(reverse=True)
print("Dit is de permanente omgekeerde alfabetische volgorde!")
print(hondenfoto)
print()

# =======================================================
# Berekening prijzengeld eerste, tweede en derde plaats
# =======================================================

INSCHRIJFGELD = 250
aantal_deelnemers = 100
SPONSORGELD = 25_000
totale_inschrijfgeld = INSCHRIJFGELD * aantal_deelnemers
totale_prijzenpot = totale_inschrijfgeld + SPONSORGELD
print(f"Het totale inschrijfgeld is €{totale_inschrijfgeld:.2f}")
print(f"De totale prijzenpot is €{totale_prijzenpot:.2f}")
print()
eerste_prijs = totale_prijzenpot * 0.50
tweede_prijs = totale_prijzenpot * 0.35
derde_prijs = totale_prijzenpot * 0.15
print(f"De eerste plek wint een prijs van €{eerste_prijs:.2f}")
print(f"De tweede plek wint een prijs van €{tweede_prijs:.2f}")
print(f"De derde plek wint een prijs van €{derde_prijs:.2f}")