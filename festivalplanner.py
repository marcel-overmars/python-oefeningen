# ============================================================
# PROJECT: FESTIVALPLANNER
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor het
# plannen van een muziekfestival. Tijdens het programma worden
# artiesten toegevoegd, gewijzigd en verwijderd. Daarnaast wordt
# de artiestenlijst tijdelijk en permanent gesorteerd en maak ik
# een berekening van de verwachte kosten, inkomsten en winst van
# het festival.
#
# In dit project oefen ik met:
# - Lists maken en gebruiken
# - Een lege list vullen met append()
# - Elementen wijzigen met een index
# - Nieuwe elementen invoegen met insert()
# - Elementen verwijderen met del
# - Elementen verwijderen en bewaren met pop()
# - Gegevens ophalen met positieve en negatieve indexen
# - Lijsten tijdelijk sorteren met sorted()
# - Lijsten permanent sorteren met sort()
# - Sorteren in omgekeerde volgorde met reverse=True
# - String-methodes zoals .upper() en .title()
# - Variabelen
# - Integers en floats
# - Constanten gebruiken
# - Rekenen met kosten, inkomsten en winst
# - F-strings gebruiken
# - Getallen leesbaar maken met underscores (bijvoorbeeld 25_000)
# - print(), \n en \t gebruiken voor een overzichtelijke uitvoer
# - Mijn programma indelen met duidelijke commentaren en kopjes
#
# Doel:
# Leren hoe verschillende bewerkingen op lijsten gecombineerd
# kunnen worden binnen één groter programma. Daarnaast oefen ik
# met het maken van berekeningen en het overzichtelijk presenteren
# van informatie aan de gebruiker.
# ============================================================

print("\t\t\t\t=======================")
print("\t\t\t\t=== Festivalplanner ===")
print("\t\t\t\t=======================")
print()


# =================================================
# Lijst met artiesten voor de Festivalplanner
# =================================================

artiesten = []
artiesten.append("linkin park")
artiesten.append("eminem")
artiesten.append("taylor swift")
artiesten.append("bad bunny")
artiesten.append("snoop dogg")
artiesten.append("weeknd")
print(f"\t{artiesten}")
print()

# =============================================
# Vervanging van artiesten die af hebben gezegd
# =============================================

artiesten[3] = "ed sheeran"
artiesten[-1] = "drake"

# =====================================================================
# Via pop() halen we een onzekere artiest uit de lijst en bewaren we
# deze in een variabele. Daardoor kunnen we de artiest later nog tonen
# of opnieuw aan de lijst toevoegen.
# =====================================================================

onzekere_artiest = artiesten.pop(2)
print(f"\tVan de volgende artiest is het nog niet zeker of deze komt:")
print()
print(f"\t{onzekere_artiest.title()}")
print()

# ==========================================================================
# Er is 1 artiest die heeft afgezegd en we hebben niet direct een vervanger.
# ==========================================================================

del artiesten[2]

# =============================================================================
# Er is een update voor het vorige punt en hebben toch een vervanging gevonden.
# =============================================================================

artiesten.insert(2, 'elton john')

# ====================================================
# De volgende artiesten zullen op de main stage staan.
# ====================================================

print("\t\t\t\t===========================")
print("\t\t\t\t=== Mainstage artiesten ===")
print("\t\t\t\t===========================")
print()
print(f"\t\t\t\t\t{artiesten[0].upper()}")
print(f"\t\t\t\t\t{artiesten[3].upper()}")
print(f"\t\t\t\t\t{artiesten[-1].upper()}")
print()

# =========================================================================================
# Eerst wordt de lijst tijdelijk alfabetisch gesorteerd met sorted().
# Daarna wordt de lijst permanent omgekeerd alfabetisch gesorteerd met sort().
# =========================================================================================

print("\t\t\t\t============================")
print("\t\t\t\t=== Artiesten gesorteerd ===")
print("\t\t\t\t============================")
print()

print(f"\t\t{sorted(artiesten)}")
print()
artiesten.sort(reverse=True)
print(f"\t\t{artiesten}")
print()

# ==========================================================================
# Berekening kosten artiesten, catering, beveiliging, EHBO en podium opbouw.
# Verwachting inkomen kaartjes en drinken.
# ==========================================================================

print("\t\t\t\t============================")
print("\t\t\t\t=== Verwachte winstmarge ===")
print("\t\t\t\t============================")
print()

snoop_dogg, linkin_park, eminem, elton_john, drake = 25_000, 25_000, 16_500, 19_000, 25_000
totale_artiestenkosten = snoop_dogg + linkin_park + elton_john + eminem + drake
PODIUM_VERHUUR = 25_000
CATERING = 20_000
BEVEILIGING = 15_000
EHBO = 15_000
totale_kosten = totale_artiestenkosten + PODIUM_VERHUUR + CATERING + BEVEILIGING + EHBO
print(f"\t\tDe totale kosten voor het muziekfestival bedragen €{totale_kosten:.2f}")
print()

verwachte_bezoekers = 25_000
verwachte_verkochte_drankjes = 75_000
KOSTEN_KAARTJES = 75
KOSTEN_DRANKJES = 3.75
totaal_kaartjes_verkocht = verwachte_bezoekers * KOSTEN_KAARTJES
totaal_drankjes_verkocht = verwachte_verkochte_drankjes * KOSTEN_DRANKJES
totale_inkomsten = totaal_kaartjes_verkocht + totaal_drankjes_verkocht
print(f"\t\tDe verwachte inkomsten zijn €{totale_inkomsten:.2f}")
print()

totale_winst = totale_inkomsten - totale_kosten
print(f"\t\tDe totale verwachte winst is €{totale_winst:.2f}")