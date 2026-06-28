# ============================================================
# PROJECT: Filmavond Planner
#
# In dit oefenproject heb ik geoefend met:
# - Lists (lijsten) maken en gebruiken.
# - Elementen uit een list ophalen met indexen.
# - Positieve en negatieve indexen gebruiken.
# - String-methodes zoals .title() en .upper().
# - F-strings gebruiken om nette zinnen te maken.
# - Een eenvoudige berekening uitvoeren.
# - De uitvoer overzichtelijk opmaken met print(), \n en
#   scheidingslijnen.
#
# Doel:
# Een programma maken dat een filmavond plant, de films en
# vrienden weergeeft en berekent hoeveel iedere persoon moet
# betalen.
# ============================================================

films = ['fantastic four', 'the avengers', 'age of ultron', 'the hulk', 'spiderman', 'thor', 'infinity war', 'end game']

print()
print("+-+-+-+-+-+-+-+-+-+")
print("Filmavond planning")
print("+-+-+-+-+-+-+-+-+-+")
print()

# Films lijst

print(films)
print()
print(films[0].title())
print(films[1].title())
print(films[3].title())
print(films[-1].title())
print()
print(f"We gaan de 4 films, {films[0].upper()}, {films[1].upper()}, {films[3].upper()} en {films[-1].upper()} kijken!")
print()
print()

# Vrienden die langs komen

vrienden = ['lars', 'dennis', 'rob', 'jeroen']

print("----------")
print("VRIENDEN")
print("----------")
print()
print(f"De vrienden die komen kijken zijn {vrienden[0].title()}, {vrienden[1].title()}, {vrienden[2].title()} en {vrienden[3].title()}")
print(f"Het eten, drinken en extra's kosten 65 euro en we betalen het samen")
print()

# Berekening van de kosten per persoon

rekening = 65 / 5

print("----------")
print("BETALING")
print("----------")
print()
print(f"Ik zal elke vriend een tikkie sturen van €{rekening}!")