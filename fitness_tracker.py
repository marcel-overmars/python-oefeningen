# Oefenproject: Fitness Tracker
#
# Dit programma maakt een eenvoudige trainingssamenvatting van een sporter.
# Er worden persoonlijke gegevens, oefeningen, sets en gewichten
# weergegeven. Daarnaast berekent het programma het totale aantal sets
# en het gemiddelde trainingsgewicht.
#
# In dit project oefen ik met:
# - Variabelen (strings, integers en floats)
# - Multiple assignment
# - Constanten (BTW_PERCENTAGE of andere vaste waarden)
# - Rekenen met getallen (+, /)
# - Berekeningen opslaan in nieuwe variabelen
# - f-strings
# - print()
# - \n (nieuwe regel)
# - \t (inspringing)
# - .title()
# - Het overzichtelijk opmaken van de uitvoer
#
# Leerdoel:
# Meerdere onderwerpen combineren in één programma en de code
# overzichtelijk en leesbaar houden.


# Persoonlijke gegevens

voornaam = "marcel"
achternaam = "overmars"
volledige_naam = f"{voornaam} {achternaam}"
leeftijd = 41
gewicht = 90 

# oefeningen gegevens

oefening_1 = "legpress"
oefening_2 = "chestpress"
oefening_3 = "arm curl"
sets_1, sets_2, sets_3 = 3, 3, 3
gewicht_1, gewicht_2, gewicht_3 = 100.00, 80.00, 16.00

print("====================")
print("fitness_tracker")
print("====================")
print()
print(f"PERSOONLIJKE GEGEVENS:\n\nnaam: {volledige_naam.title()}\nLeeftijd: {leeftijd}\nGewicht: {gewicht} kg")
print()
print("==============================================================")
print()
print(f"{oefening_1}\t\t\t{sets_1}\t\t\t{gewicht_1}")
print()
print(f"{oefening_2}\t\t\t{sets_2}\t\t\t{gewicht_2}")
print()
print(f"{oefening_3}\t\t\t{sets_3}\t\t\t{gewicht_3}")
print()
print("==============================================================")
print()

totale_sets = sets_1 + sets_2 + sets_3
print(f"totale sets: {totale_sets}")
print()

gemiddelde_gewicht = (gewicht_1 + gewicht_2 + gewicht_3) / 3
print(f"Gemiddelde gewicht: {gemiddelde_gewicht} kg")
print()
print(f"Gister ging het goed maar vandaag zal het nog beter gaan!")
