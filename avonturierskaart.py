# Oefenproject: Avonturierskaart
#
# Dit programma maakt een eenvoudige avonturierskaart.
# De gebruiker heeft een voornaam, achternaam, klasse, wapen
# en een bestandsnaam.
#
# In dit project oefen ik met:
# - Variabelen
# - Strings
# - f-strings
# - \n (nieuwe regel)
# - \t (inspringing)
# - .title()
# - .upper()
# - .lower()
# - .removesuffix()
#
# Het programma toont:
# - De volledige naam van de avonturier
# - De klasse en het wapen
# - Een welkomstbericht
# - De naam in hoofdletters en kleine letters
# - De bestandsnaam zonder de .txt extensie

voornaam = "marcel"
achternaam = "overmars"
klasse = "ridder"
wapen = "ijzeren zwaard"
bestand = "karakter_data.txt"

volledige_naam = f"{voornaam} {achternaam}"

print("====================")
print("AVONTURIERSKAART")
print("====================")
print()
print(f"\tNaam: {volledige_naam.title()}\n\tKlasse: {klasse.title()}\n\tWapen: {wapen.title()}\n\n")
print(f"Welkom terug, {klasse.title()} {volledige_naam.title()}!\n\n")
print(f"NAAM IN HOOFDLETTERS:\n{volledige_naam.upper()}\n\n")
print(f"naam in kleine letters:\n{volledige_naam.lower()}\n\n")
print(f"Bestand geladen:\n{bestand.removesuffix('.txt')}")