# ============================================================
# PROJECT: DVD_VERHUUR
# ============================================================
#
# In dit oefenproject maak ik een eenvoudig programma voor een
# DVD-verhuurbedrijf. Ik beheer een lijst met beschikbare films,
# verhuur films aan klanten en bereken vervolgens de huurprijs.
#
# In dit project oefen ik met:
# - Lists maken en gebruiken
# - Een lege list vullen met append()
# - Elementen verwijderen met pop()
# - Een specifiek element verwijderen met pop(index)
# - Opgeslagen waarden uit pop() opnieuw gebruiken
# - Gegevens ophalen met positieve en negatieve indexen
# - String-methodes zoals .title(), .upper() en .lower()
# - Variabelen
# - Integers en floats
# - Een constante gebruiken
# - Rekenen met huurprijzen, kortingen en totaalbedragen
# - F-strings gebruiken
# - print(), \n en duidelijke kopjes gebruiken voor een
#   overzichtelijke uitvoer
#
# Doel:
# Leren hoe gegevens uit een lijst verwijderd én tegelijkertijd
# bewaard kunnen worden met pop(), zodat deze later opnieuw
# gebruikt kunnen worden binnen het programma, bijvoorbeeld voor
# het tonen van verhuurde films en het berekenen van de huurprijs.
# ============================================================


# =============
# Films te huur
# =============

print("====================")
print(f"Beschikbare films!")
print("====================")
print()

dvd_films = []

dvd_films.append('2012')
dvd_films.append('armageddon')
dvd_films.append('frozen')
dvd_films.append('the avengers')
dvd_films.append('the lion king')
dvd_films.append('the mummy')
dvd_films.append('the godfather')
print(dvd_films)
print()

# ===============
# Verhuurde films
# ===============

print("============================")
print(f"Welke films verhuurd zijn!")
print("============================")
print()

dvd_film_1 = dvd_films.pop()
print(dvd_films)
print()
print(dvd_film_1.upper())
print()

dvd_film_2 = dvd_films.pop(3)
print(dvd_films)
print()
print(dvd_film_2.upper())
print()

# ================
# Aanbevolen films
# ================

print("================")
print(f"Aanbevolen films")
print("================")
print()

print(dvd_films[0])
print(dvd_films[3].title())
print(dvd_films[-1].title())
print()

# ======================
# Verhuurde films prijs!
# ======================

print("=========")
print("Huurprijs")
print("=========")
print()

dvd_huurprijs = 2.50
print(f"€{dvd_huurprijs} per dag!")
print()
KORTING = 0.10
print(f"Korting is 10% na 7 dagen!")
print()
print(f"{dvd_film_1.title()} is 5 dagen verhuurd!")
print(f"{dvd_film_2.title()} is 8 dagen verhuurd!")
print()

huur_film_1 = dvd_huurprijs * 5
huur_film_2_normaal = dvd_huurprijs * 8
huur_film_2_korting = huur_film_2_normaal * KORTING
huur_film_2 = huur_film_2_normaal - huur_film_2_korting
totale_huurprijs = huur_film_1 + huur_film_2
print(f"De kosten voor {dvd_film_1.title()} zijn €{huur_film_1}!")
print(f"De kosten voor {dvd_film_2.title()} zijn €{huur_film_2}!")
print(f"De totale kosten bedragen €{totale_huurprijs}!")
print()
print(f"We hopen dat u van de films genoten heeft!")
