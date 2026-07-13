# ============================================================
# PROJECT: RESTAURANT RESERVERINGEN
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor het
# beheren van reserveringen in een restaurant. Tijdens het
# programma worden reserveringen toegevoegd, gewijzigd en
# verwijderd. Vervolgens bereken ik het aantal reserveringen,
# het totale aantal gasten en de verwachte omzet van een buffet.
#
# In dit project oefen ik met:
# - Lists maken en gebruiken
# - Een lege list vullen met append()
# - Elementen wijzigen met een index
# - Nieuwe elementen invoegen met insert()
# - Elementen verwijderen met del
# - Elementen verwijderen op waarde met remove()
# - Elementen verwijderen en bewaren met pop()
# - De lengte van een list bepalen met len()
# - Variabelen gebruiken
# - Constanten gebruiken
# - Integers en floats
# - Rekenen met aantallen, prijzen en omzet
# - F-strings gebruiken
# - String-methodes zoals .title()
# - print(), \n en duidelijke commentaren gebruiken
#
# Doel:
# Leren hoe een reserveringssysteem eenvoudig beheerd kan worden
# met behulp van lijsten. Daarnaast oefen ik met het berekenen
# van aantallen, het werken met reserveringen en het berekenen
# van de verwachte omzet van een restaurant.
# ============================================================


# ============================
# Reserveringen voor 1 tafel
# ============================

print("====================")
print("Aantal reserveringen")
print("====================")
print()

gasten = []
gasten.append('overmars')
gasten.append('vink')
gasten.append('van_leeuwen')
gasten.append('de_haan')
gasten.append('bergkamp')
gasten.append('robben')
gasten.append('de_boer')
gasten.append('obama')
gasten.append('koeman')
gasten.append('ronaldo')
print(gasten)
print()

# =============================
# Wijzigingen in reserveringen
# =============================

gasten[2] = 'smith'
gasten[4] = 'parker'
gasten[-2] = 'banner'

komt_mogelijk_niet = gasten.pop(0)
print(f"{komt_mogelijk_niet.title()} is niet zeker of ze komen. (reservering niet vasthouden)")
print()

del gasten[-1]
del gasten[3]

gasten.remove('de_haan')
print(gasten)
print()

gasten.insert(3, 'holtrigter')
gasten.insert(-1, 'brookhuis')
print(f"De aangepaste lijst is:")
print()
print(gasten)
print()

aantal_reserveringen = len(gasten)
print(f"Aantal reserveringen:\t{aantal_reserveringen}")


# ================
# Verwachte omzet
# ================

vink, smith, robben, holtrigter, de_boer, obama, brookhuis, banner = 2, 4, 3, 3, 7, 2, 2, 4
totaal_aantal_personen = vink + smith + robben + holtrigter + de_boer + obama + brookhuis + banner
print(f"Het totaal aantal gasten is:\t{totaal_aantal_personen}")
print()

BUFFET_PRIJS = 35
DRANK_PRIJS = 2.50
print(f"De prijs voor het buffet bedraagt €{BUFFET_PRIJS:.2f} en drankjes zijn apart €{DRANK_PRIJS:.2f} per drankje")
DRANK_PP = 3
totaal_drankjes = DRANK_PP * totaal_aantal_personen
drank_omzet = totaal_drankjes * DRANK_PRIJS
buffet_omzet = BUFFET_PRIJS * totaal_aantal_personen
totaal_omzet = buffet_omzet + drank_omzet
print(f"De totaal verwachte omzet bedraagt €{totaal_omzet:.2f}")