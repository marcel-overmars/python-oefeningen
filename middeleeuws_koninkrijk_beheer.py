# ==========================================================
# UITLEG PROJECT - KONINKRIJK BEHEERSYSTEEM
# ==========================================================
#
# In dit project heb ik meerdere onderdelen uit de basis van
# Python gecombineerd in één groter programma. Het doel was
# om zoveel mogelijk eerder geleerde onderwerpen opnieuw te
# gebruiken, zodat de basis beter blijft hangen.
#
# Ik begin met een tuple waarin de vaste regio's van het
# koninkrijk worden opgeslagen. Omdat deze regio's tijdens
# het programma niet veranderen, is een tuple hiervoor een
# geschikte keuze.
#
# Vervolgens werk ik met verschillende lijsten waarin gegevens
# kunnen veranderen. Ik oefen hierbij met:
# - append()
# - pop()
# - del
# - het aanpassen van bestaande items
#
# Bij de officieren gebruik ik voor het eerst uitgebreid
# if-elif-else. Op basis van leeftijd en ervaringsscore wordt
# automatisch bepaald in welke rang een officier terechtkomt.
#
# In de wapenkamer en voorraadschuur oefen ik met:
# - in
# - not in
# - and
# - if / elif / else
#
# Hiermee controleer ik of materialen aanwezig zijn, of er
# tekorten zijn en of bepaalde voorwerpen beschadigd zijn.
#
# Voor de dagelijkse verdediging gebruik ik een for-loop met
# range() om automatisch gegevens voor een hele week te
# genereren. Deze waarden sla ik op in een lijst.
#
# Daarna gebruik ik verschillende functies om de gegevens te
# analyseren:
# - len()
# - min()
# - max()
# - sum()
#
# Ook bereken ik voor het eerst zelf een gemiddelde door het
# totaal van de lijst te delen door het aantal elementen.
#
# Daarnaast oefen ik opnieuw met:
# - slices
# - title()
# - upper()
# - nette uitvoer met f-strings
# - duidelijke commentaarblokken
#
# Tot slot sluit ik het programma af met een overzichtelijk
# eindrapport waarin alle belangrijke informatie van het
# koninkrijk wordt samengevat.
#
# Met dit project heb ik geoefend met:
# - tuples
# - lists
# - append()
# - pop()
# - del
# - indexen aanpassen
# - for-loops
# - range()
# - if
# - elif
# - else
# - and
# - in
# - not in
# - slices
# - len()
# - min()
# - max()
# - sum()
# - gemiddelde berekenen
# - title()
# - upper()
# - f-strings
# ==========================================================

lijn = "======================================="

# ===================================
# Vaste regio's van het koninkrijk
# ===================================

regios =(
    'noordrijk',
    'zuidrijk',
    'oostpoort',
    'westhaven',
    'ijzervallei',
    'koningsstad',
)
print(lijn)
print()

for regio in regios:
    print(regio.title())
print()
print(lijn)
print()

# ======================================
# Lijst van het leger en aanpassingen
# ======================================

legers =[
    'riders',
    'boogschutters',
    'ruiters',
    'verkenners',
    'katapulten',
    'speermannen',
    'zwaardvechters',
    'bijlvechters',
]

legers[0] = 'ridders'
del legers[-1]
legers.append('kruisboogschutters')
missie = legers.pop(3)

print("De actuele legerlijst:")
print(legers)
print("De bijlvechters zijn vertrokken uit het leger.")
print(f"{legers[-1].title()} zijn er voor in de plaats gekomen.")
print(f"De {missie} zijn op een speciale missie.")
print()
print(lijn)
print()

# =======================
# Officieren en rang
# =======================

naam_1 = 'marcel'
leeftijd_1 = 41
ervaringsscore_1 = 80

naam_2 = 'lucas'
leeftijd_2 = 20
ervaringsscore_2 = 29

naam_3 = 'rob'
leeftijd_3 = 33
ervaringsscore_3 = 40

if ervaringsscore_1 <= 35 and leeftijd_1 <= 23:
    print(f"{naam_1.title()} is rekruut.")
elif ervaringsscore_1 <= 69 and leeftijd_1 <=35:
    print(f"{naam_1.title()} is ervaren.")
else:
    print(f"{naam_1.title()} is elitecommandant.")
print()

if ervaringsscore_2 <= 35 and leeftijd_2 <= 23:
    print(f"{naam_2.title()} is rekruut.")
elif ervaringsscore_2 <= 69 and leeftijd_2 <= 35:
    print(f"{naam_2.title()} is ervaren.")
else:
    print(f"{naam_2.title()} is elitecommandant.")
print()

if ervaringsscore_3 <= 35 and leeftijd_3 <= 23:
    print(f"{naam_3.title()} is rekruut.")
elif ervaringsscore_3 <= 69 and leeftijd_3 <= 35:
    print(f"{naam_3.title()} is ervaren.")
else:
    print(f"{naam_3.title()} is elitecommandant.")
print()
print(lijn)
print()

# ==============
# Wapenkamer
# ==============

wapens =[
    'zwaard',
    'speer',
    'kruisboog',
    'boog',
    'schild',
    'bijl',
    'hamer',
    'helm',
    'harnas',
    'hellebaard',
]

if 'helm' in wapens:
    print("Helm is voldoende op voorraad.")
else:
    print("Er is een tekort aan helmen, bestel extra!")

if 'knots' not in wapens:
    print("Er is een tekort aan knotsen, bestel bij!")
else:
    print("Er zijn voldoende knotsen.")
print()
print(lijn)
print()

for wapen in wapens:
    if wapen == 'bijl':
        print(f"Het volgende wapen is beschadigd: {wapen.upper()}")
    else:
        print(f"Het volgende wapen is gereed voor gebruik: {wapen}")
print()
print(lijn)
print()

# ==================
# Voorraadschuur
# ==================

voorraden =[
    'hout',
    'ijzer',
    'vlees',
    'water',
    'kruiden',
]

tekorten =[
    'graan',
    'steen',
    'leer',
]

if 'hout' in voorraden:
    print("Er is voldoende hout op voorraad!")
else:
    print("Er is een tekort aan hout en er moet bij verzameld worden.")
print()

if 'graan' in tekorten:
    print("Er is een tekort aan graan en actie is noodzakelijk.")
else:
    print("Er is voldoende graan op voorraad.")
print()

if 'leer' not in voorraden:
    print("Er is een tekort aan leer, verhoog de productie.")
else:
    print("Er is voldoende leer op voorraad.")

# =========================
# Dagelijkse verdediging
# =========================

verdediging = []

for dag in range(1, 8):
    verslagen_vijanden = dag * 65
    verdediging.append(verslagen_vijanden)

gemiddelde = sum(verdediging) / len(verdediging)

print(f"Verslagen vijanden per dag in een week: {verdediging}")
print(f"Verslagen vijanden per dag in de eerste 3 dagen: {verdediging[:3]}")
print(f"Verslagen vijanden per dag in de laatste 3 dagen: {verdediging[-3:]}")
print(f"Het minste aantal verslagen vijanden op een dag: {min(verdediging)} ")
print(f"Het hoogste aantal verslagen vijanden op een dag: {max(verdediging)}")
print(f"Het totale aantal verslagen vijanden in de week: {sum(verdediging)}")
print(f"Het aantal dagen dat er gemeten is: {len(verdediging)}")
print(f"Het gemiddelde aantal verslagen vijanden per dag: {gemiddelde:.0f}")
print()
print(lijn)
print()

# =================
# Wachtrapport
# =================

wachttorens =[
    'noordelijke wachttoren',
    'oostelijke wachttoren',
    'zuidelijke wachttoren',
    'westelijke wachttoren',
    'centrale wachttoren',
    'grote wachttoren',
]

for wachttoren in wachttorens:
    if wachttoren != 'zuidelijke wachttoren':
        print(f"De volgende wachttoren is veilig: {wachttoren}")
    else:
        print(f"De volgende wachttoren is zwaar beschadigd: {wachttoren}")
print()
print(lijn)
print()

# ===============
# Eindrapport
# ===============

print("==============================")
print("=== KONINKRIJK EINDRAPPORT ===")
print("==============================")
print()
print(f"Aantal regio's: {len(regios)}")
print(f"Aantal actieve soldaten: {len(legers)}")
print(f"Nieuwe legereenheid: {legers[-1]}")
print(f"Legereenheid op missie: {missie}")
print(f"Aantal wapens: {len(wapens)}")
print(f"Aantal beschikbare voorraden: {len(voorraden)}")
print(f"Aantal tekorten: {len(tekorten)}")
print(f"Het minste aantal verslagen vijanden op een dag: {min(verdediging)}")
print(f"Het meeste aantal verslagen vijanden op een dag: {max(verdediging)}")
print(f"Het totale aantal verslagen vijanden in de week: {sum(verdediging)}")
print(f"Het gemiddelde aantal verslagen tegenstanders van de dag: {gemiddelde:.0f}")
print()
print(lijn)